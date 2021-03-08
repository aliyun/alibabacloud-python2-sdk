# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class AddAITemplateRequest(TeaModel):
    def __init__(self, template_name=None, template_type=None, template_config=None):
        self.template_name = TeaConverter.to_unicode(template_name)  # type: unicode
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        return self


class AddAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class AddAITemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddAITemplateResponseBody

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
            temp_model = AddAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCategoryRequest(TeaModel):
    def __init__(self, cate_name=None, parent_id=None, type=None):
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.parent_id = parent_id  # type: long
        self.type = TeaConverter.to_unicode(type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddCategoryResponseBodyCategory(TeaModel):
    def __init__(self, type=None, parent_id=None, cate_name=None, cate_id=None, level=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.parent_id = parent_id  # type: long
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.level = level  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class AddCategoryResponseBody(TeaModel):
    def __init__(self, category=None, request_id=None):
        self.category = category  # type: AddCategoryResponseBodyCategory
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.category:
            self.category.validate()

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = AddCategoryResponseBodyCategory()
            self.category = temp_model.from_map(m['Category'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddCategoryResponseBody

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
            temp_model = AddCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEditingProjectRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 title=None, description=None, timeline=None, cover_url=None, division=None, feextend=None, duration=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.timeline = TeaConverter.to_unicode(timeline)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.division = TeaConverter.to_unicode(division)  # type: unicode
        self.feextend = TeaConverter.to_unicode(feextend)  # type: unicode
        self.duration = duration  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.division is not None:
            result['Division'] = self.division
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Division') is not None:
            self.division = m.get('Division')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class AddEditingProjectResponseBodyProject(TeaModel):
    def __init__(self, creation_time=None, status=None, modified_time=None, description=None, project_id=None,
                 title=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.modified_time = TeaConverter.to_unicode(modified_time)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.project_id = TeaConverter.to_unicode(project_id)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.description is not None:
            result['Description'] = self.description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class AddEditingProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: AddEditingProjectResponseBodyProject
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = AddEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddEditingProjectResponseBody

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
            temp_model = AddEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, name=None, transcode_template_list=None, transcode_template_group_id=None, app_id=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.transcode_template_list = TeaConverter.to_unicode(transcode_template_list)  # type: unicode
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.transcode_template_list is not None:
            result['TranscodeTemplateList'] = self.transcode_template_list
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TranscodeTemplateList') is not None:
            self.transcode_template_list = m.get('TranscodeTemplateList')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class AddTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_template_group_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        return self


class AddTranscodeTemplateGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddTranscodeTemplateGroupResponseBody

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
            temp_model = AddTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVodDomainRequest(TeaModel):
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_name=None, sources=None,
                 check_url=None, scope=None, top_level_domain=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.sources = TeaConverter.to_unicode(sources)  # type: unicode
        self.check_url = TeaConverter.to_unicode(check_url)  # type: unicode
        self.scope = TeaConverter.to_unicode(scope)  # type: unicode
        self.top_level_domain = TeaConverter.to_unicode(top_level_domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class AddVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddVodDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddVodDomainResponseBody

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
            temp_model = AddVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVodTemplateRequest(TeaModel):
    def __init__(self, name=None, template_type=None, sub_template_type=None, template_config=None, app_id=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode
        self.sub_template_type = TeaConverter.to_unicode(sub_template_type)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.sub_template_type is not None:
            result['SubTemplateType'] = self.sub_template_type
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('SubTemplateType') is not None:
            self.sub_template_type = m.get('SubTemplateType')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class AddVodTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, vod_template_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.vod_template_id = TeaConverter.to_unicode(vod_template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        return self


class AddVodTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddVodTemplateResponseBody

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
            temp_model = AddVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddWatermarkRequest(TeaModel):
    def __init__(self, type=None, name=None, watermark_config=None, file_url=None, app_id=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.watermark_config = TeaConverter.to_unicode(watermark_config)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class AddWatermarkResponseBodyWatermarkInfo(TeaModel):
    def __init__(self, creation_time=None, type=None, is_default=None, file_url=None, watermark_config=None,
                 name=None, watermark_id=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.watermark_config = TeaConverter.to_unicode(watermark_config)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.watermark_id = TeaConverter.to_unicode(watermark_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.type is not None:
            result['Type'] = self.type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class AddWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, watermark_info=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.watermark_info = watermark_info  # type: AddWatermarkResponseBodyWatermarkInfo

    def validate(self):
        if self.watermark_info:
            self.watermark_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.watermark_info is not None:
            result['WatermarkInfo'] = self.watermark_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WatermarkInfo') is not None:
            temp_model = AddWatermarkResponseBodyWatermarkInfo()
            self.watermark_info = temp_model.from_map(m['WatermarkInfo'])
        return self


class AddWatermarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AddWatermarkResponseBody

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
            temp_model = AddWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachAppPolicyToIdentityRequest(TeaModel):
    def __init__(self, identity_type=None, identity_name=None, app_id=None, policy_names=None,
                 resource_real_owner_id=None):
        self.identity_type = TeaConverter.to_unicode(identity_type)  # type: unicode
        self.identity_name = TeaConverter.to_unicode(identity_name)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.policy_names = TeaConverter.to_unicode(policy_names)  # type: unicode
        self.resource_real_owner_id = TeaConverter.to_unicode(resource_real_owner_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        return self


class AttachAppPolicyToIdentityResponseBody(TeaModel):
    def __init__(self, request_id=None, non_exist_policy_names=None, failed_policy_names=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.non_exist_policy_names = non_exist_policy_names  # type: list[unicode]
        self.failed_policy_names = failed_policy_names  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.non_exist_policy_names is not None:
            result['NonExistPolicyNames'] = self.non_exist_policy_names
        if self.failed_policy_names is not None:
            result['FailedPolicyNames'] = self.failed_policy_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NonExistPolicyNames') is not None:
            self.non_exist_policy_names = m.get('NonExistPolicyNames')
        if m.get('FailedPolicyNames') is not None:
            self.failed_policy_names = m.get('FailedPolicyNames')
        return self


class AttachAppPolicyToIdentityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: AttachAppPolicyToIdentityResponseBody

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
            temp_model = AttachAppPolicyToIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetVodDomainConfigsRequest(TeaModel):
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_names=None, functions=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_names = TeaConverter.to_unicode(domain_names)  # type: unicode
        self.functions = TeaConverter.to_unicode(functions)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        return self


class BatchSetVodDomainConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchSetVodDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: BatchSetVodDomainConfigsResponseBody

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
            temp_model = BatchSetVodDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartVodDomainRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_names=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_names = TeaConverter.to_unicode(domain_names)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class BatchStartVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchStartVodDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: BatchStartVodDomainResponseBody

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
            temp_model = BatchStartVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopVodDomainRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_names=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_names = TeaConverter.to_unicode(domain_names)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class BatchStopVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchStopVodDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: BatchStopVodDomainResponseBody

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
            temp_model = BatchStopVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppInfoRequest(TeaModel):
    def __init__(self, resource_real_owner_id=None, app_name=None, description=None):
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.app_name = TeaConverter.to_unicode(app_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateAppInfoResponseBody(TeaModel):
    def __init__(self, app_id=None, request_id=None):
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateAppInfoResponseBody

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
            temp_model = CreateAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuditRequest(TeaModel):
    def __init__(self, audit_content=None):
        self.audit_content = TeaConverter.to_unicode(audit_content)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.audit_content is not None:
            result['AuditContent'] = self.audit_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditContent') is not None:
            self.audit_content = m.get('AuditContent')
        return self


class CreateAuditResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAuditResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateAuditResponseBody

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
            temp_model = CreateAuditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadAttachedMediaRequest(TeaModel):
    def __init__(self, title=None, business_type=None, media_ext=None, file_name=None, file_size=None, tags=None,
                 cate_id=None, storage_location=None, description=None, user_data=None, cate_ids=None, app_id=None,
                 icon=None):
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.business_type = TeaConverter.to_unicode(business_type)  # type: unicode
        self.media_ext = TeaConverter.to_unicode(media_ext)  # type: unicode
        self.file_name = TeaConverter.to_unicode(file_name)  # type: unicode
        self.file_size = TeaConverter.to_unicode(file_size)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.cate_ids = TeaConverter.to_unicode(cate_ids)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.icon = TeaConverter.to_unicode(icon)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.media_ext is not None:
            result['MediaExt'] = self.media_ext
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.description is not None:
            result['Description'] = self.description
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.icon is not None:
            result['Icon'] = self.icon
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('MediaExt') is not None:
            self.media_ext = m.get('MediaExt')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        return self


class CreateUploadAttachedMediaResponseBody(TeaModel):
    def __init__(self, file_url=None, media_url=None, upload_address=None, request_id=None, media_id=None,
                 upload_auth=None):
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.media_url = TeaConverter.to_unicode(media_url)  # type: unicode
        self.upload_address = TeaConverter.to_unicode(upload_address)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.upload_auth = TeaConverter.to_unicode(upload_auth)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')
        return self


class CreateUploadAttachedMediaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateUploadAttachedMediaResponseBody

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
            temp_model = CreateUploadAttachedMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadImageRequest(TeaModel):
    def __init__(self, title=None, image_type=None, image_ext=None, original_file_name=None, tags=None,
                 storage_location=None, cate_id=None, user_data=None, description=None, app_id=None):
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.image_type = TeaConverter.to_unicode(image_type)  # type: unicode
        self.image_ext = TeaConverter.to_unicode(image_ext)  # type: unicode
        self.original_file_name = TeaConverter.to_unicode(original_file_name)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_ext is not None:
            result['ImageExt'] = self.image_ext
        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageExt') is not None:
            self.image_ext = m.get('ImageExt')
        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CreateUploadImageResponseBody(TeaModel):
    def __init__(self, file_url=None, upload_address=None, request_id=None, upload_auth=None, image_id=None,
                 image_url=None):
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.upload_address = TeaConverter.to_unicode(upload_address)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.upload_auth = TeaConverter.to_unicode(upload_auth)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.image_url = TeaConverter.to_unicode(image_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        return self


class CreateUploadImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateUploadImageResponseBody

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
            temp_model = CreateUploadImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadVideoRequest(TeaModel):
    def __init__(self, cover_url=None, description=None, file_name=None, file_size=None, ip=None, title=None,
                 cate_id=None, tags=None, transcode_mode=None, user_data=None, template_group_id=None, workflow_id=None,
                 storage_location=None, custom_media_info=None, app_id=None):
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.file_name = TeaConverter.to_unicode(file_name)  # type: unicode
        self.file_size = file_size  # type: long
        self.ip = TeaConverter.to_unicode(ip)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.transcode_mode = TeaConverter.to_unicode(transcode_mode)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.template_group_id = TeaConverter.to_unicode(template_group_id)  # type: unicode
        self.workflow_id = TeaConverter.to_unicode(workflow_id)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.custom_media_info = TeaConverter.to_unicode(custom_media_info)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.ip is not None:
            result['IP'] = self.ip
        if self.title is not None:
            result['Title'] = self.title
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.transcode_mode is not None:
            result['TranscodeMode'] = self.transcode_mode
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.custom_media_info is not None:
            result['CustomMediaInfo'] = self.custom_media_info
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TranscodeMode') is not None:
            self.transcode_mode = m.get('TranscodeMode')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('CustomMediaInfo') is not None:
            self.custom_media_info = m.get('CustomMediaInfo')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CreateUploadVideoResponseBody(TeaModel):
    def __init__(self, upload_address=None, video_id=None, request_id=None, upload_auth=None):
        self.upload_address = TeaConverter.to_unicode(upload_address)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.upload_auth = TeaConverter.to_unicode(upload_auth)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')
        return self


class CreateUploadVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateUploadVideoResponseBody

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
            temp_model = CreateUploadVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAIImageInfosRequest(TeaModel):
    def __init__(self, aiimage_info_ids=None):
        self.aiimage_info_ids = TeaConverter.to_unicode(aiimage_info_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.aiimage_info_ids is not None:
            result['AIImageInfoIds'] = self.aiimage_info_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIImageInfoIds') is not None:
            self.aiimage_info_ids = m.get('AIImageInfoIds')
        return self


class DeleteAIImageInfosResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAIImageInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAIImageInfosResponseBody

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
            temp_model = DeleteAIImageInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAITemplateRequest(TeaModel):
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


class DeleteAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class DeleteAITemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAITemplateResponseBody

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
            temp_model = DeleteAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInfoRequest(TeaModel):
    def __init__(self, resource_real_owner_id=None, app_id=None):
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAppInfoResponseBody

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
            temp_model = DeleteAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAttachedMediaRequest(TeaModel):
    def __init__(self, media_ids=None):
        self.media_ids = TeaConverter.to_unicode(media_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        return self


class DeleteAttachedMediaResponseBody(TeaModel):
    def __init__(self, non_exist_media_ids=None, request_id=None):
        self.non_exist_media_ids = non_exist_media_ids  # type: list[unicode]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAttachedMediaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteAttachedMediaResponseBody

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
            temp_model = DeleteAttachedMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryRequest(TeaModel):
    def __init__(self, cate_id=None):
        self.cate_id = cate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        return self


class DeleteCategoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteCategoryResponseBody

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
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDynamicImageRequest(TeaModel):
    def __init__(self, video_id=None, dynamic_image_ids=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.dynamic_image_ids = TeaConverter.to_unicode(dynamic_image_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.dynamic_image_ids is not None:
            result['DynamicImageIds'] = self.dynamic_image_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('DynamicImageIds') is not None:
            self.dynamic_image_ids = m.get('DynamicImageIds')
        return self


class DeleteDynamicImageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDynamicImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteDynamicImageResponseBody

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
            temp_model = DeleteDynamicImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEditingProjectRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 project_ids=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.project_ids = TeaConverter.to_unicode(project_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class DeleteEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteEditingProjectResponseBody

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
            temp_model = DeleteEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(self, delete_image_type=None, image_urls=None, image_ids=None, video_id=None, image_type=None):
        self.delete_image_type = TeaConverter.to_unicode(delete_image_type)  # type: unicode
        self.image_urls = TeaConverter.to_unicode(image_urls)  # type: unicode
        self.image_ids = TeaConverter.to_unicode(image_ids)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.image_type = TeaConverter.to_unicode(image_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.delete_image_type is not None:
            result['DeleteImageType'] = self.delete_image_type
        if self.image_urls is not None:
            result['ImageURLs'] = self.image_urls
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteImageType') is not None:
            self.delete_image_type = m.get('DeleteImageType')
        if m.get('ImageURLs') is not None:
            self.image_urls = m.get('ImageURLs')
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteImageResponseBody

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
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMessageCallbackRequest(TeaModel):
    def __init__(self, owner_account=None, resource_real_owner_id=None, app_id=None):
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteMessageCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMessageCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteMessageCallbackResponseBody

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
            temp_model = DeleteMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMezzaninesRequest(TeaModel):
    def __init__(self, video_ids=None, force=None):
        self.video_ids = TeaConverter.to_unicode(video_ids)  # type: unicode
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteMezzaninesResponseBody(TeaModel):
    def __init__(self, request_id=None, non_exist_video_ids=None, un_removeable_video_ids=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.non_exist_video_ids = non_exist_video_ids  # type: list[unicode]
        self.un_removeable_video_ids = un_removeable_video_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        if self.un_removeable_video_ids is not None:
            result['UnRemoveableVideoIds'] = self.un_removeable_video_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        if m.get('UnRemoveableVideoIds') is not None:
            self.un_removeable_video_ids = m.get('UnRemoveableVideoIds')
        return self


class DeleteMezzaninesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteMezzaninesResponseBody

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
            temp_model = DeleteMezzaninesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMultipartUploadRequest(TeaModel):
    def __init__(self, owner_account=None, resource_real_owner_id=None, media_id=None, media_type=None):
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.media_type = TeaConverter.to_unicode(media_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        return self


class DeleteMultipartUploadResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMultipartUploadResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteMultipartUploadResponseBody

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
            temp_model = DeleteMultipartUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStreamRequest(TeaModel):
    def __init__(self, job_ids=None, video_id=None):
        self.job_ids = TeaConverter.to_unicode(job_ids)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class DeleteStreamResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteStreamResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteStreamResponseBody

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
            temp_model = DeleteStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, transcode_template_group_id=None, transcode_template_ids=None, force_del_group=None):
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode
        self.transcode_template_ids = TeaConverter.to_unicode(transcode_template_ids)  # type: unicode
        self.force_del_group = TeaConverter.to_unicode(force_del_group)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.transcode_template_ids is not None:
            result['TranscodeTemplateIds'] = self.transcode_template_ids
        if self.force_del_group is not None:
            result['ForceDelGroup'] = self.force_del_group
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('TranscodeTemplateIds') is not None:
            self.transcode_template_ids = m.get('TranscodeTemplateIds')
        if m.get('ForceDelGroup') is not None:
            self.force_del_group = m.get('ForceDelGroup')
        return self


class DeleteTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, non_exist_transcode_template_ids=None, request_id=None):
        self.non_exist_transcode_template_ids = non_exist_transcode_template_ids  # type: list[unicode]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.non_exist_transcode_template_ids is not None:
            result['NonExistTranscodeTemplateIds'] = self.non_exist_transcode_template_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExistTranscodeTemplateIds') is not None:
            self.non_exist_transcode_template_ids = m.get('NonExistTranscodeTemplateIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTranscodeTemplateGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteTranscodeTemplateGroupResponseBody

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
            temp_model = DeleteTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVideoRequest(TeaModel):
    def __init__(self, video_ids=None):
        self.video_ids = TeaConverter.to_unicode(video_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')
        return self


class DeleteVideoResponseBody(TeaModel):
    def __init__(self, request_id=None, forbidden_video_ids=None, non_exist_video_ids=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.forbidden_video_ids = forbidden_video_ids  # type: list[unicode]
        self.non_exist_video_ids = non_exist_video_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.forbidden_video_ids is not None:
            result['ForbiddenVideoIds'] = self.forbidden_video_ids
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ForbiddenVideoIds') is not None:
            self.forbidden_video_ids = m.get('ForbiddenVideoIds')
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        return self


class DeleteVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteVideoResponseBody

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
            temp_model = DeleteVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVodDomainRequest(TeaModel):
    def __init__(self, owner_id=None, owner_account=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVodDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteVodDomainResponseBody

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
            temp_model = DeleteVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVodSpecificConfigRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_name=None, config_id=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.config_id = TeaConverter.to_unicode(config_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        return self


class DeleteVodSpecificConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVodSpecificConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteVodSpecificConfigResponseBody

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
            temp_model = DeleteVodSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVodTemplateRequest(TeaModel):
    def __init__(self, vod_template_id=None):
        self.vod_template_id = TeaConverter.to_unicode(vod_template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        return self


class DeleteVodTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, vod_template_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.vod_template_id = TeaConverter.to_unicode(vod_template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        return self


class DeleteVodTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteVodTemplateResponseBody

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
            temp_model = DeleteVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWatermarkRequest(TeaModel):
    def __init__(self, watermark_id=None):
        self.watermark_id = TeaConverter.to_unicode(watermark_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class DeleteWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWatermarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteWatermarkResponseBody

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
            temp_model = DeleteWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlayTopVideosRequest(TeaModel):
    def __init__(self, owner_id=None, biz_date=None, page_no=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.biz_date = TeaConverter.to_unicode(biz_date)  # type: unicode
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePlayTopVideosResponseBodyTopPlayVideosTopPlayVideoStatis(TeaModel):
    def __init__(self, play_duration=None, video_id=None, title=None, vv=None, uv=None):
        self.play_duration = TeaConverter.to_unicode(play_duration)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.vv = TeaConverter.to_unicode(vv)  # type: unicode
        self.uv = TeaConverter.to_unicode(uv)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.title is not None:
            result['Title'] = self.title
        if self.vv is not None:
            result['VV'] = self.vv
        if self.uv is not None:
            result['UV'] = self.uv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VV') is not None:
            self.vv = m.get('VV')
        if m.get('UV') is not None:
            self.uv = m.get('UV')
        return self


class DescribePlayTopVideosResponseBodyTopPlayVideos(TeaModel):
    def __init__(self, top_play_video_statis=None):
        self.top_play_video_statis = top_play_video_statis  # type: list[DescribePlayTopVideosResponseBodyTopPlayVideosTopPlayVideoStatis]

    def validate(self):
        if self.top_play_video_statis:
            for k in self.top_play_video_statis:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TopPlayVideoStatis'] = []
        if self.top_play_video_statis is not None:
            for k in self.top_play_video_statis:
                result['TopPlayVideoStatis'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.top_play_video_statis = []
        if m.get('TopPlayVideoStatis') is not None:
            for k in m.get('TopPlayVideoStatis'):
                temp_model = DescribePlayTopVideosResponseBodyTopPlayVideosTopPlayVideoStatis()
                self.top_play_video_statis.append(temp_model.from_map(k))
        return self


class DescribePlayTopVideosResponseBody(TeaModel):
    def __init__(self, top_play_videos=None, total_num=None, request_id=None, page_size=None, page_no=None):
        self.top_play_videos = top_play_videos  # type: DescribePlayTopVideosResponseBodyTopPlayVideos
        self.total_num = total_num  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: long
        self.page_no = page_no  # type: long

    def validate(self):
        if self.top_play_videos:
            self.top_play_videos.validate()

    def to_map(self):
        result = dict()
        if self.top_play_videos is not None:
            result['TopPlayVideos'] = self.top_play_videos.to_map()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TopPlayVideos') is not None:
            temp_model = DescribePlayTopVideosResponseBodyTopPlayVideos()
            self.top_play_videos = temp_model.from_map(m['TopPlayVideos'])
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class DescribePlayTopVideosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePlayTopVideosResponseBody

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
            temp_model = DescribePlayTopVideosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlayUserAvgRequest(TeaModel):
    def __init__(self, owner_id=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribePlayUserAvgResponseBodyUserPlayStatisAvgsUserPlayStatisAvg(TeaModel):
    def __init__(self, avg_play_duration=None, avg_play_count=None, date=None):
        self.avg_play_duration = TeaConverter.to_unicode(avg_play_duration)  # type: unicode
        self.avg_play_count = TeaConverter.to_unicode(avg_play_count)  # type: unicode
        self.date = TeaConverter.to_unicode(date)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avg_play_duration is not None:
            result['AvgPlayDuration'] = self.avg_play_duration
        if self.avg_play_count is not None:
            result['AvgPlayCount'] = self.avg_play_count
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgPlayDuration') is not None:
            self.avg_play_duration = m.get('AvgPlayDuration')
        if m.get('AvgPlayCount') is not None:
            self.avg_play_count = m.get('AvgPlayCount')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class DescribePlayUserAvgResponseBodyUserPlayStatisAvgs(TeaModel):
    def __init__(self, user_play_statis_avg=None):
        self.user_play_statis_avg = user_play_statis_avg  # type: list[DescribePlayUserAvgResponseBodyUserPlayStatisAvgsUserPlayStatisAvg]

    def validate(self):
        if self.user_play_statis_avg:
            for k in self.user_play_statis_avg:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UserPlayStatisAvg'] = []
        if self.user_play_statis_avg is not None:
            for k in self.user_play_statis_avg:
                result['UserPlayStatisAvg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user_play_statis_avg = []
        if m.get('UserPlayStatisAvg') is not None:
            for k in m.get('UserPlayStatisAvg'):
                temp_model = DescribePlayUserAvgResponseBodyUserPlayStatisAvgsUserPlayStatisAvg()
                self.user_play_statis_avg.append(temp_model.from_map(k))
        return self


class DescribePlayUserAvgResponseBody(TeaModel):
    def __init__(self, request_id=None, user_play_statis_avgs=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.user_play_statis_avgs = user_play_statis_avgs  # type: DescribePlayUserAvgResponseBodyUserPlayStatisAvgs

    def validate(self):
        if self.user_play_statis_avgs:
            self.user_play_statis_avgs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_play_statis_avgs is not None:
            result['UserPlayStatisAvgs'] = self.user_play_statis_avgs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserPlayStatisAvgs') is not None:
            temp_model = DescribePlayUserAvgResponseBodyUserPlayStatisAvgs()
            self.user_play_statis_avgs = temp_model.from_map(m['UserPlayStatisAvgs'])
        return self


class DescribePlayUserAvgResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePlayUserAvgResponseBody

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
            temp_model = DescribePlayUserAvgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlayUserTotalRequest(TeaModel):
    def __init__(self, owner_id=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV(TeaModel):
    def __init__(self, i_os=None, android=None, flash=None, html5=None):
        self.i_os = TeaConverter.to_unicode(i_os)  # type: unicode
        self.android = TeaConverter.to_unicode(android)  # type: unicode
        self.flash = TeaConverter.to_unicode(flash)  # type: unicode
        self.html5 = TeaConverter.to_unicode(html5)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.i_os is not None:
            result['iOS'] = self.i_os
        if self.android is not None:
            result['Android'] = self.android
        if self.flash is not None:
            result['Flash'] = self.flash
        if self.html5 is not None:
            result['HTML5'] = self.html5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('iOS') is not None:
            self.i_os = m.get('iOS')
        if m.get('Android') is not None:
            self.android = m.get('Android')
        if m.get('Flash') is not None:
            self.flash = m.get('Flash')
        if m.get('HTML5') is not None:
            self.html5 = m.get('HTML5')
        return self


class DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV(TeaModel):
    def __init__(self, i_os=None, android=None, flash=None, html5=None):
        self.i_os = TeaConverter.to_unicode(i_os)  # type: unicode
        self.android = TeaConverter.to_unicode(android)  # type: unicode
        self.flash = TeaConverter.to_unicode(flash)  # type: unicode
        self.html5 = TeaConverter.to_unicode(html5)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.i_os is not None:
            result['iOS'] = self.i_os
        if self.android is not None:
            result['Android'] = self.android
        if self.flash is not None:
            result['Flash'] = self.flash
        if self.html5 is not None:
            result['HTML5'] = self.html5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('iOS') is not None:
            self.i_os = m.get('iOS')
        if m.get('Android') is not None:
            self.android = m.get('Android')
        if m.get('Flash') is not None:
            self.flash = m.get('Flash')
        if m.get('HTML5') is not None:
            self.html5 = m.get('HTML5')
        return self


class DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotal(TeaModel):
    def __init__(self, play_duration=None, date=None, vv=None, play_range=None, uv=None):
        self.play_duration = TeaConverter.to_unicode(play_duration)  # type: unicode
        self.date = TeaConverter.to_unicode(date)  # type: unicode
        self.vv = vv  # type: DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV
        self.play_range = TeaConverter.to_unicode(play_range)  # type: unicode
        self.uv = uv  # type: DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV

    def validate(self):
        if self.vv:
            self.vv.validate()
        if self.uv:
            self.uv.validate()

    def to_map(self):
        result = dict()
        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration
        if self.date is not None:
            result['Date'] = self.date
        if self.vv is not None:
            result['VV'] = self.vv.to_map()
        if self.play_range is not None:
            result['PlayRange'] = self.play_range
        if self.uv is not None:
            result['UV'] = self.uv.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('VV') is not None:
            temp_model = DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV()
            self.vv = temp_model.from_map(m['VV'])
        if m.get('PlayRange') is not None:
            self.play_range = m.get('PlayRange')
        if m.get('UV') is not None:
            temp_model = DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV()
            self.uv = temp_model.from_map(m['UV'])
        return self


class DescribePlayUserTotalResponseBodyUserPlayStatisTotals(TeaModel):
    def __init__(self, user_play_statis_total=None):
        self.user_play_statis_total = user_play_statis_total  # type: list[DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotal]

    def validate(self):
        if self.user_play_statis_total:
            for k in self.user_play_statis_total:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UserPlayStatisTotal'] = []
        if self.user_play_statis_total is not None:
            for k in self.user_play_statis_total:
                result['UserPlayStatisTotal'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user_play_statis_total = []
        if m.get('UserPlayStatisTotal') is not None:
            for k in m.get('UserPlayStatisTotal'):
                temp_model = DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotal()
                self.user_play_statis_total.append(temp_model.from_map(k))
        return self


class DescribePlayUserTotalResponseBody(TeaModel):
    def __init__(self, request_id=None, user_play_statis_totals=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.user_play_statis_totals = user_play_statis_totals  # type: DescribePlayUserTotalResponseBodyUserPlayStatisTotals

    def validate(self):
        if self.user_play_statis_totals:
            self.user_play_statis_totals.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_play_statis_totals is not None:
            result['UserPlayStatisTotals'] = self.user_play_statis_totals.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserPlayStatisTotals') is not None:
            temp_model = DescribePlayUserTotalResponseBodyUserPlayStatisTotals()
            self.user_play_statis_totals = temp_model.from_map(m['UserPlayStatisTotals'])
        return self


class DescribePlayUserTotalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePlayUserTotalResponseBody

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
            temp_model = DescribePlayUserTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlayVideoStatisRequest(TeaModel):
    def __init__(self, owner_id=None, start_time=None, end_time=None, video_id=None):
        self.owner_id = owner_id  # type: long
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class DescribePlayVideoStatisResponseBodyVideoPlayStatisDetailsVideoPlayStatisDetail(TeaModel):
    def __init__(self, play_duration=None, date=None, vv=None, title=None, uv=None, play_range=None):
        self.play_duration = TeaConverter.to_unicode(play_duration)  # type: unicode
        self.date = TeaConverter.to_unicode(date)  # type: unicode
        self.vv = TeaConverter.to_unicode(vv)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.uv = TeaConverter.to_unicode(uv)  # type: unicode
        self.play_range = TeaConverter.to_unicode(play_range)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration
        if self.date is not None:
            result['Date'] = self.date
        if self.vv is not None:
            result['VV'] = self.vv
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['UV'] = self.uv
        if self.play_range is not None:
            result['PlayRange'] = self.play_range
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('VV') is not None:
            self.vv = m.get('VV')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UV') is not None:
            self.uv = m.get('UV')
        if m.get('PlayRange') is not None:
            self.play_range = m.get('PlayRange')
        return self


class DescribePlayVideoStatisResponseBodyVideoPlayStatisDetails(TeaModel):
    def __init__(self, video_play_statis_detail=None):
        self.video_play_statis_detail = video_play_statis_detail  # type: list[DescribePlayVideoStatisResponseBodyVideoPlayStatisDetailsVideoPlayStatisDetail]

    def validate(self):
        if self.video_play_statis_detail:
            for k in self.video_play_statis_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VideoPlayStatisDetail'] = []
        if self.video_play_statis_detail is not None:
            for k in self.video_play_statis_detail:
                result['VideoPlayStatisDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.video_play_statis_detail = []
        if m.get('VideoPlayStatisDetail') is not None:
            for k in m.get('VideoPlayStatisDetail'):
                temp_model = DescribePlayVideoStatisResponseBodyVideoPlayStatisDetailsVideoPlayStatisDetail()
                self.video_play_statis_detail.append(temp_model.from_map(k))
        return self


class DescribePlayVideoStatisResponseBody(TeaModel):
    def __init__(self, video_play_statis_details=None, request_id=None):
        self.video_play_statis_details = video_play_statis_details  # type: DescribePlayVideoStatisResponseBodyVideoPlayStatisDetails
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.video_play_statis_details:
            self.video_play_statis_details.validate()

    def to_map(self):
        result = dict()
        if self.video_play_statis_details is not None:
            result['VideoPlayStatisDetails'] = self.video_play_statis_details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoPlayStatisDetails') is not None:
            temp_model = DescribePlayVideoStatisResponseBodyVideoPlayStatisDetails()
            self.video_play_statis_details = temp_model.from_map(m['VideoPlayStatisDetails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePlayVideoStatisResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribePlayVideoStatisResponseBody

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
            temp_model = DescribePlayVideoStatisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodAIDataRequest(TeaModel):
    def __init__(self, owner_id=None, start_time=None, end_time=None, region=None, aitype=None):
        self.owner_id = owner_id  # type: long
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.region = TeaConverter.to_unicode(region)  # type: unicode
        self.aitype = TeaConverter.to_unicode(aitype)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region is not None:
            result['Region'] = self.region
        if self.aitype is not None:
            result['AIType'] = self.aitype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AIType') is not None:
            self.aitype = m.get('AIType')
        return self


class DescribeVodAIDataResponseBodyAIDataAIDataItemDataDataItem(TeaModel):
    def __init__(self, value=None, name=None):
        self.value = TeaConverter.to_unicode(value)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeVodAIDataResponseBodyAIDataAIDataItemData(TeaModel):
    def __init__(self, data_item=None):
        self.data_item = data_item  # type: list[DescribeVodAIDataResponseBodyAIDataAIDataItemDataDataItem]

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataItem'] = []
        if self.data_item is not None:
            for k in self.data_item:
                result['DataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k in m.get('DataItem'):
                temp_model = DescribeVodAIDataResponseBodyAIDataAIDataItemDataDataItem()
                self.data_item.append(temp_model.from_map(k))
        return self


class DescribeVodAIDataResponseBodyAIDataAIDataItem(TeaModel):
    def __init__(self, data=None, time_stamp=None):
        self.data = data  # type: DescribeVodAIDataResponseBodyAIDataAIDataItemData
        self.time_stamp = TeaConverter.to_unicode(time_stamp)  # type: unicode

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeVodAIDataResponseBodyAIDataAIDataItemData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVodAIDataResponseBodyAIData(TeaModel):
    def __init__(self, aidata_item=None):
        self.aidata_item = aidata_item  # type: list[DescribeVodAIDataResponseBodyAIDataAIDataItem]

    def validate(self):
        if self.aidata_item:
            for k in self.aidata_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AIDataItem'] = []
        if self.aidata_item is not None:
            for k in self.aidata_item:
                result['AIDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aidata_item = []
        if m.get('AIDataItem') is not None:
            for k in m.get('AIDataItem'):
                temp_model = DescribeVodAIDataResponseBodyAIDataAIDataItem()
                self.aidata_item.append(temp_model.from_map(k))
        return self


class DescribeVodAIDataResponseBody(TeaModel):
    def __init__(self, aidata=None, request_id=None, data_interval=None):
        self.aidata = aidata  # type: DescribeVodAIDataResponseBodyAIData
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data_interval = TeaConverter.to_unicode(data_interval)  # type: unicode

    def validate(self):
        if self.aidata:
            self.aidata.validate()

    def to_map(self):
        result = dict()
        if self.aidata is not None:
            result['AIData'] = self.aidata.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIData') is not None:
            temp_model = DescribeVodAIDataResponseBodyAIData()
            self.aidata = temp_model.from_map(m['AIData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeVodAIDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodAIDataResponseBody

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
            temp_model = DescribeVodAIDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodCertificateListRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVodCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
    def __init__(self, last_time=None, fingerprint=None, cert_name=None, issuer=None, cert_id=None, common=None):
        self.last_time = last_time  # type: long
        self.fingerprint = TeaConverter.to_unicode(fingerprint)  # type: unicode
        self.cert_name = TeaConverter.to_unicode(cert_name)  # type: unicode
        self.issuer = TeaConverter.to_unicode(issuer)  # type: unicode
        self.cert_id = cert_id  # type: long
        self.common = TeaConverter.to_unicode(common)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.common is not None:
            result['Common'] = self.common
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        return self


class DescribeVodCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(self, cert=None):
        self.cert = cert  # type: list[DescribeVodCertificateListResponseBodyCertificateListModelCertListCert]

    def validate(self):
        if self.cert:
            for k in self.cert:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Cert'] = []
        if self.cert is not None:
            for k in self.cert:
                result['Cert'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert = []
        if m.get('Cert') is not None:
            for k in m.get('Cert'):
                temp_model = DescribeVodCertificateListResponseBodyCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        return self


class DescribeVodCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(self, cert_list=None, count=None):
        self.cert_list = cert_list  # type: DescribeVodCertificateListResponseBodyCertificateListModelCertList
        self.count = count  # type: int

    def validate(self):
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        result = dict()
        if self.cert_list is not None:
            result['CertList'] = self.cert_list.to_map()
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertList') is not None:
            temp_model = DescribeVodCertificateListResponseBodyCertificateListModelCertList()
            self.cert_list = temp_model.from_map(m['CertList'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeVodCertificateListResponseBody(TeaModel):
    def __init__(self, request_id=None, certificate_list_model=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.certificate_list_model = certificate_list_model  # type: DescribeVodCertificateListResponseBodyCertificateListModel

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeVodCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        return self


class DescribeVodCertificateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodCertificateListResponseBody

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
            temp_model = DescribeVodCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainBpsDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.interval = TeaConverter.to_unicode(interval)  # type: unicode
        self.isp_name_en = TeaConverter.to_unicode(isp_name_en)  # type: unicode
        self.location_name_en = TeaConverter.to_unicode(location_name_en)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeVodDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, https_domestic_value=None, value=None, overseas_value=None, https_value=None,
                 https_overseas_value=None, time_stamp=None, domestic_value=None):
        self.https_domestic_value = TeaConverter.to_unicode(https_domestic_value)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode
        self.overseas_value = TeaConverter.to_unicode(overseas_value)  # type: unicode
        self.https_value = TeaConverter.to_unicode(https_value)  # type: unicode
        self.https_overseas_value = TeaConverter.to_unicode(https_overseas_value)  # type: unicode
        self.time_stamp = TeaConverter.to_unicode(time_stamp)  # type: unicode
        self.domestic_value = TeaConverter.to_unicode(domestic_value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.value is not None:
            result['Value'] = self.value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        return self


class DescribeVodDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVodDomainBpsDataResponseBodyBpsDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVodDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVodDomainBpsDataResponseBody(TeaModel):
    def __init__(self, isp_name_en=None, end_time=None, request_id=None, domain_name=None, location_name_en=None,
                 start_time=None, data_interval=None, bps_data_per_interval=None):
        self.isp_name_en = TeaConverter.to_unicode(isp_name_en)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.location_name_en = TeaConverter.to_unicode(location_name_en)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.data_interval = TeaConverter.to_unicode(data_interval)  # type: unicode
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeVodDomainBpsDataResponseBodyBpsDataPerInterval

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeVodDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        return self


class DescribeVodDomainBpsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodDomainBpsDataResponseBody

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
            temp_model = DescribeVodDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainCertificateInfoRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVodDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, status=None, cert_life=None, cert_expire_time=None, cert_type=None,
                 server_certificate_status=None, cert_domain_name=None, cert_name=None, cert_org=None, domain_name=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.cert_life = TeaConverter.to_unicode(cert_life)  # type: unicode
        self.cert_expire_time = TeaConverter.to_unicode(cert_expire_time)  # type: unicode
        self.cert_type = TeaConverter.to_unicode(cert_type)  # type: unicode
        self.server_certificate_status = TeaConverter.to_unicode(server_certificate_status)  # type: unicode
        self.cert_domain_name = TeaConverter.to_unicode(cert_domain_name)  # type: unicode
        self.cert_name = TeaConverter.to_unicode(cert_name)  # type: unicode
        self.cert_org = TeaConverter.to_unicode(cert_org)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVodDomainCertificateInfoResponseBodyCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info  # type: list[DescribeVodDomainCertificateInfoResponseBodyCertInfosCertInfo]

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeVodDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeVodDomainCertificateInfoResponseBody(TeaModel):
    def __init__(self, cert_infos=None, request_id=None):
        self.cert_infos = cert_infos  # type: DescribeVodDomainCertificateInfoResponseBodyCertInfos
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeVodDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVodDomainCertificateInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodDomainCertificateInfoResponseBody

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
            temp_model = DescribeVodDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainConfigsRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_name=None, function_names=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.function_names = TeaConverter.to_unicode(function_names)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        return self


class DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = TeaConverter.to_unicode(arg_name)  # type: unicode
        self.arg_value = TeaConverter.to_unicode(arg_value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(self, function_arg=None):
        self.function_arg = function_arg  # type: list[DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg]

    def validate(self):
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k in self.function_arg:
                result['FunctionArg'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.function_arg = []
        if m.get('FunctionArg') is not None:
            for k in m.get('FunctionArg'):
                temp_model = DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        return self


class DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfig(TeaModel):
    def __init__(self, status=None, config_id=None, function_name=None, function_args=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.config_id = TeaConverter.to_unicode(config_id)  # type: unicode
        self.function_name = TeaConverter.to_unicode(function_name)  # type: unicode
        self.function_args = function_args  # type: DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        return self


class DescribeVodDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(self, domain_config=None):
        self.domain_config = domain_config  # type: list[DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfig]

    def validate(self):
        if self.domain_config:
            for k in self.domain_config:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainConfig'] = []
        if self.domain_config is not None:
            for k in self.domain_config:
                result['DomainConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_config = []
        if m.get('DomainConfig') is not None:
            for k in m.get('DomainConfig'):
                temp_model = DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        return self


class DescribeVodDomainConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_configs=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.domain_configs = domain_configs  # type: DescribeVodDomainConfigsResponseBodyDomainConfigs

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainConfigs') is not None:
            temp_model = DescribeVodDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        return self


class DescribeVodDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodDomainConfigsResponseBody

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
            temp_model = DescribeVodDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainDetailRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVodDomainDetailResponseBodyDomainDetailSourcesSource(TeaModel):
    def __init__(self, type=None, enabled=None, priority=None, port=None, content=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.enabled = TeaConverter.to_unicode(enabled)  # type: unicode
        self.priority = TeaConverter.to_unicode(priority)  # type: unicode
        self.port = port  # type: int
        self.content = TeaConverter.to_unicode(content)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeVodDomainDetailResponseBodyDomainDetailSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[DescribeVodDomainDetailResponseBodyDomainDetailSourcesSource]

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeVodDomainDetailResponseBodyDomainDetailSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeVodDomainDetailResponseBodyDomainDetail(TeaModel):
    def __init__(self, sslpub=None, sources=None, gmt_modified=None, domain_name=None, gmt_created=None, weight=None,
                 description=None, sslprotocol=None, cert_name=None, scope=None, cname=None, domain_status=None):
        self.sslpub = TeaConverter.to_unicode(sslpub)  # type: unicode
        self.sources = sources  # type: DescribeVodDomainDetailResponseBodyDomainDetailSources
        self.gmt_modified = TeaConverter.to_unicode(gmt_modified)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.gmt_created = TeaConverter.to_unicode(gmt_created)  # type: unicode
        self.weight = TeaConverter.to_unicode(weight)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.sslprotocol = TeaConverter.to_unicode(sslprotocol)  # type: unicode
        self.cert_name = TeaConverter.to_unicode(cert_name)  # type: unicode
        self.scope = TeaConverter.to_unicode(scope)  # type: unicode
        self.cname = TeaConverter.to_unicode(cname)  # type: unicode
        self.domain_status = TeaConverter.to_unicode(domain_status)  # type: unicode

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        result = dict()
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.description is not None:
            result['Description'] = self.description
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Sources') is not None:
            temp_model = DescribeVodDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        return self


class DescribeVodDomainDetailResponseBody(TeaModel):
    def __init__(self, domain_detail=None, request_id=None):
        self.domain_detail = domain_detail  # type: DescribeVodDomainDetailResponseBodyDomainDetail
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        result = dict()
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainDetail') is not None:
            temp_model = DescribeVodDomainDetailResponseBodyDomainDetail()
            self.domain_detail = temp_model.from_map(m['DomainDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVodDomainDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodDomainDetailResponseBody

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
            temp_model = DescribeVodDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainLogRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, page_size=None, page_number=None, start_time=None,
                 end_time=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos(TeaModel):
    def __init__(self, page_number=None, page_size=None, total=None):
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(TeaModel):
    def __init__(self, end_time=None, start_time=None, log_path=None, log_size=None, log_name=None):
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.log_path = TeaConverter.to_unicode(log_path)  # type: unicode
        self.log_size = log_size  # type: long
        self.log_name = TeaConverter.to_unicode(log_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.log_name is not None:
            result['LogName'] = self.log_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        return self


class DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos(TeaModel):
    def __init__(self, log_info_detail=None):
        self.log_info_detail = log_info_detail  # type: list[DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail]

    def validate(self):
        if self.log_info_detail:
            for k in self.log_info_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LogInfoDetail'] = []
        if self.log_info_detail is not None:
            for k in self.log_info_detail:
                result['LogInfoDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_info_detail = []
        if m.get('LogInfoDetail') is not None:
            for k in m.get('LogInfoDetail'):
                temp_model = DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail()
                self.log_info_detail.append(temp_model.from_map(k))
        return self


class DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetail(TeaModel):
    def __init__(self, page_infos=None, log_count=None, domain_name=None, log_infos=None):
        self.page_infos = page_infos  # type: DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos
        self.log_count = log_count  # type: long
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.log_infos = log_infos  # type: DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos

    def validate(self):
        if self.page_infos:
            self.page_infos.validate()
        if self.log_infos:
            self.log_infos.validate()

    def to_map(self):
        result = dict()
        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()
        if self.log_count is not None:
            result['LogCount'] = self.log_count
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageInfos') is not None:
            temp_model = DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m['PageInfos'])
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LogInfos') is not None:
            temp_model = DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        return self


class DescribeVodDomainLogResponseBodyDomainLogDetails(TeaModel):
    def __init__(self, domain_log_detail=None):
        self.domain_log_detail = domain_log_detail  # type: list[DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetail]

    def validate(self):
        if self.domain_log_detail:
            for k in self.domain_log_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DomainLogDetail'] = []
        if self.domain_log_detail is not None:
            for k in self.domain_log_detail:
                result['DomainLogDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_log_detail = []
        if m.get('DomainLogDetail') is not None:
            for k in m.get('DomainLogDetail'):
                temp_model = DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetail()
                self.domain_log_detail.append(temp_model.from_map(k))
        return self


class DescribeVodDomainLogResponseBody(TeaModel):
    def __init__(self, request_id=None, domain_log_details=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.domain_log_details = domain_log_details  # type: DescribeVodDomainLogResponseBodyDomainLogDetails

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeVodDomainLogResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
        return self


class DescribeVodDomainLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodDomainLogResponseBody

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
            temp_model = DescribeVodDomainLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainTrafficDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, interval=None,
                 isp_name_en=None, location_name_en=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.interval = TeaConverter.to_unicode(interval)  # type: unicode
        self.isp_name_en = TeaConverter.to_unicode(isp_name_en)  # type: unicode
        self.location_name_en = TeaConverter.to_unicode(location_name_en)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        return self


class DescribeVodDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, https_domestic_value=None, value=None, overseas_value=None, https_value=None,
                 https_overseas_value=None, time_stamp=None, domestic_value=None):
        self.https_domestic_value = TeaConverter.to_unicode(https_domestic_value)  # type: unicode
        self.value = TeaConverter.to_unicode(value)  # type: unicode
        self.overseas_value = TeaConverter.to_unicode(overseas_value)  # type: unicode
        self.https_value = TeaConverter.to_unicode(https_value)  # type: unicode
        self.https_overseas_value = TeaConverter.to_unicode(https_overseas_value)  # type: unicode
        self.time_stamp = TeaConverter.to_unicode(time_stamp)  # type: unicode
        self.domestic_value = TeaConverter.to_unicode(domestic_value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.value is not None:
            result['Value'] = self.value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        return self


class DescribeVodDomainTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVodDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVodDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVodDomainTrafficDataResponseBody(TeaModel):
    def __init__(self, end_time=None, request_id=None, domain_name=None, traffic_data_per_interval=None,
                 start_time=None, data_interval=None):
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeVodDomainTrafficDataResponseBodyTrafficDataPerInterval
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.data_interval = TeaConverter.to_unicode(data_interval)  # type: unicode

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeVodDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeVodDomainTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodDomainTrafficDataResponseBody

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
            temp_model = DescribeVodDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainUsageDataRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, start_time=None, end_time=None, type=None, area=None,
                 field=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.area = TeaConverter.to_unicode(area)  # type: unicode
        self.field = TeaConverter.to_unicode(field)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.type is not None:
            result['Type'] = self.type
        if self.area is not None:
            result['Area'] = self.area
        if self.field is not None:
            result['Field'] = self.field
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        return self


class DescribeVodDomainUsageDataResponseBodyUsageDataPerIntervalDataModule(TeaModel):
    def __init__(self, value=None, time_stamp=None):
        self.value = TeaConverter.to_unicode(value)  # type: unicode
        self.time_stamp = TeaConverter.to_unicode(time_stamp)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVodDomainUsageDataResponseBodyUsageDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: list[DescribeVodDomainUsageDataResponseBodyUsageDataPerIntervalDataModule]

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVodDomainUsageDataResponseBodyUsageDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVodDomainUsageDataResponseBody(TeaModel):
    def __init__(self, usage_data_per_interval=None, type=None, area=None, end_time=None, request_id=None,
                 domain_name=None, start_time=None, data_interval=None):
        self.usage_data_per_interval = usage_data_per_interval  # type: DescribeVodDomainUsageDataResponseBodyUsageDataPerInterval
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.area = TeaConverter.to_unicode(area)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.data_interval = TeaConverter.to_unicode(data_interval)  # type: unicode

    def validate(self):
        if self.usage_data_per_interval:
            self.usage_data_per_interval.validate()

    def to_map(self):
        result = dict()
        if self.usage_data_per_interval is not None:
            result['UsageDataPerInterval'] = self.usage_data_per_interval.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.area is not None:
            result['Area'] = self.area
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UsageDataPerInterval') is not None:
            temp_model = DescribeVodDomainUsageDataResponseBodyUsageDataPerInterval()
            self.usage_data_per_interval = temp_model.from_map(m['UsageDataPerInterval'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeVodDomainUsageDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodDomainUsageDataResponseBody

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
            temp_model = DescribeVodDomainUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodRefreshQuotaRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeVodRefreshQuotaResponseBody(TeaModel):
    def __init__(self, request_id=None, url_remain=None, preload_remain=None, block_quota=None, dir_remain=None,
                 url_quota=None, dir_quota=None, block_remain=None, preload_quota=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.url_remain = TeaConverter.to_unicode(url_remain)  # type: unicode
        self.preload_remain = TeaConverter.to_unicode(preload_remain)  # type: unicode
        self.block_quota = TeaConverter.to_unicode(block_quota)  # type: unicode
        self.dir_remain = TeaConverter.to_unicode(dir_remain)  # type: unicode
        self.url_quota = TeaConverter.to_unicode(url_quota)  # type: unicode
        self.dir_quota = TeaConverter.to_unicode(dir_quota)  # type: unicode
        self.block_remain = TeaConverter.to_unicode(block_remain)  # type: unicode
        self.preload_quota = TeaConverter.to_unicode(preload_quota)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain
        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota
        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota
        if self.block_remain is not None:
            result['blockRemain'] = self.block_remain
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')
        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')
        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')
        if m.get('blockRemain') is not None:
            self.block_remain = m.get('blockRemain')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        return self


class DescribeVodRefreshQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodRefreshQuotaResponseBody

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
            temp_model = DescribeVodRefreshQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodRefreshTasksRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, task_id=None, object_path=None, page_number=None,
                 object_type=None, domain_name=None, status=None, page_size=None, start_time=None, end_time=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode
        self.object_path = TeaConverter.to_unicode(object_path)  # type: unicode
        self.page_number = page_number  # type: int
        self.object_type = TeaConverter.to_unicode(object_type)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.page_size = page_size  # type: int
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeVodRefreshTasksResponseBodyTasksTask(TeaModel):
    def __init__(self, status=None, creation_time=None, object_type=None, process=None, description=None,
                 object_path=None, task_id=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.object_type = TeaConverter.to_unicode(object_type)  # type: unicode
        self.process = TeaConverter.to_unicode(process)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.object_path = TeaConverter.to_unicode(object_path)  # type: unicode
        self.task_id = TeaConverter.to_unicode(task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeVodRefreshTasksResponseBodyTasks(TeaModel):
    def __init__(self, task=None):
        self.task = task  # type: list[DescribeVodRefreshTasksResponseBodyTasksTask]

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Task'] = []
        if self.task is not None:
            for k in self.task:
                result['Task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k in m.get('Task'):
                temp_model = DescribeVodRefreshTasksResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeVodRefreshTasksResponseBody(TeaModel):
    def __init__(self, total_count=None, tasks=None, request_id=None, page_size=None, page_number=None):
        self.total_count = total_count  # type: long
        self.tasks = tasks  # type: DescribeVodRefreshTasksResponseBodyTasks
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Tasks') is not None:
            temp_model = DescribeVodRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeVodRefreshTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodRefreshTasksResponseBody

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
            temp_model = DescribeVodRefreshTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodStorageDataRequest(TeaModel):
    def __init__(self, owner_id=None, start_time=None, end_time=None, region=None, storage_type=None, storage=None,
                 interval=None):
        self.owner_id = owner_id  # type: long
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.region = TeaConverter.to_unicode(region)  # type: unicode
        self.storage_type = TeaConverter.to_unicode(storage_type)  # type: unicode
        self.storage = TeaConverter.to_unicode(storage)  # type: unicode
        self.interval = TeaConverter.to_unicode(interval)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region is not None:
            result['Region'] = self.region
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeVodStorageDataResponseBodyStorageDataStorageDataItem(TeaModel):
    def __init__(self, storage_utilization=None, time_stamp=None, network_out=None):
        self.storage_utilization = TeaConverter.to_unicode(storage_utilization)  # type: unicode
        self.time_stamp = TeaConverter.to_unicode(time_stamp)  # type: unicode
        self.network_out = TeaConverter.to_unicode(network_out)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.storage_utilization is not None:
            result['StorageUtilization'] = self.storage_utilization
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.network_out is not None:
            result['NetworkOut'] = self.network_out
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageUtilization') is not None:
            self.storage_utilization = m.get('StorageUtilization')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('NetworkOut') is not None:
            self.network_out = m.get('NetworkOut')
        return self


class DescribeVodStorageDataResponseBodyStorageData(TeaModel):
    def __init__(self, storage_data_item=None):
        self.storage_data_item = storage_data_item  # type: list[DescribeVodStorageDataResponseBodyStorageDataStorageDataItem]

    def validate(self):
        if self.storage_data_item:
            for k in self.storage_data_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['StorageDataItem'] = []
        if self.storage_data_item is not None:
            for k in self.storage_data_item:
                result['StorageDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.storage_data_item = []
        if m.get('StorageDataItem') is not None:
            for k in m.get('StorageDataItem'):
                temp_model = DescribeVodStorageDataResponseBodyStorageDataStorageDataItem()
                self.storage_data_item.append(temp_model.from_map(k))
        return self


class DescribeVodStorageDataResponseBody(TeaModel):
    def __init__(self, request_id=None, data_interval=None, storage_data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data_interval = TeaConverter.to_unicode(data_interval)  # type: unicode
        self.storage_data = storage_data  # type: DescribeVodStorageDataResponseBodyStorageData

    def validate(self):
        if self.storage_data:
            self.storage_data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.storage_data is not None:
            result['StorageData'] = self.storage_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('StorageData') is not None:
            temp_model = DescribeVodStorageDataResponseBodyStorageData()
            self.storage_data = temp_model.from_map(m['StorageData'])
        return self


class DescribeVodStorageDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodStorageDataResponseBody

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
            temp_model = DescribeVodStorageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodTagResourcesRequestTag(TeaModel):
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


class DescribeVodTagResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_type=None, scope=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.scope = TeaConverter.to_unicode(scope)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag = tag  # type: list[DescribeVodTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeVodTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeVodTagResourcesResponseBodyTagResourcesTag(TeaModel):
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


class DescribeVodTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag=None, resource_id=None):
        self.tag = tag  # type: list[DescribeVodTagResourcesResponseBodyTagResourcesTag]
        self.resource_id = TeaConverter.to_unicode(resource_id)  # type: unicode

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeVodTagResourcesResponseBodyTagResourcesTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DescribeVodTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_resources=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.tag_resources = tag_resources  # type: list[DescribeVodTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = DescribeVodTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeVodTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodTagResourcesResponseBody

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
            temp_model = DescribeVodTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodTranscodeDataRequest(TeaModel):
    def __init__(self, owner_id=None, start_time=None, end_time=None, region=None, interval=None, storage=None,
                 specification=None):
        self.owner_id = owner_id  # type: long
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.region = TeaConverter.to_unicode(region)  # type: unicode
        self.interval = TeaConverter.to_unicode(interval)  # type: unicode
        self.storage = TeaConverter.to_unicode(storage)  # type: unicode
        self.specification = TeaConverter.to_unicode(specification)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region is not None:
            result['Region'] = self.region
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemDataDataItem(TeaModel):
    def __init__(self, value=None, name=None):
        self.value = TeaConverter.to_unicode(value)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemData(TeaModel):
    def __init__(self, data_item=None):
        self.data_item = data_item  # type: list[DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemDataDataItem]

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataItem'] = []
        if self.data_item is not None:
            for k in self.data_item:
                result['DataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_item = []
        if m.get('DataItem') is not None:
            for k in m.get('DataItem'):
                temp_model = DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemDataDataItem()
                self.data_item.append(temp_model.from_map(k))
        return self


class DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItem(TeaModel):
    def __init__(self, data=None, time_stamp=None):
        self.data = data  # type: DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemData
        self.time_stamp = TeaConverter.to_unicode(time_stamp)  # type: unicode

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVodTranscodeDataResponseBodyTranscodeData(TeaModel):
    def __init__(self, transcode_data_item=None):
        self.transcode_data_item = transcode_data_item  # type: list[DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItem]

    def validate(self):
        if self.transcode_data_item:
            for k in self.transcode_data_item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TranscodeDataItem'] = []
        if self.transcode_data_item is not None:
            for k in self.transcode_data_item:
                result['TranscodeDataItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.transcode_data_item = []
        if m.get('TranscodeDataItem') is not None:
            for k in m.get('TranscodeDataItem'):
                temp_model = DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItem()
                self.transcode_data_item.append(temp_model.from_map(k))
        return self


class DescribeVodTranscodeDataResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_data=None, data_interval=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.transcode_data = transcode_data  # type: DescribeVodTranscodeDataResponseBodyTranscodeData
        self.data_interval = TeaConverter.to_unicode(data_interval)  # type: unicode

    def validate(self):
        if self.transcode_data:
            self.transcode_data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transcode_data is not None:
            result['TranscodeData'] = self.transcode_data.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TranscodeData') is not None:
            temp_model = DescribeVodTranscodeDataResponseBodyTranscodeData()
            self.transcode_data = temp_model.from_map(m['TranscodeData'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        return self


class DescribeVodTranscodeDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodTranscodeDataResponseBody

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
            temp_model = DescribeVodTranscodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodUserDomainsRequestTag(TeaModel):
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


class DescribeVodUserDomainsRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, page_size=None, page_number=None, domain_name=None,
                 domain_status=None, domain_search_type=None, cdn_type=None, check_domain_show=None, func_id=None,
                 func_filter=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.domain_status = TeaConverter.to_unicode(domain_status)  # type: unicode
        self.domain_search_type = TeaConverter.to_unicode(domain_search_type)  # type: unicode
        self.cdn_type = TeaConverter.to_unicode(cdn_type)  # type: unicode
        self.check_domain_show = check_domain_show  # type: bool
        self.func_id = TeaConverter.to_unicode(func_id)  # type: unicode
        self.func_filter = TeaConverter.to_unicode(func_filter)  # type: unicode
        self.tag = tag  # type: list[DescribeVodUserDomainsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type
        if self.check_domain_show is not None:
            result['CheckDomainShow'] = self.check_domain_show
        if self.func_id is not None:
            result['FuncId'] = self.func_id
        if self.func_filter is not None:
            result['FuncFilter'] = self.func_filter
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')
        if m.get('CheckDomainShow') is not None:
            self.check_domain_show = m.get('CheckDomainShow')
        if m.get('FuncId') is not None:
            self.func_id = m.get('FuncId')
        if m.get('FuncFilter') is not None:
            self.func_filter = m.get('FuncFilter')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeVodUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeVodUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, type=None, priority=None, port=None, content=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.priority = TeaConverter.to_unicode(priority)  # type: unicode
        self.port = port  # type: int
        self.content = TeaConverter.to_unicode(content)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.port is not None:
            result['Port'] = self.port
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeVodUserDomainsResponseBodyDomainsPageDataSources(TeaModel):
    def __init__(self, source=None):
        self.source = source  # type: list[DescribeVodUserDomainsResponseBodyDomainsPageDataSourcesSource]

    def validate(self):
        if self.source:
            for k in self.source:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Source'] = []
        if self.source is not None:
            for k in self.source:
                result['Source'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.source = []
        if m.get('Source') is not None:
            for k in m.get('Source'):
                temp_model = DescribeVodUserDomainsResponseBodyDomainsPageDataSourcesSource()
                self.source.append(temp_model.from_map(k))
        return self


class DescribeVodUserDomainsResponseBodyDomainsPageData(TeaModel):
    def __init__(self, gmt_created=None, ssl_protocol=None, description=None, sandbox=None, cname=None,
                 domain_status=None, sources=None, gmt_modified=None, domain_name=None):
        self.gmt_created = TeaConverter.to_unicode(gmt_created)  # type: unicode
        self.ssl_protocol = TeaConverter.to_unicode(ssl_protocol)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.sandbox = TeaConverter.to_unicode(sandbox)  # type: unicode
        self.cname = TeaConverter.to_unicode(cname)  # type: unicode
        self.domain_status = TeaConverter.to_unicode(domain_status)  # type: unicode
        self.sources = sources  # type: DescribeVodUserDomainsResponseBodyDomainsPageDataSources
        self.gmt_modified = TeaConverter.to_unicode(gmt_modified)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        if self.description is not None:
            result['Description'] = self.description
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('Sources') is not None:
            temp_model = DescribeVodUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVodUserDomainsResponseBodyDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data  # type: list[DescribeVodUserDomainsResponseBodyDomainsPageData]

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = DescribeVodUserDomainsResponseBodyDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        return self


class DescribeVodUserDomainsResponseBody(TeaModel):
    def __init__(self, domains=None, total_count=None, request_id=None, page_size=None, page_number=None):
        self.domains = domains  # type: DescribeVodUserDomainsResponseBodyDomains
        self.total_count = total_count  # type: long
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
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
        if m.get('Domains') is not None:
            temp_model = DescribeVodUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeVodUserDomainsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodUserDomainsResponseBody

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
            temp_model = DescribeVodUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodUserTagsRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVodUserTagsResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = TeaConverter.to_unicode(key)  # type: unicode
        self.value = value  # type: list[unicode]

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


class DescribeVodUserTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.tags = tags  # type: list[DescribeVodUserTagsResponseBodyTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeVodUserTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeVodUserTagsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodUserTagsResponseBody

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
            temp_model = DescribeVodUserTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodVerifyContentRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribeVodVerifyContentResponseBody(TeaModel):
    def __init__(self, request_id=None, content=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.content = TeaConverter.to_unicode(content)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeVodVerifyContentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DescribeVodVerifyContentResponseBody

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
            temp_model = DescribeVodVerifyContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachAppPolicyFromIdentityRequest(TeaModel):
    def __init__(self, identity_type=None, identity_name=None, app_id=None, policy_names=None):
        self.identity_type = TeaConverter.to_unicode(identity_type)  # type: unicode
        self.identity_name = TeaConverter.to_unicode(identity_name)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.policy_names = TeaConverter.to_unicode(policy_names)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        return self


class DetachAppPolicyFromIdentityResponseBody(TeaModel):
    def __init__(self, request_id=None, non_exist_policy_names=None, failed_policy_names=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.non_exist_policy_names = non_exist_policy_names  # type: list[unicode]
        self.failed_policy_names = failed_policy_names  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.non_exist_policy_names is not None:
            result['NonExistPolicyNames'] = self.non_exist_policy_names
        if self.failed_policy_names is not None:
            result['FailedPolicyNames'] = self.failed_policy_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NonExistPolicyNames') is not None:
            self.non_exist_policy_names = m.get('NonExistPolicyNames')
        if m.get('FailedPolicyNames') is not None:
            self.failed_policy_names = m.get('FailedPolicyNames')
        return self


class DetachAppPolicyFromIdentityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DetachAppPolicyFromIdentityResponseBody

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
            temp_model = DetachAppPolicyFromIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAICaptionExtractionJobsRequest(TeaModel):
    def __init__(self, job_ids=None):
        self.job_ids = TeaConverter.to_unicode(job_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class GetAICaptionExtractionJobsResponseBodyAICaptionExtractionJobList(TeaModel):
    def __init__(self, status=None, creation_time=None, video_id=None, job_id=None, user_data=None, code=None,
                 aicaption_extraction_result=None, message=None, template_config=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.aicaption_extraction_result = TeaConverter.to_unicode(aicaption_extraction_result)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.code is not None:
            result['Code'] = self.code
        if self.aicaption_extraction_result is not None:
            result['AICaptionExtractionResult'] = self.aicaption_extraction_result
        if self.message is not None:
            result['Message'] = self.message
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('AICaptionExtractionResult') is not None:
            self.aicaption_extraction_result = m.get('AICaptionExtractionResult')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        return self


class GetAICaptionExtractionJobsResponseBody(TeaModel):
    def __init__(self, request_id=None, aicaption_extraction_job_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.aicaption_extraction_job_list = aicaption_extraction_job_list  # type: list[GetAICaptionExtractionJobsResponseBodyAICaptionExtractionJobList]

    def validate(self):
        if self.aicaption_extraction_job_list:
            for k in self.aicaption_extraction_job_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AICaptionExtractionJobList'] = []
        if self.aicaption_extraction_job_list is not None:
            for k in self.aicaption_extraction_job_list:
                result['AICaptionExtractionJobList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.aicaption_extraction_job_list = []
        if m.get('AICaptionExtractionJobList') is not None:
            for k in m.get('AICaptionExtractionJobList'):
                temp_model = GetAICaptionExtractionJobsResponseBodyAICaptionExtractionJobList()
                self.aicaption_extraction_job_list.append(temp_model.from_map(k))
        return self


class GetAICaptionExtractionJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAICaptionExtractionJobsResponseBody

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
            temp_model = GetAICaptionExtractionJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIImageJobsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 job_ids=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.job_ids = TeaConverter.to_unicode(job_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class GetAIImageJobsResponseBodyAIImageJobList(TeaModel):
    def __init__(self, status=None, creation_time=None, aiimage_result=None, video_id=None, job_id=None,
                 user_data=None, code=None, message=None, template_config=None, template_id=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.aiimage_result = TeaConverter.to_unicode(aiimage_result)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.aiimage_result is not None:
            result['AIImageResult'] = self.aiimage_result
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('AIImageResult') is not None:
            self.aiimage_result = m.get('AIImageResult')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetAIImageJobsResponseBody(TeaModel):
    def __init__(self, aiimage_job_list=None, request_id=None):
        self.aiimage_job_list = aiimage_job_list  # type: list[GetAIImageJobsResponseBodyAIImageJobList]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.aiimage_job_list:
            for k in self.aiimage_job_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AIImageJobList'] = []
        if self.aiimage_job_list is not None:
            for k in self.aiimage_job_list:
                result['AIImageJobList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aiimage_job_list = []
        if m.get('AIImageJobList') is not None:
            for k in m.get('AIImageJobList'):
                temp_model = GetAIImageJobsResponseBodyAIImageJobList()
                self.aiimage_job_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAIImageJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAIImageJobsResponseBody

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
            temp_model = GetAIImageJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIMediaAuditJobRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult(TeaModel):
    def __init__(self, suggestion=None, score=None, label=None, scene=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.scene = TeaConverter.to_unicode(scene)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.score is not None:
            result['Score'] = self.score
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult(TeaModel):
    def __init__(self, type=None, suggestion=None, result=None, url=None, label=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.result = result  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult]
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.url is not None:
            result['Url'] = self.url
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult(TeaModel):
    def __init__(self, suggestion=None, score=None, label=None, scene=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.scene = TeaConverter.to_unicode(scene)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.score is not None:
            result['Score'] = self.score
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult(TeaModel):
    def __init__(self, logo_result=None, suggestion=None, live_result=None, porn_result=None, ad_result=None,
                 label=None, terrorism_result=None):
        self.logo_result = logo_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.live_result = live_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult
        self.porn_result = porn_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult
        self.ad_result = ad_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.terrorism_result = terrorism_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult

    def validate(self):
        if self.logo_result:
            self.logo_result.validate()
        if self.live_result:
            self.live_result.validate()
        if self.porn_result:
            self.porn_result.validate()
        if self.ad_result:
            self.ad_result.validate()
        if self.terrorism_result:
            self.terrorism_result.validate()

    def to_map(self):
        result = dict()
        if self.logo_result is not None:
            result['LogoResult'] = self.logo_result.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.live_result is not None:
            result['LiveResult'] = self.live_result.to_map()
        if self.porn_result is not None:
            result['PornResult'] = self.porn_result.to_map()
        if self.ad_result is not None:
            result['AdResult'] = self.ad_result.to_map()
        if self.label is not None:
            result['Label'] = self.label
        if self.terrorism_result is not None:
            result['TerrorismResult'] = self.terrorism_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogoResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult()
            self.logo_result = temp_model.from_map(m['LogoResult'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('LiveResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult()
            self.live_result = temp_model.from_map(m['LiveResult'])
        if m.get('PornResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult()
            self.porn_result = temp_model.from_map(m['PornResult'])
        if m.get('AdResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult()
            self.ad_result = temp_model.from_map(m['AdResult'])
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('TerrorismResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult()
            self.terrorism_result = temp_model.from_map(m['TerrorismResult'])
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult(TeaModel):
    def __init__(self, type=None, suggestion=None, score=None, label=None, content=None, scene=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.content = TeaConverter.to_unicode(content)  # type: unicode
        self.scene = TeaConverter.to_unicode(scene)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.score is not None:
            result['Score'] = self.score
        if self.label is not None:
            result['Label'] = self.label
        if self.content is not None:
            result['Content'] = self.content
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobData(TeaModel):
    def __init__(self, suggestion=None, image_result=None, audio_result=None, video_result=None,
                 abnormal_modules=None, label=None, text_result=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.image_result = image_result  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult]
        self.audio_result = audio_result  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult]
        self.video_result = video_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult
        self.abnormal_modules = TeaConverter.to_unicode(abnormal_modules)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.text_result = text_result  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult]

    def validate(self):
        if self.image_result:
            for k in self.image_result:
                if k:
                    k.validate()
        if self.audio_result:
            for k in self.audio_result:
                if k:
                    k.validate()
        if self.video_result:
            self.video_result.validate()
        if self.text_result:
            for k in self.text_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['ImageResult'] = []
        if self.image_result is not None:
            for k in self.image_result:
                result['ImageResult'].append(k.to_map() if k else None)
        result['AudioResult'] = []
        if self.audio_result is not None:
            for k in self.audio_result:
                result['AudioResult'].append(k.to_map() if k else None)
        if self.video_result is not None:
            result['VideoResult'] = self.video_result.to_map()
        if self.abnormal_modules is not None:
            result['AbnormalModules'] = self.abnormal_modules
        if self.label is not None:
            result['Label'] = self.label
        result['TextResult'] = []
        if self.text_result is not None:
            for k in self.text_result:
                result['TextResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.image_result = []
        if m.get('ImageResult') is not None:
            for k in m.get('ImageResult'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult()
                self.image_result.append(temp_model.from_map(k))
        self.audio_result = []
        if m.get('AudioResult') is not None:
            for k in m.get('AudioResult'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult()
                self.audio_result.append(temp_model.from_map(k))
        if m.get('VideoResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult()
            self.video_result = temp_model.from_map(m['VideoResult'])
        if m.get('AbnormalModules') is not None:
            self.abnormal_modules = m.get('AbnormalModules')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        self.text_result = []
        if m.get('TextResult') is not None:
            for k in m.get('TextResult'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult()
                self.text_result.append(temp_model.from_map(k))
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJob(TeaModel):
    def __init__(self, creation_time=None, type=None, status=None, data=None, complete_time=None, job_id=None,
                 code=None, message=None, media_id=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.data = data  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobData
        self.complete_time = TeaConverter.to_unicode(complete_time)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Data') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetAIMediaAuditJobResponseBody(TeaModel):
    def __init__(self, request_id=None, media_audit_job=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.media_audit_job = media_audit_job  # type: GetAIMediaAuditJobResponseBodyMediaAuditJob

    def validate(self):
        if self.media_audit_job:
            self.media_audit_job.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_audit_job is not None:
            result['MediaAuditJob'] = self.media_audit_job.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaAuditJob') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJob()
            self.media_audit_job = temp_model.from_map(m['MediaAuditJob'])
        return self


class GetAIMediaAuditJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAIMediaAuditJobResponseBody

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
            temp_model = GetAIMediaAuditJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAITemplateRequest(TeaModel):
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


class GetAITemplateResponseBodyTemplateInfo(TeaModel):
    def __init__(self, creation_time=None, is_default=None, template_type=None, template_config=None,
                 template_name=None, source=None, template_id=None, modify_time=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode
        self.template_name = TeaConverter.to_unicode(template_name)  # type: unicode
        self.source = TeaConverter.to_unicode(source)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.modify_time = TeaConverter.to_unicode(modify_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.source is not None:
            result['Source'] = self.source
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetAITemplateResponseBody(TeaModel):
    def __init__(self, template_info=None, request_id=None):
        self.template_info = template_info  # type: GetAITemplateResponseBodyTemplateInfo
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        result = dict()
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateInfo') is not None:
            temp_model = GetAITemplateResponseBodyTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAITemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAITemplateResponseBody

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
            temp_model = GetAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIVideoTagResultRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 media_id=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultTime(TeaModel):
    def __init__(self, times=None, tag=None):
        self.times = times  # type: list[unicode]
        self.tag = TeaConverter.to_unicode(tag)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.times is not None:
            result['Times'] = self.times
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Times') is not None:
            self.times = m.get('Times')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultKeyword(TeaModel):
    def __init__(self, times=None, tag=None):
        self.times = times  # type: list[unicode]
        self.tag = TeaConverter.to_unicode(tag)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.times is not None:
            result['Times'] = self.times
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Times') is not None:
            self.times = m.get('Times')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultCategory(TeaModel):
    def __init__(self, tag=None):
        self.tag = TeaConverter.to_unicode(tag)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultPerson(TeaModel):
    def __init__(self, face_url=None, times=None, tag=None):
        self.face_url = TeaConverter.to_unicode(face_url)  # type: unicode
        self.times = times  # type: list[unicode]
        self.tag = TeaConverter.to_unicode(tag)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.times is not None:
            result['Times'] = self.times
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultLocation(TeaModel):
    def __init__(self, times=None, tag=None):
        self.times = times  # type: list[unicode]
        self.tag = TeaConverter.to_unicode(tag)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.times is not None:
            result['Times'] = self.times
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Times') is not None:
            self.times = m.get('Times')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResult(TeaModel):
    def __init__(self, time=None, keyword=None, category=None, person=None, location=None):
        self.time = time  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultTime]
        self.keyword = keyword  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultKeyword]
        self.category = category  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultCategory]
        self.person = person  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultPerson]
        self.location = location  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultLocation]

    def validate(self):
        if self.time:
            for k in self.time:
                if k:
                    k.validate()
        if self.keyword:
            for k in self.keyword:
                if k:
                    k.validate()
        if self.category:
            for k in self.category:
                if k:
                    k.validate()
        if self.person:
            for k in self.person:
                if k:
                    k.validate()
        if self.location:
            for k in self.location:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Time'] = []
        if self.time is not None:
            for k in self.time:
                result['Time'].append(k.to_map() if k else None)
        result['Keyword'] = []
        if self.keyword is not None:
            for k in self.keyword:
                result['Keyword'].append(k.to_map() if k else None)
        result['Category'] = []
        if self.category is not None:
            for k in self.category:
                result['Category'].append(k.to_map() if k else None)
        result['Person'] = []
        if self.person is not None:
            for k in self.person:
                result['Person'].append(k.to_map() if k else None)
        result['Location'] = []
        if self.location is not None:
            for k in self.location:
                result['Location'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.time = []
        if m.get('Time') is not None:
            for k in m.get('Time'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultTime()
                self.time.append(temp_model.from_map(k))
        self.keyword = []
        if m.get('Keyword') is not None:
            for k in m.get('Keyword'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultKeyword()
                self.keyword.append(temp_model.from_map(k))
        self.category = []
        if m.get('Category') is not None:
            for k in m.get('Category'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultCategory()
                self.category.append(temp_model.from_map(k))
        self.person = []
        if m.get('Person') is not None:
            for k in m.get('Person'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultPerson()
                self.person.append(temp_model.from_map(k))
        self.location = []
        if m.get('Location') is not None:
            for k in m.get('Location'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultLocation()
                self.location.append(temp_model.from_map(k))
        return self


class GetAIVideoTagResultResponseBody(TeaModel):
    def __init__(self, request_id=None, video_tag_result=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.video_tag_result = video_tag_result  # type: GetAIVideoTagResultResponseBodyVideoTagResult

    def validate(self):
        if self.video_tag_result:
            self.video_tag_result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.video_tag_result is not None:
            result['VideoTagResult'] = self.video_tag_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VideoTagResult') is not None:
            temp_model = GetAIVideoTagResultResponseBodyVideoTagResult()
            self.video_tag_result = temp_model.from_map(m['VideoTagResult'])
        return self


class GetAIVideoTagResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAIVideoTagResultResponseBody

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
            temp_model = GetAIVideoTagResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppInfosRequest(TeaModel):
    def __init__(self, resource_real_owner_id=None, app_ids=None):
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.app_ids = TeaConverter.to_unicode(app_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        return self


class GetAppInfosResponseBodyAppInfoList(TeaModel):
    def __init__(self, type=None, status=None, creation_time=None, app_name=None, description=None, app_id=None,
                 modification_time=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.app_name = TeaConverter.to_unicode(app_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        return self


class GetAppInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, app_info_list=None, non_exist_app_ids=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.app_info_list = app_info_list  # type: list[GetAppInfosResponseBodyAppInfoList]
        self.non_exist_app_ids = non_exist_app_ids  # type: list[unicode]

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        if self.non_exist_app_ids is not None:
            result['NonExistAppIds'] = self.non_exist_app_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = GetAppInfosResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        if m.get('NonExistAppIds') is not None:
            self.non_exist_app_ids = m.get('NonExistAppIds')
        return self


class GetAppInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAppInfosResponseBody

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
            temp_model = GetAppInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAttachedMediaInfoRequest(TeaModel):
    def __init__(self, media_ids=None, auth_timeout=None, resource_real_owner_id=None, output_type=None):
        self.media_ids = TeaConverter.to_unicode(media_ids)  # type: unicode
        self.auth_timeout = auth_timeout  # type: long
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.output_type = TeaConverter.to_unicode(output_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class GetAttachedMediaInfoResponseBodyAttachedMediaListCategories(TeaModel):
    def __init__(self, parent_id=None, cate_name=None, cate_id=None, level=None):
        self.parent_id = parent_id  # type: long
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.level = level  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class GetAttachedMediaInfoResponseBodyAttachedMediaList(TeaModel):
    def __init__(self, status=None, creation_time=None, storage_location=None, type=None, tags=None,
                 modification_time=None, media_id=None, description=None, categories=None, app_id=None, url=None, title=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.categories = categories  # type: list[GetAttachedMediaInfoResponseBodyAttachedMediaListCategories]
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.type is not None:
            result['Type'] = self.type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.description is not None:
            result['Description'] = self.description
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.url is not None:
            result['URL'] = self.url
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = GetAttachedMediaInfoResponseBodyAttachedMediaListCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetAttachedMediaInfoResponseBody(TeaModel):
    def __init__(self, non_exist_media_ids=None, request_id=None, attached_media_list=None):
        self.non_exist_media_ids = non_exist_media_ids  # type: list[unicode]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.attached_media_list = attached_media_list  # type: list[GetAttachedMediaInfoResponseBodyAttachedMediaList]

    def validate(self):
        if self.attached_media_list:
            for k in self.attached_media_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AttachedMediaList'] = []
        if self.attached_media_list is not None:
            for k in self.attached_media_list:
                result['AttachedMediaList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.attached_media_list = []
        if m.get('AttachedMediaList') is not None:
            for k in m.get('AttachedMediaList'):
                temp_model = GetAttachedMediaInfoResponseBodyAttachedMediaList()
                self.attached_media_list.append(temp_model.from_map(k))
        return self


class GetAttachedMediaInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAttachedMediaInfoResponseBody

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
            temp_model = GetAttachedMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditHistoryRequest(TeaModel):
    def __init__(self, video_id=None, page_no=None, page_size=None, sort_by=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = TeaConverter.to_unicode(sort_by)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class GetAuditHistoryResponseBodyHistories(TeaModel):
    def __init__(self, status=None, creation_time=None, comment=None, reason=None, auditor=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.comment = TeaConverter.to_unicode(comment)  # type: unicode
        self.reason = TeaConverter.to_unicode(reason)  # type: unicode
        self.auditor = TeaConverter.to_unicode(auditor)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.auditor is not None:
            result['Auditor'] = self.auditor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Auditor') is not None:
            self.auditor = m.get('Auditor')
        return self


class GetAuditHistoryResponseBody(TeaModel):
    def __init__(self, status=None, request_id=None, total=None, histories=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total = total  # type: long
        self.histories = histories  # type: list[GetAuditHistoryResponseBodyHistories]

    def validate(self):
        if self.histories:
            for k in self.histories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Histories'] = []
        if self.histories is not None:
            for k in self.histories:
                result['Histories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.histories = []
        if m.get('Histories') is not None:
            for k in m.get('Histories'):
                temp_model = GetAuditHistoryResponseBodyHistories()
                self.histories.append(temp_model.from_map(k))
        return self


class GetAuditHistoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetAuditHistoryResponseBody

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
            temp_model = GetAuditHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCategoriesRequest(TeaModel):
    def __init__(self, cate_id=None, page_no=None, page_size=None, sort_by=None, type=None):
        self.cate_id = cate_id  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = TeaConverter.to_unicode(sort_by)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetCategoriesResponseBodyCategory(TeaModel):
    def __init__(self, type=None, parent_id=None, cate_name=None, cate_id=None, level=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.parent_id = parent_id  # type: long
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.level = level  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class GetCategoriesResponseBodySubCategoriesCategory(TeaModel):
    def __init__(self, type=None, cate_name=None, parent_id=None, cate_id=None, sub_total=None, level=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.parent_id = parent_id  # type: long
        self.cate_id = cate_id  # type: long
        self.sub_total = sub_total  # type: long
        self.level = level  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.sub_total is not None:
            result['SubTotal'] = self.sub_total
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('SubTotal') is not None:
            self.sub_total = m.get('SubTotal')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class GetCategoriesResponseBodySubCategories(TeaModel):
    def __init__(self, category=None):
        self.category = category  # type: list[GetCategoriesResponseBodySubCategoriesCategory]

    def validate(self):
        if self.category:
            for k in self.category:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Category'] = []
        if self.category is not None:
            for k in self.category:
                result['Category'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.category = []
        if m.get('Category') is not None:
            for k in m.get('Category'):
                temp_model = GetCategoriesResponseBodySubCategoriesCategory()
                self.category.append(temp_model.from_map(k))
        return self


class GetCategoriesResponseBody(TeaModel):
    def __init__(self, category=None, request_id=None, sub_total=None, sub_categories=None):
        self.category = category  # type: GetCategoriesResponseBodyCategory
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.sub_total = sub_total  # type: long
        self.sub_categories = sub_categories  # type: GetCategoriesResponseBodySubCategories

    def validate(self):
        if self.category:
            self.category.validate()
        if self.sub_categories:
            self.sub_categories.validate()

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_total is not None:
            result['SubTotal'] = self.sub_total
        if self.sub_categories is not None:
            result['SubCategories'] = self.sub_categories.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = GetCategoriesResponseBodyCategory()
            self.category = temp_model.from_map(m['Category'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubTotal') is not None:
            self.sub_total = m.get('SubTotal')
        if m.get('SubCategories') is not None:
            temp_model = GetCategoriesResponseBodySubCategories()
            self.sub_categories = temp_model.from_map(m['SubCategories'])
        return self


class GetCategoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetCategoriesResponseBody

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
            temp_model = GetCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultAITemplateRequest(TeaModel):
    def __init__(self, template_type=None):
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetDefaultAITemplateResponseBodyTemplateInfo(TeaModel):
    def __init__(self, creation_time=None, is_default=None, template_type=None, template_config=None,
                 template_name=None, source=None, template_id=None, modify_time=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode
        self.template_name = TeaConverter.to_unicode(template_name)  # type: unicode
        self.source = TeaConverter.to_unicode(source)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.modify_time = TeaConverter.to_unicode(modify_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.source is not None:
            result['Source'] = self.source
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetDefaultAITemplateResponseBody(TeaModel):
    def __init__(self, template_info=None, request_id=None):
        self.template_info = template_info  # type: GetDefaultAITemplateResponseBodyTemplateInfo
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        result = dict()
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateInfo') is not None:
            temp_model = GetDefaultAITemplateResponseBodyTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultAITemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetDefaultAITemplateResponseBody

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
            temp_model = GetDefaultAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 project_id=None, feextend_flag=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.project_id = TeaConverter.to_unicode(project_id)  # type: unicode
        self.feextend_flag = feextend_flag  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.feextend_flag is not None:
            result['FEExtendFlag'] = self.feextend_flag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('FEExtendFlag') is not None:
            self.feextend_flag = m.get('FEExtendFlag')
        return self


class GetEditingProjectResponseBodyProject(TeaModel):
    def __init__(self, storage_location=None, status=None, creation_time=None, modified_time=None, description=None,
                 cover_url=None, project_id=None, timeline=None, title=None, region_id=None):
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.modified_time = TeaConverter.to_unicode(modified_time)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.project_id = TeaConverter.to_unicode(project_id)  # type: unicode
        self.timeline = TeaConverter.to_unicode(timeline)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.description is not None:
            result['Description'] = self.description
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetEditingProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: GetEditingProjectResponseBodyProject
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = GetEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetEditingProjectResponseBody

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
            temp_model = GetEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 project_id=None, type=None, material_type=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.project_id = TeaConverter.to_unicode(project_id)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.material_type = TeaConverter.to_unicode(material_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        return self


class GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites(TeaModel):
    def __init__(self, sprite=None):
        self.sprite = sprite  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sprite is not None:
            result['Sprite'] = self.sprite
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Sprite') is not None:
            self.sprite = m.get('Sprite')
        return self


class GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        return self


class GetEditingProjectMaterialsResponseBodyMaterialListMaterial(TeaModel):
    def __init__(self, creation_time=None, status=None, sprites=None, cate_id=None, tags=None, material_type=None,
                 sprite_config=None, source=None, snapshots=None, cate_name=None, modified_time=None, description=None,
                 material_id=None, size=None, cover_url=None, duration=None, title=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.sprites = sprites  # type: GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites
        self.cate_id = cate_id  # type: int
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.material_type = TeaConverter.to_unicode(material_type)  # type: unicode
        self.sprite_config = TeaConverter.to_unicode(sprite_config)  # type: unicode
        self.source = TeaConverter.to_unicode(source)  # type: unicode
        self.snapshots = snapshots  # type: GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.modified_time = TeaConverter.to_unicode(modified_time)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.material_id = TeaConverter.to_unicode(material_id)  # type: unicode
        self.size = size  # type: long
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.duration = duration  # type: float
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        if self.sprites:
            self.sprites.validate()
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.sprites is not None:
            result['Sprites'] = self.sprites.to_map()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.sprite_config is not None:
            result['SpriteConfig'] = self.sprite_config
        if self.source is not None:
            result['Source'] = self.source
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.description is not None:
            result['Description'] = self.description
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.size is not None:
            result['Size'] = self.size
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sprites') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites()
            self.sprites = temp_model.from_map(m['Sprites'])
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('SpriteConfig') is not None:
            self.sprite_config = m.get('SpriteConfig')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Snapshots') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetEditingProjectMaterialsResponseBodyMaterialList(TeaModel):
    def __init__(self, material=None):
        self.material = material  # type: list[GetEditingProjectMaterialsResponseBodyMaterialListMaterial]

    def validate(self):
        if self.material:
            for k in self.material:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Material'] = []
        if self.material is not None:
            for k in self.material:
                result['Material'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.material = []
        if m.get('Material') is not None:
            for k in m.get('Material'):
                temp_model = GetEditingProjectMaterialsResponseBodyMaterialListMaterial()
                self.material.append(temp_model.from_map(k))
        return self


class GetEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(self, request_id=None, material_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.material_list = material_list  # type: GetEditingProjectMaterialsResponseBodyMaterialList

    def validate(self):
        if self.material_list:
            self.material_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.material_list is not None:
            result['MaterialList'] = self.material_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaterialList') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMaterialList()
            self.material_list = temp_model.from_map(m['MaterialList'])
        return self


class GetEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetEditingProjectMaterialsResponseBody

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
            temp_model = GetEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageInfoRequest(TeaModel):
    def __init__(self, image_id=None, auth_timeout=None, output_type=None):
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode
        self.auth_timeout = auth_timeout  # type: long
        self.output_type = TeaConverter.to_unicode(output_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class GetImageInfoResponseBodyImageInfoMezzanine(TeaModel):
    def __init__(self, file_url=None, width=None, height=None, original_file_name=None, file_size=None):
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.width = width  # type: int
        self.height = height  # type: int
        self.original_file_name = TeaConverter.to_unicode(original_file_name)  # type: unicode
        self.file_size = TeaConverter.to_unicode(file_size)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class GetImageInfoResponseBodyImageInfo(TeaModel):
    def __init__(self, mezzanine=None, status=None, storage_location=None, creation_time=None, cate_id=None,
                 tags=None, cate_name=None, image_type=None, description=None, app_id=None, url=None, title=None,
                 image_id=None):
        self.mezzanine = mezzanine  # type: GetImageInfoResponseBodyImageInfoMezzanine
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.image_type = TeaConverter.to_unicode(image_type)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode

    def validate(self):
        if self.mezzanine:
            self.mezzanine.validate()

    def to_map(self):
        result = dict()
        if self.mezzanine is not None:
            result['Mezzanine'] = self.mezzanine.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.url is not None:
            result['URL'] = self.url
        if self.title is not None:
            result['Title'] = self.title
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mezzanine') is not None:
            temp_model = GetImageInfoResponseBodyImageInfoMezzanine()
            self.mezzanine = temp_model.from_map(m['Mezzanine'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class GetImageInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, image_info=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.image_info = image_info  # type: GetImageInfoResponseBodyImageInfo

    def validate(self):
        if self.image_info:
            self.image_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_info is not None:
            result['ImageInfo'] = self.image_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageInfo') is not None:
            temp_model = GetImageInfoResponseBodyImageInfo()
            self.image_info = temp_model.from_map(m['ImageInfo'])
        return self


class GetImageInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetImageInfoResponseBody

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
            temp_model = GetImageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaAuditAudioResultDetailRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 media_id=None, page_no=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.page_no = page_no  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetailList(TeaModel):
    def __init__(self, end_time=None, start_time=None, text=None, label=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.text = TeaConverter.to_unicode(text)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.text is not None:
            result['Text'] = self.text
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetail(TeaModel):
    def __init__(self, list=None, page_total=None, total=None):
        self.list = list  # type: list[GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetailList]
        self.page_total = page_total  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetailList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetMediaAuditAudioResultDetailResponseBody(TeaModel):
    def __init__(self, media_audit_audio_result_detail=None, request_id=None):
        self.media_audit_audio_result_detail = media_audit_audio_result_detail  # type: GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetail
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.media_audit_audio_result_detail:
            self.media_audit_audio_result_detail.validate()

    def to_map(self):
        result = dict()
        if self.media_audit_audio_result_detail is not None:
            result['MediaAuditAudioResultDetail'] = self.media_audit_audio_result_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaAuditAudioResultDetail') is not None:
            temp_model = GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetail()
            self.media_audit_audio_result_detail = temp_model.from_map(m['MediaAuditAudioResultDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMediaAuditAudioResultDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetMediaAuditAudioResultDetailResponseBody

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
            temp_model = GetMediaAuditAudioResultDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaAuditResultRequest(TeaModel):
    def __init__(self, media_id=None):
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult(TeaModel):
    def __init__(self, suggestion=None, score=None, label=None, scene=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.scene = TeaConverter.to_unicode(scene)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.score is not None:
            result['Score'] = self.score
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultImageResult(TeaModel):
    def __init__(self, type=None, suggestion=None, result=None, url=None, label=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.result = result  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult]
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.url is not None:
            result['Url'] = self.url
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultAudioResult(TeaModel):
    def __init__(self, suggestion=None, score=None, label=None, scene=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.scene = TeaConverter.to_unicode(scene)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.score is not None:
            result['Score'] = self.score
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList(TeaModel):
    def __init__(self, url=None, score=None, timestamp=None, label=None):
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultCounterList(TeaModel):
    def __init__(self, label=None, count=None):
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.count = count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult(TeaModel):
    def __init__(self, suggestion=None, top_list=None, average_score=None, counter_list=None, label=None,
                 max_score=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList]
        self.average_score = TeaConverter.to_unicode(average_score)  # type: unicode
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultCounterList]
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.max_score = TeaConverter.to_unicode(max_score)  # type: unicode

    def validate(self):
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        if self.average_score is not None:
            result['AverageScore'] = self.average_score
        result['CounterList'] = []
        if self.counter_list is not None:
            for k in self.counter_list:
                result['CounterList'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList()
                self.top_list.append(temp_model.from_map(k))
        if m.get('AverageScore') is not None:
            self.average_score = m.get('AverageScore')
        self.counter_list = []
        if m.get('CounterList') is not None:
            for k in m.get('CounterList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultCounterList()
                self.counter_list.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResult(TeaModel):
    def __init__(self, logo_result=None, suggestion=None, live_result=None, porn_result=None, ad_result=None,
                 label=None, terrorism_result=None):
        self.logo_result = logo_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.live_result = live_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult
        self.porn_result = porn_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult
        self.ad_result = ad_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.terrorism_result = terrorism_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult

    def validate(self):
        if self.logo_result:
            self.logo_result.validate()
        if self.live_result:
            self.live_result.validate()
        if self.porn_result:
            self.porn_result.validate()
        if self.ad_result:
            self.ad_result.validate()
        if self.terrorism_result:
            self.terrorism_result.validate()

    def to_map(self):
        result = dict()
        if self.logo_result is not None:
            result['LogoResult'] = self.logo_result.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.live_result is not None:
            result['LiveResult'] = self.live_result.to_map()
        if self.porn_result is not None:
            result['PornResult'] = self.porn_result.to_map()
        if self.ad_result is not None:
            result['AdResult'] = self.ad_result.to_map()
        if self.label is not None:
            result['Label'] = self.label
        if self.terrorism_result is not None:
            result['TerrorismResult'] = self.terrorism_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogoResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult()
            self.logo_result = temp_model.from_map(m['LogoResult'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('LiveResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult()
            self.live_result = temp_model.from_map(m['LiveResult'])
        if m.get('PornResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult()
            self.porn_result = temp_model.from_map(m['PornResult'])
        if m.get('AdResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult()
            self.ad_result = temp_model.from_map(m['AdResult'])
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('TerrorismResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult()
            self.terrorism_result = temp_model.from_map(m['TerrorismResult'])
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultTextResult(TeaModel):
    def __init__(self, type=None, suggestion=None, score=None, label=None, content=None, scene=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.content = TeaConverter.to_unicode(content)  # type: unicode
        self.scene = TeaConverter.to_unicode(scene)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.score is not None:
            result['Score'] = self.score
        if self.label is not None:
            result['Label'] = self.label
        if self.content is not None:
            result['Content'] = self.content
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResult(TeaModel):
    def __init__(self, suggestion=None, image_result=None, audio_result=None, video_result=None,
                 abnormal_modules=None, label=None, text_result=None):
        self.suggestion = TeaConverter.to_unicode(suggestion)  # type: unicode
        self.image_result = image_result  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultImageResult]
        self.audio_result = audio_result  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultAudioResult]
        self.video_result = video_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResult
        self.abnormal_modules = TeaConverter.to_unicode(abnormal_modules)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode
        self.text_result = text_result  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultTextResult]

    def validate(self):
        if self.image_result:
            for k in self.image_result:
                if k:
                    k.validate()
        if self.audio_result:
            for k in self.audio_result:
                if k:
                    k.validate()
        if self.video_result:
            self.video_result.validate()
        if self.text_result:
            for k in self.text_result:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['ImageResult'] = []
        if self.image_result is not None:
            for k in self.image_result:
                result['ImageResult'].append(k.to_map() if k else None)
        result['AudioResult'] = []
        if self.audio_result is not None:
            for k in self.audio_result:
                result['AudioResult'].append(k.to_map() if k else None)
        if self.video_result is not None:
            result['VideoResult'] = self.video_result.to_map()
        if self.abnormal_modules is not None:
            result['AbnormalModules'] = self.abnormal_modules
        if self.label is not None:
            result['Label'] = self.label
        result['TextResult'] = []
        if self.text_result is not None:
            for k in self.text_result:
                result['TextResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.image_result = []
        if m.get('ImageResult') is not None:
            for k in m.get('ImageResult'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultImageResult()
                self.image_result.append(temp_model.from_map(k))
        self.audio_result = []
        if m.get('AudioResult') is not None:
            for k in m.get('AudioResult'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultAudioResult()
                self.audio_result.append(temp_model.from_map(k))
        if m.get('VideoResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResult()
            self.video_result = temp_model.from_map(m['VideoResult'])
        if m.get('AbnormalModules') is not None:
            self.abnormal_modules = m.get('AbnormalModules')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        self.text_result = []
        if m.get('TextResult') is not None:
            for k in m.get('TextResult'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultTextResult()
                self.text_result.append(temp_model.from_map(k))
        return self


class GetMediaAuditResultResponseBody(TeaModel):
    def __init__(self, request_id=None, media_audit_result=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.media_audit_result = media_audit_result  # type: GetMediaAuditResultResponseBodyMediaAuditResult

    def validate(self):
        if self.media_audit_result:
            self.media_audit_result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_audit_result is not None:
            result['MediaAuditResult'] = self.media_audit_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaAuditResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResult()
            self.media_audit_result = temp_model.from_map(m['MediaAuditResult'])
        return self


class GetMediaAuditResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetMediaAuditResultResponseBody

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
            temp_model = GetMediaAuditResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaAuditResultDetailRequest(TeaModel):
    def __init__(self, media_id=None, page_no=None):
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.page_no = page_no  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class GetMediaAuditResultDetailResponseBodyMediaAuditResultDetailList(TeaModel):
    def __init__(self, terrorism_score=None, ad_label=None, porn_score=None, porn_label=None, live_label=None,
                 url=None, timestamp=None, live_score=None, ad_score=None, logo_score=None, logo_label=None,
                 terrorism_label=None):
        self.terrorism_score = TeaConverter.to_unicode(terrorism_score)  # type: unicode
        self.ad_label = TeaConverter.to_unicode(ad_label)  # type: unicode
        self.porn_score = TeaConverter.to_unicode(porn_score)  # type: unicode
        self.porn_label = TeaConverter.to_unicode(porn_label)  # type: unicode
        self.live_label = TeaConverter.to_unicode(live_label)  # type: unicode
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.live_score = TeaConverter.to_unicode(live_score)  # type: unicode
        self.ad_score = TeaConverter.to_unicode(ad_score)  # type: unicode
        self.logo_score = TeaConverter.to_unicode(logo_score)  # type: unicode
        self.logo_label = TeaConverter.to_unicode(logo_label)  # type: unicode
        self.terrorism_label = TeaConverter.to_unicode(terrorism_label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.terrorism_score is not None:
            result['TerrorismScore'] = self.terrorism_score
        if self.ad_label is not None:
            result['AdLabel'] = self.ad_label
        if self.porn_score is not None:
            result['PornScore'] = self.porn_score
        if self.porn_label is not None:
            result['PornLabel'] = self.porn_label
        if self.live_label is not None:
            result['LiveLabel'] = self.live_label
        if self.url is not None:
            result['Url'] = self.url
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.live_score is not None:
            result['LiveScore'] = self.live_score
        if self.ad_score is not None:
            result['AdScore'] = self.ad_score
        if self.logo_score is not None:
            result['LogoScore'] = self.logo_score
        if self.logo_label is not None:
            result['LogoLabel'] = self.logo_label
        if self.terrorism_label is not None:
            result['TerrorismLabel'] = self.terrorism_label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TerrorismScore') is not None:
            self.terrorism_score = m.get('TerrorismScore')
        if m.get('AdLabel') is not None:
            self.ad_label = m.get('AdLabel')
        if m.get('PornScore') is not None:
            self.porn_score = m.get('PornScore')
        if m.get('PornLabel') is not None:
            self.porn_label = m.get('PornLabel')
        if m.get('LiveLabel') is not None:
            self.live_label = m.get('LiveLabel')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('LiveScore') is not None:
            self.live_score = m.get('LiveScore')
        if m.get('AdScore') is not None:
            self.ad_score = m.get('AdScore')
        if m.get('LogoScore') is not None:
            self.logo_score = m.get('LogoScore')
        if m.get('LogoLabel') is not None:
            self.logo_label = m.get('LogoLabel')
        if m.get('TerrorismLabel') is not None:
            self.terrorism_label = m.get('TerrorismLabel')
        return self


class GetMediaAuditResultDetailResponseBodyMediaAuditResultDetail(TeaModel):
    def __init__(self, list=None, total=None):
        self.list = list  # type: list[GetMediaAuditResultDetailResponseBodyMediaAuditResultDetailList]
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetMediaAuditResultDetailResponseBodyMediaAuditResultDetailList()
                self.list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetMediaAuditResultDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, media_audit_result_detail=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.media_audit_result_detail = media_audit_result_detail  # type: GetMediaAuditResultDetailResponseBodyMediaAuditResultDetail

    def validate(self):
        if self.media_audit_result_detail:
            self.media_audit_result_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_audit_result_detail is not None:
            result['MediaAuditResultDetail'] = self.media_audit_result_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaAuditResultDetail') is not None:
            temp_model = GetMediaAuditResultDetailResponseBodyMediaAuditResultDetail()
            self.media_audit_result_detail = temp_model.from_map(m['MediaAuditResultDetail'])
        return self


class GetMediaAuditResultDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetMediaAuditResultDetailResponseBody

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
            temp_model = GetMediaAuditResultDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaAuditResultTimelineRequest(TeaModel):
    def __init__(self, media_id=None):
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive(TeaModel):
    def __init__(self, score=None, timestamp=None, label=None):
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd(TeaModel):
    def __init__(self, score=None, timestamp=None, label=None):
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo(TeaModel):
    def __init__(self, score=None, timestamp=None, label=None):
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism(TeaModel):
    def __init__(self, score=None, timestamp=None, label=None):
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn(TeaModel):
    def __init__(self, score=None, timestamp=None, label=None):
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.timestamp = TeaConverter.to_unicode(timestamp)  # type: unicode
        self.label = TeaConverter.to_unicode(label)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline(TeaModel):
    def __init__(self, live=None, ad=None, logo=None, terrorism=None, porn=None):
        self.live = live  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive]
        self.ad = ad  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd]
        self.logo = logo  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo]
        self.terrorism = terrorism  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism]
        self.porn = porn  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn]

    def validate(self):
        if self.live:
            for k in self.live:
                if k:
                    k.validate()
        if self.ad:
            for k in self.ad:
                if k:
                    k.validate()
        if self.logo:
            for k in self.logo:
                if k:
                    k.validate()
        if self.terrorism:
            for k in self.terrorism:
                if k:
                    k.validate()
        if self.porn:
            for k in self.porn:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Live'] = []
        if self.live is not None:
            for k in self.live:
                result['Live'].append(k.to_map() if k else None)
        result['Ad'] = []
        if self.ad is not None:
            for k in self.ad:
                result['Ad'].append(k.to_map() if k else None)
        result['Logo'] = []
        if self.logo is not None:
            for k in self.logo:
                result['Logo'].append(k.to_map() if k else None)
        result['Terrorism'] = []
        if self.terrorism is not None:
            for k in self.terrorism:
                result['Terrorism'].append(k.to_map() if k else None)
        result['Porn'] = []
        if self.porn is not None:
            for k in self.porn:
                result['Porn'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live = []
        if m.get('Live') is not None:
            for k in m.get('Live'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive()
                self.live.append(temp_model.from_map(k))
        self.ad = []
        if m.get('Ad') is not None:
            for k in m.get('Ad'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd()
                self.ad.append(temp_model.from_map(k))
        self.logo = []
        if m.get('Logo') is not None:
            for k in m.get('Logo'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo()
                self.logo.append(temp_model.from_map(k))
        self.terrorism = []
        if m.get('Terrorism') is not None:
            for k in m.get('Terrorism'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism()
                self.terrorism.append(temp_model.from_map(k))
        self.porn = []
        if m.get('Porn') is not None:
            for k in m.get('Porn'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn()
                self.porn.append(temp_model.from_map(k))
        return self


class GetMediaAuditResultTimelineResponseBody(TeaModel):
    def __init__(self, request_id=None, media_audit_result_timeline=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.media_audit_result_timeline = media_audit_result_timeline  # type: GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline

    def validate(self):
        if self.media_audit_result_timeline:
            self.media_audit_result_timeline.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_audit_result_timeline is not None:
            result['MediaAuditResultTimeline'] = self.media_audit_result_timeline.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaAuditResultTimeline') is not None:
            temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline()
            self.media_audit_result_timeline = temp_model.from_map(m['MediaAuditResultTimeline'])
        return self


class GetMediaAuditResultTimelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetMediaAuditResultTimelineResponseBody

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
            temp_model = GetMediaAuditResultTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaDNAResultRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 media_id=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetMediaDNAResultResponseBodyDNAResultVideoDNADetailDuplication(TeaModel):
    def __init__(self, start=None, duration=None):
        self.start = TeaConverter.to_unicode(start)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class GetMediaDNAResultResponseBodyDNAResultVideoDNADetailInput(TeaModel):
    def __init__(self, start=None, duration=None):
        self.start = TeaConverter.to_unicode(start)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class GetMediaDNAResultResponseBodyDNAResultVideoDNADetail(TeaModel):
    def __init__(self, duplication=None, input=None):
        self.duplication = duplication  # type: GetMediaDNAResultResponseBodyDNAResultVideoDNADetailDuplication
        self.input = input  # type: GetMediaDNAResultResponseBodyDNAResultVideoDNADetailInput

    def validate(self):
        if self.duplication:
            self.duplication.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        if self.duplication is not None:
            result['Duplication'] = self.duplication.to_map()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duplication') is not None:
            temp_model = GetMediaDNAResultResponseBodyDNAResultVideoDNADetailDuplication()
            self.duplication = temp_model.from_map(m['Duplication'])
        if m.get('Input') is not None:
            temp_model = GetMediaDNAResultResponseBodyDNAResultVideoDNADetailInput()
            self.input = temp_model.from_map(m['Input'])
        return self


class GetMediaDNAResultResponseBodyDNAResultVideoDNA(TeaModel):
    def __init__(self, primary_key=None, similarity=None, detail=None):
        self.primary_key = TeaConverter.to_unicode(primary_key)  # type: unicode
        self.similarity = TeaConverter.to_unicode(similarity)  # type: unicode
        self.detail = detail  # type: list[GetMediaDNAResultResponseBodyDNAResultVideoDNADetail]

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = GetMediaDNAResultResponseBodyDNAResultVideoDNADetail()
                self.detail.append(temp_model.from_map(k))
        return self


class GetMediaDNAResultResponseBodyDNAResult(TeaModel):
    def __init__(self, video_dna=None):
        self.video_dna = video_dna  # type: list[GetMediaDNAResultResponseBodyDNAResultVideoDNA]

    def validate(self):
        if self.video_dna:
            for k in self.video_dna:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VideoDNA'] = []
        if self.video_dna is not None:
            for k in self.video_dna:
                result['VideoDNA'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.video_dna = []
        if m.get('VideoDNA') is not None:
            for k in m.get('VideoDNA'):
                temp_model = GetMediaDNAResultResponseBodyDNAResultVideoDNA()
                self.video_dna.append(temp_model.from_map(k))
        return self


class GetMediaDNAResultResponseBody(TeaModel):
    def __init__(self, request_id=None, dnaresult=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dnaresult = dnaresult  # type: GetMediaDNAResultResponseBodyDNAResult

    def validate(self):
        if self.dnaresult:
            self.dnaresult.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dnaresult is not None:
            result['DNAResult'] = self.dnaresult.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DNAResult') is not None:
            temp_model = GetMediaDNAResultResponseBodyDNAResult()
            self.dnaresult = temp_model.from_map(m['DNAResult'])
        return self


class GetMediaDNAResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetMediaDNAResultResponseBody

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
            temp_model = GetMediaDNAResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageCallbackRequest(TeaModel):
    def __init__(self, owner_account=None, resource_real_owner_id=None, app_id=None):
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetMessageCallbackResponseBodyMessageCallback(TeaModel):
    def __init__(self, callback_type=None, callback_url=None, event_type_list=None, app_id=None,
                 mns_queue_name=None, auth_key=None, auth_switch=None, mns_endpoint=None):
        self.callback_type = TeaConverter.to_unicode(callback_type)  # type: unicode
        self.callback_url = TeaConverter.to_unicode(callback_url)  # type: unicode
        self.event_type_list = TeaConverter.to_unicode(event_type_list)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.mns_queue_name = TeaConverter.to_unicode(mns_queue_name)  # type: unicode
        self.auth_key = TeaConverter.to_unicode(auth_key)  # type: unicode
        self.auth_switch = TeaConverter.to_unicode(auth_switch)  # type: unicode
        self.mns_endpoint = TeaConverter.to_unicode(mns_endpoint)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type
        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.mns_queue_name is not None:
            result['MnsQueueName'] = self.mns_queue_name
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_switch is not None:
            result['AuthSwitch'] = self.auth_switch
        if self.mns_endpoint is not None:
            result['MnsEndpoint'] = self.mns_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')
        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MnsQueueName') is not None:
            self.mns_queue_name = m.get('MnsQueueName')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSwitch') is not None:
            self.auth_switch = m.get('AuthSwitch')
        if m.get('MnsEndpoint') is not None:
            self.mns_endpoint = m.get('MnsEndpoint')
        return self


class GetMessageCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None, message_callback=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.message_callback = message_callback  # type: GetMessageCallbackResponseBodyMessageCallback

    def validate(self):
        if self.message_callback:
            self.message_callback.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_callback is not None:
            result['MessageCallback'] = self.message_callback.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageCallback') is not None:
            temp_model = GetMessageCallbackResponseBodyMessageCallback()
            self.message_callback = temp_model.from_map(m['MessageCallback'])
        return self


class GetMessageCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetMessageCallbackResponseBody

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
            temp_model = GetMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMezzanineInfoRequest(TeaModel):
    def __init__(self, video_id=None, auth_timeout=None, preview_segment=None, output_type=None, addition_type=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.auth_timeout = auth_timeout  # type: long
        self.preview_segment = preview_segment  # type: bool
        self.output_type = TeaConverter.to_unicode(output_type)  # type: unicode
        self.addition_type = TeaConverter.to_unicode(addition_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.preview_segment is not None:
            result['PreviewSegment'] = self.preview_segment
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('PreviewSegment') is not None:
            self.preview_segment = m.get('PreviewSegment')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')
        return self


class GetMezzanineInfoResponseBodyMezzanineVideoStreamList(TeaModel):
    def __init__(self, index=None, timebase=None, avg_fps=None, pix_fmt=None, sar=None, lang=None,
                 codec_long_name=None, height=None, num_frames=None, rotate=None, bitrate=None, codec_tag_string=None,
                 has_bframes=None, profile=None, start_time=None, dar=None, codec_name=None, width=None, duration=None, fps=None,
                 codec_tag=None, codec_time_base=None, level=None):
        self.index = TeaConverter.to_unicode(index)  # type: unicode
        self.timebase = TeaConverter.to_unicode(timebase)  # type: unicode
        self.avg_fps = TeaConverter.to_unicode(avg_fps)  # type: unicode
        self.pix_fmt = TeaConverter.to_unicode(pix_fmt)  # type: unicode
        self.sar = TeaConverter.to_unicode(sar)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.codec_long_name = TeaConverter.to_unicode(codec_long_name)  # type: unicode
        self.height = TeaConverter.to_unicode(height)  # type: unicode
        self.num_frames = TeaConverter.to_unicode(num_frames)  # type: unicode
        self.rotate = TeaConverter.to_unicode(rotate)  # type: unicode
        self.bitrate = TeaConverter.to_unicode(bitrate)  # type: unicode
        self.codec_tag_string = TeaConverter.to_unicode(codec_tag_string)  # type: unicode
        self.has_bframes = TeaConverter.to_unicode(has_bframes)  # type: unicode
        self.profile = TeaConverter.to_unicode(profile)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.dar = TeaConverter.to_unicode(dar)  # type: unicode
        self.codec_name = TeaConverter.to_unicode(codec_name)  # type: unicode
        self.width = TeaConverter.to_unicode(width)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.fps = TeaConverter.to_unicode(fps)  # type: unicode
        self.codec_tag = TeaConverter.to_unicode(codec_tag)  # type: unicode
        self.codec_time_base = TeaConverter.to_unicode(codec_time_base)  # type: unicode
        self.level = TeaConverter.to_unicode(level)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.avg_fps is not None:
            result['AvgFPS'] = self.avg_fps
        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt
        if self.sar is not None:
            result['Sar'] = self.sar
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.height is not None:
            result['Height'] = self.height
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.dar is not None:
            result['Dar'] = self.dar
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.width is not None:
            result['Width'] = self.width
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('AvgFPS') is not None:
            self.avg_fps = m.get('AvgFPS')
        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')
        if m.get('Sar') is not None:
            self.sar = m.get('Sar')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Dar') is not None:
            self.dar = m.get('Dar')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class GetMezzanineInfoResponseBodyMezzanineAudioStreamList(TeaModel):
    def __init__(self, timebase=None, index=None, sample_rate=None, sample_fmt=None, channel_layout=None, lang=None,
                 codec_long_name=None, channels=None, num_frames=None, bitrate=None, codec_tag_string=None, start_time=None,
                 codec_name=None, duration=None, codec_tag=None, codec_time_base=None):
        self.timebase = TeaConverter.to_unicode(timebase)  # type: unicode
        self.index = TeaConverter.to_unicode(index)  # type: unicode
        self.sample_rate = TeaConverter.to_unicode(sample_rate)  # type: unicode
        self.sample_fmt = TeaConverter.to_unicode(sample_fmt)  # type: unicode
        self.channel_layout = TeaConverter.to_unicode(channel_layout)  # type: unicode
        self.lang = TeaConverter.to_unicode(lang)  # type: unicode
        self.codec_long_name = TeaConverter.to_unicode(codec_long_name)  # type: unicode
        self.channels = TeaConverter.to_unicode(channels)  # type: unicode
        self.num_frames = TeaConverter.to_unicode(num_frames)  # type: unicode
        self.bitrate = TeaConverter.to_unicode(bitrate)  # type: unicode
        self.codec_tag_string = TeaConverter.to_unicode(codec_tag_string)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.codec_name = TeaConverter.to_unicode(codec_name)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.codec_tag = TeaConverter.to_unicode(codec_tag)  # type: unicode
        self.codec_time_base = TeaConverter.to_unicode(codec_time_base)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.index is not None:
            result['Index'] = self.index
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        return self


class GetMezzanineInfoResponseBodyMezzanine(TeaModel):
    def __init__(self, status=None, creation_time=None, video_stream_list=None, file_url=None, video_id=None,
                 height=None, file_name=None, bitrate=None, audio_stream_list=None, output_type=None, width=None, size=None,
                 duration=None, fps=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.video_stream_list = video_stream_list  # type: list[GetMezzanineInfoResponseBodyMezzanineVideoStreamList]
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.height = height  # type: long
        self.file_name = TeaConverter.to_unicode(file_name)  # type: unicode
        self.bitrate = TeaConverter.to_unicode(bitrate)  # type: unicode
        self.audio_stream_list = audio_stream_list  # type: list[GetMezzanineInfoResponseBodyMezzanineAudioStreamList]
        self.output_type = TeaConverter.to_unicode(output_type)  # type: unicode
        self.width = width  # type: long
        self.size = size  # type: long
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.fps = TeaConverter.to_unicode(fps)  # type: unicode

    def validate(self):
        if self.video_stream_list:
            for k in self.video_stream_list:
                if k:
                    k.validate()
        if self.audio_stream_list:
            for k in self.audio_stream_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        result['VideoStreamList'] = []
        if self.video_stream_list is not None:
            for k in self.video_stream_list:
                result['VideoStreamList'].append(k.to_map() if k else None)
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.height is not None:
            result['Height'] = self.height
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        result['AudioStreamList'] = []
        if self.audio_stream_list is not None:
            for k in self.audio_stream_list:
                result['AudioStreamList'].append(k.to_map() if k else None)
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        if self.width is not None:
            result['Width'] = self.width
        if self.size is not None:
            result['Size'] = self.size
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.fps is not None:
            result['Fps'] = self.fps
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        self.video_stream_list = []
        if m.get('VideoStreamList') is not None:
            for k in m.get('VideoStreamList'):
                temp_model = GetMezzanineInfoResponseBodyMezzanineVideoStreamList()
                self.video_stream_list.append(temp_model.from_map(k))
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        self.audio_stream_list = []
        if m.get('AudioStreamList') is not None:
            for k in m.get('AudioStreamList'):
                temp_model = GetMezzanineInfoResponseBodyMezzanineAudioStreamList()
                self.audio_stream_list.append(temp_model.from_map(k))
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        return self


class GetMezzanineInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, mezzanine=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.mezzanine = mezzanine  # type: GetMezzanineInfoResponseBodyMezzanine

    def validate(self):
        if self.mezzanine:
            self.mezzanine.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mezzanine is not None:
            result['Mezzanine'] = self.mezzanine.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Mezzanine') is not None:
            temp_model = GetMezzanineInfoResponseBodyMezzanine()
            self.mezzanine = temp_model.from_map(m['Mezzanine'])
        return self


class GetMezzanineInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetMezzanineInfoResponseBody

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
            temp_model = GetMezzanineInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPlayInfoRequest(TeaModel):
    def __init__(self, video_id=None, formats=None, auth_timeout=None, rand=None, auth_info=None, channel=None,
                 player_version=None, output_type=None, stream_type=None, re_auth_info=None, definition=None, result_type=None,
                 play_config=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.formats = TeaConverter.to_unicode(formats)  # type: unicode
        self.auth_timeout = auth_timeout  # type: long
        self.rand = TeaConverter.to_unicode(rand)  # type: unicode
        self.auth_info = TeaConverter.to_unicode(auth_info)  # type: unicode
        self.channel = TeaConverter.to_unicode(channel)  # type: unicode
        self.player_version = TeaConverter.to_unicode(player_version)  # type: unicode
        self.output_type = TeaConverter.to_unicode(output_type)  # type: unicode
        self.stream_type = TeaConverter.to_unicode(stream_type)  # type: unicode
        self.re_auth_info = TeaConverter.to_unicode(re_auth_info)  # type: unicode
        self.definition = TeaConverter.to_unicode(definition)  # type: unicode
        self.result_type = TeaConverter.to_unicode(result_type)  # type: unicode
        self.play_config = TeaConverter.to_unicode(play_config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.formats is not None:
            result['Formats'] = self.formats
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.rand is not None:
            result['Rand'] = self.rand
        if self.auth_info is not None:
            result['AuthInfo'] = self.auth_info
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.player_version is not None:
            result['PlayerVersion'] = self.player_version
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.re_auth_info is not None:
            result['ReAuthInfo'] = self.re_auth_info
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.play_config is not None:
            result['PlayConfig'] = self.play_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Formats') is not None:
            self.formats = m.get('Formats')
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('Rand') is not None:
            self.rand = m.get('Rand')
        if m.get('AuthInfo') is not None:
            self.auth_info = m.get('AuthInfo')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('PlayerVersion') is not None:
            self.player_version = m.get('PlayerVersion')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('ReAuthInfo') is not None:
            self.re_auth_info = m.get('ReAuthInfo')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('PlayConfig') is not None:
            self.play_config = m.get('PlayConfig')
        return self


class GetPlayInfoResponseBodyVideoBase(TeaModel):
    def __init__(self, creation_time=None, status=None, video_id=None, cover_url=None, duration=None, title=None,
                 media_type=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.media_type = TeaConverter.to_unicode(media_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        return self


class GetPlayInfoResponseBodyPlayInfoListPlayInfo(TeaModel):
    def __init__(self, status=None, creation_time=None, specification=None, narrow_band_type=None, height=None,
                 bitrate=None, modification_time=None, watermark_id=None, encrypt=None, definition=None, encrypt_type=None,
                 stream_type=None, job_id=None, size=None, width=None, fps=None, duration=None, play_url=None, format=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.specification = TeaConverter.to_unicode(specification)  # type: unicode
        self.narrow_band_type = TeaConverter.to_unicode(narrow_band_type)  # type: unicode
        self.height = height  # type: long
        self.bitrate = TeaConverter.to_unicode(bitrate)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.watermark_id = TeaConverter.to_unicode(watermark_id)  # type: unicode
        self.encrypt = encrypt  # type: long
        self.definition = TeaConverter.to_unicode(definition)  # type: unicode
        self.encrypt_type = TeaConverter.to_unicode(encrypt_type)  # type: unicode
        self.stream_type = TeaConverter.to_unicode(stream_type)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.size = size  # type: long
        self.width = width  # type: long
        self.fps = TeaConverter.to_unicode(fps)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.play_url = TeaConverter.to_unicode(play_url)  # type: unicode
        self.format = TeaConverter.to_unicode(format)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.narrow_band_type is not None:
            result['NarrowBandType'] = self.narrow_band_type
        if self.height is not None:
            result['Height'] = self.height
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.size is not None:
            result['Size'] = self.size
        if self.width is not None:
            result['Width'] = self.width
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.play_url is not None:
            result['PlayURL'] = self.play_url
        if self.format is not None:
            result['Format'] = self.format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('NarrowBandType') is not None:
            self.narrow_band_type = m.get('NarrowBandType')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PlayURL') is not None:
            self.play_url = m.get('PlayURL')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        return self


class GetPlayInfoResponseBodyPlayInfoList(TeaModel):
    def __init__(self, play_info=None):
        self.play_info = play_info  # type: list[GetPlayInfoResponseBodyPlayInfoListPlayInfo]

    def validate(self):
        if self.play_info:
            for k in self.play_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PlayInfo'] = []
        if self.play_info is not None:
            for k in self.play_info:
                result['PlayInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.play_info = []
        if m.get('PlayInfo') is not None:
            for k in m.get('PlayInfo'):
                temp_model = GetPlayInfoResponseBodyPlayInfoListPlayInfo()
                self.play_info.append(temp_model.from_map(k))
        return self


class GetPlayInfoResponseBody(TeaModel):
    def __init__(self, video_base=None, request_id=None, play_info_list=None):
        self.video_base = video_base  # type: GetPlayInfoResponseBodyVideoBase
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.play_info_list = play_info_list  # type: GetPlayInfoResponseBodyPlayInfoList

    def validate(self):
        if self.video_base:
            self.video_base.validate()
        if self.play_info_list:
            self.play_info_list.validate()

    def to_map(self):
        result = dict()
        if self.video_base is not None:
            result['VideoBase'] = self.video_base.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.play_info_list is not None:
            result['PlayInfoList'] = self.play_info_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoBase') is not None:
            temp_model = GetPlayInfoResponseBodyVideoBase()
            self.video_base = temp_model.from_map(m['VideoBase'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PlayInfoList') is not None:
            temp_model = GetPlayInfoResponseBodyPlayInfoList()
            self.play_info_list = temp_model.from_map(m['PlayInfoList'])
        return self


class GetPlayInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetPlayInfoResponseBody

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
            temp_model = GetPlayInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranscodeSummaryRequest(TeaModel):
    def __init__(self, video_ids=None):
        self.video_ids = TeaConverter.to_unicode(video_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')
        return self


class GetTranscodeSummaryResponseBodyTranscodeSummaryListTranscodeJobInfoSummaryList(TeaModel):
    def __init__(self, creation_time=None, error_message=None, height=None, transcode_progress=None, bitrate=None,
                 transcode_template_id=None, error_code=None, watermark_id_list=None, width=None, complete_time=None, duration=None,
                 fps=None, transcode_job_status=None, filesize=None, format=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.error_message = TeaConverter.to_unicode(error_message)  # type: unicode
        self.height = TeaConverter.to_unicode(height)  # type: unicode
        self.transcode_progress = transcode_progress  # type: long
        self.bitrate = TeaConverter.to_unicode(bitrate)  # type: unicode
        self.transcode_template_id = TeaConverter.to_unicode(transcode_template_id)  # type: unicode
        self.error_code = TeaConverter.to_unicode(error_code)  # type: unicode
        self.watermark_id_list = watermark_id_list  # type: list[unicode]
        self.width = TeaConverter.to_unicode(width)  # type: unicode
        self.complete_time = TeaConverter.to_unicode(complete_time)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.fps = TeaConverter.to_unicode(fps)  # type: unicode
        self.transcode_job_status = TeaConverter.to_unicode(transcode_job_status)  # type: unicode
        self.filesize = filesize  # type: long
        self.format = TeaConverter.to_unicode(format)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.height is not None:
            result['Height'] = self.height
        if self.transcode_progress is not None:
            result['TranscodeProgress'] = self.transcode_progress
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.watermark_id_list is not None:
            result['WatermarkIdList'] = self.watermark_id_list
        if self.width is not None:
            result['Width'] = self.width
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.transcode_job_status is not None:
            result['TranscodeJobStatus'] = self.transcode_job_status
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.format is not None:
            result['Format'] = self.format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('TranscodeProgress') is not None:
            self.transcode_progress = m.get('TranscodeProgress')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('WatermarkIdList') is not None:
            self.watermark_id_list = m.get('WatermarkIdList')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('TranscodeJobStatus') is not None:
            self.transcode_job_status = m.get('TranscodeJobStatus')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        return self


class GetTranscodeSummaryResponseBodyTranscodeSummaryList(TeaModel):
    def __init__(self, creation_time=None, transcode_job_info_summary_list=None, video_id=None, complete_time=None,
                 transcode_status=None, transcode_template_group_id=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.transcode_job_info_summary_list = transcode_job_info_summary_list  # type: list[GetTranscodeSummaryResponseBodyTranscodeSummaryListTranscodeJobInfoSummaryList]
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.complete_time = TeaConverter.to_unicode(complete_time)  # type: unicode
        self.transcode_status = TeaConverter.to_unicode(transcode_status)  # type: unicode
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode

    def validate(self):
        if self.transcode_job_info_summary_list:
            for k in self.transcode_job_info_summary_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        result['TranscodeJobInfoSummaryList'] = []
        if self.transcode_job_info_summary_list is not None:
            for k in self.transcode_job_info_summary_list:
                result['TranscodeJobInfoSummaryList'].append(k.to_map() if k else None)
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        self.transcode_job_info_summary_list = []
        if m.get('TranscodeJobInfoSummaryList') is not None:
            for k in m.get('TranscodeJobInfoSummaryList'):
                temp_model = GetTranscodeSummaryResponseBodyTranscodeSummaryListTranscodeJobInfoSummaryList()
                self.transcode_job_info_summary_list.append(temp_model.from_map(k))
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        return self


class GetTranscodeSummaryResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_summary_list=None, non_exist_video_ids=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.transcode_summary_list = transcode_summary_list  # type: list[GetTranscodeSummaryResponseBodyTranscodeSummaryList]
        self.non_exist_video_ids = non_exist_video_ids  # type: list[unicode]

    def validate(self):
        if self.transcode_summary_list:
            for k in self.transcode_summary_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TranscodeSummaryList'] = []
        if self.transcode_summary_list is not None:
            for k in self.transcode_summary_list:
                result['TranscodeSummaryList'].append(k.to_map() if k else None)
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.transcode_summary_list = []
        if m.get('TranscodeSummaryList') is not None:
            for k in m.get('TranscodeSummaryList'):
                temp_model = GetTranscodeSummaryResponseBodyTranscodeSummaryList()
                self.transcode_summary_list.append(temp_model.from_map(k))
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        return self


class GetTranscodeSummaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetTranscodeSummaryResponseBody

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
            temp_model = GetTranscodeSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranscodeTaskRequest(TeaModel):
    def __init__(self, transcode_task_id=None):
        self.transcode_task_id = TeaConverter.to_unicode(transcode_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')
        return self


class GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoListOutputFile(TeaModel):
    def __init__(self, video_stream_list=None, output_file_url=None, encryption=None, subtitle_stream_list=None,
                 height=None, bitrate=None, audio_stream_list=None, watermark_id_list=None, width=None, duration=None,
                 fps=None, format=None, filesize=None):
        self.video_stream_list = TeaConverter.to_unicode(video_stream_list)  # type: unicode
        self.output_file_url = TeaConverter.to_unicode(output_file_url)  # type: unicode
        self.encryption = TeaConverter.to_unicode(encryption)  # type: unicode
        self.subtitle_stream_list = TeaConverter.to_unicode(subtitle_stream_list)  # type: unicode
        self.height = TeaConverter.to_unicode(height)  # type: unicode
        self.bitrate = TeaConverter.to_unicode(bitrate)  # type: unicode
        self.audio_stream_list = TeaConverter.to_unicode(audio_stream_list)  # type: unicode
        self.watermark_id_list = watermark_id_list  # type: list[unicode]
        self.width = TeaConverter.to_unicode(width)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.fps = TeaConverter.to_unicode(fps)  # type: unicode
        self.format = TeaConverter.to_unicode(format)  # type: unicode
        self.filesize = filesize  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_stream_list is not None:
            result['VideoStreamList'] = self.video_stream_list
        if self.output_file_url is not None:
            result['OutputFileUrl'] = self.output_file_url
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.subtitle_stream_list is not None:
            result['SubtitleStreamList'] = self.subtitle_stream_list
        if self.height is not None:
            result['Height'] = self.height
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.audio_stream_list is not None:
            result['AudioStreamList'] = self.audio_stream_list
        if self.watermark_id_list is not None:
            result['WatermarkIdList'] = self.watermark_id_list
        if self.width is not None:
            result['Width'] = self.width
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.format is not None:
            result['Format'] = self.format
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoStreamList') is not None:
            self.video_stream_list = m.get('VideoStreamList')
        if m.get('OutputFileUrl') is not None:
            self.output_file_url = m.get('OutputFileUrl')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('SubtitleStreamList') is not None:
            self.subtitle_stream_list = m.get('SubtitleStreamList')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('AudioStreamList') is not None:
            self.audio_stream_list = m.get('AudioStreamList')
        if m.get('WatermarkIdList') is not None:
            self.watermark_id_list = m.get('WatermarkIdList')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        return self


class GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList(TeaModel):
    def __init__(self, creation_time=None, error_message=None, output_file=None, transcode_progress=None,
                 priority=None, transcode_template_id=None, transcode_job_id=None, definition=None, input_file_url=None,
                 error_code=None, complete_time=None, transcode_job_status=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.error_message = TeaConverter.to_unicode(error_message)  # type: unicode
        self.output_file = output_file  # type: GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoListOutputFile
        self.transcode_progress = transcode_progress  # type: long
        self.priority = TeaConverter.to_unicode(priority)  # type: unicode
        self.transcode_template_id = TeaConverter.to_unicode(transcode_template_id)  # type: unicode
        self.transcode_job_id = TeaConverter.to_unicode(transcode_job_id)  # type: unicode
        self.definition = TeaConverter.to_unicode(definition)  # type: unicode
        self.input_file_url = TeaConverter.to_unicode(input_file_url)  # type: unicode
        self.error_code = TeaConverter.to_unicode(error_code)  # type: unicode
        self.complete_time = TeaConverter.to_unicode(complete_time)  # type: unicode
        self.transcode_job_status = TeaConverter.to_unicode(transcode_job_status)  # type: unicode

    def validate(self):
        if self.output_file:
            self.output_file.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.output_file is not None:
            result['OutputFile'] = self.output_file.to_map()
        if self.transcode_progress is not None:
            result['TranscodeProgress'] = self.transcode_progress
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id
        if self.transcode_job_id is not None:
            result['TranscodeJobId'] = self.transcode_job_id
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.transcode_job_status is not None:
            result['TranscodeJobStatus'] = self.transcode_job_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('OutputFile') is not None:
            temp_model = GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoListOutputFile()
            self.output_file = temp_model.from_map(m['OutputFile'])
        if m.get('TranscodeProgress') is not None:
            self.transcode_progress = m.get('TranscodeProgress')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')
        if m.get('TranscodeJobId') is not None:
            self.transcode_job_id = m.get('TranscodeJobId')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('TranscodeJobStatus') is not None:
            self.transcode_job_status = m.get('TranscodeJobStatus')
        return self


class GetTranscodeTaskResponseBodyTranscodeTask(TeaModel):
    def __init__(self, creation_time=None, trigger=None, task_status=None, video_id=None, complete_time=None,
                 transcode_template_group_id=None, transcode_task_id=None, transcode_job_info_list=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.trigger = TeaConverter.to_unicode(trigger)  # type: unicode
        self.task_status = TeaConverter.to_unicode(task_status)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.complete_time = TeaConverter.to_unicode(complete_time)  # type: unicode
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode
        self.transcode_task_id = TeaConverter.to_unicode(transcode_task_id)  # type: unicode
        self.transcode_job_info_list = transcode_job_info_list  # type: list[GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList]

    def validate(self):
        if self.transcode_job_info_list:
            for k in self.transcode_job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id
        result['TranscodeJobInfoList'] = []
        if self.transcode_job_info_list is not None:
            for k in self.transcode_job_info_list:
                result['TranscodeJobInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')
        self.transcode_job_info_list = []
        if m.get('TranscodeJobInfoList') is not None:
            for k in m.get('TranscodeJobInfoList'):
                temp_model = GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList()
                self.transcode_job_info_list.append(temp_model.from_map(k))
        return self


class GetTranscodeTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_task=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.transcode_task = transcode_task  # type: GetTranscodeTaskResponseBodyTranscodeTask

    def validate(self):
        if self.transcode_task:
            self.transcode_task.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transcode_task is not None:
            result['TranscodeTask'] = self.transcode_task.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TranscodeTask') is not None:
            temp_model = GetTranscodeTaskResponseBodyTranscodeTask()
            self.transcode_task = temp_model.from_map(m['TranscodeTask'])
        return self


class GetTranscodeTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetTranscodeTaskResponseBody

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
            temp_model = GetTranscodeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, transcode_template_group_id=None):
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        return self


class GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupTranscodeTemplateList(TeaModel):
    def __init__(self, video=None, type=None, trans_config=None, transcode_template_id=None, rotate=None,
                 encrypt_setting=None, template_name=None, audio=None, container=None, transcode_file_regular=None, definition=None,
                 clip=None, package_setting=None, watermark_ids=None, subtitle_list=None, mux_config=None):
        self.video = TeaConverter.to_unicode(video)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.trans_config = TeaConverter.to_unicode(trans_config)  # type: unicode
        self.transcode_template_id = TeaConverter.to_unicode(transcode_template_id)  # type: unicode
        self.rotate = TeaConverter.to_unicode(rotate)  # type: unicode
        self.encrypt_setting = TeaConverter.to_unicode(encrypt_setting)  # type: unicode
        self.template_name = TeaConverter.to_unicode(template_name)  # type: unicode
        self.audio = TeaConverter.to_unicode(audio)  # type: unicode
        self.container = TeaConverter.to_unicode(container)  # type: unicode
        self.transcode_file_regular = TeaConverter.to_unicode(transcode_file_regular)  # type: unicode
        self.definition = TeaConverter.to_unicode(definition)  # type: unicode
        self.clip = TeaConverter.to_unicode(clip)  # type: unicode
        self.package_setting = TeaConverter.to_unicode(package_setting)  # type: unicode
        self.watermark_ids = watermark_ids  # type: list[unicode]
        self.subtitle_list = TeaConverter.to_unicode(subtitle_list)  # type: unicode
        self.mux_config = TeaConverter.to_unicode(mux_config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video is not None:
            result['Video'] = self.video
        if self.type is not None:
            result['Type'] = self.type
        if self.trans_config is not None:
            result['TransConfig'] = self.trans_config
        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.encrypt_setting is not None:
            result['EncryptSetting'] = self.encrypt_setting
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.audio is not None:
            result['Audio'] = self.audio
        if self.container is not None:
            result['Container'] = self.container
        if self.transcode_file_regular is not None:
            result['TranscodeFileRegular'] = self.transcode_file_regular
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.clip is not None:
            result['Clip'] = self.clip
        if self.package_setting is not None:
            result['PackageSetting'] = self.package_setting
        if self.watermark_ids is not None:
            result['WatermarkIds'] = self.watermark_ids
        if self.subtitle_list is not None:
            result['SubtitleList'] = self.subtitle_list
        if self.mux_config is not None:
            result['MuxConfig'] = self.mux_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Video') is not None:
            self.video = m.get('Video')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TransConfig') is not None:
            self.trans_config = m.get('TransConfig')
        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('EncryptSetting') is not None:
            self.encrypt_setting = m.get('EncryptSetting')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')
        if m.get('Container') is not None:
            self.container = m.get('Container')
        if m.get('TranscodeFileRegular') is not None:
            self.transcode_file_regular = m.get('TranscodeFileRegular')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Clip') is not None:
            self.clip = m.get('Clip')
        if m.get('PackageSetting') is not None:
            self.package_setting = m.get('PackageSetting')
        if m.get('WatermarkIds') is not None:
            self.watermark_ids = m.get('WatermarkIds')
        if m.get('SubtitleList') is not None:
            self.subtitle_list = m.get('SubtitleList')
        if m.get('MuxConfig') is not None:
            self.mux_config = m.get('MuxConfig')
        return self


class GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroup(TeaModel):
    def __init__(self, creation_time=None, is_default=None, app_id=None, transcode_template_list=None,
                 transcode_template_group_id=None, name=None, modify_time=None, locked=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.transcode_template_list = transcode_template_list  # type: list[GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupTranscodeTemplateList]
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.modify_time = TeaConverter.to_unicode(modify_time)  # type: unicode
        self.locked = TeaConverter.to_unicode(locked)  # type: unicode

    def validate(self):
        if self.transcode_template_list:
            for k in self.transcode_template_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.app_id is not None:
            result['AppId'] = self.app_id
        result['TranscodeTemplateList'] = []
        if self.transcode_template_list is not None:
            for k in self.transcode_template_list:
                result['TranscodeTemplateList'].append(k.to_map() if k else None)
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.locked is not None:
            result['Locked'] = self.locked
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        self.transcode_template_list = []
        if m.get('TranscodeTemplateList') is not None:
            for k in m.get('TranscodeTemplateList'):
                temp_model = GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupTranscodeTemplateList()
                self.transcode_template_list.append(temp_model.from_map(k))
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        return self


class GetTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_template_group=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.transcode_template_group = transcode_template_group  # type: GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroup

    def validate(self):
        if self.transcode_template_group:
            self.transcode_template_group.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transcode_template_group is not None:
            result['TranscodeTemplateGroup'] = self.transcode_template_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TranscodeTemplateGroup') is not None:
            temp_model = GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroup()
            self.transcode_template_group = temp_model.from_map(m['TranscodeTemplateGroup'])
        return self


class GetTranscodeTemplateGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetTranscodeTemplateGroupResponseBody

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
            temp_model = GetTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadDetailsRequest(TeaModel):
    def __init__(self, resource_real_owner_id=None, media_ids=None, media_type=None):
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.media_ids = TeaConverter.to_unicode(media_ids)  # type: unicode
        self.media_type = TeaConverter.to_unicode(media_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        return self


class GetUploadDetailsResponseBodyUploadDetails(TeaModel):
    def __init__(self, upload_source=None, creation_time=None, status=None, upload_ip=None, device_model=None,
                 modification_time=None, completion_time=None, media_id=None, upload_size=None, upload_ratio=None, upload_status=None,
                 title=None, file_size=None):
        self.upload_source = TeaConverter.to_unicode(upload_source)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.upload_ip = TeaConverter.to_unicode(upload_ip)  # type: unicode
        self.device_model = TeaConverter.to_unicode(device_model)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.completion_time = TeaConverter.to_unicode(completion_time)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.upload_size = upload_size  # type: long
        self.upload_ratio = upload_ratio  # type: float
        self.upload_status = TeaConverter.to_unicode(upload_status)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.file_size = file_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.upload_source is not None:
            result['UploadSource'] = self.upload_source
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.upload_ip is not None:
            result['UploadIP'] = self.upload_ip
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.upload_size is not None:
            result['UploadSize'] = self.upload_size
        if self.upload_ratio is not None:
            result['UploadRatio'] = self.upload_ratio
        if self.upload_status is not None:
            result['UploadStatus'] = self.upload_status
        if self.title is not None:
            result['Title'] = self.title
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UploadSource') is not None:
            self.upload_source = m.get('UploadSource')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UploadIP') is not None:
            self.upload_ip = m.get('UploadIP')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('UploadSize') is not None:
            self.upload_size = m.get('UploadSize')
        if m.get('UploadRatio') is not None:
            self.upload_ratio = m.get('UploadRatio')
        if m.get('UploadStatus') is not None:
            self.upload_status = m.get('UploadStatus')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class GetUploadDetailsResponseBody(TeaModel):
    def __init__(self, non_exist_media_ids=None, upload_details=None, request_id=None, forbidden_media_ids=None):
        self.non_exist_media_ids = non_exist_media_ids  # type: list[unicode]
        self.upload_details = upload_details  # type: list[GetUploadDetailsResponseBodyUploadDetails]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.forbidden_media_ids = forbidden_media_ids  # type: list[unicode]

    def validate(self):
        if self.upload_details:
            for k in self.upload_details:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids
        result['UploadDetails'] = []
        if self.upload_details is not None:
            for k in self.upload_details:
                result['UploadDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.forbidden_media_ids is not None:
            result['ForbiddenMediaIds'] = self.forbidden_media_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')
        self.upload_details = []
        if m.get('UploadDetails') is not None:
            for k in m.get('UploadDetails'):
                temp_model = GetUploadDetailsResponseBodyUploadDetails()
                self.upload_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ForbiddenMediaIds') is not None:
            self.forbidden_media_ids = m.get('ForbiddenMediaIds')
        return self


class GetUploadDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetUploadDetailsResponseBody

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
            temp_model = GetUploadDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetURLUploadInfosRequest(TeaModel):
    def __init__(self, job_ids=None, upload_urls=None):
        self.job_ids = TeaConverter.to_unicode(job_ids)  # type: unicode
        self.upload_urls = TeaConverter.to_unicode(upload_urls)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        if self.upload_urls is not None:
            result['UploadURLs'] = self.upload_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        if m.get('UploadURLs') is not None:
            self.upload_urls = m.get('UploadURLs')
        return self


class GetURLUploadInfosResponseBodyURLUploadInfoList(TeaModel):
    def __init__(self, creation_time=None, status=None, error_message=None, error_code=None, complete_time=None,
                 job_id=None, user_data=None, upload_url=None, media_id=None, file_size=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.error_message = TeaConverter.to_unicode(error_message)  # type: unicode
        self.error_code = TeaConverter.to_unicode(error_code)  # type: unicode
        self.complete_time = TeaConverter.to_unicode(complete_time)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.upload_url = TeaConverter.to_unicode(upload_url)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.file_size = TeaConverter.to_unicode(file_size)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.upload_url is not None:
            result['UploadURL'] = self.upload_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UploadURL') is not None:
            self.upload_url = m.get('UploadURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class GetURLUploadInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, urlupload_info_list=None, non_exists=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.urlupload_info_list = urlupload_info_list  # type: list[GetURLUploadInfosResponseBodyURLUploadInfoList]
        self.non_exists = non_exists  # type: list[unicode]

    def validate(self):
        if self.urlupload_info_list:
            for k in self.urlupload_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['URLUploadInfoList'] = []
        if self.urlupload_info_list is not None:
            for k in self.urlupload_info_list:
                result['URLUploadInfoList'].append(k.to_map() if k else None)
        if self.non_exists is not None:
            result['NonExists'] = self.non_exists
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.urlupload_info_list = []
        if m.get('URLUploadInfoList') is not None:
            for k in m.get('URLUploadInfoList'):
                temp_model = GetURLUploadInfosResponseBodyURLUploadInfoList()
                self.urlupload_info_list.append(temp_model.from_map(k))
        if m.get('NonExists') is not None:
            self.non_exists = m.get('NonExists')
        return self


class GetURLUploadInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetURLUploadInfosResponseBody

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
            temp_model = GetURLUploadInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoInfoRequest(TeaModel):
    def __init__(self, video_id=None, result_types=None, addition_type=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.result_types = TeaConverter.to_unicode(result_types)  # type: unicode
        self.addition_type = TeaConverter.to_unicode(addition_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.result_types is not None:
            result['ResultTypes'] = self.result_types
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('ResultTypes') is not None:
            self.result_types = m.get('ResultTypes')
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')
        return self


class GetVideoInfoResponseBodyVideoSnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        return self


class GetVideoInfoResponseBodyVideo(TeaModel):
    def __init__(self, status=None, creation_time=None, storage_location=None, cate_id=None, tags=None,
                 modification_time=None, description=None, app_id=None, cover_url=None, template_group_id=None, audit_status=None,
                 video_id=None, snapshots=None, region_id=None, custom_media_info=None, cate_name=None, size=None,
                 duration=None, title=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.template_group_id = TeaConverter.to_unicode(template_group_id)  # type: unicode
        self.audit_status = TeaConverter.to_unicode(audit_status)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.snapshots = snapshots  # type: GetVideoInfoResponseBodyVideoSnapshots
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode
        self.custom_media_info = TeaConverter.to_unicode(custom_media_info)  # type: unicode
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.size = size  # type: long
        self.duration = duration  # type: float
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.custom_media_info is not None:
            result['CustomMediaInfo'] = self.custom_media_info
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.size is not None:
            result['Size'] = self.size
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Snapshots') is not None:
            temp_model = GetVideoInfoResponseBodyVideoSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CustomMediaInfo') is not None:
            self.custom_media_info = m.get('CustomMediaInfo')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetVideoInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, video=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.video = video  # type: GetVideoInfoResponseBodyVideo

    def validate(self):
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Video') is not None:
            temp_model = GetVideoInfoResponseBodyVideo()
            self.video = temp_model.from_map(m['Video'])
        return self


class GetVideoInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetVideoInfoResponseBody

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
            temp_model = GetVideoInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoInfosRequest(TeaModel):
    def __init__(self, video_ids=None, addition_type=None):
        self.video_ids = TeaConverter.to_unicode(video_ids)  # type: unicode
        self.addition_type = TeaConverter.to_unicode(addition_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')
        return self


class GetVideoInfosResponseBodyVideoList(TeaModel):
    def __init__(self, status=None, creation_time=None, storage_location=None, cate_id=None, video_id=None,
                 tags=None, modification_time=None, snapshots=None, cate_name=None, description=None, app_id=None,
                 size=None, cover_url=None, template_group_id=None, duration=None, title=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.snapshots = snapshots  # type: list[unicode]
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.size = size  # type: long
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.template_group_id = TeaConverter.to_unicode(template_group_id)  # type: unicode
        self.duration = duration  # type: float
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.size is not None:
            result['Size'] = self.size
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetVideoInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, non_exist_video_ids=None, video_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.non_exist_video_ids = non_exist_video_ids  # type: list[unicode]
        self.video_list = video_list  # type: list[GetVideoInfosResponseBodyVideoList]

    def validate(self):
        if self.video_list:
            for k in self.video_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        result['VideoList'] = []
        if self.video_list is not None:
            for k in self.video_list:
                result['VideoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        self.video_list = []
        if m.get('VideoList') is not None:
            for k in m.get('VideoList'):
                temp_model = GetVideoInfosResponseBodyVideoList()
                self.video_list.append(temp_model.from_map(k))
        return self


class GetVideoInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetVideoInfosResponseBody

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
            temp_model = GetVideoInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoListRequest(TeaModel):
    def __init__(self, cate_id=None, status=None, page_no=None, page_size=None, sort_by=None, start_time=None,
                 end_time=None, storage_location=None):
        self.cate_id = cate_id  # type: long
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = TeaConverter.to_unicode(sort_by)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.status is not None:
            result['Status'] = self.status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        return self


class GetVideoListResponseBodyVideoListVideoSnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        return self


class GetVideoListResponseBodyVideoListVideo(TeaModel):
    def __init__(self, creation_time=None, status=None, storage_location=None, cate_id=None, video_id=None,
                 tags=None, modification_time=None, snapshots=None, cate_name=None, description=None, app_id=None,
                 size=None, cover_url=None, duration=None, title=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.snapshots = snapshots  # type: GetVideoListResponseBodyVideoListVideoSnapshots
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.size = size  # type: long
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.duration = duration  # type: float
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.size is not None:
            result['Size'] = self.size
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Snapshots') is not None:
            temp_model = GetVideoListResponseBodyVideoListVideoSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetVideoListResponseBodyVideoList(TeaModel):
    def __init__(self, video=None):
        self.video = video  # type: list[GetVideoListResponseBodyVideoListVideo]

    def validate(self):
        if self.video:
            for k in self.video:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Video'] = []
        if self.video is not None:
            for k in self.video:
                result['Video'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.video = []
        if m.get('Video') is not None:
            for k in m.get('Video'):
                temp_model = GetVideoListResponseBodyVideoListVideo()
                self.video.append(temp_model.from_map(k))
        return self


class GetVideoListResponseBody(TeaModel):
    def __init__(self, request_id=None, total=None, video_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total = total  # type: int
        self.video_list = video_list  # type: GetVideoListResponseBodyVideoList

    def validate(self):
        if self.video_list:
            self.video_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.video_list is not None:
            result['VideoList'] = self.video_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('VideoList') is not None:
            temp_model = GetVideoListResponseBodyVideoList()
            self.video_list = temp_model.from_map(m['VideoList'])
        return self


class GetVideoListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetVideoListResponseBody

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
            temp_model = GetVideoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoPlayAuthRequest(TeaModel):
    def __init__(self, video_id=None, auth_info_timeout=None, re_auth_info=None, play_config=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.auth_info_timeout = auth_info_timeout  # type: long
        self.re_auth_info = TeaConverter.to_unicode(re_auth_info)  # type: unicode
        self.play_config = TeaConverter.to_unicode(play_config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.auth_info_timeout is not None:
            result['AuthInfoTimeout'] = self.auth_info_timeout
        if self.re_auth_info is not None:
            result['ReAuthInfo'] = self.re_auth_info
        if self.play_config is not None:
            result['PlayConfig'] = self.play_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('AuthInfoTimeout') is not None:
            self.auth_info_timeout = m.get('AuthInfoTimeout')
        if m.get('ReAuthInfo') is not None:
            self.re_auth_info = m.get('ReAuthInfo')
        if m.get('PlayConfig') is not None:
            self.play_config = m.get('PlayConfig')
        return self


class GetVideoPlayAuthResponseBodyVideoMeta(TeaModel):
    def __init__(self, status=None, video_id=None, cover_url=None, duration=None, title=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.duration = duration  # type: float
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetVideoPlayAuthResponseBody(TeaModel):
    def __init__(self, play_auth=None, video_meta=None, request_id=None):
        self.play_auth = TeaConverter.to_unicode(play_auth)  # type: unicode
        self.video_meta = video_meta  # type: GetVideoPlayAuthResponseBodyVideoMeta
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        if self.video_meta:
            self.video_meta.validate()

    def to_map(self):
        result = dict()
        if self.play_auth is not None:
            result['PlayAuth'] = self.play_auth
        if self.video_meta is not None:
            result['VideoMeta'] = self.video_meta.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlayAuth') is not None:
            self.play_auth = m.get('PlayAuth')
        if m.get('VideoMeta') is not None:
            temp_model = GetVideoPlayAuthResponseBodyVideoMeta()
            self.video_meta = temp_model.from_map(m['VideoMeta'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVideoPlayAuthResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetVideoPlayAuthResponseBody

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
            temp_model = GetVideoPlayAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVodTemplateRequest(TeaModel):
    def __init__(self, vod_template_id=None):
        self.vod_template_id = TeaConverter.to_unicode(vod_template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        return self


class GetVodTemplateResponseBodyVodTemplateInfo(TeaModel):
    def __init__(self, creation_time=None, is_default=None, template_type=None, vod_template_id=None,
                 template_config=None, name=None, modify_time=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode
        self.vod_template_id = TeaConverter.to_unicode(vod_template_id)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.modify_time = TeaConverter.to_unicode(modify_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.name is not None:
            result['Name'] = self.name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetVodTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, vod_template_info=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.vod_template_info = vod_template_info  # type: GetVodTemplateResponseBodyVodTemplateInfo

    def validate(self):
        if self.vod_template_info:
            self.vod_template_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vod_template_info is not None:
            result['VodTemplateInfo'] = self.vod_template_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VodTemplateInfo') is not None:
            temp_model = GetVodTemplateResponseBodyVodTemplateInfo()
            self.vod_template_info = temp_model.from_map(m['VodTemplateInfo'])
        return self


class GetVodTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetVodTemplateResponseBody

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
            temp_model = GetVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWatermarkRequest(TeaModel):
    def __init__(self, watermark_id=None):
        self.watermark_id = TeaConverter.to_unicode(watermark_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class GetWatermarkResponseBodyWatermarkInfo(TeaModel):
    def __init__(self, creation_time=None, type=None, is_default=None, file_url=None, app_id=None,
                 watermark_config=None, name=None, watermark_id=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.watermark_config = TeaConverter.to_unicode(watermark_config)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.watermark_id = TeaConverter.to_unicode(watermark_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.type is not None:
            result['Type'] = self.type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class GetWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, watermark_info=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.watermark_info = watermark_info  # type: GetWatermarkResponseBodyWatermarkInfo

    def validate(self):
        if self.watermark_info:
            self.watermark_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.watermark_info is not None:
            result['WatermarkInfo'] = self.watermark_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WatermarkInfo') is not None:
            temp_model = GetWatermarkResponseBodyWatermarkInfo()
            self.watermark_info = temp_model.from_map(m['WatermarkInfo'])
        return self


class GetWatermarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetWatermarkResponseBody

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
            temp_model = GetWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAIImageInfoRequest(TeaModel):
    def __init__(self, video_id=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class ListAIImageInfoResponseBodyAIImageInfoList(TeaModel):
    def __init__(self, creation_time=None, aiimage_info_id=None, file_url=None, version=None, video_id=None,
                 job_id=None, score=None, format=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.aiimage_info_id = TeaConverter.to_unicode(aiimage_info_id)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.version = TeaConverter.to_unicode(version)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.score = TeaConverter.to_unicode(score)  # type: unicode
        self.format = TeaConverter.to_unicode(format)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.aiimage_info_id is not None:
            result['AIImageInfoId'] = self.aiimage_info_id
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.version is not None:
            result['Version'] = self.version
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.score is not None:
            result['Score'] = self.score
        if self.format is not None:
            result['Format'] = self.format
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('AIImageInfoId') is not None:
            self.aiimage_info_id = m.get('AIImageInfoId')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        return self


class ListAIImageInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, aiimage_info_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.aiimage_info_list = aiimage_info_list  # type: list[ListAIImageInfoResponseBodyAIImageInfoList]

    def validate(self):
        if self.aiimage_info_list:
            for k in self.aiimage_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AIImageInfoList'] = []
        if self.aiimage_info_list is not None:
            for k in self.aiimage_info_list:
                result['AIImageInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.aiimage_info_list = []
        if m.get('AIImageInfoList') is not None:
            for k in m.get('AIImageInfoList'):
                temp_model = ListAIImageInfoResponseBodyAIImageInfoList()
                self.aiimage_info_list.append(temp_model.from_map(k))
        return self


class ListAIImageInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListAIImageInfoResponseBody

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
            temp_model = ListAIImageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAIJobRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 job_ids=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.job_ids = TeaConverter.to_unicode(job_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class ListAIJobResponseBodyNonExistAIJobIds(TeaModel):
    def __init__(self, string=None):
        self.string = string  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class ListAIJobResponseBodyAIJobListAIJob(TeaModel):
    def __init__(self, creation_time=None, status=None, type=None, data=None, complete_time=None, job_id=None,
                 code=None, message=None, media_id=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.data = TeaConverter.to_unicode(data)  # type: unicode
        self.complete_time = TeaConverter.to_unicode(complete_time)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.data is not None:
            result['Data'] = self.data
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class ListAIJobResponseBodyAIJobList(TeaModel):
    def __init__(self, aijob=None):
        self.aijob = aijob  # type: list[ListAIJobResponseBodyAIJobListAIJob]

    def validate(self):
        if self.aijob:
            for k in self.aijob:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AIJob'] = []
        if self.aijob is not None:
            for k in self.aijob:
                result['AIJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aijob = []
        if m.get('AIJob') is not None:
            for k in m.get('AIJob'):
                temp_model = ListAIJobResponseBodyAIJobListAIJob()
                self.aijob.append(temp_model.from_map(k))
        return self


class ListAIJobResponseBody(TeaModel):
    def __init__(self, request_id=None, non_exist_aijob_ids=None, aijob_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.non_exist_aijob_ids = non_exist_aijob_ids  # type: ListAIJobResponseBodyNonExistAIJobIds
        self.aijob_list = aijob_list  # type: ListAIJobResponseBodyAIJobList

    def validate(self):
        if self.non_exist_aijob_ids:
            self.non_exist_aijob_ids.validate()
        if self.aijob_list:
            self.aijob_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.non_exist_aijob_ids is not None:
            result['NonExistAIJobIds'] = self.non_exist_aijob_ids.to_map()
        if self.aijob_list is not None:
            result['AIJobList'] = self.aijob_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NonExistAIJobIds') is not None:
            temp_model = ListAIJobResponseBodyNonExistAIJobIds()
            self.non_exist_aijob_ids = temp_model.from_map(m['NonExistAIJobIds'])
        if m.get('AIJobList') is not None:
            temp_model = ListAIJobResponseBodyAIJobList()
            self.aijob_list = temp_model.from_map(m['AIJobList'])
        return self


class ListAIJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListAIJobResponseBody

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
            temp_model = ListAIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAITemplateRequest(TeaModel):
    def __init__(self, template_type=None):
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListAITemplateResponseBodyTemplateInfoList(TeaModel):
    def __init__(self, creation_time=None, is_default=None, template_type=None, template_config=None,
                 template_name=None, source=None, template_id=None, modify_time=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode
        self.template_name = TeaConverter.to_unicode(template_name)  # type: unicode
        self.source = TeaConverter.to_unicode(source)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.modify_time = TeaConverter.to_unicode(modify_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.source is not None:
            result['Source'] = self.source
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_info_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.template_info_list = template_info_list  # type: list[ListAITemplateResponseBodyTemplateInfoList]

    def validate(self):
        if self.template_info_list:
            for k in self.template_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TemplateInfoList'] = []
        if self.template_info_list is not None:
            for k in self.template_info_list:
                result['TemplateInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_info_list = []
        if m.get('TemplateInfoList') is not None:
            for k in m.get('TemplateInfoList'):
                temp_model = ListAITemplateResponseBodyTemplateInfoList()
                self.template_info_list.append(temp_model.from_map(k))
        return self


class ListAITemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListAITemplateResponseBody

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
            temp_model = ListAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInfoRequest(TeaModel):
    def __init__(self, resource_real_owner_id=None, status=None, page_no=None, page_size=None):
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppInfoResponseBodyAppInfoList(TeaModel):
    def __init__(self, type=None, status=None, creation_time=None, app_name=None, description=None, app_id=None,
                 modification_time=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.app_name = TeaConverter.to_unicode(app_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        return self


class ListAppInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, total=None, app_info_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total = total  # type: int
        self.app_info_list = app_info_list  # type: list[ListAppInfoResponseBodyAppInfoList]

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = ListAppInfoResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        return self


class ListAppInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListAppInfoResponseBody

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
            temp_model = ListAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppPoliciesForIdentityRequest(TeaModel):
    def __init__(self, identity_type=None, identity_name=None, app_id=None):
        self.identity_type = TeaConverter.to_unicode(identity_type)  # type: unicode
        self.identity_name = TeaConverter.to_unicode(identity_name)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListAppPoliciesForIdentityResponseBodyAppPolicyList(TeaModel):
    def __init__(self, creation_time=None, description=None, app_id=None, policy_value=None, policy_name=None,
                 modification_time=None, policy_type=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.policy_value = TeaConverter.to_unicode(policy_value)  # type: unicode
        self.policy_name = TeaConverter.to_unicode(policy_name)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.policy_type = TeaConverter.to_unicode(policy_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.policy_value is not None:
            result['PolicyValue'] = self.policy_value
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PolicyValue') is not None:
            self.policy_value = m.get('PolicyValue')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListAppPoliciesForIdentityResponseBody(TeaModel):
    def __init__(self, request_id=None, app_policy_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.app_policy_list = app_policy_list  # type: list[ListAppPoliciesForIdentityResponseBodyAppPolicyList]

    def validate(self):
        if self.app_policy_list:
            for k in self.app_policy_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AppPolicyList'] = []
        if self.app_policy_list is not None:
            for k in self.app_policy_list:
                result['AppPolicyList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.app_policy_list = []
        if m.get('AppPolicyList') is not None:
            for k in m.get('AppPolicyList'):
                temp_model = ListAppPoliciesForIdentityResponseBodyAppPolicyList()
                self.app_policy_list.append(temp_model.from_map(k))
        return self


class ListAppPoliciesForIdentityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListAppPoliciesForIdentityResponseBody

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
            temp_model = ListAppPoliciesForIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuditSecurityIpRequest(TeaModel):
    def __init__(self, security_group_name=None):
        self.security_group_name = TeaConverter.to_unicode(security_group_name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class ListAuditSecurityIpResponseBodySecurityIpList(TeaModel):
    def __init__(self, creation_time=None, security_group_name=None, ips=None, modification_time=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.security_group_name = TeaConverter.to_unicode(security_group_name)  # type: unicode
        self.ips = TeaConverter.to_unicode(ips)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        return self


class ListAuditSecurityIpResponseBody(TeaModel):
    def __init__(self, request_id=None, security_ip_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.security_ip_list = security_ip_list  # type: list[ListAuditSecurityIpResponseBodySecurityIpList]

    def validate(self):
        if self.security_ip_list:
            for k in self.security_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityIpList'] = []
        if self.security_ip_list is not None:
            for k in self.security_ip_list:
                result['SecurityIpList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_ip_list = []
        if m.get('SecurityIpList') is not None:
            for k in m.get('SecurityIpList'):
                temp_model = ListAuditSecurityIpResponseBodySecurityIpList()
                self.security_ip_list.append(temp_model.from_map(k))
        return self


class ListAuditSecurityIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListAuditSecurityIpResponseBody

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
            temp_model = ListAuditSecurityIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDynamicImageRequest(TeaModel):
    def __init__(self, video_id=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class ListDynamicImageResponseBodyDynamicImageList(TeaModel):
    def __init__(self, creation_time=None, file_url=None, video_id=None, width=None, job_id=None, height=None,
                 fps=None, duration=None, format=None, dynamic_image_id=None, file_size=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.width = TeaConverter.to_unicode(width)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.height = TeaConverter.to_unicode(height)  # type: unicode
        self.fps = TeaConverter.to_unicode(fps)  # type: unicode
        self.duration = TeaConverter.to_unicode(duration)  # type: unicode
        self.format = TeaConverter.to_unicode(format)  # type: unicode
        self.dynamic_image_id = TeaConverter.to_unicode(dynamic_image_id)  # type: unicode
        self.file_size = TeaConverter.to_unicode(file_size)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.width is not None:
            result['Width'] = self.width
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.height is not None:
            result['Height'] = self.height
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.format is not None:
            result['Format'] = self.format
        if self.dynamic_image_id is not None:
            result['DynamicImageId'] = self.dynamic_image_id
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('DynamicImageId') is not None:
            self.dynamic_image_id = m.get('DynamicImageId')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class ListDynamicImageResponseBody(TeaModel):
    def __init__(self, request_id=None, dynamic_image_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dynamic_image_list = dynamic_image_list  # type: list[ListDynamicImageResponseBodyDynamicImageList]

    def validate(self):
        if self.dynamic_image_list:
            for k in self.dynamic_image_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DynamicImageList'] = []
        if self.dynamic_image_list is not None:
            for k in self.dynamic_image_list:
                result['DynamicImageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.dynamic_image_list = []
        if m.get('DynamicImageList') is not None:
            for k in m.get('DynamicImageList'):
                temp_model = ListDynamicImageResponseBodyDynamicImageList()
                self.dynamic_image_list.append(temp_model.from_map(k))
        return self


class ListDynamicImageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListDynamicImageResponseBody

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
            temp_model = ListDynamicImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveRecordVideoRequest(TeaModel):
    def __init__(self, stream_name=None, domain_name=None, app_name=None, query_type=None, page_no=None,
                 page_size=None, sort_by=None, start_time=None, end_time=None):
        self.stream_name = TeaConverter.to_unicode(stream_name)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.app_name = TeaConverter.to_unicode(app_name)  # type: unicode
        self.query_type = TeaConverter.to_unicode(query_type)  # type: unicode
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = TeaConverter.to_unicode(sort_by)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        return self


class ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideo(TeaModel):
    def __init__(self, status=None, creation_time=None, cate_id=None, video_id=None, tags=None, snapshots=None,
                 cate_name=None, description=None, size=None, cover_url=None, template_group_id=None, duration=None,
                 title=None, modify_time=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.cate_id = cate_id  # type: int
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.snapshots = snapshots  # type: ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.size = size  # type: long
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.template_group_id = TeaConverter.to_unicode(template_group_id)  # type: unicode
        self.duration = duration  # type: float
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.modify_time = TeaConverter.to_unicode(modify_time)  # type: unicode

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.description is not None:
            result['Description'] = self.description
        if self.size is not None:
            result['Size'] = self.size
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Snapshots') is not None:
            temp_model = ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideo(TeaModel):
    def __init__(self, video=None, app_name=None, playlist_id=None, stream_name=None, record_end_time=None,
                 record_start_time=None, domain_name=None):
        self.video = video  # type: ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideo
        self.app_name = TeaConverter.to_unicode(app_name)  # type: unicode
        self.playlist_id = TeaConverter.to_unicode(playlist_id)  # type: unicode
        self.stream_name = TeaConverter.to_unicode(stream_name)  # type: unicode
        self.record_end_time = TeaConverter.to_unicode(record_end_time)  # type: unicode
        self.record_start_time = TeaConverter.to_unicode(record_start_time)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode

    def validate(self):
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        if self.video is not None:
            result['Video'] = self.video.to_map()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.playlist_id is not None:
            result['PlaylistId'] = self.playlist_id
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.record_end_time is not None:
            result['RecordEndTime'] = self.record_end_time
        if self.record_start_time is not None:
            result['RecordStartTime'] = self.record_start_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Video') is not None:
            temp_model = ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideo()
            self.video = temp_model.from_map(m['Video'])
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('PlaylistId') is not None:
            self.playlist_id = m.get('PlaylistId')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('RecordEndTime') is not None:
            self.record_end_time = m.get('RecordEndTime')
        if m.get('RecordStartTime') is not None:
            self.record_start_time = m.get('RecordStartTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class ListLiveRecordVideoResponseBodyLiveRecordVideoList(TeaModel):
    def __init__(self, live_record_video=None):
        self.live_record_video = live_record_video  # type: list[ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideo]

    def validate(self):
        if self.live_record_video:
            for k in self.live_record_video:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LiveRecordVideo'] = []
        if self.live_record_video is not None:
            for k in self.live_record_video:
                result['LiveRecordVideo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.live_record_video = []
        if m.get('LiveRecordVideo') is not None:
            for k in m.get('LiveRecordVideo'):
                temp_model = ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideo()
                self.live_record_video.append(temp_model.from_map(k))
        return self


class ListLiveRecordVideoResponseBody(TeaModel):
    def __init__(self, request_id=None, total=None, live_record_video_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total = total  # type: int
        self.live_record_video_list = live_record_video_list  # type: ListLiveRecordVideoResponseBodyLiveRecordVideoList

    def validate(self):
        if self.live_record_video_list:
            self.live_record_video_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.live_record_video_list is not None:
            result['LiveRecordVideoList'] = self.live_record_video_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('LiveRecordVideoList') is not None:
            temp_model = ListLiveRecordVideoResponseBodyLiveRecordVideoList()
            self.live_record_video_list = temp_model.from_map(m['LiveRecordVideoList'])
        return self


class ListLiveRecordVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListLiveRecordVideoResponseBody

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
            temp_model = ListLiveRecordVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMediaDNADeleteJobRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 job_ids=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.job_ids = TeaConverter.to_unicode(job_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        return self


class ListMediaDNADeleteJobResponseBodyNonExistAIJobIds(TeaModel):
    def __init__(self, string=None):
        self.string = string  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class ListMediaDNADeleteJobResponseBodyAIJobListAIJob(TeaModel):
    def __init__(self, status=None, job_id=None, code=None, message=None, media_id=None, fp_dbid=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.fp_dbid = TeaConverter.to_unicode(fp_dbid)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')
        return self


class ListMediaDNADeleteJobResponseBodyAIJobList(TeaModel):
    def __init__(self, aijob=None):
        self.aijob = aijob  # type: list[ListMediaDNADeleteJobResponseBodyAIJobListAIJob]

    def validate(self):
        if self.aijob:
            for k in self.aijob:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AIJob'] = []
        if self.aijob is not None:
            for k in self.aijob:
                result['AIJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aijob = []
        if m.get('AIJob') is not None:
            for k in m.get('AIJob'):
                temp_model = ListMediaDNADeleteJobResponseBodyAIJobListAIJob()
                self.aijob.append(temp_model.from_map(k))
        return self


class ListMediaDNADeleteJobResponseBody(TeaModel):
    def __init__(self, request_id=None, non_exist_aijob_ids=None, aijob_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.non_exist_aijob_ids = non_exist_aijob_ids  # type: ListMediaDNADeleteJobResponseBodyNonExistAIJobIds
        self.aijob_list = aijob_list  # type: ListMediaDNADeleteJobResponseBodyAIJobList

    def validate(self):
        if self.non_exist_aijob_ids:
            self.non_exist_aijob_ids.validate()
        if self.aijob_list:
            self.aijob_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.non_exist_aijob_ids is not None:
            result['NonExistAIJobIds'] = self.non_exist_aijob_ids.to_map()
        if self.aijob_list is not None:
            result['AIJobList'] = self.aijob_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NonExistAIJobIds') is not None:
            temp_model = ListMediaDNADeleteJobResponseBodyNonExistAIJobIds()
            self.non_exist_aijob_ids = temp_model.from_map(m['NonExistAIJobIds'])
        if m.get('AIJobList') is not None:
            temp_model = ListMediaDNADeleteJobResponseBodyAIJobList()
            self.aijob_list = temp_model.from_map(m['AIJobList'])
        return self


class ListMediaDNADeleteJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListMediaDNADeleteJobResponseBody

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
            temp_model = ListMediaDNADeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotsRequest(TeaModel):
    def __init__(self, video_id=None, snapshot_type=None, auth_timeout=None, page_size=None, page_no=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.snapshot_type = TeaConverter.to_unicode(snapshot_type)  # type: unicode
        self.auth_timeout = TeaConverter.to_unicode(auth_timeout)  # type: unicode
        self.page_size = TeaConverter.to_unicode(page_size)  # type: unicode
        self.page_no = TeaConverter.to_unicode(page_no)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class ListSnapshotsResponseBodyMediaSnapshotSnapshotsSnapshot(TeaModel):
    def __init__(self, index=None, url=None):
        self.index = index  # type: long
        self.url = TeaConverter.to_unicode(url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListSnapshotsResponseBodyMediaSnapshotSnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[ListSnapshotsResponseBodyMediaSnapshotSnapshotsSnapshot]

    def validate(self):
        if self.snapshot:
            for k in self.snapshot:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k in self.snapshot:
                result['Snapshot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k in m.get('Snapshot'):
                temp_model = ListSnapshotsResponseBodyMediaSnapshotSnapshotsSnapshot()
                self.snapshot.append(temp_model.from_map(k))
        return self


class ListSnapshotsResponseBodyMediaSnapshot(TeaModel):
    def __init__(self, creation_time=None, job_id=None, regular=None, total=None, snapshots=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.regular = TeaConverter.to_unicode(regular)  # type: unicode
        self.total = total  # type: long
        self.snapshots = snapshots  # type: ListSnapshotsResponseBodyMediaSnapshotSnapshots

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.regular is not None:
            result['Regular'] = self.regular
        if self.total is not None:
            result['Total'] = self.total
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Regular') is not None:
            self.regular = m.get('Regular')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Snapshots') is not None:
            temp_model = ListSnapshotsResponseBodyMediaSnapshotSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        return self


class ListSnapshotsResponseBody(TeaModel):
    def __init__(self, request_id=None, media_snapshot=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.media_snapshot = media_snapshot  # type: ListSnapshotsResponseBodyMediaSnapshot

    def validate(self):
        if self.media_snapshot:
            self.media_snapshot.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_snapshot is not None:
            result['MediaSnapshot'] = self.media_snapshot.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaSnapshot') is not None:
            temp_model = ListSnapshotsResponseBodyMediaSnapshot()
            self.media_snapshot = temp_model.from_map(m['MediaSnapshot'])
        return self


class ListSnapshotsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListSnapshotsResponseBody

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
            temp_model = ListSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTranscodeTaskRequest(TeaModel):
    def __init__(self, video_id=None, start_time=None, end_time=None, page_size=None, page_no=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.page_size = page_size  # type: int
        self.page_no = page_no  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class ListTranscodeTaskResponseBodyTranscodeTaskList(TeaModel):
    def __init__(self, creation_time=None, trigger=None, task_status=None, video_id=None, complete_time=None,
                 transcode_template_group_id=None, transcode_task_id=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.trigger = TeaConverter.to_unicode(trigger)  # type: unicode
        self.task_status = TeaConverter.to_unicode(task_status)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.complete_time = TeaConverter.to_unicode(complete_time)  # type: unicode
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode
        self.transcode_task_id = TeaConverter.to_unicode(transcode_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')
        return self


class ListTranscodeTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_task_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.transcode_task_list = transcode_task_list  # type: list[ListTranscodeTaskResponseBodyTranscodeTaskList]

    def validate(self):
        if self.transcode_task_list:
            for k in self.transcode_task_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TranscodeTaskList'] = []
        if self.transcode_task_list is not None:
            for k in self.transcode_task_list:
                result['TranscodeTaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.transcode_task_list = []
        if m.get('TranscodeTaskList') is not None:
            for k in m.get('TranscodeTaskList'):
                temp_model = ListTranscodeTaskResponseBodyTranscodeTaskList()
                self.transcode_task_list.append(temp_model.from_map(k))
        return self


class ListTranscodeTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListTranscodeTaskResponseBody

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
            temp_model = ListTranscodeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, page_size=None, page_no=None, app_id=None):
        self.page_size = page_size  # type: int
        self.page_no = page_no  # type: int
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupList(TeaModel):
    def __init__(self, creation_time=None, is_default=None, app_id=None, transcode_template_group_id=None,
                 name=None, modify_time=None, locked=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.modify_time = TeaConverter.to_unicode(modify_time)  # type: unicode
        self.locked = TeaConverter.to_unicode(locked)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.locked is not None:
            result['Locked'] = self.locked
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        return self


class ListTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_template_group_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.transcode_template_group_list = transcode_template_group_list  # type: list[ListTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupList]

    def validate(self):
        if self.transcode_template_group_list:
            for k in self.transcode_template_group_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TranscodeTemplateGroupList'] = []
        if self.transcode_template_group_list is not None:
            for k in self.transcode_template_group_list:
                result['TranscodeTemplateGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.transcode_template_group_list = []
        if m.get('TranscodeTemplateGroupList') is not None:
            for k in m.get('TranscodeTemplateGroupList'):
                temp_model = ListTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupList()
                self.transcode_template_group_list.append(temp_model.from_map(k))
        return self


class ListTranscodeTemplateGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListTranscodeTemplateGroupResponseBody

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
            temp_model = ListTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVodTemplateRequest(TeaModel):
    def __init__(self, template_type=None, app_id=None):
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListVodTemplateResponseBodyVodTemplateInfoList(TeaModel):
    def __init__(self, creation_time=None, is_default=None, app_id=None, template_type=None, vod_template_id=None,
                 template_config=None, name=None, modify_time=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.template_type = TeaConverter.to_unicode(template_type)  # type: unicode
        self.vod_template_id = TeaConverter.to_unicode(vod_template_id)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.modify_time = TeaConverter.to_unicode(modify_time)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.name is not None:
            result['Name'] = self.name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListVodTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, vod_template_info_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.vod_template_info_list = vod_template_info_list  # type: list[ListVodTemplateResponseBodyVodTemplateInfoList]

    def validate(self):
        if self.vod_template_info_list:
            for k in self.vod_template_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VodTemplateInfoList'] = []
        if self.vod_template_info_list is not None:
            for k in self.vod_template_info_list:
                result['VodTemplateInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.vod_template_info_list = []
        if m.get('VodTemplateInfoList') is not None:
            for k in m.get('VodTemplateInfoList'):
                temp_model = ListVodTemplateResponseBodyVodTemplateInfoList()
                self.vod_template_info_list.append(temp_model.from_map(k))
        return self


class ListVodTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListVodTemplateResponseBody

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
            temp_model = ListVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWatermarkRequest(TeaModel):
    def __init__(self, page_size=None, page_no=None, app_id=None):
        self.page_size = page_size  # type: int
        self.page_no = page_no  # type: int
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListWatermarkResponseBodyWatermarkInfos(TeaModel):
    def __init__(self, creation_time=None, type=None, is_default=None, file_url=None, app_id=None,
                 watermark_config=None, name=None, watermark_id=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.watermark_config = TeaConverter.to_unicode(watermark_config)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.watermark_id = TeaConverter.to_unicode(watermark_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.type is not None:
            result['Type'] = self.type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class ListWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, watermark_infos=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.watermark_infos = watermark_infos  # type: list[ListWatermarkResponseBodyWatermarkInfos]

    def validate(self):
        if self.watermark_infos:
            for k in self.watermark_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['WatermarkInfos'] = []
        if self.watermark_infos is not None:
            for k in self.watermark_infos:
                result['WatermarkInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.watermark_infos = []
        if m.get('WatermarkInfos') is not None:
            for k in m.get('WatermarkInfos'):
                temp_model = ListWatermarkResponseBodyWatermarkInfos()
                self.watermark_infos.append(temp_model.from_map(k))
        return self


class ListWatermarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListWatermarkResponseBody

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
            temp_model = ListWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveAppResourceRequest(TeaModel):
    def __init__(self, resource_real_owner_id=None, target_app_id=None, resource_type=None, resource_ids=None):
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.target_app_id = TeaConverter.to_unicode(target_app_id)  # type: unicode
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.resource_ids = TeaConverter.to_unicode(resource_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.target_app_id is not None:
            result['TargetAppId'] = self.target_app_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('TargetAppId') is not None:
            self.target_app_id = m.get('TargetAppId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        return self


class MoveAppResourceResponseBody(TeaModel):
    def __init__(self, failed_resource_ids=None, request_id=None, non_exist_resource_ids=None):
        self.failed_resource_ids = failed_resource_ids  # type: list[unicode]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.non_exist_resource_ids = non_exist_resource_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.failed_resource_ids is not None:
            result['FailedResourceIds'] = self.failed_resource_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.non_exist_resource_ids is not None:
            result['NonExistResourceIds'] = self.non_exist_resource_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedResourceIds') is not None:
            self.failed_resource_ids = m.get('FailedResourceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NonExistResourceIds') is not None:
            self.non_exist_resource_ids = m.get('NonExistResourceIds')
        return self


class MoveAppResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: MoveAppResourceResponseBody

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
            temp_model = MoveAppResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreloadVodObjectCachesRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, object_path=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.object_path = TeaConverter.to_unicode(object_path)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        return self


class PreloadVodObjectCachesResponseBody(TeaModel):
    def __init__(self, request_id=None, preload_task_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.preload_task_id = TeaConverter.to_unicode(preload_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.preload_task_id is not None:
            result['PreloadTaskId'] = self.preload_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreloadTaskId') is not None:
            self.preload_task_id = m.get('PreloadTaskId')
        return self


class PreloadVodObjectCachesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: PreloadVodObjectCachesResponseBody

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
            temp_model = PreloadVodObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProduceEditingProjectVideoRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, project_id=None,
                 timeline=None, title=None, description=None, cover_url=None, media_metadata=None, produce_config=None,
                 user_data=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.project_id = TeaConverter.to_unicode(project_id)  # type: unicode
        self.timeline = TeaConverter.to_unicode(timeline)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.media_metadata = TeaConverter.to_unicode(media_metadata)  # type: unicode
        self.produce_config = TeaConverter.to_unicode(produce_config)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.media_metadata is not None:
            result['MediaMetadata'] = self.media_metadata
        if self.produce_config is not None:
            result['ProduceConfig'] = self.produce_config
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('MediaMetadata') is not None:
            self.media_metadata = m.get('MediaMetadata')
        if m.get('ProduceConfig') is not None:
            self.produce_config = m.get('ProduceConfig')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class ProduceEditingProjectVideoResponseBody(TeaModel):
    def __init__(self, request_id=None, media_id=None, project_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.project_id = TeaConverter.to_unicode(project_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ProduceEditingProjectVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ProduceEditingProjectVideoResponseBody

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
            temp_model = ProduceEditingProjectVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshUploadVideoRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, video_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.resource_owner_id = resource_owner_id  # type: long
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class RefreshUploadVideoResponseBody(TeaModel):
    def __init__(self, upload_address=None, video_id=None, request_id=None, upload_auth=None):
        self.upload_address = TeaConverter.to_unicode(upload_address)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.upload_auth = TeaConverter.to_unicode(upload_auth)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')
        return self


class RefreshUploadVideoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RefreshUploadVideoResponseBody

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
            temp_model = RefreshUploadVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshVodObjectCachesRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, object_path=None, object_type=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.object_path = TeaConverter.to_unicode(object_path)  # type: unicode
        self.object_type = TeaConverter.to_unicode(object_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        return self


class RefreshVodObjectCachesResponseBody(TeaModel):
    def __init__(self, request_id=None, refresh_task_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.refresh_task_id = TeaConverter.to_unicode(refresh_task_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refresh_task_id is not None:
            result['RefreshTaskId'] = self.refresh_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefreshTaskId') is not None:
            self.refresh_task_id = m.get('RefreshTaskId')
        return self


class RefreshVodObjectCachesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RefreshVodObjectCachesResponseBody

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
            temp_model = RefreshVodObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterMediaRequest(TeaModel):
    def __init__(self, register_metadatas=None, template_group_id=None, user_data=None, workflow_id=None):
        self.register_metadatas = TeaConverter.to_unicode(register_metadatas)  # type: unicode
        self.template_group_id = TeaConverter.to_unicode(template_group_id)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.workflow_id = TeaConverter.to_unicode(workflow_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.register_metadatas is not None:
            result['RegisterMetadatas'] = self.register_metadatas
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegisterMetadatas') is not None:
            self.register_metadatas = m.get('RegisterMetadatas')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class RegisterMediaResponseBodyRegisteredMediaList(TeaModel):
    def __init__(self, new_register=None, file_url=None, media_id=None):
        self.new_register = new_register  # type: bool
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.new_register is not None:
            result['NewRegister'] = self.new_register
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewRegister') is not None:
            self.new_register = m.get('NewRegister')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class RegisterMediaResponseBody(TeaModel):
    def __init__(self, request_id=None, failed_file_urls=None, registered_media_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.failed_file_urls = failed_file_urls  # type: list[unicode]
        self.registered_media_list = registered_media_list  # type: list[RegisterMediaResponseBodyRegisteredMediaList]

    def validate(self):
        if self.registered_media_list:
            for k in self.registered_media_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.failed_file_urls is not None:
            result['FailedFileURLs'] = self.failed_file_urls
        result['RegisteredMediaList'] = []
        if self.registered_media_list is not None:
            for k in self.registered_media_list:
                result['RegisteredMediaList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FailedFileURLs') is not None:
            self.failed_file_urls = m.get('FailedFileURLs')
        self.registered_media_list = []
        if m.get('RegisteredMediaList') is not None:
            for k in m.get('RegisteredMediaList'):
                temp_model = RegisterMediaResponseBodyRegisteredMediaList()
                self.registered_media_list.append(temp_model.from_map(k))
        return self


class RegisterMediaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RegisterMediaResponseBody

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
            temp_model = RegisterMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEditingProjectRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 end_time=None, start_time=None, status=None, page_no=None, page_size=None, sort_by=None, title=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.end_time = TeaConverter.to_unicode(end_time)  # type: unicode
        self.start_time = TeaConverter.to_unicode(start_time)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = TeaConverter.to_unicode(sort_by)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchEditingProjectResponseBodyProjectListProject(TeaModel):
    def __init__(self, storage_location=None, status=None, creation_time=None, modified_time=None, description=None,
                 cover_url=None, project_id=None, duration=None, title=None, region_id=None):
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.modified_time = TeaConverter.to_unicode(modified_time)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.project_id = TeaConverter.to_unicode(project_id)  # type: unicode
        self.duration = duration  # type: float
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.region_id = TeaConverter.to_unicode(region_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.description is not None:
            result['Description'] = self.description
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchEditingProjectResponseBodyProjectList(TeaModel):
    def __init__(self, project=None):
        self.project = project  # type: list[SearchEditingProjectResponseBodyProjectListProject]

    def validate(self):
        if self.project:
            for k in self.project:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Project'] = []
        if self.project is not None:
            for k in self.project:
                result['Project'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.project = []
        if m.get('Project') is not None:
            for k in m.get('Project'):
                temp_model = SearchEditingProjectResponseBodyProjectListProject()
                self.project.append(temp_model.from_map(k))
        return self


class SearchEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, total=None, project_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.total = total  # type: int
        self.project_list = project_list  # type: SearchEditingProjectResponseBodyProjectList

    def validate(self):
        if self.project_list:
            self.project_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.project_list is not None:
            result['ProjectList'] = self.project_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('ProjectList') is not None:
            temp_model = SearchEditingProjectResponseBodyProjectList()
            self.project_list = temp_model.from_map(m['ProjectList'])
        return self


class SearchEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SearchEditingProjectResponseBody

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
            temp_model = SearchEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchMediaRequest(TeaModel):
    def __init__(self, search_type=None, fields=None, match=None, sort_by=None, page_no=None, page_size=None,
                 scroll_token=None, session_id=None, result_types=None):
        self.search_type = TeaConverter.to_unicode(search_type)  # type: unicode
        self.fields = TeaConverter.to_unicode(fields)  # type: unicode
        self.match = TeaConverter.to_unicode(match)  # type: unicode
        self.sort_by = TeaConverter.to_unicode(sort_by)  # type: unicode
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.scroll_token = TeaConverter.to_unicode(scroll_token)  # type: unicode
        self.session_id = TeaConverter.to_unicode(session_id)  # type: unicode
        self.result_types = TeaConverter.to_unicode(result_types)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.match is not None:
            result['Match'] = self.match
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scroll_token is not None:
            result['ScrollToken'] = self.scroll_token
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.result_types is not None:
            result['ResultTypes'] = self.result_types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Match') is not None:
            self.match = m.get('Match')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScrollToken') is not None:
            self.scroll_token = m.get('ScrollToken')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('ResultTypes') is not None:
            self.result_types = m.get('ResultTypes')
        return self


class SearchMediaResponseBodyMediaListVideo(TeaModel):
    def __init__(self, status=None, creation_time=None, storage_location=None, cate_id=None, tags=None,
                 modification_time=None, media_source=None, description=None, app_id=None, cover_url=None, video_id=None,
                 download_switch=None, snapshots=None, transcode_mode=None, cate_name=None, preprocess_status=None,
                 sprite_snapshots=None, size=None, duration=None, title=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.media_source = TeaConverter.to_unicode(media_source)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.download_switch = TeaConverter.to_unicode(download_switch)  # type: unicode
        self.snapshots = snapshots  # type: list[unicode]
        self.transcode_mode = TeaConverter.to_unicode(transcode_mode)  # type: unicode
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.preprocess_status = TeaConverter.to_unicode(preprocess_status)  # type: unicode
        self.sprite_snapshots = sprite_snapshots  # type: list[unicode]
        self.size = size  # type: long
        self.duration = duration  # type: float
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.media_source is not None:
            result['MediaSource'] = self.media_source
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.download_switch is not None:
            result['DownloadSwitch'] = self.download_switch
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.transcode_mode is not None:
            result['TranscodeMode'] = self.transcode_mode
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.preprocess_status is not None:
            result['PreprocessStatus'] = self.preprocess_status
        if self.sprite_snapshots is not None:
            result['SpriteSnapshots'] = self.sprite_snapshots
        if self.size is not None:
            result['Size'] = self.size
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('MediaSource') is not None:
            self.media_source = m.get('MediaSource')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('DownloadSwitch') is not None:
            self.download_switch = m.get('DownloadSwitch')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('TranscodeMode') is not None:
            self.transcode_mode = m.get('TranscodeMode')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('PreprocessStatus') is not None:
            self.preprocess_status = m.get('PreprocessStatus')
        if m.get('SpriteSnapshots') is not None:
            self.sprite_snapshots = m.get('SpriteSnapshots')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchMediaResponseBodyMediaListAttachedMediaCategories(TeaModel):
    def __init__(self, parent_id=None, cate_name=None, cate_id=None, level=None):
        self.parent_id = parent_id  # type: long
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.level = level  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class SearchMediaResponseBodyMediaListAttachedMedia(TeaModel):
    def __init__(self, storage_location=None, status=None, creation_time=None, tags=None, modification_time=None,
                 media_id=None, business_type=None, description=None, categories=None, app_id=None, url=None, title=None):
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.business_type = TeaConverter.to_unicode(business_type)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.categories = categories  # type: list[SearchMediaResponseBodyMediaListAttachedMediaCategories]
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.description is not None:
            result['Description'] = self.description
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.url is not None:
            result['URL'] = self.url
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = SearchMediaResponseBodyMediaListAttachedMediaCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchMediaResponseBodyMediaListImage(TeaModel):
    def __init__(self, status=None, creation_time=None, storage_location=None, cate_id=None, tags=None,
                 modification_time=None, cate_name=None, description=None, app_id=None, url=None, title=None, image_id=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.url = TeaConverter.to_unicode(url)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.image_id = TeaConverter.to_unicode(image_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.url is not None:
            result['URL'] = self.url
        if self.title is not None:
            result['Title'] = self.title
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class SearchMediaResponseBodyMediaListAudio(TeaModel):
    def __init__(self, status=None, creation_time=None, storage_location=None, cate_id=None, tags=None,
                 modification_time=None, media_source=None, description=None, app_id=None, cover_url=None, audio_id=None,
                 download_switch=None, snapshots=None, transcode_mode=None, cate_name=None, preprocess_status=None,
                 sprite_snapshots=None, size=None, duration=None, title=None):
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.modification_time = TeaConverter.to_unicode(modification_time)  # type: unicode
        self.media_source = TeaConverter.to_unicode(media_source)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.audio_id = TeaConverter.to_unicode(audio_id)  # type: unicode
        self.download_switch = TeaConverter.to_unicode(download_switch)  # type: unicode
        self.snapshots = snapshots  # type: list[unicode]
        self.transcode_mode = TeaConverter.to_unicode(transcode_mode)  # type: unicode
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.preprocess_status = TeaConverter.to_unicode(preprocess_status)  # type: unicode
        self.sprite_snapshots = sprite_snapshots  # type: list[unicode]
        self.size = size  # type: long
        self.duration = duration  # type: float
        self.title = TeaConverter.to_unicode(title)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.media_source is not None:
            result['MediaSource'] = self.media_source
        if self.description is not None:
            result['Description'] = self.description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.download_switch is not None:
            result['DownloadSwitch'] = self.download_switch
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.transcode_mode is not None:
            result['TranscodeMode'] = self.transcode_mode
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.preprocess_status is not None:
            result['PreprocessStatus'] = self.preprocess_status
        if self.sprite_snapshots is not None:
            result['SpriteSnapshots'] = self.sprite_snapshots
        if self.size is not None:
            result['Size'] = self.size
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('MediaSource') is not None:
            self.media_source = m.get('MediaSource')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('DownloadSwitch') is not None:
            self.download_switch = m.get('DownloadSwitch')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('TranscodeMode') is not None:
            self.transcode_mode = m.get('TranscodeMode')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('PreprocessStatus') is not None:
            self.preprocess_status = m.get('PreprocessStatus')
        if m.get('SpriteSnapshots') is not None:
            self.sprite_snapshots = m.get('SpriteSnapshots')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchMediaResponseBodyMediaList(TeaModel):
    def __init__(self, creation_time=None, video=None, attached_media=None, image=None, media_type=None, audio=None,
                 media_id=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.video = video  # type: SearchMediaResponseBodyMediaListVideo
        self.attached_media = attached_media  # type: SearchMediaResponseBodyMediaListAttachedMedia
        self.image = image  # type: SearchMediaResponseBodyMediaListImage
        self.media_type = TeaConverter.to_unicode(media_type)  # type: unicode
        self.audio = audio  # type: SearchMediaResponseBodyMediaListAudio
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode

    def validate(self):
        if self.video:
            self.video.validate()
        if self.attached_media:
            self.attached_media.validate()
        if self.image:
            self.image.validate()
        if self.audio:
            self.audio.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.video is not None:
            result['Video'] = self.video.to_map()
        if self.attached_media is not None:
            result['AttachedMedia'] = self.attached_media.to_map()
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Video') is not None:
            temp_model = SearchMediaResponseBodyMediaListVideo()
            self.video = temp_model.from_map(m['Video'])
        if m.get('AttachedMedia') is not None:
            temp_model = SearchMediaResponseBodyMediaListAttachedMedia()
            self.attached_media = temp_model.from_map(m['AttachedMedia'])
        if m.get('Image') is not None:
            temp_model = SearchMediaResponseBodyMediaListImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Audio') is not None:
            temp_model = SearchMediaResponseBodyMediaListAudio()
            self.audio = temp_model.from_map(m['Audio'])
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class SearchMediaResponseBody(TeaModel):
    def __init__(self, media_list=None, request_id=None, scroll_token=None, total=None):
        self.media_list = media_list  # type: list[SearchMediaResponseBodyMediaList]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.scroll_token = TeaConverter.to_unicode(scroll_token)  # type: unicode
        self.total = total  # type: long

    def validate(self):
        if self.media_list:
            for k in self.media_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MediaList'] = []
        if self.media_list is not None:
            for k in self.media_list:
                result['MediaList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scroll_token is not None:
            result['ScrollToken'] = self.scroll_token
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.media_list = []
        if m.get('MediaList') is not None:
            for k in m.get('MediaList'):
                temp_model = SearchMediaResponseBodyMediaList()
                self.media_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScrollToken') is not None:
            self.scroll_token = m.get('ScrollToken')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SearchMediaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SearchMediaResponseBody

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
            temp_model = SearchMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAuditSecurityIpRequest(TeaModel):
    def __init__(self, security_group_name=None, ips=None, operate_mode=None):
        self.security_group_name = TeaConverter.to_unicode(security_group_name)  # type: unicode
        self.ips = TeaConverter.to_unicode(ips)  # type: unicode
        self.operate_mode = TeaConverter.to_unicode(operate_mode)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.operate_mode is not None:
            result['OperateMode'] = self.operate_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('OperateMode') is not None:
            self.operate_mode = m.get('OperateMode')
        return self


class SetAuditSecurityIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetAuditSecurityIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetAuditSecurityIpResponseBody

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
            temp_model = SetAuditSecurityIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultAITemplateRequest(TeaModel):
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


class SetDefaultAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class SetDefaultAITemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetDefaultAITemplateResponseBody

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
            temp_model = SetDefaultAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, transcode_template_group_id=None):
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        return self


class SetDefaultTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDefaultTranscodeTemplateGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetDefaultTranscodeTemplateGroupResponseBody

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
            temp_model = SetDefaultTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultWatermarkRequest(TeaModel):
    def __init__(self, watermark_id=None):
        self.watermark_id = TeaConverter.to_unicode(watermark_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class SetDefaultWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDefaultWatermarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetDefaultWatermarkResponseBody

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
            temp_model = SetDefaultWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 project_id=None, material_ids=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.project_id = TeaConverter.to_unicode(project_id)  # type: unicode
        self.material_ids = TeaConverter.to_unicode(material_ids)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.material_ids is not None:
            result['MaterialIds'] = self.material_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('MaterialIds') is not None:
            self.material_ids = m.get('MaterialIds')
        return self


class SetEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetEditingProjectMaterialsResponseBody

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
            temp_model = SetEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMessageCallbackRequest(TeaModel):
    def __init__(self, owner_account=None, callback_switch=None, callback_type=None, callback_url=None,
                 event_type_list=None, auth_switch=None, auth_key=None, resource_real_owner_id=None, mns_endpoint=None,
                 mns_queue_name=None, app_id=None):
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.callback_switch = TeaConverter.to_unicode(callback_switch)  # type: unicode
        self.callback_type = TeaConverter.to_unicode(callback_type)  # type: unicode
        self.callback_url = TeaConverter.to_unicode(callback_url)  # type: unicode
        self.event_type_list = TeaConverter.to_unicode(event_type_list)  # type: unicode
        self.auth_switch = TeaConverter.to_unicode(auth_switch)  # type: unicode
        self.auth_key = TeaConverter.to_unicode(auth_key)  # type: unicode
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.mns_endpoint = TeaConverter.to_unicode(mns_endpoint)  # type: unicode
        self.mns_queue_name = TeaConverter.to_unicode(mns_queue_name)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.callback_switch is not None:
            result['CallbackSwitch'] = self.callback_switch
        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type
        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        if self.auth_switch is not None:
            result['AuthSwitch'] = self.auth_switch
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.mns_endpoint is not None:
            result['MnsEndpoint'] = self.mns_endpoint
        if self.mns_queue_name is not None:
            result['MnsQueueName'] = self.mns_queue_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('CallbackSwitch') is not None:
            self.callback_switch = m.get('CallbackSwitch')
        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')
        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        if m.get('AuthSwitch') is not None:
            self.auth_switch = m.get('AuthSwitch')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('MnsEndpoint') is not None:
            self.mns_endpoint = m.get('MnsEndpoint')
        if m.get('MnsQueueName') is not None:
            self.mns_queue_name = m.get('MnsQueueName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class SetMessageCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetMessageCallbackResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetMessageCallbackResponseBody

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
            temp_model = SetMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetVodDomainCertificateRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_name=None, cert_name=None, sslprotocol=None,
                 sslpub=None, sslpri=None, region=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.cert_name = TeaConverter.to_unicode(cert_name)  # type: unicode
        self.sslprotocol = TeaConverter.to_unicode(sslprotocol)  # type: unicode
        self.sslpub = TeaConverter.to_unicode(sslpub)  # type: unicode
        self.sslpri = TeaConverter.to_unicode(sslpri)  # type: unicode
        self.region = TeaConverter.to_unicode(region)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SetVodDomainCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetVodDomainCertificateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SetVodDomainCertificateResponseBody

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
            temp_model = SetVodDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAICaptionExtractionJobRequest(TeaModel):
    def __init__(self, video_id=None, job_config=None, aipipeline_id=None, user_data=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.job_config = TeaConverter.to_unicode(job_config)  # type: unicode
        self.aipipeline_id = TeaConverter.to_unicode(aipipeline_id)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.job_config is not None:
            result['JobConfig'] = self.job_config
        if self.aipipeline_id is not None:
            result['AIPipelineId'] = self.aipipeline_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('JobConfig') is not None:
            self.job_config = m.get('JobConfig')
        if m.get('AIPipelineId') is not None:
            self.aipipeline_id = m.get('AIPipelineId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitAICaptionExtractionJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitAICaptionExtractionJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitAICaptionExtractionJobResponseBody

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
            temp_model = SubmitAICaptionExtractionJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAIImageAuditJobRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 media_id=None, template_id=None, media_audit_configuration=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.media_audit_configuration = TeaConverter.to_unicode(media_audit_configuration)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.media_audit_configuration is not None:
            result['MediaAuditConfiguration'] = self.media_audit_configuration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('MediaAuditConfiguration') is not None:
            self.media_audit_configuration = m.get('MediaAuditConfiguration')
        return self


class SubmitAIImageAuditJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitAIImageAuditJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitAIImageAuditJobResponseBody

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
            temp_model = SubmitAIImageAuditJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAIImageJobRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 video_id=None, aitemplate_id=None, user_data=None, aipipeline_id=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.aitemplate_id = TeaConverter.to_unicode(aitemplate_id)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.aipipeline_id = TeaConverter.to_unicode(aipipeline_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.aitemplate_id is not None:
            result['AITemplateId'] = self.aitemplate_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.aipipeline_id is not None:
            result['AIPipelineId'] = self.aipipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('AITemplateId') is not None:
            self.aitemplate_id = m.get('AITemplateId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('AIPipelineId') is not None:
            self.aipipeline_id = m.get('AIPipelineId')
        return self


class SubmitAIImageJobResponseBody(TeaModel):
    def __init__(self, request_id=None, job_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitAIImageJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitAIImageJobResponseBody

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
            temp_model = SubmitAIImageJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAIJobRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 media_id=None, types=None, config=None, user_data=None, input=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.types = TeaConverter.to_unicode(types)  # type: unicode
        self.config = TeaConverter.to_unicode(config)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.input = TeaConverter.to_unicode(input)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.types is not None:
            result['Types'] = self.types
        if self.config is not None:
            result['Config'] = self.config
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.input is not None:
            result['Input'] = self.input
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        return self


class SubmitAIJobResponseBodyAIJobListAIJob(TeaModel):
    def __init__(self, type=None, job_id=None, media_id=None):
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class SubmitAIJobResponseBodyAIJobList(TeaModel):
    def __init__(self, aijob=None):
        self.aijob = aijob  # type: list[SubmitAIJobResponseBodyAIJobListAIJob]

    def validate(self):
        if self.aijob:
            for k in self.aijob:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AIJob'] = []
        if self.aijob is not None:
            for k in self.aijob:
                result['AIJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aijob = []
        if m.get('AIJob') is not None:
            for k in m.get('AIJob'):
                temp_model = SubmitAIJobResponseBodyAIJobListAIJob()
                self.aijob.append(temp_model.from_map(k))
        return self


class SubmitAIJobResponseBody(TeaModel):
    def __init__(self, request_id=None, aijob_list=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.aijob_list = aijob_list  # type: SubmitAIJobResponseBodyAIJobList

    def validate(self):
        if self.aijob_list:
            self.aijob_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.aijob_list is not None:
            result['AIJobList'] = self.aijob_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AIJobList') is not None:
            temp_model = SubmitAIJobResponseBodyAIJobList()
            self.aijob_list = temp_model.from_map(m['AIJobList'])
        return self


class SubmitAIJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitAIJobResponseBody

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
            temp_model = SubmitAIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAIMediaAuditJobRequest(TeaModel):
    def __init__(self, media_id=None, template_id=None, user_data=None, media_type=None,
                 media_audit_configuration=None):
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.media_type = TeaConverter.to_unicode(media_type)  # type: unicode
        self.media_audit_configuration = TeaConverter.to_unicode(media_audit_configuration)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.media_audit_configuration is not None:
            result['MediaAuditConfiguration'] = self.media_audit_configuration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('MediaAuditConfiguration') is not None:
            self.media_audit_configuration = m.get('MediaAuditConfiguration')
        return self


class SubmitAIMediaAuditJobResponseBody(TeaModel):
    def __init__(self, request_id=None, media_id=None, job_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitAIMediaAuditJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitAIMediaAuditJobResponseBody

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
            temp_model = SubmitAIMediaAuditJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDynamicImageJobRequest(TeaModel):
    def __init__(self, video_id=None, dynamic_image_template_id=None, override_params=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.dynamic_image_template_id = TeaConverter.to_unicode(dynamic_image_template_id)  # type: unicode
        self.override_params = TeaConverter.to_unicode(override_params)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.dynamic_image_template_id is not None:
            result['DynamicImageTemplateId'] = self.dynamic_image_template_id
        if self.override_params is not None:
            result['OverrideParams'] = self.override_params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('DynamicImageTemplateId') is not None:
            self.dynamic_image_template_id = m.get('DynamicImageTemplateId')
        if m.get('OverrideParams') is not None:
            self.override_params = m.get('OverrideParams')
        return self


class SubmitDynamicImageJobResponseBodyDynamicImageJob(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitDynamicImageJobResponseBody(TeaModel):
    def __init__(self, request_id=None, dynamic_image_job=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.dynamic_image_job = dynamic_image_job  # type: SubmitDynamicImageJobResponseBodyDynamicImageJob

    def validate(self):
        if self.dynamic_image_job:
            self.dynamic_image_job.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dynamic_image_job is not None:
            result['DynamicImageJob'] = self.dynamic_image_job.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DynamicImageJob') is not None:
            temp_model = SubmitDynamicImageJobResponseBodyDynamicImageJob()
            self.dynamic_image_job = temp_model.from_map(m['DynamicImageJob'])
        return self


class SubmitDynamicImageJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitDynamicImageJobResponseBody

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
            temp_model = SubmitDynamicImageJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitMediaDNADeleteJobRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 media_id=None, fp_dbid=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.fp_dbid = TeaConverter.to_unicode(fp_dbid)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')
        return self


class SubmitMediaDNADeleteJobResponseBody(TeaModel):
    def __init__(self, request_id=None, media_id=None, job_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitMediaDNADeleteJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitMediaDNADeleteJobResponseBody

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
            temp_model = SubmitMediaDNADeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPreprocessJobsRequest(TeaModel):
    def __init__(self, video_id=None, preprocess_type=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.preprocess_type = TeaConverter.to_unicode(preprocess_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.preprocess_type is not None:
            result['PreprocessType'] = self.preprocess_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('PreprocessType') is not None:
            self.preprocess_type = m.get('PreprocessType')
        return self


class SubmitPreprocessJobsResponseBodyPreprocessJobsPreprocessJob(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitPreprocessJobsResponseBodyPreprocessJobs(TeaModel):
    def __init__(self, preprocess_job=None):
        self.preprocess_job = preprocess_job  # type: list[SubmitPreprocessJobsResponseBodyPreprocessJobsPreprocessJob]

    def validate(self):
        if self.preprocess_job:
            for k in self.preprocess_job:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PreprocessJob'] = []
        if self.preprocess_job is not None:
            for k in self.preprocess_job:
                result['PreprocessJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.preprocess_job = []
        if m.get('PreprocessJob') is not None:
            for k in m.get('PreprocessJob'):
                temp_model = SubmitPreprocessJobsResponseBodyPreprocessJobsPreprocessJob()
                self.preprocess_job.append(temp_model.from_map(k))
        return self


class SubmitPreprocessJobsResponseBody(TeaModel):
    def __init__(self, request_id=None, preprocess_jobs=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.preprocess_jobs = preprocess_jobs  # type: SubmitPreprocessJobsResponseBodyPreprocessJobs

    def validate(self):
        if self.preprocess_jobs:
            self.preprocess_jobs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.preprocess_jobs is not None:
            result['PreprocessJobs'] = self.preprocess_jobs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreprocessJobs') is not None:
            temp_model = SubmitPreprocessJobsResponseBodyPreprocessJobs()
            self.preprocess_jobs = temp_model.from_map(m['PreprocessJobs'])
        return self


class SubmitPreprocessJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitPreprocessJobsResponseBody

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
            temp_model = SubmitPreprocessJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSnapshotJobRequest(TeaModel):
    def __init__(self, video_id=None, specified_offset_time=None, width=None, height=None, count=None, interval=None,
                 sprite_snapshot_config=None, snapshot_template_id=None, user_data=None, file_url=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.specified_offset_time = specified_offset_time  # type: long
        self.width = TeaConverter.to_unicode(width)  # type: unicode
        self.height = TeaConverter.to_unicode(height)  # type: unicode
        self.count = count  # type: long
        self.interval = interval  # type: long
        self.sprite_snapshot_config = TeaConverter.to_unicode(sprite_snapshot_config)  # type: unicode
        self.snapshot_template_id = TeaConverter.to_unicode(snapshot_template_id)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.specified_offset_time is not None:
            result['SpecifiedOffsetTime'] = self.specified_offset_time
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.sprite_snapshot_config is not None:
            result['SpriteSnapshotConfig'] = self.sprite_snapshot_config
        if self.snapshot_template_id is not None:
            result['SnapshotTemplateId'] = self.snapshot_template_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('SpecifiedOffsetTime') is not None:
            self.specified_offset_time = m.get('SpecifiedOffsetTime')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('SpriteSnapshotConfig') is not None:
            self.sprite_snapshot_config = m.get('SpriteSnapshotConfig')
        if m.get('SnapshotTemplateId') is not None:
            self.snapshot_template_id = m.get('SnapshotTemplateId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitSnapshotJobResponseBodySnapshotJob(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitSnapshotJobResponseBody(TeaModel):
    def __init__(self, request_id=None, snapshot_job=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.snapshot_job = snapshot_job  # type: SubmitSnapshotJobResponseBodySnapshotJob

    def validate(self):
        if self.snapshot_job:
            self.snapshot_job.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_job is not None:
            result['SnapshotJob'] = self.snapshot_job.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotJob') is not None:
            temp_model = SubmitSnapshotJobResponseBodySnapshotJob()
            self.snapshot_job = temp_model.from_map(m['SnapshotJob'])
        return self


class SubmitSnapshotJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitSnapshotJobResponseBody

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
            temp_model = SubmitSnapshotJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTranscodeJobsRequest(TeaModel):
    def __init__(self, video_id=None, template_group_id=None, pipeline_id=None, encrypt_config=None,
                 override_params=None, priority=None, user_data=None, file_url=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.template_group_id = TeaConverter.to_unicode(template_group_id)  # type: unicode
        self.pipeline_id = TeaConverter.to_unicode(pipeline_id)  # type: unicode
        self.encrypt_config = TeaConverter.to_unicode(encrypt_config)  # type: unicode
        self.override_params = TeaConverter.to_unicode(override_params)  # type: unicode
        self.priority = TeaConverter.to_unicode(priority)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.encrypt_config is not None:
            result['EncryptConfig'] = self.encrypt_config
        if self.override_params is not None:
            result['OverrideParams'] = self.override_params
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('EncryptConfig') is not None:
            self.encrypt_config = m.get('EncryptConfig')
        if m.get('OverrideParams') is not None:
            self.override_params = m.get('OverrideParams')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitTranscodeJobsResponseBodyTranscodeJobsTranscodeJob(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitTranscodeJobsResponseBodyTranscodeJobs(TeaModel):
    def __init__(self, transcode_job=None):
        self.transcode_job = transcode_job  # type: list[SubmitTranscodeJobsResponseBodyTranscodeJobsTranscodeJob]

    def validate(self):
        if self.transcode_job:
            for k in self.transcode_job:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TranscodeJob'] = []
        if self.transcode_job is not None:
            for k in self.transcode_job:
                result['TranscodeJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.transcode_job = []
        if m.get('TranscodeJob') is not None:
            for k in m.get('TranscodeJob'):
                temp_model = SubmitTranscodeJobsResponseBodyTranscodeJobsTranscodeJob()
                self.transcode_job.append(temp_model.from_map(k))
        return self


class SubmitTranscodeJobsResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_jobs=None, transcode_task_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.transcode_jobs = transcode_jobs  # type: SubmitTranscodeJobsResponseBodyTranscodeJobs
        self.transcode_task_id = TeaConverter.to_unicode(transcode_task_id)  # type: unicode

    def validate(self):
        if self.transcode_jobs:
            self.transcode_jobs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transcode_jobs is not None:
            result['TranscodeJobs'] = self.transcode_jobs.to_map()
        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TranscodeJobs') is not None:
            temp_model = SubmitTranscodeJobsResponseBodyTranscodeJobs()
            self.transcode_jobs = temp_model.from_map(m['TranscodeJobs'])
        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')
        return self


class SubmitTranscodeJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitTranscodeJobsResponseBody

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
            temp_model = SubmitTranscodeJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitWorkflowJobRequest(TeaModel):
    def __init__(self, workflow_id=None, media_id=None, file_url=None):
        self.workflow_id = TeaConverter.to_unicode(workflow_id)  # type: unicode
        self.media_id = TeaConverter.to_unicode(media_id)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class SubmitWorkflowJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitWorkflowJobResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SubmitWorkflowJobResponseBody

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
            temp_model = SubmitWorkflowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagVodResourcesRequestTag(TeaModel):
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


class TagVodResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_type=None, resource_id=None, tag=None):
        self.owner_id = owner_id  # type: long
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.resource_id = resource_id  # type: list[unicode]
        self.tag = tag  # type: list[TagVodResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
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
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagVodResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagVodResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagVodResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: TagVodResourcesResponseBody

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
            temp_model = TagVodResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnTagVodResourcesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_type=None, all=None, resource_id=None, tag_key=None):
        self.owner_id = owner_id  # type: long
        self.resource_type = TeaConverter.to_unicode(resource_type)  # type: unicode
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[unicode]
        self.tag_key = tag_key  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
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
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UnTagVodResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnTagVodResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UnTagVodResourcesResponseBody

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
            temp_model = UnTagVodResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAITemplateRequest(TeaModel):
    def __init__(self, template_id=None, template_name=None, template_config=None):
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode
        self.template_name = TeaConverter.to_unicode(template_name)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        return self


class UpdateAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.template_id = TeaConverter.to_unicode(template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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


class UpdateAITemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateAITemplateResponseBody

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
            temp_model = UpdateAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppInfoRequest(TeaModel):
    def __init__(self, resource_real_owner_id=None, app_id=None, app_name=None, description=None, status=None):
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.app_name = TeaConverter.to_unicode(app_name)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAppInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateAppInfoResponseBody

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
            temp_model = UpdateAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAttachedMediaInfosRequest(TeaModel):
    def __init__(self, resource_real_owner_id=None, update_content=None):
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.update_content = TeaConverter.to_unicode(update_content)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.update_content is not None:
            result['UpdateContent'] = self.update_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('UpdateContent') is not None:
            self.update_content = m.get('UpdateContent')
        return self


class UpdateAttachedMediaInfosResponseBody(TeaModel):
    def __init__(self, non_exist_media_ids=None, request_id=None):
        self.non_exist_media_ids = non_exist_media_ids  # type: list[unicode]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAttachedMediaInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateAttachedMediaInfosResponseBody

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
            temp_model = UpdateAttachedMediaInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCategoryRequest(TeaModel):
    def __init__(self, cate_name=None, cate_id=None):
        self.cate_name = TeaConverter.to_unicode(cate_name)  # type: unicode
        self.cate_id = cate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        return self


class UpdateCategoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCategoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateCategoryResponseBody

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
            temp_model = UpdateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEditingProjectRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_id=None, resource_owner_account=None, owner_account=None,
                 project_id=None, title=None, timeline=None, description=None, cover_url=None, feextend=None, duration=None):
        self.owner_id = TeaConverter.to_unicode(owner_id)  # type: unicode
        self.resource_owner_id = TeaConverter.to_unicode(resource_owner_id)  # type: unicode
        self.resource_owner_account = TeaConverter.to_unicode(resource_owner_account)  # type: unicode
        self.owner_account = TeaConverter.to_unicode(owner_account)  # type: unicode
        self.project_id = TeaConverter.to_unicode(project_id)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.timeline = TeaConverter.to_unicode(timeline)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.feextend = TeaConverter.to_unicode(feextend)  # type: unicode
        self.duration = duration  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.title is not None:
            result['Title'] = self.title
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.description is not None:
            result['Description'] = self.description
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.feextend is not None:
            result['FEExtend'] = self.feextend
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('FEExtend') is not None:
            self.feextend = m.get('FEExtend')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class UpdateEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateEditingProjectResponseBody

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
            temp_model = UpdateEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageInfosRequest(TeaModel):
    def __init__(self, resource_real_owner_id=None, update_content=None):
        self.resource_real_owner_id = resource_real_owner_id  # type: long
        self.update_content = TeaConverter.to_unicode(update_content)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.update_content is not None:
            result['UpdateContent'] = self.update_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('UpdateContent') is not None:
            self.update_content = m.get('UpdateContent')
        return self


class UpdateImageInfosResponseBodyNonExistImageIds(TeaModel):
    def __init__(self, image_id=None):
        self.image_id = image_id  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class UpdateImageInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, non_exist_image_ids=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.non_exist_image_ids = non_exist_image_ids  # type: UpdateImageInfosResponseBodyNonExistImageIds

    def validate(self):
        if self.non_exist_image_ids:
            self.non_exist_image_ids.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.non_exist_image_ids is not None:
            result['NonExistImageIds'] = self.non_exist_image_ids.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NonExistImageIds') is not None:
            temp_model = UpdateImageInfosResponseBodyNonExistImageIds()
            self.non_exist_image_ids = temp_model.from_map(m['NonExistImageIds'])
        return self


class UpdateImageInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateImageInfosResponseBody

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
            temp_model = UpdateImageInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, name=None, transcode_template_list=None, locked=None, transcode_template_group_id=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.transcode_template_list = TeaConverter.to_unicode(transcode_template_list)  # type: unicode
        self.locked = TeaConverter.to_unicode(locked)  # type: unicode
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.transcode_template_list is not None:
            result['TranscodeTemplateList'] = self.transcode_template_list
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TranscodeTemplateList') is not None:
            self.transcode_template_list = m.get('TranscodeTemplateList')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        return self


class UpdateTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_template_group_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.transcode_template_group_id = TeaConverter.to_unicode(transcode_template_group_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        return self


class UpdateTranscodeTemplateGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateTranscodeTemplateGroupResponseBody

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
            temp_model = UpdateTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVideoInfoRequest(TeaModel):
    def __init__(self, video_id=None, title=None, tags=None, description=None, cover_url=None, cate_id=None,
                 download_switch=None, status=None, custom_media_info=None):
        self.video_id = TeaConverter.to_unicode(video_id)  # type: unicode
        self.title = TeaConverter.to_unicode(title)  # type: unicode
        self.tags = TeaConverter.to_unicode(tags)  # type: unicode
        self.description = TeaConverter.to_unicode(description)  # type: unicode
        self.cover_url = TeaConverter.to_unicode(cover_url)  # type: unicode
        self.cate_id = cate_id  # type: long
        self.download_switch = TeaConverter.to_unicode(download_switch)  # type: unicode
        self.status = TeaConverter.to_unicode(status)  # type: unicode
        self.custom_media_info = TeaConverter.to_unicode(custom_media_info)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.title is not None:
            result['Title'] = self.title
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.description is not None:
            result['Description'] = self.description
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.download_switch is not None:
            result['DownloadSwitch'] = self.download_switch
        if self.status is not None:
            result['Status'] = self.status
        if self.custom_media_info is not None:
            result['CustomMediaInfo'] = self.custom_media_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('DownloadSwitch') is not None:
            self.download_switch = m.get('DownloadSwitch')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CustomMediaInfo') is not None:
            self.custom_media_info = m.get('CustomMediaInfo')
        return self


class UpdateVideoInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVideoInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateVideoInfoResponseBody

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
            temp_model = UpdateVideoInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVideoInfosRequest(TeaModel):
    def __init__(self, update_content=None):
        self.update_content = TeaConverter.to_unicode(update_content)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_content is not None:
            result['UpdateContent'] = self.update_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateContent') is not None:
            self.update_content = m.get('UpdateContent')
        return self


class UpdateVideoInfosResponseBody(TeaModel):
    def __init__(self, request_id=None, forbidden_video_ids=None, non_exist_video_ids=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.forbidden_video_ids = forbidden_video_ids  # type: list[unicode]
        self.non_exist_video_ids = non_exist_video_ids  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.forbidden_video_ids is not None:
            result['ForbiddenVideoIds'] = self.forbidden_video_ids
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ForbiddenVideoIds') is not None:
            self.forbidden_video_ids = m.get('ForbiddenVideoIds')
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        return self


class UpdateVideoInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateVideoInfosResponseBody

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
            temp_model = UpdateVideoInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVodDomainRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None, domain_name=None, sources=None, top_level_domain=None):
        self.owner_id = owner_id  # type: long
        self.security_token = TeaConverter.to_unicode(security_token)  # type: unicode
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.sources = TeaConverter.to_unicode(sources)  # type: unicode
        self.top_level_domain = TeaConverter.to_unicode(top_level_domain)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class UpdateVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVodDomainResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateVodDomainResponseBody

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
            temp_model = UpdateVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVodTemplateRequest(TeaModel):
    def __init__(self, vod_template_id=None, name=None, template_config=None):
        self.vod_template_id = TeaConverter.to_unicode(vod_template_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.template_config = TeaConverter.to_unicode(template_config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        return self


class UpdateVodTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, vod_template_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.vod_template_id = TeaConverter.to_unicode(vod_template_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        return self


class UpdateVodTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateVodTemplateResponseBody

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
            temp_model = UpdateVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWatermarkRequest(TeaModel):
    def __init__(self, name=None, watermark_id=None, watermark_config=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.watermark_id = TeaConverter.to_unicode(watermark_id)  # type: unicode
        self.watermark_config = TeaConverter.to_unicode(watermark_config)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        return self


class UpdateWatermarkResponseBodyWatermarkInfo(TeaModel):
    def __init__(self, creation_time=None, type=None, is_default=None, file_url=None, watermark_config=None,
                 name=None, watermark_id=None):
        self.creation_time = TeaConverter.to_unicode(creation_time)  # type: unicode
        self.type = TeaConverter.to_unicode(type)  # type: unicode
        self.is_default = TeaConverter.to_unicode(is_default)  # type: unicode
        self.file_url = TeaConverter.to_unicode(file_url)  # type: unicode
        self.watermark_config = TeaConverter.to_unicode(watermark_config)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.watermark_id = TeaConverter.to_unicode(watermark_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.type is not None:
            result['Type'] = self.type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class UpdateWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, watermark_info=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.watermark_info = watermark_info  # type: UpdateWatermarkResponseBodyWatermarkInfo

    def validate(self):
        if self.watermark_info:
            self.watermark_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.watermark_info is not None:
            result['WatermarkInfo'] = self.watermark_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WatermarkInfo') is not None:
            temp_model = UpdateWatermarkResponseBodyWatermarkInfo()
            self.watermark_info = temp_model.from_map(m['WatermarkInfo'])
        return self


class UpdateWatermarkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UpdateWatermarkResponseBody

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
            temp_model = UpdateWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadMediaByURLRequest(TeaModel):
    def __init__(self, upload_urls=None, template_group_id=None, storage_location=None, upload_metadatas=None,
                 priority=None, message_callback=None, user_data=None, app_id=None, workflow_id=None):
        self.upload_urls = TeaConverter.to_unicode(upload_urls)  # type: unicode
        self.template_group_id = TeaConverter.to_unicode(template_group_id)  # type: unicode
        self.storage_location = TeaConverter.to_unicode(storage_location)  # type: unicode
        self.upload_metadatas = TeaConverter.to_unicode(upload_metadatas)  # type: unicode
        self.priority = TeaConverter.to_unicode(priority)  # type: unicode
        self.message_callback = TeaConverter.to_unicode(message_callback)  # type: unicode
        self.user_data = TeaConverter.to_unicode(user_data)  # type: unicode
        self.app_id = TeaConverter.to_unicode(app_id)  # type: unicode
        self.workflow_id = TeaConverter.to_unicode(workflow_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.upload_urls is not None:
            result['UploadURLs'] = self.upload_urls
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.upload_metadatas is not None:
            result['UploadMetadatas'] = self.upload_metadatas
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.message_callback is not None:
            result['MessageCallback'] = self.message_callback
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UploadURLs') is not None:
            self.upload_urls = m.get('UploadURLs')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('UploadMetadatas') is not None:
            self.upload_metadatas = m.get('UploadMetadatas')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('MessageCallback') is not None:
            self.message_callback = m.get('MessageCallback')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class UploadMediaByURLResponseBodyUploadJobs(TeaModel):
    def __init__(self, job_id=None, source_url=None):
        self.job_id = TeaConverter.to_unicode(job_id)  # type: unicode
        self.source_url = TeaConverter.to_unicode(source_url)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.source_url is not None:
            result['SourceURL'] = self.source_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SourceURL') is not None:
            self.source_url = m.get('SourceURL')
        return self


class UploadMediaByURLResponseBody(TeaModel):
    def __init__(self, request_id=None, upload_jobs=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.upload_jobs = upload_jobs  # type: list[UploadMediaByURLResponseBodyUploadJobs]

    def validate(self):
        if self.upload_jobs:
            for k in self.upload_jobs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UploadJobs'] = []
        if self.upload_jobs is not None:
            for k in self.upload_jobs:
                result['UploadJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.upload_jobs = []
        if m.get('UploadJobs') is not None:
            for k in m.get('UploadJobs'):
                temp_model = UploadMediaByURLResponseBodyUploadJobs()
                self.upload_jobs.append(temp_model.from_map(k))
        return self


class UploadMediaByURLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UploadMediaByURLResponseBody

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
            temp_model = UploadMediaByURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyVodDomainOwnerRequest(TeaModel):
    def __init__(self, owner_id=None, domain_name=None, verify_type=None):
        self.owner_id = owner_id  # type: long
        self.domain_name = TeaConverter.to_unicode(domain_name)  # type: unicode
        self.verify_type = TeaConverter.to_unicode(verify_type)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class VerifyVodDomainOwnerResponseBody(TeaModel):
    def __init__(self, request_id=None, content=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.content = TeaConverter.to_unicode(content)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class VerifyVodDomainOwnerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: VerifyVodDomainOwnerResponseBody

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
            temp_model = VerifyVodDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


