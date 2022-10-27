# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddAITemplateRequest(TeaModel):
    def __init__(self, template_config=None, template_name=None, template_type=None):
        self.template_config = template_config  # type: str
        self.template_name = template_name  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAITemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class AddAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAITemplateResponseBody, self).to_map()
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


class AddAITemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddAITemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAITemplateResponse, self).to_map()
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
            temp_model = AddAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCategoryRequest(TeaModel):
    def __init__(self, cate_name=None, parent_id=None, type=None):
        self.cate_name = cate_name  # type: str
        self.parent_id = parent_id  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCategoryRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, cate_id=None, cate_name=None, level=None, parent_id=None, type=None):
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.level = level  # type: long
        self.parent_id = parent_id  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddCategoryResponseBodyCategory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.level is not None:
            result['Level'] = self.level
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddCategoryResponseBody(TeaModel):
    def __init__(self, category=None, request_id=None):
        self.category = category  # type: AddCategoryResponseBodyCategory
        self.request_id = request_id  # type: str

    def validate(self):
        if self.category:
            self.category.validate()

    def to_map(self):
        _map = super(AddCategoryResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddCategoryResponse, self).to_map()
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
            temp_model = AddCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEditingProjectRequest(TeaModel):
    def __init__(self, cover_url=None, description=None, division=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, timeline=None, title=None):
        self.cover_url = cover_url  # type: str
        self.description = description  # type: str
        self.division = division  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.timeline = timeline  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.division is not None:
            result['Division'] = self.division
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Division') is not None:
            self.division = m.get('Division')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class AddEditingProjectResponseBodyProject(TeaModel):
    def __init__(self, creation_time=None, description=None, modified_time=None, project_id=None, status=None,
                 title=None):
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.project_id = project_id  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEditingProjectResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class AddEditingProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: AddEditingProjectResponseBodyProject
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(AddEditingProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddEditingProjectResponse, self).to_map()
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
            temp_model = AddEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, app_id=None, name=None, transcode_template_group_id=None, transcode_template_list=None):
        self.app_id = app_id  # type: str
        self.name = name  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str
        self.transcode_template_list = transcode_template_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTranscodeTemplateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.transcode_template_list is not None:
            result['TranscodeTemplateList'] = self.transcode_template_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('TranscodeTemplateList') is not None:
            self.transcode_template_list = m.get('TranscodeTemplateList')
        return self


class AddTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_template_group_id=None):
        self.request_id = request_id  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTranscodeTemplateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddTranscodeTemplateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddTranscodeTemplateGroupResponse, self).to_map()
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
            temp_model = AddTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVodDomainRequest(TeaModel):
    def __init__(self, check_url=None, domain_name=None, owner_account=None, owner_id=None, scope=None,
                 security_token=None, sources=None, top_level_domain=None):
        self.check_url = check_url  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.scope = scope  # type: str
        self.security_token = security_token  # type: str
        self.sources = sources  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVodDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class AddVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVodDomainResponseBody, self).to_map()
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


class AddVodDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddVodDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddVodDomainResponse, self).to_map()
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
            temp_model = AddVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVodTemplateRequest(TeaModel):
    def __init__(self, app_id=None, name=None, template_config=None, template_type=None):
        self.app_id = app_id  # type: str
        self.name = name  # type: str
        self.template_config = template_config  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVodTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class AddVodTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, vod_template_id=None):
        self.request_id = request_id  # type: str
        self.vod_template_id = vod_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVodTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddVodTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddVodTemplateResponse, self).to_map()
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
            temp_model = AddVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddWatermarkRequest(TeaModel):
    def __init__(self, app_id=None, file_url=None, name=None, type=None, watermark_config=None):
        self.app_id = app_id  # type: str
        self.file_url = file_url  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.watermark_config = watermark_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        return self


class AddWatermarkResponseBodyWatermarkInfo(TeaModel):
    def __init__(self, creation_time=None, file_url=None, is_default=None, name=None, type=None,
                 watermark_config=None, watermark_id=None):
        self.creation_time = creation_time  # type: str
        self.file_url = file_url  # type: str
        self.is_default = is_default  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.watermark_config = watermark_config  # type: str
        self.watermark_id = watermark_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWatermarkResponseBodyWatermarkInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class AddWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, watermark_info=None):
        self.request_id = request_id  # type: str
        self.watermark_info = watermark_info  # type: AddWatermarkResponseBodyWatermarkInfo

    def validate(self):
        if self.watermark_info:
            self.watermark_info.validate()

    def to_map(self):
        _map = super(AddWatermarkResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddWatermarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddWatermarkResponse, self).to_map()
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
            temp_model = AddWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachAppPolicyToIdentityRequest(TeaModel):
    def __init__(self, app_id=None, identity_name=None, identity_type=None, policy_names=None):
        self.app_id = app_id  # type: str
        self.identity_name = identity_name  # type: str
        self.identity_type = identity_type  # type: str
        self.policy_names = policy_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachAppPolicyToIdentityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        return self


class AttachAppPolicyToIdentityResponseBody(TeaModel):
    def __init__(self, failed_policy_names=None, non_exist_policy_names=None, request_id=None):
        self.failed_policy_names = failed_policy_names  # type: list[str]
        self.non_exist_policy_names = non_exist_policy_names  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachAppPolicyToIdentityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_policy_names is not None:
            result['FailedPolicyNames'] = self.failed_policy_names
        if self.non_exist_policy_names is not None:
            result['NonExistPolicyNames'] = self.non_exist_policy_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedPolicyNames') is not None:
            self.failed_policy_names = m.get('FailedPolicyNames')
        if m.get('NonExistPolicyNames') is not None:
            self.non_exist_policy_names = m.get('NonExistPolicyNames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachAppPolicyToIdentityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachAppPolicyToIdentityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachAppPolicyToIdentityResponse, self).to_map()
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
            temp_model = AttachAppPolicyToIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetVodDomainConfigsRequest(TeaModel):
    def __init__(self, domain_names=None, functions=None, owner_account=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.functions = functions  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetVodDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchSetVodDomainConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchSetVodDomainConfigsResponseBody, self).to_map()
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


class BatchSetVodDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchSetVodDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchSetVodDomainConfigsResponse, self).to_map()
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
            temp_model = BatchSetVodDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartVodDomainRequest(TeaModel):
    def __init__(self, domain_names=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartVodDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchStartVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartVodDomainResponseBody, self).to_map()
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


class BatchStartVodDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchStartVodDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStartVodDomainResponse, self).to_map()
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
            temp_model = BatchStartVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopVodDomainRequest(TeaModel):
    def __init__(self, domain_names=None, owner_id=None, security_token=None):
        self.domain_names = domain_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopVodDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchStopVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopVodDomainResponseBody, self).to_map()
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


class BatchStopVodDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchStopVodDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStopVodDomainResponse, self).to_map()
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
            temp_model = BatchStopVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelUrlUploadJobsRequest(TeaModel):
    def __init__(self, job_ids=None, upload_urls=None):
        self.job_ids = job_ids  # type: str
        self.upload_urls = upload_urls  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelUrlUploadJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        if self.upload_urls is not None:
            result['UploadUrls'] = self.upload_urls
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        if m.get('UploadUrls') is not None:
            self.upload_urls = m.get('UploadUrls')
        return self


class CancelUrlUploadJobsResponseBody(TeaModel):
    def __init__(self, canceled_jobs=None, non_exists=None, request_id=None):
        self.canceled_jobs = canceled_jobs  # type: list[str]
        self.non_exists = non_exists  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelUrlUploadJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.canceled_jobs is not None:
            result['CanceledJobs'] = self.canceled_jobs
        if self.non_exists is not None:
            result['NonExists'] = self.non_exists
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanceledJobs') is not None:
            self.canceled_jobs = m.get('CanceledJobs')
        if m.get('NonExists') is not None:
            self.non_exists = m.get('NonExists')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelUrlUploadJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelUrlUploadJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelUrlUploadJobsResponse, self).to_map()
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
            temp_model = CancelUrlUploadJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppInfoRequest(TeaModel):
    def __init__(self, app_name=None, description=None):
        self.app_name = app_name  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateAppInfoResponseBody(TeaModel):
    def __init__(self, app_id=None, request_id=None):
        self.app_id = app_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppInfoResponse, self).to_map()
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
            temp_model = CreateAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuditRequest(TeaModel):
    def __init__(self, audit_content=None):
        self.audit_content = audit_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuditRequest, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAuditResponseBody, self).to_map()
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


class CreateAuditResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAuditResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAuditResponse, self).to_map()
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
            temp_model = CreateAuditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadAttachedMediaRequest(TeaModel):
    def __init__(self, app_id=None, business_type=None, cate_ids=None, description=None, file_name=None,
                 file_size=None, media_ext=None, storage_location=None, tags=None, title=None, user_data=None):
        self.app_id = app_id  # type: str
        self.business_type = business_type  # type: str
        self.cate_ids = cate_ids  # type: str
        self.description = description  # type: str
        self.file_name = file_name  # type: str
        self.file_size = file_size  # type: str
        self.media_ext = media_ext  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUploadAttachedMediaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.media_ext is not None:
            result['MediaExt'] = self.media_ext
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('MediaExt') is not None:
            self.media_ext = m.get('MediaExt')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateUploadAttachedMediaResponseBody(TeaModel):
    def __init__(self, file_url=None, media_id=None, media_url=None, request_id=None, upload_address=None,
                 upload_auth=None):
        self.file_url = file_url  # type: str
        self.media_id = media_id  # type: str
        self.media_url = media_url  # type: str
        self.request_id = request_id  # type: str
        self.upload_address = upload_address  # type: str
        self.upload_auth = upload_auth  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUploadAttachedMediaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_url is not None:
            result['MediaURL'] = self.media_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address
        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')
        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')
        return self


class CreateUploadAttachedMediaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUploadAttachedMediaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUploadAttachedMediaResponse, self).to_map()
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
            temp_model = CreateUploadAttachedMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadImageRequest(TeaModel):
    def __init__(self, app_id=None, cate_id=None, description=None, image_ext=None, image_type=None,
                 original_file_name=None, storage_location=None, tags=None, title=None, user_data=None):
        self.app_id = app_id  # type: str
        self.cate_id = cate_id  # type: long
        self.description = description  # type: str
        self.image_ext = image_ext  # type: str
        self.image_type = image_type  # type: str
        self.original_file_name = original_file_name  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUploadImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.description is not None:
            result['Description'] = self.description
        if self.image_ext is not None:
            result['ImageExt'] = self.image_ext
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageExt') is not None:
            self.image_ext = m.get('ImageExt')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateUploadImageResponseBody(TeaModel):
    def __init__(self, file_url=None, image_id=None, image_url=None, request_id=None, upload_address=None,
                 upload_auth=None):
        self.file_url = file_url  # type: str
        self.image_id = image_id  # type: str
        self.image_url = image_url  # type: str
        self.request_id = request_id  # type: str
        self.upload_address = upload_address  # type: str
        self.upload_auth = upload_auth  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUploadImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address
        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')
        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')
        return self


class CreateUploadImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUploadImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUploadImageResponse, self).to_map()
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
            temp_model = CreateUploadImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadVideoRequest(TeaModel):
    def __init__(self, app_id=None, cate_id=None, cover_url=None, description=None, file_name=None, file_size=None,
                 storage_location=None, tags=None, template_group_id=None, title=None, user_data=None, workflow_id=None):
        self.app_id = app_id  # type: str
        self.cate_id = cate_id  # type: long
        self.cover_url = cover_url  # type: str
        self.description = description  # type: str
        self.file_name = file_name  # type: str
        self.file_size = file_size  # type: long
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.template_group_id = template_group_id  # type: str
        self.title = title  # type: str
        self.user_data = user_data  # type: str
        self.workflow_id = workflow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUploadVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class CreateUploadVideoResponseBody(TeaModel):
    def __init__(self, request_id=None, upload_address=None, upload_auth=None, video_id=None):
        self.request_id = request_id  # type: str
        self.upload_address = upload_address  # type: str
        self.upload_auth = upload_auth  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUploadVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address
        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')
        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class CreateUploadVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUploadVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUploadVideoResponse, self).to_map()
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
            temp_model = CreateUploadVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecryptKMSDataKeyRequest(TeaModel):
    def __init__(self, cipher_text=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.cipher_text = cipher_text  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecryptKMSDataKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cipher_text is not None:
            result['CipherText'] = self.cipher_text
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CipherText') is not None:
            self.cipher_text = m.get('CipherText')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DecryptKMSDataKeyResponseBody(TeaModel):
    def __init__(self, key_id=None, plaintext=None, request_id=None):
        self.key_id = key_id  # type: str
        self.plaintext = plaintext  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DecryptKMSDataKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DecryptKMSDataKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DecryptKMSDataKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DecryptKMSDataKeyResponse, self).to_map()
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
            temp_model = DecryptKMSDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAIImageInfosRequest(TeaModel):
    def __init__(self, aiimage_info_ids=None):
        self.aiimage_info_ids = aiimage_info_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAIImageInfosRequest, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAIImageInfosResponseBody, self).to_map()
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


class DeleteAIImageInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAIImageInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAIImageInfosResponse, self).to_map()
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
            temp_model = DeleteAIImageInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAITemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAITemplateRequest, self).to_map()
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


class DeleteAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAITemplateResponseBody, self).to_map()
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


class DeleteAITemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAITemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAITemplateResponse, self).to_map()
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
            temp_model = DeleteAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInfoRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppInfoResponseBody, self).to_map()
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


class DeleteAppInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppInfoResponse, self).to_map()
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
            temp_model = DeleteAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAttachedMediaRequest(TeaModel):
    def __init__(self, media_ids=None):
        self.media_ids = media_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAttachedMediaRequest, self).to_map()
        if _map is not None:
            return _map

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
        self.non_exist_media_ids = non_exist_media_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAttachedMediaResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAttachedMediaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAttachedMediaResponse, self).to_map()
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
            temp_model = DeleteAttachedMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCategoryRequest(TeaModel):
    def __init__(self, cate_id=None):
        self.cate_id = cate_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCategoryRequest, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCategoryResponseBody, self).to_map()
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


class DeleteCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCategoryResponse, self).to_map()
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
            temp_model = DeleteCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDynamicImageRequest(TeaModel):
    def __init__(self, dynamic_image_ids=None, video_id=None):
        self.dynamic_image_ids = dynamic_image_ids  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDynamicImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_image_ids is not None:
            result['DynamicImageIds'] = self.dynamic_image_ids
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicImageIds') is not None:
            self.dynamic_image_ids = m.get('DynamicImageIds')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class DeleteDynamicImageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDynamicImageResponseBody, self).to_map()
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


class DeleteDynamicImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDynamicImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDynamicImageResponse, self).to_map()
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
            temp_model = DeleteDynamicImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEditingProjectRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, project_ids=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.project_ids = project_ids  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEditingProjectResponseBody, self).to_map()
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


class DeleteEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEditingProjectResponse, self).to_map()
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
            temp_model = DeleteEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(self, delete_image_type=None, image_ids=None, image_type=None, image_urls=None, video_id=None):
        self.delete_image_type = delete_image_type  # type: str
        self.image_ids = image_ids  # type: str
        self.image_type = image_type  # type: str
        self.image_urls = image_urls  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_image_type is not None:
            result['DeleteImageType'] = self.delete_image_type
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_urls is not None:
            result['ImageURLs'] = self.image_urls
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteImageType') is not None:
            self.delete_image_type = m.get('DeleteImageType')
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageURLs') is not None:
            self.image_urls = m.get('ImageURLs')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteImageResponseBody, self).to_map()
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


class DeleteImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteImageResponse, self).to_map()
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
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMessageCallbackRequest(TeaModel):
    def __init__(self, app_id=None, owner_account=None):
        self.app_id = app_id  # type: str
        self.owner_account = owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMessageCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DeleteMessageCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMessageCallbackResponseBody, self).to_map()
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


class DeleteMessageCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMessageCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMessageCallbackResponse, self).to_map()
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
            temp_model = DeleteMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMezzaninesRequest(TeaModel):
    def __init__(self, force=None, video_ids=None):
        self.force = force  # type: bool
        self.video_ids = video_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMezzaninesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')
        return self


class DeleteMezzaninesResponseBody(TeaModel):
    def __init__(self, non_exist_video_ids=None, request_id=None, un_removeable_video_ids=None):
        self.non_exist_video_ids = non_exist_video_ids  # type: list[str]
        self.request_id = request_id  # type: str
        self.un_removeable_video_ids = un_removeable_video_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMezzaninesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.un_removeable_video_ids is not None:
            result['UnRemoveableVideoIds'] = self.un_removeable_video_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UnRemoveableVideoIds') is not None:
            self.un_removeable_video_ids = m.get('UnRemoveableVideoIds')
        return self


class DeleteMezzaninesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMezzaninesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMezzaninesResponse, self).to_map()
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
            temp_model = DeleteMezzaninesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMultipartUploadRequest(TeaModel):
    def __init__(self, media_id=None, media_type=None, owner_account=None):
        self.media_id = media_id  # type: str
        self.media_type = media_type  # type: str
        self.owner_account = owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMultipartUploadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class DeleteMultipartUploadResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMultipartUploadResponseBody, self).to_map()
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


class DeleteMultipartUploadResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMultipartUploadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMultipartUploadResponse, self).to_map()
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
            temp_model = DeleteMultipartUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStreamRequest(TeaModel):
    def __init__(self, job_ids=None, video_id=None):
        self.job_ids = job_ids  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStreamRequest, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStreamResponseBody, self).to_map()
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


class DeleteStreamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteStreamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteStreamResponse, self).to_map()
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
            temp_model = DeleteStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, force_del_group=None, transcode_template_group_id=None, transcode_template_ids=None):
        self.force_del_group = force_del_group  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str
        self.transcode_template_ids = transcode_template_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTranscodeTemplateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_del_group is not None:
            result['ForceDelGroup'] = self.force_del_group
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.transcode_template_ids is not None:
            result['TranscodeTemplateIds'] = self.transcode_template_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForceDelGroup') is not None:
            self.force_del_group = m.get('ForceDelGroup')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('TranscodeTemplateIds') is not None:
            self.transcode_template_ids = m.get('TranscodeTemplateIds')
        return self


class DeleteTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, non_exist_transcode_template_ids=None, request_id=None):
        self.non_exist_transcode_template_ids = non_exist_transcode_template_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTranscodeTemplateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTranscodeTemplateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTranscodeTemplateGroupResponse, self).to_map()
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
            temp_model = DeleteTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVideoRequest(TeaModel):
    def __init__(self, video_ids=None):
        self.video_ids = video_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVideoRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, forbidden_video_ids=None, non_exist_video_ids=None, request_id=None):
        self.forbidden_video_ids = forbidden_video_ids  # type: list[str]
        self.non_exist_video_ids = non_exist_video_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forbidden_video_ids is not None:
            result['ForbiddenVideoIds'] = self.forbidden_video_ids
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForbiddenVideoIds') is not None:
            self.forbidden_video_ids = m.get('ForbiddenVideoIds')
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVideoResponse, self).to_map()
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
            temp_model = DeleteVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVodDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_account=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVodDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVodDomainResponseBody, self).to_map()
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


class DeleteVodDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVodDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVodDomainResponse, self).to_map()
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
            temp_model = DeleteVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVodSpecificConfigRequest(TeaModel):
    def __init__(self, config_id=None, domain_name=None, owner_id=None, security_token=None):
        self.config_id = config_id  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVodSpecificConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteVodSpecificConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVodSpecificConfigResponseBody, self).to_map()
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


class DeleteVodSpecificConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVodSpecificConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVodSpecificConfigResponse, self).to_map()
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
            temp_model = DeleteVodSpecificConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVodTemplateRequest(TeaModel):
    def __init__(self, vod_template_id=None):
        self.vod_template_id = vod_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVodTemplateRequest, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str
        self.vod_template_id = vod_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVodTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVodTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVodTemplateResponse, self).to_map()
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
            temp_model = DeleteVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWatermarkRequest(TeaModel):
    def __init__(self, watermark_id=None):
        self.watermark_id = watermark_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteWatermarkResponseBody, self).to_map()
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


class DeleteWatermarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteWatermarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteWatermarkResponse, self).to_map()
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
            temp_model = DeleteWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlayTopVideosRequest(TeaModel):
    def __init__(self, biz_date=None, owner_id=None, page_no=None, page_size=None):
        self.biz_date = biz_date  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlayTopVideosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribePlayTopVideosResponseBodyTopPlayVideosTopPlayVideoStatis(TeaModel):
    def __init__(self, play_duration=None, title=None, uv=None, vv=None, video_id=None):
        self.play_duration = play_duration  # type: str
        self.title = title  # type: str
        self.uv = uv  # type: str
        self.vv = vv  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlayTopVideosResponseBodyTopPlayVideosTopPlayVideoStatis, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['UV'] = self.uv
        if self.vv is not None:
            result['VV'] = self.vv
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UV') is not None:
            self.uv = m.get('UV')
        if m.get('VV') is not None:
            self.vv = m.get('VV')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
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
        _map = super(DescribePlayTopVideosResponseBodyTopPlayVideos, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, page_no=None, page_size=None, request_id=None, top_play_videos=None, total_num=None):
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.top_play_videos = top_play_videos  # type: DescribePlayTopVideosResponseBodyTopPlayVideos
        self.total_num = total_num  # type: long

    def validate(self):
        if self.top_play_videos:
            self.top_play_videos.validate()

    def to_map(self):
        _map = super(DescribePlayTopVideosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.top_play_videos is not None:
            result['TopPlayVideos'] = self.top_play_videos.to_map()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TopPlayVideos') is not None:
            temp_model = DescribePlayTopVideosResponseBodyTopPlayVideos()
            self.top_play_videos = temp_model.from_map(m['TopPlayVideos'])
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class DescribePlayTopVideosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlayTopVideosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlayTopVideosResponse, self).to_map()
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
            temp_model = DescribePlayTopVideosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlayUserAvgRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlayUserAvgRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePlayUserAvgResponseBodyUserPlayStatisAvgsUserPlayStatisAvg(TeaModel):
    def __init__(self, avg_play_count=None, avg_play_duration=None, date=None):
        self.avg_play_count = avg_play_count  # type: str
        self.avg_play_duration = avg_play_duration  # type: str
        self.date = date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlayUserAvgResponseBodyUserPlayStatisAvgsUserPlayStatisAvg, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_play_count is not None:
            result['AvgPlayCount'] = self.avg_play_count
        if self.avg_play_duration is not None:
            result['AvgPlayDuration'] = self.avg_play_duration
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgPlayCount') is not None:
            self.avg_play_count = m.get('AvgPlayCount')
        if m.get('AvgPlayDuration') is not None:
            self.avg_play_duration = m.get('AvgPlayDuration')
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
        _map = super(DescribePlayUserAvgResponseBodyUserPlayStatisAvgs, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str
        self.user_play_statis_avgs = user_play_statis_avgs  # type: DescribePlayUserAvgResponseBodyUserPlayStatisAvgs

    def validate(self):
        if self.user_play_statis_avgs:
            self.user_play_statis_avgs.validate()

    def to_map(self):
        _map = super(DescribePlayUserAvgResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlayUserAvgResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlayUserAvgResponse, self).to_map()
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
            temp_model = DescribePlayUserAvgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlayUserTotalRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlayUserTotalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV(TeaModel):
    def __init__(self, android=None, flash=None, html5=None, i_os=None):
        self.android = android  # type: str
        self.flash = flash  # type: str
        self.html5 = html5  # type: str
        self.i_os = i_os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android is not None:
            result['Android'] = self.android
        if self.flash is not None:
            result['Flash'] = self.flash
        if self.html5 is not None:
            result['HTML5'] = self.html5
        if self.i_os is not None:
            result['iOS'] = self.i_os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Android') is not None:
            self.android = m.get('Android')
        if m.get('Flash') is not None:
            self.flash = m.get('Flash')
        if m.get('HTML5') is not None:
            self.html5 = m.get('HTML5')
        if m.get('iOS') is not None:
            self.i_os = m.get('iOS')
        return self


class DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV(TeaModel):
    def __init__(self, android=None, flash=None, html5=None, i_os=None):
        self.android = android  # type: str
        self.flash = flash  # type: str
        self.html5 = html5  # type: str
        self.i_os = i_os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android is not None:
            result['Android'] = self.android
        if self.flash is not None:
            result['Flash'] = self.flash
        if self.html5 is not None:
            result['HTML5'] = self.html5
        if self.i_os is not None:
            result['iOS'] = self.i_os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Android') is not None:
            self.android = m.get('Android')
        if m.get('Flash') is not None:
            self.flash = m.get('Flash')
        if m.get('HTML5') is not None:
            self.html5 = m.get('HTML5')
        if m.get('iOS') is not None:
            self.i_os = m.get('iOS')
        return self


class DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotal(TeaModel):
    def __init__(self, date=None, play_duration=None, play_range=None, uv=None, vv=None):
        self.date = date  # type: str
        self.play_duration = play_duration  # type: str
        self.play_range = play_range  # type: str
        self.uv = uv  # type: DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV
        self.vv = vv  # type: DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV

    def validate(self):
        if self.uv:
            self.uv.validate()
        if self.vv:
            self.vv.validate()

    def to_map(self):
        _map = super(DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotal, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration
        if self.play_range is not None:
            result['PlayRange'] = self.play_range
        if self.uv is not None:
            result['UV'] = self.uv.to_map()
        if self.vv is not None:
            result['VV'] = self.vv.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')
        if m.get('PlayRange') is not None:
            self.play_range = m.get('PlayRange')
        if m.get('UV') is not None:
            temp_model = DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalUV()
            self.uv = temp_model.from_map(m['UV'])
        if m.get('VV') is not None:
            temp_model = DescribePlayUserTotalResponseBodyUserPlayStatisTotalsUserPlayStatisTotalVV()
            self.vv = temp_model.from_map(m['VV'])
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
        _map = super(DescribePlayUserTotalResponseBodyUserPlayStatisTotals, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str
        self.user_play_statis_totals = user_play_statis_totals  # type: DescribePlayUserTotalResponseBodyUserPlayStatisTotals

    def validate(self):
        if self.user_play_statis_totals:
            self.user_play_statis_totals.validate()

    def to_map(self):
        _map = super(DescribePlayUserTotalResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlayUserTotalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlayUserTotalResponse, self).to_map()
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
            temp_model = DescribePlayUserTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlayVideoStatisRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, start_time=None, video_id=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlayVideoStatisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class DescribePlayVideoStatisResponseBodyVideoPlayStatisDetailsVideoPlayStatisDetail(TeaModel):
    def __init__(self, date=None, play_duration=None, play_range=None, title=None, uv=None, vv=None):
        self.date = date  # type: str
        self.play_duration = play_duration  # type: str
        self.play_range = play_range  # type: str
        self.title = title  # type: str
        self.uv = uv  # type: str
        self.vv = vv  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePlayVideoStatisResponseBodyVideoPlayStatisDetailsVideoPlayStatisDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.play_duration is not None:
            result['PlayDuration'] = self.play_duration
        if self.play_range is not None:
            result['PlayRange'] = self.play_range
        if self.title is not None:
            result['Title'] = self.title
        if self.uv is not None:
            result['UV'] = self.uv
        if self.vv is not None:
            result['VV'] = self.vv
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PlayDuration') is not None:
            self.play_duration = m.get('PlayDuration')
        if m.get('PlayRange') is not None:
            self.play_range = m.get('PlayRange')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UV') is not None:
            self.uv = m.get('UV')
        if m.get('VV') is not None:
            self.vv = m.get('VV')
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
        _map = super(DescribePlayVideoStatisResponseBodyVideoPlayStatisDetails, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, request_id=None, video_play_statis_details=None):
        self.request_id = request_id  # type: str
        self.video_play_statis_details = video_play_statis_details  # type: DescribePlayVideoStatisResponseBodyVideoPlayStatisDetails

    def validate(self):
        if self.video_play_statis_details:
            self.video_play_statis_details.validate()

    def to_map(self):
        _map = super(DescribePlayVideoStatisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.video_play_statis_details is not None:
            result['VideoPlayStatisDetails'] = self.video_play_statis_details.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VideoPlayStatisDetails') is not None:
            temp_model = DescribePlayVideoStatisResponseBodyVideoPlayStatisDetails()
            self.video_play_statis_details = temp_model.from_map(m['VideoPlayStatisDetails'])
        return self


class DescribePlayVideoStatisResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePlayVideoStatisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePlayVideoStatisResponse, self).to_map()
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
            temp_model = DescribePlayVideoStatisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodAIDataRequest(TeaModel):
    def __init__(self, aitype=None, end_time=None, owner_id=None, region=None, start_time=None):
        self.aitype = aitype  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodAIDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aitype is not None:
            result['AIType'] = self.aitype
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIType') is not None:
            self.aitype = m.get('AIType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVodAIDataResponseBodyAIDataAIDataItemDataDataItem(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodAIDataResponseBodyAIDataAIDataItemDataDataItem, self).to_map()
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


class DescribeVodAIDataResponseBodyAIDataAIDataItemData(TeaModel):
    def __init__(self, data_item=None):
        self.data_item = data_item  # type: list[DescribeVodAIDataResponseBodyAIDataAIDataItemDataDataItem]

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVodAIDataResponseBodyAIDataAIDataItemData, self).to_map()
        if _map is not None:
            return _map

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
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeVodAIDataResponseBodyAIDataAIDataItem, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeVodAIDataResponseBodyAIData, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, aidata=None, data_interval=None, request_id=None):
        self.aidata = aidata  # type: DescribeVodAIDataResponseBodyAIData
        self.data_interval = data_interval  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.aidata:
            self.aidata.validate()

    def to_map(self):
        _map = super(DescribeVodAIDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aidata is not None:
            result['AIData'] = self.aidata.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIData') is not None:
            temp_model = DescribeVodAIDataResponseBodyAIData()
            self.aidata = temp_model.from_map(m['AIData'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVodAIDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodAIDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodAIDataResponse, self).to_map()
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
            temp_model = DescribeVodAIDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodCertificateListRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodCertificateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeVodCertificateListResponseBodyCertificateListModelCertListCert(TeaModel):
    def __init__(self, cert_id=None, cert_name=None, common=None, fingerprint=None, issuer=None, last_time=None):
        self.cert_id = cert_id  # type: long
        self.cert_name = cert_name  # type: str
        self.common = common  # type: str
        self.fingerprint = fingerprint  # type: str
        self.issuer = issuer  # type: str
        self.last_time = last_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodCertificateListResponseBodyCertificateListModelCertListCert, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common is not None:
            result['Common'] = self.common
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
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
        _map = super(DescribeVodCertificateListResponseBodyCertificateListModelCertList, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeVodCertificateListResponseBodyCertificateListModel, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, certificate_list_model=None, request_id=None):
        self.certificate_list_model = certificate_list_model  # type: DescribeVodCertificateListResponseBodyCertificateListModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super(DescribeVodCertificateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeVodCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVodCertificateListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodCertificateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodCertificateListResponse, self).to_map()
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
            temp_model = DescribeVodCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainBpsDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVodDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, domestic_value=None, https_domestic_value=None, https_overseas_value=None, https_value=None,
                 overseas_value=None, time_stamp=None, value=None):
        self.domestic_value = domestic_value  # type: str
        self.https_domestic_value = https_domestic_value  # type: str
        self.https_overseas_value = https_overseas_value  # type: str
        self.https_value = https_value  # type: str
        self.overseas_value = overseas_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainBpsDataResponseBodyBpsDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
        _map = super(DescribeVodDomainBpsDataResponseBodyBpsDataPerInterval, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, bps_data_per_interval=None, data_interval=None, domain_name=None, end_time=None,
                 isp_name_en=None, location_name_en=None, request_id=None, start_time=None):
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeVodDomainBpsDataResponseBodyBpsDataPerInterval
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVodDomainBpsDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeVodDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVodDomainBpsDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodDomainBpsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodDomainBpsDataResponse, self).to_map()
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
            temp_model = DescribeVodDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainCertificateInfoRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainCertificateInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVodDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(self, cert_domain_name=None, cert_expire_time=None, cert_life=None, cert_name=None, cert_org=None,
                 cert_type=None, domain_name=None, server_certificate_status=None, status=None):
        self.cert_domain_name = cert_domain_name  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_life = cert_life  # type: str
        self.cert_name = cert_name  # type: str
        self.cert_org = cert_org  # type: str
        self.cert_type = cert_type  # type: str
        self.domain_name = domain_name  # type: str
        self.server_certificate_status = server_certificate_status  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainCertificateInfoResponseBodyCertInfosCertInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
        _map = super(DescribeVodDomainCertificateInfoResponseBodyCertInfos, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super(DescribeVodDomainCertificateInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodDomainCertificateInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodDomainCertificateInfoResponse, self).to_map()
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
            temp_model = DescribeVodDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainConfigsRequest(TeaModel):
    def __init__(self, domain_name=None, function_names=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name  # type: str
        self.arg_value = arg_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgsFunctionArg, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, config_id=None, function_args=None, function_name=None, status=None):
        self.config_id = config_id  # type: str
        self.function_args = function_args  # type: DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs
        self.function_name = function_name  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        _map = super(DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('FunctionArgs') is not None:
            temp_model = DescribeVodDomainConfigsResponseBodyDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(m['FunctionArgs'])
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
        _map = super(DescribeVodDomainConfigsResponseBodyDomainConfigs, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, domain_configs=None, request_id=None):
        self.domain_configs = domain_configs  # type: DescribeVodDomainConfigsResponseBodyDomainConfigs
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        _map = super(DescribeVodDomainConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainConfigs') is not None:
            temp_model = DescribeVodDomainConfigsResponseBodyDomainConfigs()
            self.domain_configs = temp_model.from_map(m['DomainConfigs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVodDomainConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodDomainConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodDomainConfigsResponse, self).to_map()
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
            temp_model = DescribeVodDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainDetailRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeVodDomainDetailResponseBodyDomainDetailSourcesSource(TeaModel):
    def __init__(self, content=None, enabled=None, port=None, priority=None, type=None):
        self.content = content  # type: str
        self.enabled = enabled  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainDetailResponseBodyDomainDetailSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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
        _map = super(DescribeVodDomainDetailResponseBodyDomainDetailSources, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, cert_name=None, cname=None, description=None, domain_name=None, domain_status=None,
                 gmt_created=None, gmt_modified=None, sslprotocol=None, sslpub=None, scope=None, sources=None, weight=None):
        self.cert_name = cert_name  # type: str
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str
        self.scope = scope  # type: str
        self.sources = sources  # type: DescribeVodDomainDetailResponseBodyDomainDetailSources
        self.weight = weight  # type: str

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeVodDomainDetailResponseBodyDomainDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Sources') is not None:
            temp_model = DescribeVodDomainDetailResponseBodyDomainDetailSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeVodDomainDetailResponseBody(TeaModel):
    def __init__(self, domain_detail=None, request_id=None):
        self.domain_detail = domain_detail  # type: DescribeVodDomainDetailResponseBodyDomainDetail
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        _map = super(DescribeVodDomainDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodDomainDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodDomainDetailResponse, self).to_map()
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
            temp_model = DescribeVodDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainLogRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, owner_id=None, page_number=None, page_size=None,
                 start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail(TeaModel):
    def __init__(self, end_time=None, log_name=None, log_path=None, log_size=None, start_time=None):
        self.end_time = end_time  # type: str
        self.log_name = log_name  # type: str
        self.log_path = log_path  # type: str
        self.log_size = log_size  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfosLogInfoDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.log_name is not None:
            result['LogName'] = self.log_name
        if self.log_path is not None:
            result['LogPath'] = self.log_path
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LogName') is not None:
            self.log_name = m.get('LogName')
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
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
        _map = super(DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos, self).to_map()
        if _map is not None:
            return _map

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


class DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos(TeaModel):
    def __init__(self, page_number=None, page_size=None, total=None):
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos, self).to_map()
        if _map is not None:
            return _map

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


class DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetail(TeaModel):
    def __init__(self, domain_name=None, log_count=None, log_infos=None, page_infos=None):
        self.domain_name = domain_name  # type: str
        self.log_count = log_count  # type: long
        self.log_infos = log_infos  # type: DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos
        self.page_infos = page_infos  # type: DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos

    def validate(self):
        if self.log_infos:
            self.log_infos.validate()
        if self.page_infos:
            self.page_infos.validate()

    def to_map(self):
        _map = super(DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.log_count is not None:
            result['LogCount'] = self.log_count
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        if self.page_infos is not None:
            result['PageInfos'] = self.page_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')
        if m.get('LogInfos') is not None:
            temp_model = DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        if m.get('PageInfos') is not None:
            temp_model = DescribeVodDomainLogResponseBodyDomainLogDetailsDomainLogDetailPageInfos()
            self.page_infos = temp_model.from_map(m['PageInfos'])
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
        _map = super(DescribeVodDomainLogResponseBodyDomainLogDetails, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, domain_log_details=None, request_id=None):
        self.domain_log_details = domain_log_details  # type: DescribeVodDomainLogResponseBodyDomainLogDetails
        self.request_id = request_id  # type: str

    def validate(self):
        if self.domain_log_details:
            self.domain_log_details.validate()

    def to_map(self):
        _map = super(DescribeVodDomainLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_log_details is not None:
            result['DomainLogDetails'] = self.domain_log_details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainLogDetails') is not None:
            temp_model = DescribeVodDomainLogResponseBodyDomainLogDetails()
            self.domain_log_details = temp_model.from_map(m['DomainLogDetails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVodDomainLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodDomainLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodDomainLogResponse, self).to_map()
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
            temp_model = DescribeVodDomainLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, interval=None, isp_name_en=None, location_name_en=None,
                 owner_id=None, start_time=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainTrafficDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVodDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, domestic_value=None, https_domestic_value=None, https_overseas_value=None, https_value=None,
                 overseas_value=None, time_stamp=None, value=None):
        self.domestic_value = domestic_value  # type: str
        self.https_domestic_value = https_domestic_value  # type: str
        self.https_overseas_value = https_overseas_value  # type: str
        self.https_value = https_value  # type: str
        self.overseas_value = overseas_value  # type: str
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value
        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value
        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value
        if self.https_value is not None:
            result['HttpsValue'] = self.https_value
        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')
        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')
        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')
        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')
        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
        _map = super(DescribeVodDomainTrafficDataResponseBodyTrafficDataPerInterval, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, data_interval=None, domain_name=None, end_time=None, request_id=None, start_time=None,
                 total_traffic=None, traffic_data_per_interval=None):
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.total_traffic = total_traffic  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeVodDomainTrafficDataResponseBodyTrafficDataPerInterval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVodDomainTrafficDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeVodDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeVodDomainTrafficDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodDomainTrafficDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodDomainTrafficDataResponse, self).to_map()
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
            temp_model = DescribeVodDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodDomainUsageDataRequest(TeaModel):
    def __init__(self, area=None, domain_name=None, end_time=None, field=None, owner_id=None, start_time=None,
                 type=None):
        self.area = area  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.field = field  # type: str
        self.owner_id = owner_id  # type: long
        self.start_time = start_time  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainUsageDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.field is not None:
            result['Field'] = self.field
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeVodDomainUsageDataResponseBodyUsageDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodDomainUsageDataResponseBodyUsageDataPerIntervalDataModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
        _map = super(DescribeVodDomainUsageDataResponseBodyUsageDataPerInterval, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, area=None, data_interval=None, domain_name=None, end_time=None, request_id=None,
                 start_time=None, type=None, usage_data_per_interval=None):
        self.area = area  # type: str
        self.data_interval = data_interval  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.type = type  # type: str
        self.usage_data_per_interval = usage_data_per_interval  # type: DescribeVodDomainUsageDataResponseBodyUsageDataPerInterval

    def validate(self):
        if self.usage_data_per_interval:
            self.usage_data_per_interval.validate()

    def to_map(self):
        _map = super(DescribeVodDomainUsageDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.usage_data_per_interval is not None:
            result['UsageDataPerInterval'] = self.usage_data_per_interval.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UsageDataPerInterval') is not None:
            temp_model = DescribeVodDomainUsageDataResponseBodyUsageDataPerInterval()
            self.usage_data_per_interval = temp_model.from_map(m['UsageDataPerInterval'])
        return self


class DescribeVodDomainUsageDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodDomainUsageDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodDomainUsageDataResponse, self).to_map()
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
            temp_model = DescribeVodDomainUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodRefreshQuotaRequest(TeaModel):
    def __init__(self, owner_id=None, security_token=None):
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodRefreshQuotaRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, block_quota=None, dir_quota=None, dir_remain=None, preload_quota=None, preload_remain=None,
                 request_id=None, url_quota=None, url_remain=None, block_remain=None):
        self.block_quota = block_quota  # type: str
        self.dir_quota = dir_quota  # type: str
        self.dir_remain = dir_remain  # type: str
        self.preload_quota = preload_quota  # type: str
        self.preload_remain = preload_remain  # type: str
        self.request_id = request_id  # type: str
        self.url_quota = url_quota  # type: str
        self.url_remain = url_remain  # type: str
        self.block_remain = block_remain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodRefreshQuotaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota
        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota
        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain
        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota
        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota
        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain
        if self.block_remain is not None:
            result['blockRemain'] = self.block_remain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')
        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')
        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')
        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')
        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')
        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')
        if m.get('blockRemain') is not None:
            self.block_remain = m.get('blockRemain')
        return self


class DescribeVodRefreshQuotaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodRefreshQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodRefreshQuotaResponse, self).to_map()
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
            temp_model = DescribeVodRefreshQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodRefreshTasksRequest(TeaModel):
    def __init__(self, domain_name=None, end_time=None, object_path=None, object_type=None, owner_id=None,
                 page_number=None, page_size=None, security_token=None, start_time=None, status=None, task_id=None):
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodRefreshTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeVodRefreshTasksResponseBodyTasksTask(TeaModel):
    def __init__(self, creation_time=None, description=None, object_path=None, object_type=None, process=None,
                 status=None, task_id=None):
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str
        self.process = process  # type: str
        self.status = status  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodRefreshTasksResponseBodyTasksTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
        _map = super(DescribeVodRefreshTasksResponseBodyTasks, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, page_number=None, page_size=None, request_id=None, tasks=None, total_count=None):
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: DescribeVodRefreshTasksResponseBodyTasks
        self.total_count = total_count  # type: long

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super(DescribeVodRefreshTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tasks') is not None:
            temp_model = DescribeVodRefreshTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeVodRefreshTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodRefreshTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodRefreshTasksResponse, self).to_map()
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
            temp_model = DescribeVodRefreshTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodStorageDataRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, region=None, start_time=None, storage=None, storage_type=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.start_time = start_time  # type: str
        self.storage = storage  # type: str
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodStorageDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeVodStorageDataResponseBodyStorageDataStorageDataItem(TeaModel):
    def __init__(self, network_out=None, storage_utilization=None, time_stamp=None):
        self.network_out = network_out  # type: str
        self.storage_utilization = storage_utilization  # type: str
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodStorageDataResponseBodyStorageDataStorageDataItem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_out is not None:
            result['NetworkOut'] = self.network_out
        if self.storage_utilization is not None:
            result['StorageUtilization'] = self.storage_utilization
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NetworkOut') is not None:
            self.network_out = m.get('NetworkOut')
        if m.get('StorageUtilization') is not None:
            self.storage_utilization = m.get('StorageUtilization')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
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
        _map = super(DescribeVodStorageDataResponseBodyStorageData, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, data_interval=None, request_id=None, storage_data=None):
        self.data_interval = data_interval  # type: str
        self.request_id = request_id  # type: str
        self.storage_data = storage_data  # type: DescribeVodStorageDataResponseBodyStorageData

    def validate(self):
        if self.storage_data:
            self.storage_data.validate()

    def to_map(self):
        _map = super(DescribeVodStorageDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_data is not None:
            result['StorageData'] = self.storage_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageData') is not None:
            temp_model = DescribeVodStorageDataResponseBodyStorageData()
            self.storage_data = temp_model.from_map(m['StorageData'])
        return self


class DescribeVodStorageDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodStorageDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodStorageDataResponse, self).to_map()
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
            temp_model = DescribeVodStorageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodTranscodeDataRequest(TeaModel):
    def __init__(self, end_time=None, interval=None, owner_id=None, region=None, specification=None, start_time=None,
                 storage=None):
        self.end_time = end_time  # type: str
        self.interval = interval  # type: str
        self.owner_id = owner_id  # type: long
        self.region = region  # type: str
        self.specification = specification  # type: str
        self.start_time = start_time  # type: str
        self.storage = storage  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodTranscodeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage is not None:
            result['Storage'] = self.storage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        return self


class DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemDataDataItem(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemDataDataItem, self).to_map()
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


class DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemData(TeaModel):
    def __init__(self, data_item=None):
        self.data_item = data_item  # type: list[DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemDataDataItem]

    def validate(self):
        if self.data_item:
            for k in self.data_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItemData, self).to_map()
        if _map is not None:
            return _map

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
        self.time_stamp = time_stamp  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeVodTranscodeDataResponseBodyTranscodeDataTranscodeDataItem, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(DescribeVodTranscodeDataResponseBodyTranscodeData, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, data_interval=None, request_id=None, transcode_data=None):
        self.data_interval = data_interval  # type: str
        self.request_id = request_id  # type: str
        self.transcode_data = transcode_data  # type: DescribeVodTranscodeDataResponseBodyTranscodeData

    def validate(self):
        if self.transcode_data:
            self.transcode_data.validate()

    def to_map(self):
        _map = super(DescribeVodTranscodeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transcode_data is not None:
            result['TranscodeData'] = self.transcode_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TranscodeData') is not None:
            temp_model = DescribeVodTranscodeDataResponseBodyTranscodeData()
            self.transcode_data = temp_model.from_map(m['TranscodeData'])
        return self


class DescribeVodTranscodeDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodTranscodeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodTranscodeDataResponse, self).to_map()
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
            temp_model = DescribeVodTranscodeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodUserDomainsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodUserDomainsRequestTag, self).to_map()
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


class DescribeVodUserDomainsRequest(TeaModel):
    def __init__(self, domain_name=None, domain_search_type=None, domain_status=None, owner_id=None,
                 page_number=None, page_size=None, security_token=None, tag=None):
        self.domain_name = domain_name  # type: str
        self.domain_search_type = domain_search_type  # type: str
        self.domain_status = domain_status  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.security_token = security_token  # type: str
        self.tag = tag  # type: list[DescribeVodUserDomainsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVodUserDomainsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_search_type is not None:
            result['DomainSearchType'] = self.domain_search_type
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainSearchType') is not None:
            self.domain_search_type = m.get('DomainSearchType')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeVodUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeVodUserDomainsResponseBodyDomainsPageDataSourcesSource(TeaModel):
    def __init__(self, content=None, port=None, priority=None, type=None):
        self.content = content  # type: str
        self.port = port  # type: int
        self.priority = priority  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodUserDomainsResponseBodyDomainsPageDataSourcesSource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.port is not None:
            result['Port'] = self.port
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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
        _map = super(DescribeVodUserDomainsResponseBodyDomainsPageDataSources, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, cname=None, description=None, domain_name=None, domain_status=None, gmt_created=None,
                 gmt_modified=None, sandbox=None, sources=None, ssl_protocol=None):
        self.cname = cname  # type: str
        self.description = description  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_status = domain_status  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.sandbox = sandbox  # type: str
        self.sources = sources  # type: DescribeVodUserDomainsResponseBodyDomainsPageDataSources
        self.ssl_protocol = ssl_protocol  # type: str

    def validate(self):
        if self.sources:
            self.sources.validate()

    def to_map(self):
        _map = super(DescribeVodUserDomainsResponseBodyDomainsPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.sources is not None:
            result['Sources'] = self.sources.to_map()
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('Sources') is not None:
            temp_model = DescribeVodUserDomainsResponseBodyDomainsPageDataSources()
            self.sources = temp_model.from_map(m['Sources'])
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
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
        _map = super(DescribeVodUserDomainsResponseBodyDomains, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, domains=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.domains = domains  # type: DescribeVodUserDomainsResponseBodyDomains
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super(DescribeVodUserDomainsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
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
        if m.get('Domains') is not None:
            temp_model = DescribeVodUserDomainsResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeVodUserDomainsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodUserDomainsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodUserDomainsResponse, self).to_map()
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
            temp_model = DescribeVodUserDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodVerifyContentRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodVerifyContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVodVerifyContentResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVodVerifyContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVodVerifyContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVodVerifyContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVodVerifyContentResponse, self).to_map()
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
            temp_model = DescribeVodVerifyContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachAppPolicyFromIdentityRequest(TeaModel):
    def __init__(self, app_id=None, identity_name=None, identity_type=None, policy_names=None):
        self.app_id = app_id  # type: str
        self.identity_name = identity_name  # type: str
        self.identity_type = identity_type  # type: str
        self.policy_names = policy_names  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachAppPolicyFromIdentityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        return self


class DetachAppPolicyFromIdentityResponseBody(TeaModel):
    def __init__(self, failed_policy_names=None, non_exist_policy_names=None, request_id=None):
        self.failed_policy_names = failed_policy_names  # type: list[str]
        self.non_exist_policy_names = non_exist_policy_names  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachAppPolicyFromIdentityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_policy_names is not None:
            result['FailedPolicyNames'] = self.failed_policy_names
        if self.non_exist_policy_names is not None:
            result['NonExistPolicyNames'] = self.non_exist_policy_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedPolicyNames') is not None:
            self.failed_policy_names = m.get('FailedPolicyNames')
        if m.get('NonExistPolicyNames') is not None:
            self.non_exist_policy_names = m.get('NonExistPolicyNames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachAppPolicyFromIdentityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachAppPolicyFromIdentityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachAppPolicyFromIdentityResponse, self).to_map()
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
            temp_model = DetachAppPolicyFromIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateKMSDataKeyRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateKMSDataKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GenerateKMSDataKeyResponseBody(TeaModel):
    def __init__(self, ciphertext_blob=None, key_id=None, plaintext=None, request_id=None):
        self.ciphertext_blob = ciphertext_blob  # type: str
        self.key_id = key_id  # type: str
        self.plaintext = plaintext  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateKMSDataKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphertext_blob is not None:
            result['CiphertextBlob'] = self.ciphertext_blob
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CiphertextBlob') is not None:
            self.ciphertext_blob = m.get('CiphertextBlob')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateKMSDataKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateKMSDataKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateKMSDataKeyResponse, self).to_map()
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
            temp_model = GenerateKMSDataKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIImageJobsRequest(TeaModel):
    def __init__(self, job_ids=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.job_ids = job_ids  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIImageJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetAIImageJobsResponseBodyAIImageJobList(TeaModel):
    def __init__(self, aiimage_result=None, code=None, creation_time=None, job_id=None, message=None, status=None,
                 template_config=None, template_id=None, user_data=None, video_id=None):
        self.aiimage_result = aiimage_result  # type: str
        self.code = code  # type: str
        self.creation_time = creation_time  # type: str
        self.job_id = job_id  # type: str
        self.message = message  # type: str
        self.status = status  # type: str
        self.template_config = template_config  # type: str
        self.template_id = template_id  # type: str
        self.user_data = user_data  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIImageJobsResponseBodyAIImageJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aiimage_result is not None:
            result['AIImageResult'] = self.aiimage_result
        if self.code is not None:
            result['Code'] = self.code
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIImageResult') is not None:
            self.aiimage_result = m.get('AIImageResult')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetAIImageJobsResponseBody(TeaModel):
    def __init__(self, aiimage_job_list=None, request_id=None):
        self.aiimage_job_list = aiimage_job_list  # type: list[GetAIImageJobsResponseBodyAIImageJobList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.aiimage_job_list:
            for k in self.aiimage_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAIImageJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAIImageJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAIImageJobsResponse, self).to_map()
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
            temp_model = GetAIImageJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIMediaAuditJobRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult(TeaModel):
    def __init__(self, label=None, scene=None, score=None, suggestion=None):
        self.label = label  # type: str
        self.scene = scene  # type: str
        self.score = score  # type: str
        self.suggestion = suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.score is not None:
            result['Score'] = self.score
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult(TeaModel):
    def __init__(self, label=None, scene=None, score=None, suggestion=None):
        self.label = label  # type: str
        self.scene = scene  # type: str
        self.score = score  # type: str
        self.suggestion = suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.score is not None:
            result['Score'] = self.score
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult(TeaModel):
    def __init__(self, label=None, result=None, suggestion=None, type=None, url=None):
        self.label = label  # type: str
        self.result = result  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult]
        self.suggestion = suggestion  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResultResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult(TeaModel):
    def __init__(self, content=None, label=None, scene=None, score=None, suggestion=None, type=None):
        self.content = content  # type: str
        self.label = label  # type: str
        self.scene = scene  # type: str
        self.score = score  # type: str
        self.suggestion = suggestion  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.score is not None:
            result['Score'] = self.score
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult(TeaModel):
    def __init__(self, ad_result=None, label=None, live_result=None, logo_result=None, porn_result=None,
                 suggestion=None, terrorism_result=None):
        self.ad_result = ad_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult
        self.label = label  # type: str
        self.live_result = live_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult
        self.logo_result = logo_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult
        self.porn_result = porn_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult
        self.suggestion = suggestion  # type: str
        self.terrorism_result = terrorism_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult

    def validate(self):
        if self.ad_result:
            self.ad_result.validate()
        if self.live_result:
            self.live_result.validate()
        if self.logo_result:
            self.logo_result.validate()
        if self.porn_result:
            self.porn_result.validate()
        if self.terrorism_result:
            self.terrorism_result.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_result is not None:
            result['AdResult'] = self.ad_result.to_map()
        if self.label is not None:
            result['Label'] = self.label
        if self.live_result is not None:
            result['LiveResult'] = self.live_result.to_map()
        if self.logo_result is not None:
            result['LogoResult'] = self.logo_result.to_map()
        if self.porn_result is not None:
            result['PornResult'] = self.porn_result.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.terrorism_result is not None:
            result['TerrorismResult'] = self.terrorism_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultAdResult()
            self.ad_result = temp_model.from_map(m['AdResult'])
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LiveResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLiveResult()
            self.live_result = temp_model.from_map(m['LiveResult'])
        if m.get('LogoResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultLogoResult()
            self.logo_result = temp_model.from_map(m['LogoResult'])
        if m.get('PornResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultPornResult()
            self.porn_result = temp_model.from_map(m['PornResult'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TerrorismResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResultTerrorismResult()
            self.terrorism_result = temp_model.from_map(m['TerrorismResult'])
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJobData(TeaModel):
    def __init__(self, abnormal_modules=None, audio_result=None, image_result=None, label=None, suggestion=None,
                 text_result=None, video_result=None):
        self.abnormal_modules = abnormal_modules  # type: str
        self.audio_result = audio_result  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult]
        self.image_result = image_result  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult]
        self.label = label  # type: str
        self.suggestion = suggestion  # type: str
        self.text_result = text_result  # type: list[GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult]
        self.video_result = video_result  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult

    def validate(self):
        if self.audio_result:
            for k in self.audio_result:
                if k:
                    k.validate()
        if self.image_result:
            for k in self.image_result:
                if k:
                    k.validate()
        if self.text_result:
            for k in self.text_result:
                if k:
                    k.validate()
        if self.video_result:
            self.video_result.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJobData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_modules is not None:
            result['AbnormalModules'] = self.abnormal_modules
        result['AudioResult'] = []
        if self.audio_result is not None:
            for k in self.audio_result:
                result['AudioResult'].append(k.to_map() if k else None)
        result['ImageResult'] = []
        if self.image_result is not None:
            for k in self.image_result:
                result['ImageResult'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TextResult'] = []
        if self.text_result is not None:
            for k in self.text_result:
                result['TextResult'].append(k.to_map() if k else None)
        if self.video_result is not None:
            result['VideoResult'] = self.video_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbnormalModules') is not None:
            self.abnormal_modules = m.get('AbnormalModules')
        self.audio_result = []
        if m.get('AudioResult') is not None:
            for k in m.get('AudioResult'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataAudioResult()
                self.audio_result.append(temp_model.from_map(k))
        self.image_result = []
        if m.get('ImageResult') is not None:
            for k in m.get('ImageResult'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataImageResult()
                self.image_result.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.text_result = []
        if m.get('TextResult') is not None:
            for k in m.get('TextResult'):
                temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataTextResult()
                self.text_result.append(temp_model.from_map(k))
        if m.get('VideoResult') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobDataVideoResult()
            self.video_result = temp_model.from_map(m['VideoResult'])
        return self


class GetAIMediaAuditJobResponseBodyMediaAuditJob(TeaModel):
    def __init__(self, code=None, complete_time=None, creation_time=None, data=None, job_id=None, media_id=None,
                 message=None, status=None, type=None):
        self.code = code  # type: str
        self.complete_time = complete_time  # type: str
        self.creation_time = creation_time  # type: str
        self.data = data  # type: GetAIMediaAuditJobResponseBodyMediaAuditJobData
        self.job_id = job_id  # type: str
        self.media_id = media_id  # type: str
        self.message = message  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBodyMediaAuditJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Data') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJobData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAIMediaAuditJobResponseBody(TeaModel):
    def __init__(self, media_audit_job=None, request_id=None):
        self.media_audit_job = media_audit_job  # type: GetAIMediaAuditJobResponseBodyMediaAuditJob
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_audit_job:
            self.media_audit_job.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_audit_job is not None:
            result['MediaAuditJob'] = self.media_audit_job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaAuditJob') is not None:
            temp_model = GetAIMediaAuditJobResponseBodyMediaAuditJob()
            self.media_audit_job = temp_model.from_map(m['MediaAuditJob'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAIMediaAuditJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAIMediaAuditJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAIMediaAuditJobResponse, self).to_map()
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
            temp_model = GetAIMediaAuditJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAITemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAITemplateRequest, self).to_map()
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


class GetAITemplateResponseBodyTemplateInfo(TeaModel):
    def __init__(self, creation_time=None, is_default=None, modify_time=None, source=None, template_config=None,
                 template_id=None, template_name=None, template_type=None):
        self.creation_time = creation_time  # type: str
        self.is_default = is_default  # type: str
        self.modify_time = modify_time  # type: str
        self.source = source  # type: str
        self.template_config = template_config  # type: str
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAITemplateResponseBodyTemplateInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.source is not None:
            result['Source'] = self.source
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_info=None):
        self.request_id = request_id  # type: str
        self.template_info = template_info  # type: GetAITemplateResponseBodyTemplateInfo

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super(GetAITemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateInfo') is not None:
            temp_model = GetAITemplateResponseBodyTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class GetAITemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAITemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAITemplateResponse, self).to_map()
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
            temp_model = GetAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAIVideoTagResultRequest(TeaModel):
    def __init__(self, media_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.media_id = media_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIVideoTagResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultCategory(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIVideoTagResultResponseBodyVideoTagResultCategory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultKeyword(TeaModel):
    def __init__(self, tag=None, times=None):
        self.tag = tag  # type: str
        self.times = times  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIVideoTagResultResponseBodyVideoTagResultKeyword, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultLocation(TeaModel):
    def __init__(self, tag=None, times=None):
        self.tag = tag  # type: str
        self.times = times  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIVideoTagResultResponseBodyVideoTagResultLocation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultPerson(TeaModel):
    def __init__(self, face_url=None, tag=None, times=None):
        self.face_url = face_url  # type: str
        self.tag = tag  # type: str
        self.times = times  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIVideoTagResultResponseBodyVideoTagResultPerson, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResultTime(TeaModel):
    def __init__(self, tag=None, times=None):
        self.tag = tag  # type: str
        self.times = times  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAIVideoTagResultResponseBodyVideoTagResultTime, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class GetAIVideoTagResultResponseBodyVideoTagResult(TeaModel):
    def __init__(self, category=None, keyword=None, location=None, person=None, time=None):
        self.category = category  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultCategory]
        self.keyword = keyword  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultKeyword]
        self.location = location  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultLocation]
        self.person = person  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultPerson]
        self.time = time  # type: list[GetAIVideoTagResultResponseBodyVideoTagResultTime]

    def validate(self):
        if self.category:
            for k in self.category:
                if k:
                    k.validate()
        if self.keyword:
            for k in self.keyword:
                if k:
                    k.validate()
        if self.location:
            for k in self.location:
                if k:
                    k.validate()
        if self.person:
            for k in self.person:
                if k:
                    k.validate()
        if self.time:
            for k in self.time:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAIVideoTagResultResponseBodyVideoTagResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Category'] = []
        if self.category is not None:
            for k in self.category:
                result['Category'].append(k.to_map() if k else None)
        result['Keyword'] = []
        if self.keyword is not None:
            for k in self.keyword:
                result['Keyword'].append(k.to_map() if k else None)
        result['Location'] = []
        if self.location is not None:
            for k in self.location:
                result['Location'].append(k.to_map() if k else None)
        result['Person'] = []
        if self.person is not None:
            for k in self.person:
                result['Person'].append(k.to_map() if k else None)
        result['Time'] = []
        if self.time is not None:
            for k in self.time:
                result['Time'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.category = []
        if m.get('Category') is not None:
            for k in m.get('Category'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultCategory()
                self.category.append(temp_model.from_map(k))
        self.keyword = []
        if m.get('Keyword') is not None:
            for k in m.get('Keyword'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultKeyword()
                self.keyword.append(temp_model.from_map(k))
        self.location = []
        if m.get('Location') is not None:
            for k in m.get('Location'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultLocation()
                self.location.append(temp_model.from_map(k))
        self.person = []
        if m.get('Person') is not None:
            for k in m.get('Person'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultPerson()
                self.person.append(temp_model.from_map(k))
        self.time = []
        if m.get('Time') is not None:
            for k in m.get('Time'):
                temp_model = GetAIVideoTagResultResponseBodyVideoTagResultTime()
                self.time.append(temp_model.from_map(k))
        return self


class GetAIVideoTagResultResponseBody(TeaModel):
    def __init__(self, request_id=None, video_tag_result=None):
        self.request_id = request_id  # type: str
        self.video_tag_result = video_tag_result  # type: GetAIVideoTagResultResponseBodyVideoTagResult

    def validate(self):
        if self.video_tag_result:
            self.video_tag_result.validate()

    def to_map(self):
        _map = super(GetAIVideoTagResultResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAIVideoTagResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAIVideoTagResultResponse, self).to_map()
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
            temp_model = GetAIVideoTagResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppInfosRequest(TeaModel):
    def __init__(self, app_ids=None):
        self.app_ids = app_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        return self


class GetAppInfosResponseBodyAppInfoList(TeaModel):
    def __init__(self, app_id=None, app_name=None, creation_time=None, description=None, modification_time=None,
                 status=None, type=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.modification_time = modification_time  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppInfosResponseBodyAppInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAppInfosResponseBody(TeaModel):
    def __init__(self, app_info_list=None, non_exist_app_ids=None, request_id=None):
        self.app_info_list = app_info_list  # type: list[GetAppInfosResponseBodyAppInfoList]
        self.non_exist_app_ids = non_exist_app_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAppInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        if self.non_exist_app_ids is not None:
            result['NonExistAppIds'] = self.non_exist_app_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = GetAppInfosResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        if m.get('NonExistAppIds') is not None:
            self.non_exist_app_ids = m.get('NonExistAppIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppInfosResponse, self).to_map()
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
            temp_model = GetAppInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAttachedMediaInfoRequest(TeaModel):
    def __init__(self, auth_timeout=None, media_ids=None, output_type=None):
        self.auth_timeout = auth_timeout  # type: long
        self.media_ids = media_ids  # type: str
        self.output_type = output_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAttachedMediaInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class GetAttachedMediaInfoResponseBodyAttachedMediaListCategories(TeaModel):
    def __init__(self, cate_id=None, cate_name=None, level=None, parent_id=None):
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.level = level  # type: long
        self.parent_id = parent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAttachedMediaInfoResponseBodyAttachedMediaListCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.level is not None:
            result['Level'] = self.level
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class GetAttachedMediaInfoResponseBodyAttachedMediaList(TeaModel):
    def __init__(self, app_id=None, categories=None, creation_time=None, description=None, media_id=None,
                 modification_time=None, status=None, storage_location=None, tags=None, title=None, type=None, url=None):
        self.app_id = app_id  # type: str
        self.categories = categories  # type: list[GetAttachedMediaInfoResponseBodyAttachedMediaListCategories]
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.media_id = media_id  # type: str
        self.modification_time = modification_time  # type: str
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAttachedMediaInfoResponseBodyAttachedMediaList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = GetAttachedMediaInfoResponseBodyAttachedMediaListCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class GetAttachedMediaInfoResponseBody(TeaModel):
    def __init__(self, attached_media_list=None, non_exist_media_ids=None, request_id=None):
        self.attached_media_list = attached_media_list  # type: list[GetAttachedMediaInfoResponseBodyAttachedMediaList]
        self.non_exist_media_ids = non_exist_media_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.attached_media_list:
            for k in self.attached_media_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAttachedMediaInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AttachedMediaList'] = []
        if self.attached_media_list is not None:
            for k in self.attached_media_list:
                result['AttachedMediaList'].append(k.to_map() if k else None)
        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.attached_media_list = []
        if m.get('AttachedMediaList') is not None:
            for k in m.get('AttachedMediaList'):
                temp_model = GetAttachedMediaInfoResponseBodyAttachedMediaList()
                self.attached_media_list.append(temp_model.from_map(k))
        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAttachedMediaInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAttachedMediaInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAttachedMediaInfoResponse, self).to_map()
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
            temp_model = GetAttachedMediaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditHistoryRequest(TeaModel):
    def __init__(self, page_no=None, page_size=None, sort_by=None, video_id=None):
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditHistoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetAuditHistoryResponseBodyHistories(TeaModel):
    def __init__(self, auditor=None, comment=None, creation_time=None, reason=None, status=None):
        self.auditor = auditor  # type: str
        self.comment = comment  # type: str
        self.creation_time = creation_time  # type: str
        self.reason = reason  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditHistoryResponseBodyHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auditor is not None:
            result['Auditor'] = self.auditor
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Auditor') is not None:
            self.auditor = m.get('Auditor')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAuditHistoryResponseBody(TeaModel):
    def __init__(self, histories=None, request_id=None, status=None, total=None):
        self.histories = histories  # type: list[GetAuditHistoryResponseBodyHistories]
        self.request_id = request_id  # type: str
        self.status = status  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.histories:
            for k in self.histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAuditHistoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Histories'] = []
        if self.histories is not None:
            for k in self.histories:
                result['Histories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.histories = []
        if m.get('Histories') is not None:
            for k in m.get('Histories'):
                temp_model = GetAuditHistoryResponseBodyHistories()
                self.histories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAuditHistoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAuditHistoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuditHistoryResponse, self).to_map()
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
            temp_model = GetAuditHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCategoriesRequest(TeaModel):
    def __init__(self, cate_id=None, page_no=None, page_size=None, sort_by=None, type=None):
        self.cate_id = cate_id  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.sort_by = sort_by  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCategoriesRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, cate_id=None, cate_name=None, level=None, parent_id=None, type=None):
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.level = level  # type: long
        self.parent_id = parent_id  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCategoriesResponseBodyCategory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.level is not None:
            result['Level'] = self.level
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetCategoriesResponseBodySubCategoriesCategory(TeaModel):
    def __init__(self, cate_id=None, cate_name=None, level=None, parent_id=None, sub_total=None, type=None):
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.level = level  # type: long
        self.parent_id = parent_id  # type: long
        self.sub_total = sub_total  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCategoriesResponseBodySubCategoriesCategory, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.level is not None:
            result['Level'] = self.level
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.sub_total is not None:
            result['SubTotal'] = self.sub_total
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('SubTotal') is not None:
            self.sub_total = m.get('SubTotal')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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
        _map = super(GetCategoriesResponseBodySubCategories, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, category=None, request_id=None, sub_categories=None, sub_total=None):
        self.category = category  # type: GetCategoriesResponseBodyCategory
        self.request_id = request_id  # type: str
        self.sub_categories = sub_categories  # type: GetCategoriesResponseBodySubCategories
        self.sub_total = sub_total  # type: long

    def validate(self):
        if self.category:
            self.category.validate()
        if self.sub_categories:
            self.sub_categories.validate()

    def to_map(self):
        _map = super(GetCategoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_categories is not None:
            result['SubCategories'] = self.sub_categories.to_map()
        if self.sub_total is not None:
            result['SubTotal'] = self.sub_total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Category') is not None:
            temp_model = GetCategoriesResponseBodyCategory()
            self.category = temp_model.from_map(m['Category'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCategories') is not None:
            temp_model = GetCategoriesResponseBodySubCategories()
            self.sub_categories = temp_model.from_map(m['SubCategories'])
        if m.get('SubTotal') is not None:
            self.sub_total = m.get('SubTotal')
        return self


class GetCategoriesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCategoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCategoriesResponse, self).to_map()
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
            temp_model = GetCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultAITemplateRequest(TeaModel):
    def __init__(self, template_type=None):
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultAITemplateRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, creation_time=None, is_default=None, modify_time=None, source=None, template_config=None,
                 template_id=None, template_name=None, template_type=None):
        self.creation_time = creation_time  # type: str
        self.is_default = is_default  # type: str
        self.modify_time = modify_time  # type: str
        self.source = source  # type: str
        self.template_config = template_config  # type: str
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDefaultAITemplateResponseBodyTemplateInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.source is not None:
            result['Source'] = self.source
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class GetDefaultAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_info=None):
        self.request_id = request_id  # type: str
        self.template_info = template_info  # type: GetDefaultAITemplateResponseBodyTemplateInfo

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super(GetDefaultAITemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateInfo') is not None:
            temp_model = GetDefaultAITemplateResponseBodyTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class GetDefaultAITemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDefaultAITemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDefaultAITemplateResponse, self).to_map()
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
            temp_model = GetDefaultAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectRequest(TeaModel):
    def __init__(self, owner_account=None, owner_id=None, project_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.project_id = project_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetEditingProjectResponseBodyProject(TeaModel):
    def __init__(self, cover_url=None, creation_time=None, description=None, modified_time=None, project_id=None,
                 region_id=None, status=None, storage_location=None, timeline=None, title=None):
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.modified_time = modified_time  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.timeline = timeline  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetEditingProjectResponseBody(TeaModel):
    def __init__(self, project=None, request_id=None):
        self.project = project  # type: GetEditingProjectResponseBodyProject
        self.request_id = request_id  # type: str

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(GetEditingProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEditingProjectResponse, self).to_map()
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
            temp_model = GetEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, material_type=None, owner_account=None, owner_id=None, project_id=None,
                 resource_owner_account=None, resource_owner_id=None, type=None):
        self.material_type = material_type  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.project_id = project_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        return self


class GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites(TeaModel):
    def __init__(self, sprite=None):
        self.sprite = sprite  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sprite is not None:
            result['Sprite'] = self.sprite
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Sprite') is not None:
            self.sprite = m.get('Sprite')
        return self


class GetEditingProjectMaterialsResponseBodyMaterialListMaterial(TeaModel):
    def __init__(self, cate_id=None, cate_name=None, cover_url=None, creation_time=None, description=None,
                 duration=None, material_id=None, material_type=None, modified_time=None, size=None, snapshots=None,
                 source=None, sprite_config=None, sprites=None, status=None, tags=None, title=None):
        self.cate_id = cate_id  # type: int
        self.cate_name = cate_name  # type: str
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.duration = duration  # type: float
        self.material_id = material_id  # type: str
        self.material_type = material_type  # type: str
        self.modified_time = modified_time  # type: str
        self.size = size  # type: long
        self.snapshots = snapshots  # type: GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots
        self.source = source  # type: str
        self.sprite_config = sprite_config  # type: str
        self.sprites = sprites  # type: GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites
        self.status = status  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()
        if self.sprites:
            self.sprites.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBodyMaterialListMaterial, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.source is not None:
            result['Source'] = self.source
        if self.sprite_config is not None:
            result['SpriteConfig'] = self.sprite_config
        if self.sprites is not None:
            result['Sprites'] = self.sprites.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Snapshots') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMaterialListMaterialSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SpriteConfig') is not None:
            self.sprite_config = m.get('SpriteConfig')
        if m.get('Sprites') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMaterialListMaterialSprites()
            self.sprites = temp_model.from_map(m['Sprites'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
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
        _map = super(GetEditingProjectMaterialsResponseBodyMaterialList, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, material_list=None, request_id=None):
        self.material_list = material_list  # type: GetEditingProjectMaterialsResponseBodyMaterialList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.material_list:
            self.material_list.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_list is not None:
            result['MaterialList'] = self.material_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaterialList') is not None:
            temp_model = GetEditingProjectMaterialsResponseBodyMaterialList()
            self.material_list = temp_model.from_map(m['MaterialList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEditingProjectMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEditingProjectMaterialsResponse, self).to_map()
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
            temp_model = GetEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageInfoRequest(TeaModel):
    def __init__(self, auth_timeout=None, image_id=None, output_type=None):
        self.auth_timeout = auth_timeout  # type: long
        self.image_id = image_id  # type: str
        self.output_type = output_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class GetImageInfoResponseBodyImageInfoMezzanine(TeaModel):
    def __init__(self, file_size=None, file_url=None, height=None, original_file_name=None, width=None):
        self.file_size = file_size  # type: str
        self.file_url = file_url  # type: str
        self.height = height  # type: int
        self.original_file_name = original_file_name  # type: str
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageInfoResponseBodyImageInfoMezzanine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.height is not None:
            result['Height'] = self.height
        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetImageInfoResponseBodyImageInfo(TeaModel):
    def __init__(self, app_id=None, cate_id=None, cate_name=None, creation_time=None, description=None,
                 image_id=None, image_type=None, mezzanine=None, status=None, storage_location=None, tags=None, title=None,
                 url=None):
        self.app_id = app_id  # type: str
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.image_id = image_id  # type: str
        self.image_type = image_type  # type: str
        self.mezzanine = mezzanine  # type: GetImageInfoResponseBodyImageInfoMezzanine
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.mezzanine:
            self.mezzanine.validate()

    def to_map(self):
        _map = super(GetImageInfoResponseBodyImageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.mezzanine is not None:
            result['Mezzanine'] = self.mezzanine.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Mezzanine') is not None:
            temp_model = GetImageInfoResponseBodyImageInfoMezzanine()
            self.mezzanine = temp_model.from_map(m['Mezzanine'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class GetImageInfoResponseBody(TeaModel):
    def __init__(self, image_info=None, request_id=None):
        self.image_info = image_info  # type: GetImageInfoResponseBodyImageInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.image_info:
            self.image_info.validate()

    def to_map(self):
        _map = super(GetImageInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_info is not None:
            result['ImageInfo'] = self.image_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageInfo') is not None:
            temp_model = GetImageInfoResponseBodyImageInfo()
            self.image_info = temp_model.from_map(m['ImageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetImageInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageInfoResponse, self).to_map()
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
            temp_model = GetImageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageInfosRequest(TeaModel):
    def __init__(self, auth_timeout=None, image_ids=None, output_type=None):
        self.auth_timeout = auth_timeout  # type: long
        self.image_ids = image_ids  # type: str
        self.output_type = output_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        return self


class GetImageInfosResponseBodyImageInfoMezzanine(TeaModel):
    def __init__(self, file_size=None, file_url=None, height=None, original_file_name=None, width=None):
        self.file_size = file_size  # type: str
        self.file_url = file_url  # type: str
        self.height = height  # type: int
        self.original_file_name = original_file_name  # type: str
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetImageInfosResponseBodyImageInfoMezzanine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.height is not None:
            result['Height'] = self.height
        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetImageInfosResponseBodyImageInfo(TeaModel):
    def __init__(self, app_id=None, cate_id=None, cate_name=None, creation_time=None, description=None,
                 image_id=None, image_type=None, mezzanine=None, status=None, storage_location=None, tags=None, title=None,
                 url=None):
        self.app_id = app_id  # type: str
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.image_id = image_id  # type: str
        self.image_type = image_type  # type: str
        self.mezzanine = mezzanine  # type: GetImageInfosResponseBodyImageInfoMezzanine
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.mezzanine:
            self.mezzanine.validate()

    def to_map(self):
        _map = super(GetImageInfosResponseBodyImageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.mezzanine is not None:
            result['Mezzanine'] = self.mezzanine.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Mezzanine') is not None:
            temp_model = GetImageInfosResponseBodyImageInfoMezzanine()
            self.mezzanine = temp_model.from_map(m['Mezzanine'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class GetImageInfosResponseBody(TeaModel):
    def __init__(self, image_info=None, non_exist_image_ids=None, request_id=None):
        self.image_info = image_info  # type: list[GetImageInfosResponseBodyImageInfo]
        self.non_exist_image_ids = non_exist_image_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.image_info:
            for k in self.image_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetImageInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageInfo'] = []
        if self.image_info is not None:
            for k in self.image_info:
                result['ImageInfo'].append(k.to_map() if k else None)
        if self.non_exist_image_ids is not None:
            result['NonExistImageIds'] = self.non_exist_image_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.image_info = []
        if m.get('ImageInfo') is not None:
            for k in m.get('ImageInfo'):
                temp_model = GetImageInfosResponseBodyImageInfo()
                self.image_info.append(temp_model.from_map(k))
        if m.get('NonExistImageIds') is not None:
            self.non_exist_image_ids = m.get('NonExistImageIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetImageInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetImageInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetImageInfosResponse, self).to_map()
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
            temp_model = GetImageInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaAuditAudioResultDetailRequest(TeaModel):
    def __init__(self, media_id=None, owner_account=None, owner_id=None, page_no=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.media_id = media_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.page_no = page_no  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditAudioResultDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetailList(TeaModel):
    def __init__(self, end_time=None, label=None, start_time=None, text=None):
        self.end_time = end_time  # type: long
        self.label = label  # type: str
        self.start_time = start_time  # type: long
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Text') is not None:
            self.text = m.get('Text')
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
        _map = super(GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetail, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_audit_audio_result_detail:
            self.media_audit_audio_result_detail.validate()

    def to_map(self):
        _map = super(GetMediaAuditAudioResultDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMediaAuditAudioResultDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaAuditAudioResultDetailResponse, self).to_map()
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
            temp_model = GetMediaAuditAudioResultDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaAuditResultRequest(TeaModel):
    def __init__(self, media_id=None):
        self.media_id = media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultAudioResult(TeaModel):
    def __init__(self, label=None, scene=None, score=None, suggestion=None):
        self.label = label  # type: str
        self.scene = scene  # type: str
        self.score = score  # type: str
        self.suggestion = suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultAudioResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.score is not None:
            result['Score'] = self.score
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult(TeaModel):
    def __init__(self, label=None, scene=None, score=None, suggestion=None):
        self.label = label  # type: str
        self.scene = scene  # type: str
        self.score = score  # type: str
        self.suggestion = suggestion  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.score is not None:
            result['Score'] = self.score
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultImageResult(TeaModel):
    def __init__(self, label=None, result=None, suggestion=None, type=None, url=None):
        self.label = label  # type: str
        self.result = result  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult]
        self.suggestion = suggestion  # type: str
        self.type = type  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultImageResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultImageResultResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultTextResult(TeaModel):
    def __init__(self, content=None, label=None, scene=None, score=None, suggestion=None, type=None):
        self.content = content  # type: str
        self.label = label  # type: str
        self.scene = scene  # type: str
        self.score = score  # type: str
        self.suggestion = suggestion  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultTextResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.score is not None:
            result['Score'] = self.score
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultCounterList(TeaModel):
    def __init__(self, count=None, label=None):
        self.count = count  # type: int
        self.label = label  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultCounterList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None, url=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult(TeaModel):
    def __init__(self, average_score=None, counter_list=None, label=None, max_score=None, suggestion=None,
                 top_list=None):
        self.average_score = average_score  # type: str
        self.counter_list = counter_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultCounterList]
        self.label = label  # type: str
        self.max_score = max_score  # type: str
        self.suggestion = suggestion  # type: str
        self.top_list = top_list  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList]

    def validate(self):
        if self.counter_list:
            for k in self.counter_list:
                if k:
                    k.validate()
        if self.top_list:
            for k in self.top_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TopList'] = []
        if self.top_list is not None:
            for k in self.top_list:
                result['TopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.top_list = []
        if m.get('TopList') is not None:
            for k in m.get('TopList'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResultTopList()
                self.top_list.append(temp_model.from_map(k))
        return self


class GetMediaAuditResultResponseBodyMediaAuditResultVideoResult(TeaModel):
    def __init__(self, ad_result=None, label=None, live_result=None, logo_result=None, porn_result=None,
                 suggestion=None, terrorism_result=None):
        self.ad_result = ad_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult
        self.label = label  # type: str
        self.live_result = live_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult
        self.logo_result = logo_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult
        self.porn_result = porn_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult
        self.suggestion = suggestion  # type: str
        self.terrorism_result = terrorism_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult

    def validate(self):
        if self.ad_result:
            self.ad_result.validate()
        if self.live_result:
            self.live_result.validate()
        if self.logo_result:
            self.logo_result.validate()
        if self.porn_result:
            self.porn_result.validate()
        if self.terrorism_result:
            self.terrorism_result.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResultVideoResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_result is not None:
            result['AdResult'] = self.ad_result.to_map()
        if self.label is not None:
            result['Label'] = self.label
        if self.live_result is not None:
            result['LiveResult'] = self.live_result.to_map()
        if self.logo_result is not None:
            result['LogoResult'] = self.logo_result.to_map()
        if self.porn_result is not None:
            result['PornResult'] = self.porn_result.to_map()
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.terrorism_result is not None:
            result['TerrorismResult'] = self.terrorism_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultAdResult()
            self.ad_result = temp_model.from_map(m['AdResult'])
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LiveResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLiveResult()
            self.live_result = temp_model.from_map(m['LiveResult'])
        if m.get('LogoResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultLogoResult()
            self.logo_result = temp_model.from_map(m['LogoResult'])
        if m.get('PornResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultPornResult()
            self.porn_result = temp_model.from_map(m['PornResult'])
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TerrorismResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResultTerrorismResult()
            self.terrorism_result = temp_model.from_map(m['TerrorismResult'])
        return self


class GetMediaAuditResultResponseBodyMediaAuditResult(TeaModel):
    def __init__(self, abnormal_modules=None, audio_result=None, image_result=None, label=None, suggestion=None,
                 text_result=None, video_result=None):
        self.abnormal_modules = abnormal_modules  # type: str
        self.audio_result = audio_result  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultAudioResult]
        self.image_result = image_result  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultImageResult]
        self.label = label  # type: str
        self.suggestion = suggestion  # type: str
        self.text_result = text_result  # type: list[GetMediaAuditResultResponseBodyMediaAuditResultTextResult]
        self.video_result = video_result  # type: GetMediaAuditResultResponseBodyMediaAuditResultVideoResult

    def validate(self):
        if self.audio_result:
            for k in self.audio_result:
                if k:
                    k.validate()
        if self.image_result:
            for k in self.image_result:
                if k:
                    k.validate()
        if self.text_result:
            for k in self.text_result:
                if k:
                    k.validate()
        if self.video_result:
            self.video_result.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBodyMediaAuditResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_modules is not None:
            result['AbnormalModules'] = self.abnormal_modules
        result['AudioResult'] = []
        if self.audio_result is not None:
            for k in self.audio_result:
                result['AudioResult'].append(k.to_map() if k else None)
        result['ImageResult'] = []
        if self.image_result is not None:
            for k in self.image_result:
                result['ImageResult'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        result['TextResult'] = []
        if self.text_result is not None:
            for k in self.text_result:
                result['TextResult'].append(k.to_map() if k else None)
        if self.video_result is not None:
            result['VideoResult'] = self.video_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AbnormalModules') is not None:
            self.abnormal_modules = m.get('AbnormalModules')
        self.audio_result = []
        if m.get('AudioResult') is not None:
            for k in m.get('AudioResult'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultAudioResult()
                self.audio_result.append(temp_model.from_map(k))
        self.image_result = []
        if m.get('ImageResult') is not None:
            for k in m.get('ImageResult'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultImageResult()
                self.image_result.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        self.text_result = []
        if m.get('TextResult') is not None:
            for k in m.get('TextResult'):
                temp_model = GetMediaAuditResultResponseBodyMediaAuditResultTextResult()
                self.text_result.append(temp_model.from_map(k))
        if m.get('VideoResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResultVideoResult()
            self.video_result = temp_model.from_map(m['VideoResult'])
        return self


class GetMediaAuditResultResponseBody(TeaModel):
    def __init__(self, media_audit_result=None, request_id=None):
        self.media_audit_result = media_audit_result  # type: GetMediaAuditResultResponseBodyMediaAuditResult
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_audit_result:
            self.media_audit_result.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_audit_result is not None:
            result['MediaAuditResult'] = self.media_audit_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaAuditResult') is not None:
            temp_model = GetMediaAuditResultResponseBodyMediaAuditResult()
            self.media_audit_result = temp_model.from_map(m['MediaAuditResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMediaAuditResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMediaAuditResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultResponse, self).to_map()
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
            temp_model = GetMediaAuditResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaAuditResultDetailRequest(TeaModel):
    def __init__(self, media_id=None, page_no=None):
        self.media_id = media_id  # type: str
        self.page_no = page_no  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultDetailRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, ad_label=None, ad_score=None, live_label=None, live_score=None, logo_label=None,
                 logo_score=None, porn_label=None, porn_score=None, terrorism_label=None, terrorism_score=None, timestamp=None,
                 url=None):
        self.ad_label = ad_label  # type: str
        self.ad_score = ad_score  # type: str
        self.live_label = live_label  # type: str
        self.live_score = live_score  # type: str
        self.logo_label = logo_label  # type: str
        self.logo_score = logo_score  # type: str
        self.porn_label = porn_label  # type: str
        self.porn_score = porn_score  # type: str
        self.terrorism_label = terrorism_label  # type: str
        self.terrorism_score = terrorism_score  # type: str
        self.timestamp = timestamp  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultDetailResponseBodyMediaAuditResultDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_label is not None:
            result['AdLabel'] = self.ad_label
        if self.ad_score is not None:
            result['AdScore'] = self.ad_score
        if self.live_label is not None:
            result['LiveLabel'] = self.live_label
        if self.live_score is not None:
            result['LiveScore'] = self.live_score
        if self.logo_label is not None:
            result['LogoLabel'] = self.logo_label
        if self.logo_score is not None:
            result['LogoScore'] = self.logo_score
        if self.porn_label is not None:
            result['PornLabel'] = self.porn_label
        if self.porn_score is not None:
            result['PornScore'] = self.porn_score
        if self.terrorism_label is not None:
            result['TerrorismLabel'] = self.terrorism_label
        if self.terrorism_score is not None:
            result['TerrorismScore'] = self.terrorism_score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdLabel') is not None:
            self.ad_label = m.get('AdLabel')
        if m.get('AdScore') is not None:
            self.ad_score = m.get('AdScore')
        if m.get('LiveLabel') is not None:
            self.live_label = m.get('LiveLabel')
        if m.get('LiveScore') is not None:
            self.live_score = m.get('LiveScore')
        if m.get('LogoLabel') is not None:
            self.logo_label = m.get('LogoLabel')
        if m.get('LogoScore') is not None:
            self.logo_score = m.get('LogoScore')
        if m.get('PornLabel') is not None:
            self.porn_label = m.get('PornLabel')
        if m.get('PornScore') is not None:
            self.porn_score = m.get('PornScore')
        if m.get('TerrorismLabel') is not None:
            self.terrorism_label = m.get('TerrorismLabel')
        if m.get('TerrorismScore') is not None:
            self.terrorism_score = m.get('TerrorismScore')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
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
        _map = super(GetMediaAuditResultDetailResponseBodyMediaAuditResultDetail, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, media_audit_result_detail=None, request_id=None):
        self.media_audit_result_detail = media_audit_result_detail  # type: GetMediaAuditResultDetailResponseBodyMediaAuditResultDetail
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_audit_result_detail:
            self.media_audit_result_detail.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_audit_result_detail is not None:
            result['MediaAuditResultDetail'] = self.media_audit_result_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaAuditResultDetail') is not None:
            temp_model = GetMediaAuditResultDetailResponseBodyMediaAuditResultDetail()
            self.media_audit_result_detail = temp_model.from_map(m['MediaAuditResultDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMediaAuditResultDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMediaAuditResultDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultDetailResponse, self).to_map()
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
            temp_model = GetMediaAuditResultDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaAuditResultTimelineRequest(TeaModel):
    def __init__(self, media_id=None):
        self.media_id = media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultTimelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism(TeaModel):
    def __init__(self, label=None, score=None, timestamp=None):
        self.label = label  # type: str
        self.score = score  # type: str
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.score is not None:
            result['Score'] = self.score
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline(TeaModel):
    def __init__(self, ad=None, live=None, logo=None, porn=None, terrorism=None):
        self.ad = ad  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd]
        self.live = live  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive]
        self.logo = logo  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo]
        self.porn = porn  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn]
        self.terrorism = terrorism  # type: list[GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism]

    def validate(self):
        if self.ad:
            for k in self.ad:
                if k:
                    k.validate()
        if self.live:
            for k in self.live:
                if k:
                    k.validate()
        if self.logo:
            for k in self.logo:
                if k:
                    k.validate()
        if self.porn:
            for k in self.porn:
                if k:
                    k.validate()
        if self.terrorism:
            for k in self.terrorism:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Ad'] = []
        if self.ad is not None:
            for k in self.ad:
                result['Ad'].append(k.to_map() if k else None)
        result['Live'] = []
        if self.live is not None:
            for k in self.live:
                result['Live'].append(k.to_map() if k else None)
        result['Logo'] = []
        if self.logo is not None:
            for k in self.logo:
                result['Logo'].append(k.to_map() if k else None)
        result['Porn'] = []
        if self.porn is not None:
            for k in self.porn:
                result['Porn'].append(k.to_map() if k else None)
        result['Terrorism'] = []
        if self.terrorism is not None:
            for k in self.terrorism:
                result['Terrorism'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ad = []
        if m.get('Ad') is not None:
            for k in m.get('Ad'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineAd()
                self.ad.append(temp_model.from_map(k))
        self.live = []
        if m.get('Live') is not None:
            for k in m.get('Live'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLive()
                self.live.append(temp_model.from_map(k))
        self.logo = []
        if m.get('Logo') is not None:
            for k in m.get('Logo'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineLogo()
                self.logo.append(temp_model.from_map(k))
        self.porn = []
        if m.get('Porn') is not None:
            for k in m.get('Porn'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelinePorn()
                self.porn.append(temp_model.from_map(k))
        self.terrorism = []
        if m.get('Terrorism') is not None:
            for k in m.get('Terrorism'):
                temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimelineTerrorism()
                self.terrorism.append(temp_model.from_map(k))
        return self


class GetMediaAuditResultTimelineResponseBody(TeaModel):
    def __init__(self, media_audit_result_timeline=None, request_id=None):
        self.media_audit_result_timeline = media_audit_result_timeline  # type: GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_audit_result_timeline:
            self.media_audit_result_timeline.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultTimelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_audit_result_timeline is not None:
            result['MediaAuditResultTimeline'] = self.media_audit_result_timeline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaAuditResultTimeline') is not None:
            temp_model = GetMediaAuditResultTimelineResponseBodyMediaAuditResultTimeline()
            self.media_audit_result_timeline = temp_model.from_map(m['MediaAuditResultTimeline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMediaAuditResultTimelineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMediaAuditResultTimelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaAuditResultTimelineResponse, self).to_map()
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
            temp_model = GetMediaAuditResultTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaDNAResultRequest(TeaModel):
    def __init__(self, media_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.media_id = media_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaDNAResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetMediaDNAResultResponseBodyDNAResultVideoDNADetailDuplication(TeaModel):
    def __init__(self, duration=None, start=None):
        self.duration = duration  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaDNAResultResponseBodyDNAResultVideoDNADetailDuplication, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetMediaDNAResultResponseBodyDNAResultVideoDNADetailInput(TeaModel):
    def __init__(self, duration=None, start=None):
        self.duration = duration  # type: str
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaDNAResultResponseBodyDNAResultVideoDNADetailInput, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Start') is not None:
            self.start = m.get('Start')
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
        _map = super(GetMediaDNAResultResponseBodyDNAResultVideoDNADetail, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, detail=None, primary_key=None, similarity=None):
        self.detail = detail  # type: list[GetMediaDNAResultResponseBodyDNAResultVideoDNADetail]
        self.primary_key = primary_key  # type: str
        self.similarity = similarity  # type: str

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaDNAResultResponseBodyDNAResultVideoDNA, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = GetMediaDNAResultResponseBodyDNAResultVideoDNADetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
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
        _map = super(GetMediaDNAResultResponseBodyDNAResult, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, dnaresult=None, request_id=None):
        self.dnaresult = dnaresult  # type: GetMediaDNAResultResponseBodyDNAResult
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dnaresult:
            self.dnaresult.validate()

    def to_map(self):
        _map = super(GetMediaDNAResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dnaresult is not None:
            result['DNAResult'] = self.dnaresult.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DNAResult') is not None:
            temp_model = GetMediaDNAResultResponseBodyDNAResult()
            self.dnaresult = temp_model.from_map(m['DNAResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMediaDNAResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMediaDNAResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaDNAResultResponse, self).to_map()
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
            temp_model = GetMediaDNAResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaRefreshJobsRequest(TeaModel):
    def __init__(self, media_id=None, media_refresh_job_id=None):
        self.media_id = media_id  # type: str
        self.media_refresh_job_id = media_refresh_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaRefreshJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_refresh_job_id is not None:
            result['MediaRefreshJobId'] = self.media_refresh_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaRefreshJobId') is not None:
            self.media_refresh_job_id = m.get('MediaRefreshJobId')
        return self


class GetMediaRefreshJobsResponseBodyMediaRefreshJobs(TeaModel):
    def __init__(self, error_code=None, error_message=None, filter_policy=None, gmt_create=None, gmt_modified=None,
                 media_id=None, media_refresh_job_id=None, status=None, success_play_urls=None, task_ids=None,
                 task_type=None, user_data=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.filter_policy = filter_policy  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.media_id = media_id  # type: str
        self.media_refresh_job_id = media_refresh_job_id  # type: str
        self.status = status  # type: str
        self.success_play_urls = success_play_urls  # type: str
        self.task_ids = task_ids  # type: str
        self.task_type = task_type  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMediaRefreshJobsResponseBodyMediaRefreshJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.filter_policy is not None:
            result['FilterPolicy'] = self.filter_policy
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_refresh_job_id is not None:
            result['MediaRefreshJobId'] = self.media_refresh_job_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success_play_urls is not None:
            result['SuccessPlayUrls'] = self.success_play_urls
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FilterPolicy') is not None:
            self.filter_policy = m.get('FilterPolicy')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaRefreshJobId') is not None:
            self.media_refresh_job_id = m.get('MediaRefreshJobId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessPlayUrls') is not None:
            self.success_play_urls = m.get('SuccessPlayUrls')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetMediaRefreshJobsResponseBody(TeaModel):
    def __init__(self, media_refresh_jobs=None, request_id=None):
        self.media_refresh_jobs = media_refresh_jobs  # type: list[GetMediaRefreshJobsResponseBodyMediaRefreshJobs]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_refresh_jobs:
            for k in self.media_refresh_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMediaRefreshJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MediaRefreshJobs'] = []
        if self.media_refresh_jobs is not None:
            for k in self.media_refresh_jobs:
                result['MediaRefreshJobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.media_refresh_jobs = []
        if m.get('MediaRefreshJobs') is not None:
            for k in m.get('MediaRefreshJobs'):
                temp_model = GetMediaRefreshJobsResponseBodyMediaRefreshJobs()
                self.media_refresh_jobs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMediaRefreshJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMediaRefreshJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMediaRefreshJobsResponse, self).to_map()
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
            temp_model = GetMediaRefreshJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageCallbackRequest(TeaModel):
    def __init__(self, app_id=None, owner_account=None):
        self.app_id = app_id  # type: str
        self.owner_account = owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMessageCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class GetMessageCallbackResponseBodyMessageCallback(TeaModel):
    def __init__(self, app_id=None, auth_key=None, auth_switch=None, callback_type=None, callback_url=None,
                 event_type_list=None, mns_endpoint=None, mns_queue_name=None):
        self.app_id = app_id  # type: str
        self.auth_key = auth_key  # type: str
        self.auth_switch = auth_switch  # type: str
        self.callback_type = callback_type  # type: str
        self.callback_url = callback_url  # type: str
        self.event_type_list = event_type_list  # type: str
        self.mns_endpoint = mns_endpoint  # type: str
        self.mns_queue_name = mns_queue_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMessageCallbackResponseBodyMessageCallback, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_switch is not None:
            result['AuthSwitch'] = self.auth_switch
        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type
        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        if self.mns_endpoint is not None:
            result['MnsEndpoint'] = self.mns_endpoint
        if self.mns_queue_name is not None:
            result['MnsQueueName'] = self.mns_queue_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSwitch') is not None:
            self.auth_switch = m.get('AuthSwitch')
        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')
        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        if m.get('MnsEndpoint') is not None:
            self.mns_endpoint = m.get('MnsEndpoint')
        if m.get('MnsQueueName') is not None:
            self.mns_queue_name = m.get('MnsQueueName')
        return self


class GetMessageCallbackResponseBody(TeaModel):
    def __init__(self, message_callback=None, request_id=None):
        self.message_callback = message_callback  # type: GetMessageCallbackResponseBodyMessageCallback
        self.request_id = request_id  # type: str

    def validate(self):
        if self.message_callback:
            self.message_callback.validate()

    def to_map(self):
        _map = super(GetMessageCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_callback is not None:
            result['MessageCallback'] = self.message_callback.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MessageCallback') is not None:
            temp_model = GetMessageCallbackResponseBodyMessageCallback()
            self.message_callback = temp_model.from_map(m['MessageCallback'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMessageCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMessageCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMessageCallbackResponse, self).to_map()
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
            temp_model = GetMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMezzanineInfoRequest(TeaModel):
    def __init__(self, addition_type=None, auth_timeout=None, output_type=None, video_id=None):
        self.addition_type = addition_type  # type: str
        self.auth_timeout = auth_timeout  # type: long
        self.output_type = output_type  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMezzanineInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetMezzanineInfoResponseBodyMezzanineAudioStreamList(TeaModel):
    def __init__(self, bitrate=None, channel_layout=None, channels=None, codec_long_name=None, codec_name=None,
                 codec_tag=None, codec_tag_string=None, codec_time_base=None, duration=None, index=None, lang=None,
                 num_frames=None, sample_fmt=None, sample_rate=None, start_time=None, timebase=None):
        self.bitrate = bitrate  # type: str
        self.channel_layout = channel_layout  # type: str
        self.channels = channels  # type: str
        self.codec_long_name = codec_long_name  # type: str
        self.codec_name = codec_name  # type: str
        self.codec_tag = codec_tag  # type: str
        self.codec_tag_string = codec_tag_string  # type: str
        self.codec_time_base = codec_time_base  # type: str
        self.duration = duration  # type: str
        self.index = index  # type: str
        self.lang = lang  # type: str
        self.num_frames = num_frames  # type: str
        self.sample_fmt = sample_fmt  # type: str
        self.sample_rate = sample_rate  # type: str
        self.start_time = start_time  # type: str
        self.timebase = timebase  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMezzanineInfoResponseBodyMezzanineAudioStreamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.index is not None:
            result['Index'] = self.index
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        return self


class GetMezzanineInfoResponseBodyMezzanineVideoStreamList(TeaModel):
    def __init__(self, avg_fps=None, bitrate=None, codec_long_name=None, codec_name=None, codec_tag=None,
                 codec_tag_string=None, codec_time_base=None, dar=None, duration=None, fps=None, hdrtype=None, has_bframes=None,
                 height=None, index=None, lang=None, level=None, num_frames=None, pix_fmt=None, profile=None, rotate=None,
                 sar=None, start_time=None, timebase=None, width=None):
        self.avg_fps = avg_fps  # type: str
        self.bitrate = bitrate  # type: str
        self.codec_long_name = codec_long_name  # type: str
        self.codec_name = codec_name  # type: str
        self.codec_tag = codec_tag  # type: str
        self.codec_tag_string = codec_tag_string  # type: str
        self.codec_time_base = codec_time_base  # type: str
        self.dar = dar  # type: str
        self.duration = duration  # type: str
        self.fps = fps  # type: str
        self.hdrtype = hdrtype  # type: str
        self.has_bframes = has_bframes  # type: str
        self.height = height  # type: str
        self.index = index  # type: str
        self.lang = lang  # type: str
        self.level = level  # type: str
        self.num_frames = num_frames  # type: str
        self.pix_fmt = pix_fmt  # type: str
        self.profile = profile  # type: str
        self.rotate = rotate  # type: str
        self.sar = sar  # type: str
        self.start_time = start_time  # type: str
        self.timebase = timebase  # type: str
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMezzanineInfoResponseBodyMezzanineVideoStreamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_fps is not None:
            result['AvgFPS'] = self.avg_fps
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.dar is not None:
            result['Dar'] = self.dar
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.hdrtype is not None:
            result['HDRType'] = self.hdrtype
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.height is not None:
            result['Height'] = self.height
        if self.index is not None:
            result['Index'] = self.index
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.level is not None:
            result['Level'] = self.level
        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames
        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.sar is not None:
            result['Sar'] = self.sar
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.timebase is not None:
            result['Timebase'] = self.timebase
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgFPS') is not None:
            self.avg_fps = m.get('AvgFPS')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('Dar') is not None:
            self.dar = m.get('Dar')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('HDRType') is not None:
            self.hdrtype = m.get('HDRType')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')
        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('Sar') is not None:
            self.sar = m.get('Sar')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetMezzanineInfoResponseBodyMezzanine(TeaModel):
    def __init__(self, audio_stream_list=None, bitrate=None, creation_time=None, duration=None, file_name=None,
                 file_url=None, fps=None, height=None, output_type=None, size=None, status=None, video_id=None,
                 video_stream_list=None, width=None):
        self.audio_stream_list = audio_stream_list  # type: list[GetMezzanineInfoResponseBodyMezzanineAudioStreamList]
        self.bitrate = bitrate  # type: str
        self.creation_time = creation_time  # type: str
        self.duration = duration  # type: str
        self.file_name = file_name  # type: str
        self.file_url = file_url  # type: str
        self.fps = fps  # type: str
        self.height = height  # type: long
        self.output_type = output_type  # type: str
        self.size = size  # type: long
        self.status = status  # type: str
        self.video_id = video_id  # type: str
        self.video_stream_list = video_stream_list  # type: list[GetMezzanineInfoResponseBodyMezzanineVideoStreamList]
        self.width = width  # type: long

    def validate(self):
        if self.audio_stream_list:
            for k in self.audio_stream_list:
                if k:
                    k.validate()
        if self.video_stream_list:
            for k in self.video_stream_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetMezzanineInfoResponseBodyMezzanine, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AudioStreamList'] = []
        if self.audio_stream_list is not None:
            for k in self.audio_stream_list:
                result['AudioStreamList'].append(k.to_map() if k else None)
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.height is not None:
            result['Height'] = self.height
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        result['VideoStreamList'] = []
        if self.video_stream_list is not None:
            for k in self.video_stream_list:
                result['VideoStreamList'].append(k.to_map() if k else None)
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.audio_stream_list = []
        if m.get('AudioStreamList') is not None:
            for k in m.get('AudioStreamList'):
                temp_model = GetMezzanineInfoResponseBodyMezzanineAudioStreamList()
                self.audio_stream_list.append(temp_model.from_map(k))
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        self.video_stream_list = []
        if m.get('VideoStreamList') is not None:
            for k in m.get('VideoStreamList'):
                temp_model = GetMezzanineInfoResponseBodyMezzanineVideoStreamList()
                self.video_stream_list.append(temp_model.from_map(k))
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetMezzanineInfoResponseBody(TeaModel):
    def __init__(self, mezzanine=None, request_id=None):
        self.mezzanine = mezzanine  # type: GetMezzanineInfoResponseBodyMezzanine
        self.request_id = request_id  # type: str

    def validate(self):
        if self.mezzanine:
            self.mezzanine.validate()

    def to_map(self):
        _map = super(GetMezzanineInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mezzanine is not None:
            result['Mezzanine'] = self.mezzanine.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mezzanine') is not None:
            temp_model = GetMezzanineInfoResponseBodyMezzanine()
            self.mezzanine = temp_model.from_map(m['Mezzanine'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMezzanineInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMezzanineInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMezzanineInfoResponse, self).to_map()
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
            temp_model = GetMezzanineInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPlayInfoRequest(TeaModel):
    def __init__(self, addition_type=None, auth_timeout=None, definition=None, formats=None, output_type=None,
                 play_config=None, re_auth_info=None, result_type=None, stream_type=None, video_id=None):
        self.addition_type = addition_type  # type: str
        self.auth_timeout = auth_timeout  # type: long
        self.definition = definition  # type: str
        self.formats = formats  # type: str
        self.output_type = output_type  # type: str
        self.play_config = play_config  # type: str
        self.re_auth_info = re_auth_info  # type: str
        self.result_type = result_type  # type: str
        self.stream_type = stream_type  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPlayInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.formats is not None:
            result['Formats'] = self.formats
        if self.output_type is not None:
            result['OutputType'] = self.output_type
        if self.play_config is not None:
            result['PlayConfig'] = self.play_config
        if self.re_auth_info is not None:
            result['ReAuthInfo'] = self.re_auth_info
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Formats') is not None:
            self.formats = m.get('Formats')
        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')
        if m.get('PlayConfig') is not None:
            self.play_config = m.get('PlayConfig')
        if m.get('ReAuthInfo') is not None:
            self.re_auth_info = m.get('ReAuthInfo')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetPlayInfoResponseBodyPlayInfoListPlayInfo(TeaModel):
    def __init__(self, bit_depth=None, bitrate=None, creation_time=None, definition=None, duration=None,
                 encrypt=None, encrypt_type=None, format=None, fps=None, hdrtype=None, height=None, job_id=None,
                 modification_time=None, narrow_band_type=None, play_url=None, size=None, specification=None, status=None,
                 stream_type=None, watermark_id=None, width=None):
        self.bit_depth = bit_depth  # type: int
        self.bitrate = bitrate  # type: str
        self.creation_time = creation_time  # type: str
        self.definition = definition  # type: str
        self.duration = duration  # type: str
        self.encrypt = encrypt  # type: long
        self.encrypt_type = encrypt_type  # type: str
        self.format = format  # type: str
        self.fps = fps  # type: str
        self.hdrtype = hdrtype  # type: str
        self.height = height  # type: long
        self.job_id = job_id  # type: str
        self.modification_time = modification_time  # type: str
        self.narrow_band_type = narrow_band_type  # type: str
        self.play_url = play_url  # type: str
        self.size = size  # type: long
        self.specification = specification  # type: str
        self.status = status  # type: str
        self.stream_type = stream_type  # type: str
        self.watermark_id = watermark_id  # type: str
        self.width = width  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPlayInfoResponseBodyPlayInfoListPlayInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_depth is not None:
            result['BitDepth'] = self.bit_depth
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.encrypt is not None:
            result['Encrypt'] = self.encrypt
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.format is not None:
            result['Format'] = self.format
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.hdrtype is not None:
            result['HDRType'] = self.hdrtype
        if self.height is not None:
            result['Height'] = self.height
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.narrow_band_type is not None:
            result['NarrowBandType'] = self.narrow_band_type
        if self.play_url is not None:
            result['PlayURL'] = self.play_url
        if self.size is not None:
            result['Size'] = self.size
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitDepth') is not None:
            self.bit_depth = m.get('BitDepth')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Encrypt') is not None:
            self.encrypt = m.get('Encrypt')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('HDRType') is not None:
            self.hdrtype = m.get('HDRType')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('NarrowBandType') is not None:
            self.narrow_band_type = m.get('NarrowBandType')
        if m.get('PlayURL') is not None:
            self.play_url = m.get('PlayURL')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
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
        _map = super(GetPlayInfoResponseBodyPlayInfoList, self).to_map()
        if _map is not None:
            return _map

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


class GetPlayInfoResponseBodyVideoBase(TeaModel):
    def __init__(self, cover_url=None, creation_time=None, dan_mu_url=None, duration=None, media_type=None,
                 status=None, title=None, video_id=None):
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.dan_mu_url = dan_mu_url  # type: str
        self.duration = duration  # type: str
        self.media_type = media_type  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPlayInfoResponseBodyVideoBase, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dan_mu_url is not None:
            result['DanMuURL'] = self.dan_mu_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DanMuURL') is not None:
            self.dan_mu_url = m.get('DanMuURL')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetPlayInfoResponseBody(TeaModel):
    def __init__(self, play_info_list=None, request_id=None, video_base=None):
        self.play_info_list = play_info_list  # type: GetPlayInfoResponseBodyPlayInfoList
        self.request_id = request_id  # type: str
        self.video_base = video_base  # type: GetPlayInfoResponseBodyVideoBase

    def validate(self):
        if self.play_info_list:
            self.play_info_list.validate()
        if self.video_base:
            self.video_base.validate()

    def to_map(self):
        _map = super(GetPlayInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.play_info_list is not None:
            result['PlayInfoList'] = self.play_info_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.video_base is not None:
            result['VideoBase'] = self.video_base.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlayInfoList') is not None:
            temp_model = GetPlayInfoResponseBodyPlayInfoList()
            self.play_info_list = temp_model.from_map(m['PlayInfoList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VideoBase') is not None:
            temp_model = GetPlayInfoResponseBodyVideoBase()
            self.video_base = temp_model.from_map(m['VideoBase'])
        return self


class GetPlayInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPlayInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPlayInfoResponse, self).to_map()
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
            temp_model = GetPlayInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranscodeSummaryRequest(TeaModel):
    def __init__(self, video_ids=None):
        self.video_ids = video_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranscodeSummaryRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, bitrate=None, complete_time=None, creation_time=None, duration=None, error_code=None,
                 error_message=None, filesize=None, format=None, fps=None, height=None, transcode_job_status=None,
                 transcode_progress=None, transcode_template_id=None, watermark_id_list=None, width=None):
        self.bitrate = bitrate  # type: str
        self.complete_time = complete_time  # type: str
        self.creation_time = creation_time  # type: str
        self.duration = duration  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.filesize = filesize  # type: long
        self.format = format  # type: str
        self.fps = fps  # type: str
        self.height = height  # type: str
        self.transcode_job_status = transcode_job_status  # type: str
        self.transcode_progress = transcode_progress  # type: long
        self.transcode_template_id = transcode_template_id  # type: str
        self.watermark_id_list = watermark_id_list  # type: list[str]
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranscodeSummaryResponseBodyTranscodeSummaryListTranscodeJobInfoSummaryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.format is not None:
            result['Format'] = self.format
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.height is not None:
            result['Height'] = self.height
        if self.transcode_job_status is not None:
            result['TranscodeJobStatus'] = self.transcode_job_status
        if self.transcode_progress is not None:
            result['TranscodeProgress'] = self.transcode_progress
        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id
        if self.watermark_id_list is not None:
            result['WatermarkIdList'] = self.watermark_id_list
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('TranscodeJobStatus') is not None:
            self.transcode_job_status = m.get('TranscodeJobStatus')
        if m.get('TranscodeProgress') is not None:
            self.transcode_progress = m.get('TranscodeProgress')
        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')
        if m.get('WatermarkIdList') is not None:
            self.watermark_id_list = m.get('WatermarkIdList')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetTranscodeSummaryResponseBodyTranscodeSummaryList(TeaModel):
    def __init__(self, complete_time=None, creation_time=None, transcode_job_info_summary_list=None,
                 transcode_status=None, transcode_template_group_id=None, video_id=None):
        self.complete_time = complete_time  # type: str
        self.creation_time = creation_time  # type: str
        self.transcode_job_info_summary_list = transcode_job_info_summary_list  # type: list[GetTranscodeSummaryResponseBodyTranscodeSummaryListTranscodeJobInfoSummaryList]
        self.transcode_status = transcode_status  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        if self.transcode_job_info_summary_list:
            for k in self.transcode_job_info_summary_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTranscodeSummaryResponseBodyTranscodeSummaryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        result['TranscodeJobInfoSummaryList'] = []
        if self.transcode_job_info_summary_list is not None:
            for k in self.transcode_job_info_summary_list:
                result['TranscodeJobInfoSummaryList'].append(k.to_map() if k else None)
        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        self.transcode_job_info_summary_list = []
        if m.get('TranscodeJobInfoSummaryList') is not None:
            for k in m.get('TranscodeJobInfoSummaryList'):
                temp_model = GetTranscodeSummaryResponseBodyTranscodeSummaryListTranscodeJobInfoSummaryList()
                self.transcode_job_info_summary_list.append(temp_model.from_map(k))
        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetTranscodeSummaryResponseBody(TeaModel):
    def __init__(self, non_exist_video_ids=None, request_id=None, transcode_summary_list=None):
        self.non_exist_video_ids = non_exist_video_ids  # type: list[str]
        self.request_id = request_id  # type: str
        self.transcode_summary_list = transcode_summary_list  # type: list[GetTranscodeSummaryResponseBodyTranscodeSummaryList]

    def validate(self):
        if self.transcode_summary_list:
            for k in self.transcode_summary_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTranscodeSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TranscodeSummaryList'] = []
        if self.transcode_summary_list is not None:
            for k in self.transcode_summary_list:
                result['TranscodeSummaryList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.transcode_summary_list = []
        if m.get('TranscodeSummaryList') is not None:
            for k in m.get('TranscodeSummaryList'):
                temp_model = GetTranscodeSummaryResponseBodyTranscodeSummaryList()
                self.transcode_summary_list.append(temp_model.from_map(k))
        return self


class GetTranscodeSummaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTranscodeSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTranscodeSummaryResponse, self).to_map()
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
            temp_model = GetTranscodeSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranscodeTaskRequest(TeaModel):
    def __init__(self, transcode_task_id=None):
        self.transcode_task_id = transcode_task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranscodeTaskRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, audio_stream_list=None, bitrate=None, duration=None, encryption=None, filesize=None,
                 format=None, fps=None, height=None, output_file_url=None, subtitle_stream_list=None,
                 video_stream_list=None, watermark_id_list=None, width=None):
        self.audio_stream_list = audio_stream_list  # type: str
        self.bitrate = bitrate  # type: str
        self.duration = duration  # type: str
        self.encryption = encryption  # type: str
        self.filesize = filesize  # type: long
        self.format = format  # type: str
        self.fps = fps  # type: str
        self.height = height  # type: str
        self.output_file_url = output_file_url  # type: str
        self.subtitle_stream_list = subtitle_stream_list  # type: str
        self.video_stream_list = video_stream_list  # type: str
        self.watermark_id_list = watermark_id_list  # type: list[str]
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoListOutputFile, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_stream_list is not None:
            result['AudioStreamList'] = self.audio_stream_list
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.filesize is not None:
            result['Filesize'] = self.filesize
        if self.format is not None:
            result['Format'] = self.format
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.height is not None:
            result['Height'] = self.height
        if self.output_file_url is not None:
            result['OutputFileUrl'] = self.output_file_url
        if self.subtitle_stream_list is not None:
            result['SubtitleStreamList'] = self.subtitle_stream_list
        if self.video_stream_list is not None:
            result['VideoStreamList'] = self.video_stream_list
        if self.watermark_id_list is not None:
            result['WatermarkIdList'] = self.watermark_id_list
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AudioStreamList') is not None:
            self.audio_stream_list = m.get('AudioStreamList')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('OutputFileUrl') is not None:
            self.output_file_url = m.get('OutputFileUrl')
        if m.get('SubtitleStreamList') is not None:
            self.subtitle_stream_list = m.get('SubtitleStreamList')
        if m.get('VideoStreamList') is not None:
            self.video_stream_list = m.get('VideoStreamList')
        if m.get('WatermarkIdList') is not None:
            self.watermark_id_list = m.get('WatermarkIdList')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList(TeaModel):
    def __init__(self, complete_time=None, creation_time=None, definition=None, error_code=None, error_message=None,
                 input_file_url=None, output_file=None, priority=None, transcode_job_id=None, transcode_job_status=None,
                 transcode_progress=None, transcode_template_id=None):
        self.complete_time = complete_time  # type: str
        self.creation_time = creation_time  # type: str
        self.definition = definition  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.input_file_url = input_file_url  # type: str
        self.output_file = output_file  # type: GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoListOutputFile
        self.priority = priority  # type: str
        self.transcode_job_id = transcode_job_id  # type: str
        self.transcode_job_status = transcode_job_status  # type: str
        self.transcode_progress = transcode_progress  # type: long
        self.transcode_template_id = transcode_template_id  # type: str

    def validate(self):
        if self.output_file:
            self.output_file.validate()

    def to_map(self):
        _map = super(GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url
        if self.output_file is not None:
            result['OutputFile'] = self.output_file.to_map()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.transcode_job_id is not None:
            result['TranscodeJobId'] = self.transcode_job_id
        if self.transcode_job_status is not None:
            result['TranscodeJobStatus'] = self.transcode_job_status
        if self.transcode_progress is not None:
            result['TranscodeProgress'] = self.transcode_progress
        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')
        if m.get('OutputFile') is not None:
            temp_model = GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoListOutputFile()
            self.output_file = temp_model.from_map(m['OutputFile'])
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('TranscodeJobId') is not None:
            self.transcode_job_id = m.get('TranscodeJobId')
        if m.get('TranscodeJobStatus') is not None:
            self.transcode_job_status = m.get('TranscodeJobStatus')
        if m.get('TranscodeProgress') is not None:
            self.transcode_progress = m.get('TranscodeProgress')
        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')
        return self


class GetTranscodeTaskResponseBodyTranscodeTask(TeaModel):
    def __init__(self, complete_time=None, creation_time=None, task_status=None, transcode_job_info_list=None,
                 transcode_task_id=None, transcode_template_group_id=None, trigger=None, video_id=None):
        self.complete_time = complete_time  # type: str
        self.creation_time = creation_time  # type: str
        self.task_status = task_status  # type: str
        self.transcode_job_info_list = transcode_job_info_list  # type: list[GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList]
        self.transcode_task_id = transcode_task_id  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str
        self.trigger = trigger  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        if self.transcode_job_info_list:
            for k in self.transcode_job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTranscodeTaskResponseBodyTranscodeTask, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        result['TranscodeJobInfoList'] = []
        if self.transcode_job_info_list is not None:
            for k in self.transcode_job_info_list:
                result['TranscodeJobInfoList'].append(k.to_map() if k else None)
        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        self.transcode_job_info_list = []
        if m.get('TranscodeJobInfoList') is not None:
            for k in m.get('TranscodeJobInfoList'):
                temp_model = GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList()
                self.transcode_job_info_list.append(temp_model.from_map(k))
        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetTranscodeTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_task=None):
        self.request_id = request_id  # type: str
        self.transcode_task = transcode_task  # type: GetTranscodeTaskResponseBodyTranscodeTask

    def validate(self):
        if self.transcode_task:
            self.transcode_task.validate()

    def to_map(self):
        _map = super(GetTranscodeTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTranscodeTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTranscodeTaskResponse, self).to_map()
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
            temp_model = GetTranscodeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, transcode_template_group_id=None):
        self.transcode_template_group_id = transcode_template_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranscodeTemplateGroupRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, audio=None, clip=None, container=None, definition=None, encrypt_setting=None, mux_config=None,
                 package_setting=None, rotate=None, subtitle_list=None, template_name=None, trans_config=None,
                 transcode_file_regular=None, transcode_template_id=None, type=None, video=None, watermark_ids=None):
        self.audio = audio  # type: str
        self.clip = clip  # type: str
        self.container = container  # type: str
        self.definition = definition  # type: str
        self.encrypt_setting = encrypt_setting  # type: str
        self.mux_config = mux_config  # type: str
        self.package_setting = package_setting  # type: str
        self.rotate = rotate  # type: str
        self.subtitle_list = subtitle_list  # type: str
        self.template_name = template_name  # type: str
        self.trans_config = trans_config  # type: str
        self.transcode_file_regular = transcode_file_regular  # type: str
        self.transcode_template_id = transcode_template_id  # type: str
        self.type = type  # type: str
        self.video = video  # type: str
        self.watermark_ids = watermark_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupTranscodeTemplateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio is not None:
            result['Audio'] = self.audio
        if self.clip is not None:
            result['Clip'] = self.clip
        if self.container is not None:
            result['Container'] = self.container
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.encrypt_setting is not None:
            result['EncryptSetting'] = self.encrypt_setting
        if self.mux_config is not None:
            result['MuxConfig'] = self.mux_config
        if self.package_setting is not None:
            result['PackageSetting'] = self.package_setting
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.subtitle_list is not None:
            result['SubtitleList'] = self.subtitle_list
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trans_config is not None:
            result['TransConfig'] = self.trans_config
        if self.transcode_file_regular is not None:
            result['TranscodeFileRegular'] = self.transcode_file_regular
        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id
        if self.type is not None:
            result['Type'] = self.type
        if self.video is not None:
            result['Video'] = self.video
        if self.watermark_ids is not None:
            result['WatermarkIds'] = self.watermark_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')
        if m.get('Clip') is not None:
            self.clip = m.get('Clip')
        if m.get('Container') is not None:
            self.container = m.get('Container')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('EncryptSetting') is not None:
            self.encrypt_setting = m.get('EncryptSetting')
        if m.get('MuxConfig') is not None:
            self.mux_config = m.get('MuxConfig')
        if m.get('PackageSetting') is not None:
            self.package_setting = m.get('PackageSetting')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('SubtitleList') is not None:
            self.subtitle_list = m.get('SubtitleList')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TransConfig') is not None:
            self.trans_config = m.get('TransConfig')
        if m.get('TranscodeFileRegular') is not None:
            self.transcode_file_regular = m.get('TranscodeFileRegular')
        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Video') is not None:
            self.video = m.get('Video')
        if m.get('WatermarkIds') is not None:
            self.watermark_ids = m.get('WatermarkIds')
        return self


class GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroup(TeaModel):
    def __init__(self, app_id=None, creation_time=None, is_default=None, locked=None, modify_time=None, name=None,
                 transcode_template_group_id=None, transcode_template_list=None):
        self.app_id = app_id  # type: str
        self.creation_time = creation_time  # type: str
        self.is_default = is_default  # type: str
        self.locked = locked  # type: str
        self.modify_time = modify_time  # type: str
        self.name = name  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str
        self.transcode_template_list = transcode_template_list  # type: list[GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupTranscodeTemplateList]

    def validate(self):
        if self.transcode_template_list:
            for k in self.transcode_template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        result['TranscodeTemplateList'] = []
        if self.transcode_template_list is not None:
            for k in self.transcode_template_list:
                result['TranscodeTemplateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        self.transcode_template_list = []
        if m.get('TranscodeTemplateList') is not None:
            for k in m.get('TranscodeTemplateList'):
                temp_model = GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupTranscodeTemplateList()
                self.transcode_template_list.append(temp_model.from_map(k))
        return self


class GetTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_template_group=None):
        self.request_id = request_id  # type: str
        self.transcode_template_group = transcode_template_group  # type: GetTranscodeTemplateGroupResponseBodyTranscodeTemplateGroup

    def validate(self):
        if self.transcode_template_group:
            self.transcode_template_group.validate()

    def to_map(self):
        _map = super(GetTranscodeTemplateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTranscodeTemplateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTranscodeTemplateGroupResponse, self).to_map()
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
            temp_model = GetTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetURLUploadInfosRequest(TeaModel):
    def __init__(self, job_ids=None, upload_urls=None):
        self.job_ids = job_ids  # type: str
        self.upload_urls = upload_urls  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetURLUploadInfosRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, complete_time=None, creation_time=None, error_code=None, error_message=None, file_size=None,
                 job_id=None, media_id=None, status=None, upload_url=None, user_data=None):
        self.complete_time = complete_time  # type: str
        self.creation_time = creation_time  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.file_size = file_size  # type: str
        self.job_id = job_id  # type: str
        self.media_id = media_id  # type: str
        self.status = status  # type: str
        self.upload_url = upload_url  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetURLUploadInfosResponseBodyURLUploadInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.status is not None:
            result['Status'] = self.status
        if self.upload_url is not None:
            result['UploadURL'] = self.upload_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UploadURL') is not None:
            self.upload_url = m.get('UploadURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class GetURLUploadInfosResponseBody(TeaModel):
    def __init__(self, non_exists=None, request_id=None, urlupload_info_list=None):
        self.non_exists = non_exists  # type: list[str]
        self.request_id = request_id  # type: str
        self.urlupload_info_list = urlupload_info_list  # type: list[GetURLUploadInfosResponseBodyURLUploadInfoList]

    def validate(self):
        if self.urlupload_info_list:
            for k in self.urlupload_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetURLUploadInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_exists is not None:
            result['NonExists'] = self.non_exists
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['URLUploadInfoList'] = []
        if self.urlupload_info_list is not None:
            for k in self.urlupload_info_list:
                result['URLUploadInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExists') is not None:
            self.non_exists = m.get('NonExists')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.urlupload_info_list = []
        if m.get('URLUploadInfoList') is not None:
            for k in m.get('URLUploadInfoList'):
                temp_model = GetURLUploadInfosResponseBodyURLUploadInfoList()
                self.urlupload_info_list.append(temp_model.from_map(k))
        return self


class GetURLUploadInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetURLUploadInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetURLUploadInfosResponse, self).to_map()
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
            temp_model = GetURLUploadInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadDetailsRequest(TeaModel):
    def __init__(self, media_ids=None, media_type=None):
        self.media_ids = media_ids  # type: str
        self.media_type = media_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUploadDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        return self


class GetUploadDetailsResponseBodyUploadDetails(TeaModel):
    def __init__(self, completion_time=None, creation_time=None, device_model=None, file_size=None, media_id=None,
                 modification_time=None, status=None, title=None, upload_ip=None, upload_ratio=None, upload_size=None,
                 upload_source=None, upload_status=None):
        self.completion_time = completion_time  # type: str
        self.creation_time = creation_time  # type: str
        self.device_model = device_model  # type: str
        self.file_size = file_size  # type: long
        self.media_id = media_id  # type: str
        self.modification_time = modification_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str
        self.upload_ip = upload_ip  # type: str
        self.upload_ratio = upload_ratio  # type: float
        self.upload_size = upload_size  # type: long
        self.upload_source = upload_source  # type: str
        self.upload_status = upload_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUploadDetailsResponseBodyUploadDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.upload_ip is not None:
            result['UploadIP'] = self.upload_ip
        if self.upload_ratio is not None:
            result['UploadRatio'] = self.upload_ratio
        if self.upload_size is not None:
            result['UploadSize'] = self.upload_size
        if self.upload_source is not None:
            result['UploadSource'] = self.upload_source
        if self.upload_status is not None:
            result['UploadStatus'] = self.upload_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UploadIP') is not None:
            self.upload_ip = m.get('UploadIP')
        if m.get('UploadRatio') is not None:
            self.upload_ratio = m.get('UploadRatio')
        if m.get('UploadSize') is not None:
            self.upload_size = m.get('UploadSize')
        if m.get('UploadSource') is not None:
            self.upload_source = m.get('UploadSource')
        if m.get('UploadStatus') is not None:
            self.upload_status = m.get('UploadStatus')
        return self


class GetUploadDetailsResponseBody(TeaModel):
    def __init__(self, forbidden_media_ids=None, non_exist_media_ids=None, request_id=None, upload_details=None):
        self.forbidden_media_ids = forbidden_media_ids  # type: list[str]
        self.non_exist_media_ids = non_exist_media_ids  # type: list[str]
        self.request_id = request_id  # type: str
        self.upload_details = upload_details  # type: list[GetUploadDetailsResponseBodyUploadDetails]

    def validate(self):
        if self.upload_details:
            for k in self.upload_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUploadDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forbidden_media_ids is not None:
            result['ForbiddenMediaIds'] = self.forbidden_media_ids
        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UploadDetails'] = []
        if self.upload_details is not None:
            for k in self.upload_details:
                result['UploadDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForbiddenMediaIds') is not None:
            self.forbidden_media_ids = m.get('ForbiddenMediaIds')
        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.upload_details = []
        if m.get('UploadDetails') is not None:
            for k in m.get('UploadDetails'):
                temp_model = GetUploadDetailsResponseBodyUploadDetails()
                self.upload_details.append(temp_model.from_map(k))
        return self


class GetUploadDetailsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUploadDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUploadDetailsResponse, self).to_map()
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
            temp_model = GetUploadDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoInfoRequest(TeaModel):
    def __init__(self, video_id=None):
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetVideoInfoResponseBodyVideoSnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoInfoResponseBodyVideoSnapshots, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, app_id=None, audit_status=None, cate_id=None, cate_name=None, cover_url=None,
                 creation_time=None, custom_media_info=None, description=None, duration=None, modification_time=None,
                 region_id=None, size=None, snapshots=None, status=None, storage_location=None, tags=None,
                 template_group_id=None, title=None, video_id=None):
        self.app_id = app_id  # type: str
        self.audit_status = audit_status  # type: str
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.custom_media_info = custom_media_info  # type: str
        self.description = description  # type: str
        self.duration = duration  # type: float
        self.modification_time = modification_time  # type: str
        self.region_id = region_id  # type: str
        self.size = size  # type: long
        self.snapshots = snapshots  # type: GetVideoInfoResponseBodyVideoSnapshots
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.template_group_id = template_group_id  # type: str
        self.title = title  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super(GetVideoInfoResponseBodyVideo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.custom_media_info is not None:
            result['CustomMediaInfo'] = self.custom_media_info
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.title is not None:
            result['Title'] = self.title
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CustomMediaInfo') is not None:
            self.custom_media_info = m.get('CustomMediaInfo')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Snapshots') is not None:
            temp_model = GetVideoInfoResponseBodyVideoSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetVideoInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, video=None):
        self.request_id = request_id  # type: str
        self.video = video  # type: GetVideoInfoResponseBodyVideo

    def validate(self):
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super(GetVideoInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVideoInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoInfoResponse, self).to_map()
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
            temp_model = GetVideoInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoInfosRequest(TeaModel):
    def __init__(self, video_ids=None):
        self.video_ids = video_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')
        return self


class GetVideoInfosResponseBodyVideoList(TeaModel):
    def __init__(self, app_id=None, cate_id=None, cate_name=None, cover_url=None, creation_time=None,
                 description=None, duration=None, modification_time=None, size=None, snapshots=None, status=None,
                 storage_location=None, tags=None, template_group_id=None, title=None, video_id=None):
        self.app_id = app_id  # type: str
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.duration = duration  # type: float
        self.modification_time = modification_time  # type: str
        self.size = size  # type: long
        self.snapshots = snapshots  # type: list[str]
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.template_group_id = template_group_id  # type: str
        self.title = title  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoInfosResponseBodyVideoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.title is not None:
            result['Title'] = self.title
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetVideoInfosResponseBody(TeaModel):
    def __init__(self, non_exist_video_ids=None, request_id=None, video_list=None):
        self.non_exist_video_ids = non_exist_video_ids  # type: list[str]
        self.request_id = request_id  # type: str
        self.video_list = video_list  # type: list[GetVideoInfosResponseBodyVideoList]

    def validate(self):
        if self.video_list:
            for k in self.video_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVideoInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VideoList'] = []
        if self.video_list is not None:
            for k in self.video_list:
                result['VideoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.video_list = []
        if m.get('VideoList') is not None:
            for k in m.get('VideoList'):
                temp_model = GetVideoInfosResponseBodyVideoList()
                self.video_list.append(temp_model.from_map(k))
        return self


class GetVideoInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVideoInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoInfosResponse, self).to_map()
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
            temp_model = GetVideoInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoListRequest(TeaModel):
    def __init__(self, cate_id=None, end_time=None, page_no=None, page_size=None, sort_by=None, start_time=None,
                 status=None, storage_location=None):
        self.cate_id = cate_id  # type: long
        self.end_time = end_time  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        return self


class GetVideoListResponseBodyVideoListVideoSnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoListResponseBodyVideoListVideoSnapshots, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, app_id=None, cate_id=None, cate_name=None, cover_url=None, creation_time=None,
                 description=None, duration=None, modification_time=None, size=None, snapshots=None, status=None,
                 storage_location=None, tags=None, title=None, video_id=None):
        self.app_id = app_id  # type: str
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.duration = duration  # type: float
        self.modification_time = modification_time  # type: str
        self.size = size  # type: long
        self.snapshots = snapshots  # type: GetVideoListResponseBodyVideoListVideoSnapshots
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super(GetVideoListResponseBodyVideoListVideo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Snapshots') is not None:
            temp_model = GetVideoListResponseBodyVideoListVideoSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
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
        _map = super(GetVideoListResponseBodyVideoList, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str
        self.total = total  # type: int
        self.video_list = video_list  # type: GetVideoListResponseBodyVideoList

    def validate(self):
        if self.video_list:
            self.video_list.validate()

    def to_map(self):
        _map = super(GetVideoListResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVideoListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoListResponse, self).to_map()
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
            temp_model = GetVideoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoPlayAuthRequest(TeaModel):
    def __init__(self, api_version=None, auth_info_timeout=None, video_id=None):
        self.api_version = api_version  # type: str
        self.auth_info_timeout = auth_info_timeout  # type: long
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoPlayAuthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.auth_info_timeout is not None:
            result['AuthInfoTimeout'] = self.auth_info_timeout
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('AuthInfoTimeout') is not None:
            self.auth_info_timeout = m.get('AuthInfoTimeout')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetVideoPlayAuthResponseBodyVideoMeta(TeaModel):
    def __init__(self, cover_url=None, duration=None, status=None, title=None, video_id=None):
        self.cover_url = cover_url  # type: str
        self.duration = duration  # type: float
        self.status = status  # type: str
        self.title = title  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoPlayAuthResponseBodyVideoMeta, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class GetVideoPlayAuthResponseBody(TeaModel):
    def __init__(self, play_auth=None, request_id=None, video_meta=None):
        self.play_auth = play_auth  # type: str
        self.request_id = request_id  # type: str
        self.video_meta = video_meta  # type: GetVideoPlayAuthResponseBodyVideoMeta

    def validate(self):
        if self.video_meta:
            self.video_meta.validate()

    def to_map(self):
        _map = super(GetVideoPlayAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.play_auth is not None:
            result['PlayAuth'] = self.play_auth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.video_meta is not None:
            result['VideoMeta'] = self.video_meta.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlayAuth') is not None:
            self.play_auth = m.get('PlayAuth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VideoMeta') is not None:
            temp_model = GetVideoPlayAuthResponseBodyVideoMeta()
            self.video_meta = temp_model.from_map(m['VideoMeta'])
        return self


class GetVideoPlayAuthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVideoPlayAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoPlayAuthResponse, self).to_map()
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
            temp_model = GetVideoPlayAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVodTemplateRequest(TeaModel):
    def __init__(self, vod_template_id=None):
        self.vod_template_id = vod_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVodTemplateRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, creation_time=None, is_default=None, modify_time=None, name=None, template_config=None,
                 template_type=None, vod_template_id=None):
        self.creation_time = creation_time  # type: str
        self.is_default = is_default  # type: str
        self.modify_time = modify_time  # type: str
        self.name = name  # type: str
        self.template_config = template_config  # type: str
        self.template_type = template_type  # type: str
        self.vod_template_id = vod_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVodTemplateResponseBodyVodTemplateInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        return self


class GetVodTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, vod_template_info=None):
        self.request_id = request_id  # type: str
        self.vod_template_info = vod_template_info  # type: GetVodTemplateResponseBodyVodTemplateInfo

    def validate(self):
        if self.vod_template_info:
            self.vod_template_info.validate()

    def to_map(self):
        _map = super(GetVodTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVodTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVodTemplateResponse, self).to_map()
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
            temp_model = GetVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWatermarkRequest(TeaModel):
    def __init__(self, watermark_id=None):
        self.watermark_id = watermark_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, app_id=None, creation_time=None, file_url=None, is_default=None, name=None, type=None,
                 watermark_config=None, watermark_id=None):
        self.app_id = app_id  # type: str
        self.creation_time = creation_time  # type: str
        self.file_url = file_url  # type: str
        self.is_default = is_default  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.watermark_config = watermark_config  # type: str
        self.watermark_id = watermark_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWatermarkResponseBodyWatermarkInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class GetWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, watermark_info=None):
        self.request_id = request_id  # type: str
        self.watermark_info = watermark_info  # type: GetWatermarkResponseBodyWatermarkInfo

    def validate(self):
        if self.watermark_info:
            self.watermark_info.validate()

    def to_map(self):
        _map = super(GetWatermarkResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetWatermarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWatermarkResponse, self).to_map()
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
            temp_model = GetWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAIImageInfoRequest(TeaModel):
    def __init__(self, video_id=None):
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAIImageInfoRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, aiimage_info_id=None, creation_time=None, file_url=None, format=None, job_id=None, score=None,
                 version=None, video_id=None):
        self.aiimage_info_id = aiimage_info_id  # type: str
        self.creation_time = creation_time  # type: str
        self.file_url = file_url  # type: str
        self.format = format  # type: str
        self.job_id = job_id  # type: str
        self.score = score  # type: str
        self.version = version  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAIImageInfoResponseBodyAIImageInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aiimage_info_id is not None:
            result['AIImageInfoId'] = self.aiimage_info_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.format is not None:
            result['Format'] = self.format
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.score is not None:
            result['Score'] = self.score
        if self.version is not None:
            result['Version'] = self.version
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIImageInfoId') is not None:
            self.aiimage_info_id = m.get('AIImageInfoId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class ListAIImageInfoResponseBody(TeaModel):
    def __init__(self, aiimage_info_list=None, request_id=None):
        self.aiimage_info_list = aiimage_info_list  # type: list[ListAIImageInfoResponseBodyAIImageInfoList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.aiimage_info_list:
            for k in self.aiimage_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAIImageInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AIImageInfoList'] = []
        if self.aiimage_info_list is not None:
            for k in self.aiimage_info_list:
                result['AIImageInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.aiimage_info_list = []
        if m.get('AIImageInfoList') is not None:
            for k in m.get('AIImageInfoList'):
                temp_model = ListAIImageInfoResponseBodyAIImageInfoList()
                self.aiimage_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAIImageInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAIImageInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAIImageInfoResponse, self).to_map()
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
            temp_model = ListAIImageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAIJobRequest(TeaModel):
    def __init__(self, job_ids=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.job_ids = job_ids  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAIJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_ids is not None:
            result['JobIds'] = self.job_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListAIJobResponseBodyAIJobListAIJob(TeaModel):
    def __init__(self, code=None, complete_time=None, creation_time=None, data=None, job_id=None, media_id=None,
                 message=None, status=None, type=None):
        self.code = code  # type: str
        self.complete_time = complete_time  # type: str
        self.creation_time = creation_time  # type: str
        self.data = data  # type: str
        self.job_id = job_id  # type: str
        self.media_id = media_id  # type: str
        self.message = message  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAIJobResponseBodyAIJobListAIJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data is not None:
            result['Data'] = self.data
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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
        _map = super(ListAIJobResponseBodyAIJobList, self).to_map()
        if _map is not None:
            return _map

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


class ListAIJobResponseBodyNonExistAIJobIds(TeaModel):
    def __init__(self, string=None):
        self.string = string  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAIJobResponseBodyNonExistAIJobIds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class ListAIJobResponseBody(TeaModel):
    def __init__(self, aijob_list=None, non_exist_aijob_ids=None, request_id=None):
        self.aijob_list = aijob_list  # type: ListAIJobResponseBodyAIJobList
        self.non_exist_aijob_ids = non_exist_aijob_ids  # type: ListAIJobResponseBodyNonExistAIJobIds
        self.request_id = request_id  # type: str

    def validate(self):
        if self.aijob_list:
            self.aijob_list.validate()
        if self.non_exist_aijob_ids:
            self.non_exist_aijob_ids.validate()

    def to_map(self):
        _map = super(ListAIJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aijob_list is not None:
            result['AIJobList'] = self.aijob_list.to_map()
        if self.non_exist_aijob_ids is not None:
            result['NonExistAIJobIds'] = self.non_exist_aijob_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIJobList') is not None:
            temp_model = ListAIJobResponseBodyAIJobList()
            self.aijob_list = temp_model.from_map(m['AIJobList'])
        if m.get('NonExistAIJobIds') is not None:
            temp_model = ListAIJobResponseBodyNonExistAIJobIds()
            self.non_exist_aijob_ids = temp_model.from_map(m['NonExistAIJobIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAIJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAIJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAIJobResponse, self).to_map()
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
            temp_model = ListAIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAITemplateRequest(TeaModel):
    def __init__(self, template_type=None):
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAITemplateRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, creation_time=None, is_default=None, modify_time=None, source=None, template_config=None,
                 template_id=None, template_name=None, template_type=None):
        self.creation_time = creation_time  # type: str
        self.is_default = is_default  # type: str
        self.modify_time = modify_time  # type: str
        self.source = source  # type: str
        self.template_config = template_config  # type: str
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAITemplateResponseBodyTemplateInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.source is not None:
            result['Source'] = self.source
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_info_list=None):
        self.request_id = request_id  # type: str
        self.template_info_list = template_info_list  # type: list[ListAITemplateResponseBodyTemplateInfoList]

    def validate(self):
        if self.template_info_list:
            for k in self.template_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAITemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAITemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAITemplateResponse, self).to_map()
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
            temp_model = ListAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInfoRequest(TeaModel):
    def __init__(self, page_no=None, page_size=None, status=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInfoResponseBodyAppInfoList(TeaModel):
    def __init__(self, app_id=None, app_name=None, creation_time=None, description=None, modification_time=None,
                 status=None, type=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.modification_time = modification_time  # type: str
        self.status = status  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInfoResponseBodyAppInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAppInfoResponseBody(TeaModel):
    def __init__(self, app_info_list=None, request_id=None, total=None):
        self.app_info_list = app_info_list  # type: list[ListAppInfoResponseBodyAppInfoList]
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = ListAppInfoResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAppInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppInfoResponse, self).to_map()
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
            temp_model = ListAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppPoliciesForIdentityRequest(TeaModel):
    def __init__(self, app_id=None, identity_name=None, identity_type=None):
        self.app_id = app_id  # type: str
        self.identity_name = identity_name  # type: str
        self.identity_type = identity_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppPoliciesForIdentityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.identity_name is not None:
            result['IdentityName'] = self.identity_name
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IdentityName') is not None:
            self.identity_name = m.get('IdentityName')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        return self


class ListAppPoliciesForIdentityResponseBodyAppPolicyList(TeaModel):
    def __init__(self, app_id=None, creation_time=None, description=None, modification_time=None, policy_name=None,
                 policy_type=None, policy_value=None):
        self.app_id = app_id  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.modification_time = modification_time  # type: str
        self.policy_name = policy_name  # type: str
        self.policy_type = policy_type  # type: str
        self.policy_value = policy_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppPoliciesForIdentityResponseBodyAppPolicyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_value is not None:
            result['PolicyValue'] = self.policy_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyValue') is not None:
            self.policy_value = m.get('PolicyValue')
        return self


class ListAppPoliciesForIdentityResponseBody(TeaModel):
    def __init__(self, app_policy_list=None, request_id=None):
        self.app_policy_list = app_policy_list  # type: list[ListAppPoliciesForIdentityResponseBodyAppPolicyList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_policy_list:
            for k in self.app_policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppPoliciesForIdentityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppPolicyList'] = []
        if self.app_policy_list is not None:
            for k in self.app_policy_list:
                result['AppPolicyList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_policy_list = []
        if m.get('AppPolicyList') is not None:
            for k in m.get('AppPolicyList'):
                temp_model = ListAppPoliciesForIdentityResponseBodyAppPolicyList()
                self.app_policy_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppPoliciesForIdentityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppPoliciesForIdentityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppPoliciesForIdentityResponse, self).to_map()
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
            temp_model = ListAppPoliciesForIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuditSecurityIpRequest(TeaModel):
    def __init__(self, security_group_name=None):
        self.security_group_name = security_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuditSecurityIpRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, creation_time=None, ips=None, modification_time=None, security_group_name=None):
        self.creation_time = creation_time  # type: str
        self.ips = ips  # type: str
        self.modification_time = modification_time  # type: str
        self.security_group_name = security_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuditSecurityIpResponseBodySecurityIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class ListAuditSecurityIpResponseBody(TeaModel):
    def __init__(self, request_id=None, security_ip_list=None):
        self.request_id = request_id  # type: str
        self.security_ip_list = security_ip_list  # type: list[ListAuditSecurityIpResponseBodySecurityIpList]

    def validate(self):
        if self.security_ip_list:
            for k in self.security_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuditSecurityIpResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAuditSecurityIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuditSecurityIpResponse, self).to_map()
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
            temp_model = ListAuditSecurityIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDynamicImageRequest(TeaModel):
    def __init__(self, video_id=None):
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDynamicImageRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, creation_time=None, duration=None, dynamic_image_id=None, file_size=None, file_url=None,
                 format=None, fps=None, height=None, job_id=None, video_id=None, width=None):
        self.creation_time = creation_time  # type: str
        self.duration = duration  # type: str
        self.dynamic_image_id = dynamic_image_id  # type: str
        self.file_size = file_size  # type: str
        self.file_url = file_url  # type: str
        self.format = format  # type: str
        self.fps = fps  # type: str
        self.height = height  # type: str
        self.job_id = job_id  # type: str
        self.video_id = video_id  # type: str
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDynamicImageResponseBodyDynamicImageList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.dynamic_image_id is not None:
            result['DynamicImageId'] = self.dynamic_image_id
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.format is not None:
            result['Format'] = self.format
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.height is not None:
            result['Height'] = self.height
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DynamicImageId') is not None:
            self.dynamic_image_id = m.get('DynamicImageId')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ListDynamicImageResponseBody(TeaModel):
    def __init__(self, dynamic_image_list=None, request_id=None):
        self.dynamic_image_list = dynamic_image_list  # type: list[ListDynamicImageResponseBodyDynamicImageList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dynamic_image_list:
            for k in self.dynamic_image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDynamicImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DynamicImageList'] = []
        if self.dynamic_image_list is not None:
            for k in self.dynamic_image_list:
                result['DynamicImageList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dynamic_image_list = []
        if m.get('DynamicImageList') is not None:
            for k in m.get('DynamicImageList'):
                temp_model = ListDynamicImageResponseBodyDynamicImageList()
                self.dynamic_image_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDynamicImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDynamicImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDynamicImageResponse, self).to_map()
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
            temp_model = ListDynamicImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLiveRecordVideoRequest(TeaModel):
    def __init__(self, app_name=None, domain_name=None, end_time=None, page_no=None, page_size=None, sort_by=None,
                 start_time=None, stream_name=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.end_time = end_time  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLiveRecordVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots(TeaModel):
    def __init__(self, snapshot=None):
        self.snapshot = snapshot  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, cate_id=None, cate_name=None, cover_url=None, creation_time=None, description=None,
                 duration=None, modify_time=None, size=None, snapshots=None, status=None, tags=None, template_group_id=None,
                 title=None, video_id=None):
        self.cate_id = cate_id  # type: int
        self.cate_name = cate_name  # type: str
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.duration = duration  # type: float
        self.modify_time = modify_time  # type: str
        self.size = size  # type: long
        self.snapshots = snapshots  # type: ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots
        self.status = status  # type: str
        self.tags = tags  # type: str
        self.template_group_id = template_group_id  # type: str
        self.title = title  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super(ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.title is not None:
            result['Title'] = self.title
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Snapshots') is not None:
            temp_model = ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideoSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideo(TeaModel):
    def __init__(self, app_name=None, domain_name=None, playlist_id=None, record_end_time=None,
                 record_start_time=None, stream_name=None, video=None):
        self.app_name = app_name  # type: str
        self.domain_name = domain_name  # type: str
        self.playlist_id = playlist_id  # type: str
        self.record_end_time = record_end_time  # type: str
        self.record_start_time = record_start_time  # type: str
        self.stream_name = stream_name  # type: str
        self.video = video  # type: ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideo

    def validate(self):
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super(ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.playlist_id is not None:
            result['PlaylistId'] = self.playlist_id
        if self.record_end_time is not None:
            result['RecordEndTime'] = self.record_end_time
        if self.record_start_time is not None:
            result['RecordStartTime'] = self.record_start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PlaylistId') is not None:
            self.playlist_id = m.get('PlaylistId')
        if m.get('RecordEndTime') is not None:
            self.record_end_time = m.get('RecordEndTime')
        if m.get('RecordStartTime') is not None:
            self.record_start_time = m.get('RecordStartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('Video') is not None:
            temp_model = ListLiveRecordVideoResponseBodyLiveRecordVideoListLiveRecordVideoVideo()
            self.video = temp_model.from_map(m['Video'])
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
        _map = super(ListLiveRecordVideoResponseBodyLiveRecordVideoList, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, live_record_video_list=None, request_id=None, total=None):
        self.live_record_video_list = live_record_video_list  # type: ListLiveRecordVideoResponseBodyLiveRecordVideoList
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.live_record_video_list:
            self.live_record_video_list.validate()

    def to_map(self):
        _map = super(ListLiveRecordVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_record_video_list is not None:
            result['LiveRecordVideoList'] = self.live_record_video_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveRecordVideoList') is not None:
            temp_model = ListLiveRecordVideoResponseBodyLiveRecordVideoList()
            self.live_record_video_list = temp_model.from_map(m['LiveRecordVideoList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListLiveRecordVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLiveRecordVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLiveRecordVideoResponse, self).to_map()
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
            temp_model = ListLiveRecordVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotsRequest(TeaModel):
    def __init__(self, auth_timeout=None, page_no=None, page_size=None, snapshot_type=None, video_id=None):
        self.auth_timeout = auth_timeout  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.snapshot_type = snapshot_type  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class ListSnapshotsResponseBodyMediaSnapshotSnapshotsSnapshot(TeaModel):
    def __init__(self, index=None, url=None):
        self.index = index  # type: long
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSnapshotsResponseBodyMediaSnapshotSnapshotsSnapshot, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(ListSnapshotsResponseBodyMediaSnapshotSnapshots, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, creation_time=None, job_id=None, regular=None, snapshots=None, total=None):
        self.creation_time = creation_time  # type: str
        self.job_id = job_id  # type: str
        self.regular = regular  # type: str
        self.snapshots = snapshots  # type: ListSnapshotsResponseBodyMediaSnapshotSnapshots
        self.total = total  # type: long

    def validate(self):
        if self.snapshots:
            self.snapshots.validate()

    def to_map(self):
        _map = super(ListSnapshotsResponseBodyMediaSnapshot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.regular is not None:
            result['Regular'] = self.regular
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Regular') is not None:
            self.regular = m.get('Regular')
        if m.get('Snapshots') is not None:
            temp_model = ListSnapshotsResponseBodyMediaSnapshotSnapshots()
            self.snapshots = temp_model.from_map(m['Snapshots'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSnapshotsResponseBody(TeaModel):
    def __init__(self, media_snapshot=None, request_id=None):
        self.media_snapshot = media_snapshot  # type: ListSnapshotsResponseBodyMediaSnapshot
        self.request_id = request_id  # type: str

    def validate(self):
        if self.media_snapshot:
            self.media_snapshot.validate()

    def to_map(self):
        _map = super(ListSnapshotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_snapshot is not None:
            result['MediaSnapshot'] = self.media_snapshot.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaSnapshot') is not None:
            temp_model = ListSnapshotsResponseBodyMediaSnapshot()
            self.media_snapshot = temp_model.from_map(m['MediaSnapshot'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSnapshotsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSnapshotsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSnapshotsResponse, self).to_map()
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
            temp_model = ListSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTranscodeTaskRequest(TeaModel):
    def __init__(self, end_time=None, page_no=None, page_size=None, start_time=None, video_id=None):
        self.end_time = end_time  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.start_time = start_time  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTranscodeTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class ListTranscodeTaskResponseBodyTranscodeTaskList(TeaModel):
    def __init__(self, complete_time=None, creation_time=None, task_status=None, transcode_task_id=None,
                 transcode_template_group_id=None, trigger=None, video_id=None):
        self.complete_time = complete_time  # type: str
        self.creation_time = creation_time  # type: str
        self.task_status = task_status  # type: str
        self.transcode_task_id = transcode_task_id  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str
        self.trigger = trigger  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTranscodeTaskResponseBodyTranscodeTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class ListTranscodeTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_task_list=None):
        self.request_id = request_id  # type: str
        self.transcode_task_list = transcode_task_list  # type: list[ListTranscodeTaskResponseBodyTranscodeTaskList]

    def validate(self):
        if self.transcode_task_list:
            for k in self.transcode_task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTranscodeTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTranscodeTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTranscodeTaskResponse, self).to_map()
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
            temp_model = ListTranscodeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTranscodeTemplateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupList(TeaModel):
    def __init__(self, app_id=None, creation_time=None, is_default=None, locked=None, modify_time=None, name=None,
                 transcode_template_group_id=None):
        self.app_id = app_id  # type: str
        self.creation_time = creation_time  # type: str
        self.is_default = is_default  # type: str
        self.locked = locked  # type: str
        self.modify_time = modify_time  # type: str
        self.name = name  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        return self


class ListTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_template_group_list=None):
        self.request_id = request_id  # type: str
        self.transcode_template_group_list = transcode_template_group_list  # type: list[ListTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupList]

    def validate(self):
        if self.transcode_template_group_list:
            for k in self.transcode_template_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTranscodeTemplateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTranscodeTemplateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTranscodeTemplateGroupResponse, self).to_map()
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
            temp_model = ListTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVodTemplateRequest(TeaModel):
    def __init__(self, app_id=None, template_type=None):
        self.app_id = app_id  # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVodTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListVodTemplateResponseBodyVodTemplateInfoList(TeaModel):
    def __init__(self, app_id=None, creation_time=None, is_default=None, modify_time=None, name=None,
                 template_config=None, template_type=None, vod_template_id=None):
        self.app_id = app_id  # type: str
        self.creation_time = creation_time  # type: str
        self.is_default = is_default  # type: str
        self.modify_time = modify_time  # type: str
        self.name = name  # type: str
        self.template_config = template_config  # type: str
        self.template_type = template_type  # type: str
        self.vod_template_id = vod_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVodTemplateResponseBodyVodTemplateInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        return self


class ListVodTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, vod_template_info_list=None):
        self.request_id = request_id  # type: str
        self.vod_template_info_list = vod_template_info_list  # type: list[ListVodTemplateResponseBodyVodTemplateInfoList]

    def validate(self):
        if self.vod_template_info_list:
            for k in self.vod_template_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVodTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVodTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVodTemplateResponse, self).to_map()
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
            temp_model = ListVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWatermarkRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListWatermarkResponseBodyWatermarkInfos(TeaModel):
    def __init__(self, app_id=None, creation_time=None, file_url=None, is_default=None, name=None, type=None,
                 watermark_config=None, watermark_id=None):
        self.app_id = app_id  # type: str
        self.creation_time = creation_time  # type: str
        self.file_url = file_url  # type: str
        self.is_default = is_default  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.watermark_config = watermark_config  # type: str
        self.watermark_id = watermark_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWatermarkResponseBodyWatermarkInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class ListWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, watermark_infos=None):
        self.request_id = request_id  # type: str
        self.watermark_infos = watermark_infos  # type: list[ListWatermarkResponseBodyWatermarkInfos]

    def validate(self):
        if self.watermark_infos:
            for k in self.watermark_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWatermarkResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListWatermarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWatermarkResponse, self).to_map()
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
            temp_model = ListWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveAppResourceRequest(TeaModel):
    def __init__(self, resource_ids=None, resource_type=None, target_app_id=None):
        self.resource_ids = resource_ids  # type: str
        self.resource_type = resource_type  # type: str
        self.target_app_id = target_app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveAppResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.target_app_id is not None:
            result['TargetAppId'] = self.target_app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TargetAppId') is not None:
            self.target_app_id = m.get('TargetAppId')
        return self


class MoveAppResourceResponseBody(TeaModel):
    def __init__(self, failed_resource_ids=None, non_exist_resource_ids=None, request_id=None):
        self.failed_resource_ids = failed_resource_ids  # type: list[str]
        self.non_exist_resource_ids = non_exist_resource_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveAppResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_resource_ids is not None:
            result['FailedResourceIds'] = self.failed_resource_ids
        if self.non_exist_resource_ids is not None:
            result['NonExistResourceIds'] = self.non_exist_resource_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedResourceIds') is not None:
            self.failed_resource_ids = m.get('FailedResourceIds')
        if m.get('NonExistResourceIds') is not None:
            self.non_exist_resource_ids = m.get('NonExistResourceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MoveAppResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MoveAppResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveAppResourceResponse, self).to_map()
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
            temp_model = MoveAppResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreloadVodObjectCachesRequest(TeaModel):
    def __init__(self, object_path=None, owner_id=None, security_token=None):
        self.object_path = object_path  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreloadVodObjectCachesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class PreloadVodObjectCachesResponseBody(TeaModel):
    def __init__(self, preload_task_id=None, request_id=None):
        self.preload_task_id = preload_task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PreloadVodObjectCachesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preload_task_id is not None:
            result['PreloadTaskId'] = self.preload_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PreloadTaskId') is not None:
            self.preload_task_id = m.get('PreloadTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PreloadVodObjectCachesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PreloadVodObjectCachesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PreloadVodObjectCachesResponse, self).to_map()
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
            temp_model = PreloadVodObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProduceEditingProjectVideoRequest(TeaModel):
    def __init__(self, cover_url=None, description=None, media_metadata=None, owner_id=None, produce_config=None,
                 project_id=None, resource_owner_account=None, resource_owner_id=None, timeline=None, title=None,
                 user_data=None):
        self.cover_url = cover_url  # type: str
        self.description = description  # type: str
        self.media_metadata = media_metadata  # type: str
        self.owner_id = owner_id  # type: long
        self.produce_config = produce_config  # type: str
        self.project_id = project_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.timeline = timeline  # type: str
        self.title = title  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProduceEditingProjectVideoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.media_metadata is not None:
            result['MediaMetadata'] = self.media_metadata
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.produce_config is not None:
            result['ProduceConfig'] = self.produce_config
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MediaMetadata') is not None:
            self.media_metadata = m.get('MediaMetadata')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProduceConfig') is not None:
            self.produce_config = m.get('ProduceConfig')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class ProduceEditingProjectVideoResponseBody(TeaModel):
    def __init__(self, media_id=None, project_id=None, request_id=None):
        self.media_id = media_id  # type: str
        self.project_id = project_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProduceEditingProjectVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ProduceEditingProjectVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ProduceEditingProjectVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ProduceEditingProjectVideoResponse, self).to_map()
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
            temp_model = ProduceEditingProjectVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshMediaPlayUrlsRequest(TeaModel):
    def __init__(self, definitions=None, formats=None, media_ids=None, result_type=None, slice_count=None,
                 slice_flag=None, stream_type=None, task_type=None, user_data=None):
        self.definitions = definitions  # type: str
        self.formats = formats  # type: str
        self.media_ids = media_ids  # type: str
        self.result_type = result_type  # type: str
        self.slice_count = slice_count  # type: int
        self.slice_flag = slice_flag  # type: bool
        self.stream_type = stream_type  # type: str
        self.task_type = task_type  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshMediaPlayUrlsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definitions is not None:
            result['Definitions'] = self.definitions
        if self.formats is not None:
            result['Formats'] = self.formats
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.slice_count is not None:
            result['SliceCount'] = self.slice_count
        if self.slice_flag is not None:
            result['SliceFlag'] = self.slice_flag
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Definitions') is not None:
            self.definitions = m.get('Definitions')
        if m.get('Formats') is not None:
            self.formats = m.get('Formats')
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SliceCount') is not None:
            self.slice_count = m.get('SliceCount')
        if m.get('SliceFlag') is not None:
            self.slice_flag = m.get('SliceFlag')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class RefreshMediaPlayUrlsResponseBody(TeaModel):
    def __init__(self, forbidden_media_ids=None, media_refresh_job_id=None, non_exist_media_ids=None,
                 request_id=None):
        self.forbidden_media_ids = forbidden_media_ids  # type: str
        self.media_refresh_job_id = media_refresh_job_id  # type: str
        self.non_exist_media_ids = non_exist_media_ids  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshMediaPlayUrlsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forbidden_media_ids is not None:
            result['ForbiddenMediaIds'] = self.forbidden_media_ids
        if self.media_refresh_job_id is not None:
            result['MediaRefreshJobId'] = self.media_refresh_job_id
        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForbiddenMediaIds') is not None:
            self.forbidden_media_ids = m.get('ForbiddenMediaIds')
        if m.get('MediaRefreshJobId') is not None:
            self.media_refresh_job_id = m.get('MediaRefreshJobId')
        if m.get('NonExistMediaIds') is not None:
            self.non_exist_media_ids = m.get('NonExistMediaIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshMediaPlayUrlsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshMediaPlayUrlsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshMediaPlayUrlsResponse, self).to_map()
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
            temp_model = RefreshMediaPlayUrlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshUploadVideoRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, video_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshUploadVideoRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, request_id=None, upload_address=None, upload_auth=None, video_id=None):
        self.request_id = request_id  # type: str
        self.upload_address = upload_address  # type: str
        self.upload_auth = upload_auth  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshUploadVideoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_address is not None:
            result['UploadAddress'] = self.upload_address
        if self.upload_auth is not None:
            result['UploadAuth'] = self.upload_auth
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadAddress') is not None:
            self.upload_address = m.get('UploadAddress')
        if m.get('UploadAuth') is not None:
            self.upload_auth = m.get('UploadAuth')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class RefreshUploadVideoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshUploadVideoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshUploadVideoResponse, self).to_map()
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
            temp_model = RefreshUploadVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshVodObjectCachesRequest(TeaModel):
    def __init__(self, object_path=None, object_type=None, owner_id=None, security_token=None):
        self.object_path = object_path  # type: str
        self.object_type = object_type  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshVodObjectCachesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_path is not None:
            result['ObjectPath'] = self.object_path
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RefreshVodObjectCachesResponseBody(TeaModel):
    def __init__(self, refresh_task_id=None, request_id=None):
        self.refresh_task_id = refresh_task_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshVodObjectCachesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_task_id is not None:
            result['RefreshTaskId'] = self.refresh_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RefreshTaskId') is not None:
            self.refresh_task_id = m.get('RefreshTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshVodObjectCachesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshVodObjectCachesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshVodObjectCachesResponse, self).to_map()
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
            temp_model = RefreshVodObjectCachesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterMediaRequest(TeaModel):
    def __init__(self, register_metadatas=None, template_group_id=None, user_data=None, workflow_id=None):
        self.register_metadatas = register_metadatas  # type: str
        self.template_group_id = template_group_id  # type: str
        self.user_data = user_data  # type: str
        self.workflow_id = workflow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterMediaRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, file_url=None, media_id=None, new_register=None):
        self.file_url = file_url  # type: str
        self.media_id = media_id  # type: str
        self.new_register = new_register  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterMediaResponseBodyRegisteredMediaList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.new_register is not None:
            result['NewRegister'] = self.new_register
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('NewRegister') is not None:
            self.new_register = m.get('NewRegister')
        return self


class RegisterMediaResponseBody(TeaModel):
    def __init__(self, failed_file_urls=None, registered_media_list=None, request_id=None):
        self.failed_file_urls = failed_file_urls  # type: list[str]
        self.registered_media_list = registered_media_list  # type: list[RegisterMediaResponseBodyRegisteredMediaList]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.registered_media_list:
            for k in self.registered_media_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RegisterMediaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_file_urls is not None:
            result['FailedFileURLs'] = self.failed_file_urls
        result['RegisteredMediaList'] = []
        if self.registered_media_list is not None:
            for k in self.registered_media_list:
                result['RegisteredMediaList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailedFileURLs') is not None:
            self.failed_file_urls = m.get('FailedFileURLs')
        self.registered_media_list = []
        if m.get('RegisteredMediaList') is not None:
            for k in m.get('RegisteredMediaList'):
                temp_model = RegisterMediaResponseBodyRegisteredMediaList()
                self.registered_media_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterMediaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterMediaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterMediaResponse, self).to_map()
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
            temp_model = RegisterMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEditingProjectRequest(TeaModel):
    def __init__(self, end_time=None, owner_account=None, owner_id=None, page_no=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, sort_by=None, start_time=None, status=None, title=None):
        self.end_time = end_time  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.sort_by = sort_by  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchEditingProjectResponseBodyProjectListProject(TeaModel):
    def __init__(self, cover_url=None, creation_time=None, description=None, duration=None, modified_time=None,
                 project_id=None, region_id=None, status=None, storage_location=None, title=None):
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.duration = duration  # type: float
        self.modified_time = modified_time  # type: str
        self.project_id = project_id  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchEditingProjectResponseBodyProjectListProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Title') is not None:
            self.title = m.get('Title')
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
        _map = super(SearchEditingProjectResponseBodyProjectList, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, project_list=None, request_id=None, total=None):
        self.project_list = project_list  # type: SearchEditingProjectResponseBodyProjectList
        self.request_id = request_id  # type: str
        self.total = total  # type: int

    def validate(self):
        if self.project_list:
            self.project_list.validate()

    def to_map(self):
        _map = super(SearchEditingProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_list is not None:
            result['ProjectList'] = self.project_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectList') is not None:
            temp_model = SearchEditingProjectResponseBodyProjectList()
            self.project_list = temp_model.from_map(m['ProjectList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SearchEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchEditingProjectResponse, self).to_map()
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
            temp_model = SearchEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchMediaRequest(TeaModel):
    def __init__(self, fields=None, match=None, page_no=None, page_size=None, scroll_token=None, search_type=None,
                 sort_by=None):
        self.fields = fields  # type: str
        self.match = match  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.scroll_token = scroll_token  # type: str
        self.search_type = search_type  # type: str
        self.sort_by = sort_by  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchMediaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.match is not None:
            result['Match'] = self.match
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scroll_token is not None:
            result['ScrollToken'] = self.scroll_token
        if self.search_type is not None:
            result['SearchType'] = self.search_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Match') is not None:
            self.match = m.get('Match')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScrollToken') is not None:
            self.scroll_token = m.get('ScrollToken')
        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class SearchMediaResponseBodyMediaListAttachedMediaCategories(TeaModel):
    def __init__(self, cate_id=None, cate_name=None, level=None, parent_id=None):
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.level = level  # type: long
        self.parent_id = parent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchMediaResponseBodyMediaListAttachedMediaCategories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.level is not None:
            result['Level'] = self.level
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class SearchMediaResponseBodyMediaListAttachedMedia(TeaModel):
    def __init__(self, app_id=None, business_type=None, categories=None, creation_time=None, description=None,
                 media_id=None, modification_time=None, status=None, storage_location=None, tags=None, title=None, url=None):
        self.app_id = app_id  # type: str
        self.business_type = business_type  # type: str
        self.categories = categories  # type: list[SearchMediaResponseBodyMediaListAttachedMediaCategories]
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.media_id = media_id  # type: str
        self.modification_time = modification_time  # type: str
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchMediaResponseBodyMediaListAttachedMedia, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = SearchMediaResponseBodyMediaListAttachedMediaCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class SearchMediaResponseBodyMediaListAudio(TeaModel):
    def __init__(self, app_id=None, audio_id=None, cate_id=None, cate_name=None, cover_url=None, creation_time=None,
                 description=None, download_switch=None, duration=None, media_source=None, modification_time=None,
                 preprocess_status=None, size=None, snapshots=None, sprite_snapshots=None, status=None, storage_location=None,
                 tags=None, title=None, transcode_mode=None):
        self.app_id = app_id  # type: str
        self.audio_id = audio_id  # type: str
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.download_switch = download_switch  # type: str
        self.duration = duration  # type: float
        self.media_source = media_source  # type: str
        self.modification_time = modification_time  # type: str
        self.preprocess_status = preprocess_status  # type: str
        self.size = size  # type: long
        self.snapshots = snapshots  # type: list[str]
        self.sprite_snapshots = sprite_snapshots  # type: list[str]
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.transcode_mode = transcode_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchMediaResponseBodyMediaListAudio, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.download_switch is not None:
            result['DownloadSwitch'] = self.download_switch
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.media_source is not None:
            result['MediaSource'] = self.media_source
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.preprocess_status is not None:
            result['PreprocessStatus'] = self.preprocess_status
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.sprite_snapshots is not None:
            result['SpriteSnapshots'] = self.sprite_snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.transcode_mode is not None:
            result['TranscodeMode'] = self.transcode_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DownloadSwitch') is not None:
            self.download_switch = m.get('DownloadSwitch')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MediaSource') is not None:
            self.media_source = m.get('MediaSource')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('PreprocessStatus') is not None:
            self.preprocess_status = m.get('PreprocessStatus')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('SpriteSnapshots') is not None:
            self.sprite_snapshots = m.get('SpriteSnapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TranscodeMode') is not None:
            self.transcode_mode = m.get('TranscodeMode')
        return self


class SearchMediaResponseBodyMediaListImage(TeaModel):
    def __init__(self, app_id=None, cate_id=None, cate_name=None, creation_time=None, description=None,
                 image_id=None, modification_time=None, status=None, storage_location=None, tags=None, title=None, url=None):
        self.app_id = app_id  # type: str
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.image_id = image_id  # type: str
        self.modification_time = modification_time  # type: str
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchMediaResponseBodyMediaListImage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class SearchMediaResponseBodyMediaListVideo(TeaModel):
    def __init__(self, app_id=None, cate_id=None, cate_name=None, cover_url=None, creation_time=None,
                 description=None, download_switch=None, duration=None, media_source=None, modification_time=None,
                 preprocess_status=None, size=None, snapshots=None, sprite_snapshots=None, status=None, storage_location=None,
                 tags=None, title=None, transcode_mode=None, video_id=None):
        self.app_id = app_id  # type: str
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str
        self.cover_url = cover_url  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.download_switch = download_switch  # type: str
        self.duration = duration  # type: float
        self.media_source = media_source  # type: str
        self.modification_time = modification_time  # type: str
        self.preprocess_status = preprocess_status  # type: str
        self.size = size  # type: long
        self.snapshots = snapshots  # type: list[str]
        self.sprite_snapshots = sprite_snapshots  # type: list[str]
        self.status = status  # type: str
        self.storage_location = storage_location  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.transcode_mode = transcode_mode  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchMediaResponseBodyMediaListVideo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.download_switch is not None:
            result['DownloadSwitch'] = self.download_switch
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.media_source is not None:
            result['MediaSource'] = self.media_source
        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time
        if self.preprocess_status is not None:
            result['PreprocessStatus'] = self.preprocess_status
        if self.size is not None:
            result['Size'] = self.size
        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots
        if self.sprite_snapshots is not None:
            result['SpriteSnapshots'] = self.sprite_snapshots
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.transcode_mode is not None:
            result['TranscodeMode'] = self.transcode_mode
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DownloadSwitch') is not None:
            self.download_switch = m.get('DownloadSwitch')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MediaSource') is not None:
            self.media_source = m.get('MediaSource')
        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')
        if m.get('PreprocessStatus') is not None:
            self.preprocess_status = m.get('PreprocessStatus')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')
        if m.get('SpriteSnapshots') is not None:
            self.sprite_snapshots = m.get('SpriteSnapshots')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TranscodeMode') is not None:
            self.transcode_mode = m.get('TranscodeMode')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class SearchMediaResponseBodyMediaList(TeaModel):
    def __init__(self, attached_media=None, audio=None, creation_time=None, image=None, media_id=None,
                 media_type=None, video=None):
        self.attached_media = attached_media  # type: SearchMediaResponseBodyMediaListAttachedMedia
        self.audio = audio  # type: SearchMediaResponseBodyMediaListAudio
        self.creation_time = creation_time  # type: str
        self.image = image  # type: SearchMediaResponseBodyMediaListImage
        self.media_id = media_id  # type: str
        self.media_type = media_type  # type: str
        self.video = video  # type: SearchMediaResponseBodyMediaListVideo

    def validate(self):
        if self.attached_media:
            self.attached_media.validate()
        if self.audio:
            self.audio.validate()
        if self.image:
            self.image.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        _map = super(SearchMediaResponseBodyMediaList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attached_media is not None:
            result['AttachedMedia'] = self.attached_media.to_map()
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.video is not None:
            result['Video'] = self.video.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachedMedia') is not None:
            temp_model = SearchMediaResponseBodyMediaListAttachedMedia()
            self.attached_media = temp_model.from_map(m['AttachedMedia'])
        if m.get('Audio') is not None:
            temp_model = SearchMediaResponseBodyMediaListAudio()
            self.audio = temp_model.from_map(m['Audio'])
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Image') is not None:
            temp_model = SearchMediaResponseBodyMediaListImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Video') is not None:
            temp_model = SearchMediaResponseBodyMediaListVideo()
            self.video = temp_model.from_map(m['Video'])
        return self


class SearchMediaResponseBody(TeaModel):
    def __init__(self, media_list=None, request_id=None, scroll_token=None, total=None):
        self.media_list = media_list  # type: list[SearchMediaResponseBodyMediaList]
        self.request_id = request_id  # type: str
        self.scroll_token = scroll_token  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.media_list:
            for k in self.media_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchMediaResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchMediaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchMediaResponse, self).to_map()
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
            temp_model = SearchMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAuditSecurityIpRequest(TeaModel):
    def __init__(self, ips=None, operate_mode=None, security_group_name=None):
        self.ips = ips  # type: str
        self.operate_mode = operate_mode  # type: str
        self.security_group_name = security_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAuditSecurityIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.operate_mode is not None:
            result['OperateMode'] = self.operate_mode
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('OperateMode') is not None:
            self.operate_mode = m.get('OperateMode')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        return self


class SetAuditSecurityIpResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetAuditSecurityIpResponseBody, self).to_map()
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


class SetAuditSecurityIpResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetAuditSecurityIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetAuditSecurityIpResponse, self).to_map()
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
            temp_model = SetAuditSecurityIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCrossdomainContentRequest(TeaModel):
    def __init__(self, content=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, resource_real_owner_id=None, storage_location=None):
        self.content = content  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.resource_real_owner_id = resource_real_owner_id  # type: str
        self.storage_location = storage_location  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCrossdomainContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_real_owner_id is not None:
            result['ResourceRealOwnerId'] = self.resource_real_owner_id
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceRealOwnerId') is not None:
            self.resource_real_owner_id = m.get('ResourceRealOwnerId')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        return self


class SetCrossdomainContentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetCrossdomainContentResponseBody, self).to_map()
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


class SetCrossdomainContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetCrossdomainContentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetCrossdomainContentResponse, self).to_map()
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
            temp_model = SetCrossdomainContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultAITemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultAITemplateRequest, self).to_map()
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


class SetDefaultAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultAITemplateResponseBody, self).to_map()
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


class SetDefaultAITemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDefaultAITemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDefaultAITemplateResponse, self).to_map()
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
            temp_model = SetDefaultAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, transcode_template_group_id=None):
        self.transcode_template_group_id = transcode_template_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultTranscodeTemplateGroupRequest, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultTranscodeTemplateGroupResponseBody, self).to_map()
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


class SetDefaultTranscodeTemplateGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDefaultTranscodeTemplateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDefaultTranscodeTemplateGroupResponse, self).to_map()
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
            temp_model = SetDefaultTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDefaultWatermarkRequest(TeaModel):
    def __init__(self, watermark_id=None):
        self.watermark_id = watermark_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDefaultWatermarkResponseBody, self).to_map()
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


class SetDefaultWatermarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDefaultWatermarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDefaultWatermarkResponse, self).to_map()
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
            temp_model = SetDefaultWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEditingProjectMaterialsRequest(TeaModel):
    def __init__(self, material_ids=None, owner_account=None, owner_id=None, project_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.material_ids = material_ids  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.project_id = project_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetEditingProjectMaterialsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_ids is not None:
            result['MaterialIds'] = self.material_ids
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaterialIds') is not None:
            self.material_ids = m.get('MaterialIds')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SetEditingProjectMaterialsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetEditingProjectMaterialsResponseBody, self).to_map()
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


class SetEditingProjectMaterialsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetEditingProjectMaterialsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetEditingProjectMaterialsResponse, self).to_map()
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
            temp_model = SetEditingProjectMaterialsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMessageCallbackRequest(TeaModel):
    def __init__(self, app_id=None, auth_key=None, auth_switch=None, callback_type=None, callback_url=None,
                 event_type_list=None, mns_endpoint=None, mns_queue_name=None, owner_account=None):
        self.app_id = app_id  # type: str
        self.auth_key = auth_key  # type: str
        self.auth_switch = auth_switch  # type: str
        self.callback_type = callback_type  # type: str
        self.callback_url = callback_url  # type: str
        self.event_type_list = event_type_list  # type: str
        self.mns_endpoint = mns_endpoint  # type: str
        self.mns_queue_name = mns_queue_name  # type: str
        self.owner_account = owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMessageCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_switch is not None:
            result['AuthSwitch'] = self.auth_switch
        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type
        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url
        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list
        if self.mns_endpoint is not None:
            result['MnsEndpoint'] = self.mns_endpoint
        if self.mns_queue_name is not None:
            result['MnsQueueName'] = self.mns_queue_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSwitch') is not None:
            self.auth_switch = m.get('AuthSwitch')
        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')
        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')
        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')
        if m.get('MnsEndpoint') is not None:
            self.mns_endpoint = m.get('MnsEndpoint')
        if m.get('MnsQueueName') is not None:
            self.mns_queue_name = m.get('MnsQueueName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class SetMessageCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetMessageCallbackResponseBody, self).to_map()
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


class SetMessageCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetMessageCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetMessageCallbackResponse, self).to_map()
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
            temp_model = SetMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetVodDomainCertificateRequest(TeaModel):
    def __init__(self, cert_name=None, domain_name=None, owner_id=None, sslpri=None, sslprotocol=None, sslpub=None,
                 security_token=None):
        self.cert_name = cert_name  # type: str
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.sslpri = sslpri  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetVodDomainCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetVodDomainCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetVodDomainCertificateResponseBody, self).to_map()
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


class SetVodDomainCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetVodDomainCertificateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetVodDomainCertificateResponse, self).to_map()
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
            temp_model = SetVodDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAIImageAuditJobRequest(TeaModel):
    def __init__(self, media_audit_configuration=None, media_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, template_id=None):
        self.media_audit_configuration = media_audit_configuration  # type: str
        self.media_id = media_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAIImageAuditJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_audit_configuration is not None:
            result['MediaAuditConfiguration'] = self.media_audit_configuration
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaAuditConfiguration') is not None:
            self.media_audit_configuration = m.get('MediaAuditConfiguration')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SubmitAIImageAuditJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAIImageAuditJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitAIImageAuditJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitAIImageAuditJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAIImageAuditJobResponse, self).to_map()
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
            temp_model = SubmitAIImageAuditJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAIImageJobRequest(TeaModel):
    def __init__(self, aipipeline_id=None, aitemplate_id=None, owner_account=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, user_data=None, video_id=None):
        self.aipipeline_id = aipipeline_id  # type: str
        self.aitemplate_id = aitemplate_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.user_data = user_data  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAIImageJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aipipeline_id is not None:
            result['AIPipelineId'] = self.aipipeline_id
        if self.aitemplate_id is not None:
            result['AITemplateId'] = self.aitemplate_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIPipelineId') is not None:
            self.aipipeline_id = m.get('AIPipelineId')
        if m.get('AITemplateId') is not None:
            self.aitemplate_id = m.get('AITemplateId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class SubmitAIImageJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAIImageJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitAIImageJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitAIImageJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAIImageJobResponse, self).to_map()
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
            temp_model = SubmitAIImageJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAIJobRequest(TeaModel):
    def __init__(self, config=None, media_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, types=None, user_data=None):
        self.config = config  # type: str
        self.media_id = media_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.types = types  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAIJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.types is not None:
            result['Types'] = self.types
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitAIJobResponseBodyAIJobListAIJob(TeaModel):
    def __init__(self, job_id=None, media_id=None, type=None):
        self.job_id = job_id  # type: str
        self.media_id = media_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAIJobResponseBodyAIJobListAIJob, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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
        _map = super(SubmitAIJobResponseBodyAIJobList, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, aijob_list=None, request_id=None):
        self.aijob_list = aijob_list  # type: SubmitAIJobResponseBodyAIJobList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.aijob_list:
            self.aijob_list.validate()

    def to_map(self):
        _map = super(SubmitAIJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aijob_list is not None:
            result['AIJobList'] = self.aijob_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AIJobList') is not None:
            temp_model = SubmitAIJobResponseBodyAIJobList()
            self.aijob_list = temp_model.from_map(m['AIJobList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitAIJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitAIJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAIJobResponse, self).to_map()
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
            temp_model = SubmitAIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAIMediaAuditJobRequest(TeaModel):
    def __init__(self, media_audit_configuration=None, media_id=None, media_type=None, template_id=None,
                 user_data=None):
        self.media_audit_configuration = media_audit_configuration  # type: str
        self.media_id = media_id  # type: str
        self.media_type = media_type  # type: str
        self.template_id = template_id  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAIMediaAuditJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_audit_configuration is not None:
            result['MediaAuditConfiguration'] = self.media_audit_configuration
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaAuditConfiguration') is not None:
            self.media_audit_configuration = m.get('MediaAuditConfiguration')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitAIMediaAuditJobResponseBody(TeaModel):
    def __init__(self, job_id=None, media_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.media_id = media_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAIMediaAuditJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitAIMediaAuditJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitAIMediaAuditJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAIMediaAuditJobResponse, self).to_map()
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
            temp_model = SubmitAIMediaAuditJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDynamicImageJobRequest(TeaModel):
    def __init__(self, dynamic_image_template_id=None, override_params=None, video_id=None):
        self.dynamic_image_template_id = dynamic_image_template_id  # type: str
        self.override_params = override_params  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDynamicImageJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_image_template_id is not None:
            result['DynamicImageTemplateId'] = self.dynamic_image_template_id
        if self.override_params is not None:
            result['OverrideParams'] = self.override_params
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicImageTemplateId') is not None:
            self.dynamic_image_template_id = m.get('DynamicImageTemplateId')
        if m.get('OverrideParams') is not None:
            self.override_params = m.get('OverrideParams')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class SubmitDynamicImageJobResponseBodyDynamicImageJob(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitDynamicImageJobResponseBodyDynamicImageJob, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, dynamic_image_job=None, request_id=None):
        self.dynamic_image_job = dynamic_image_job  # type: SubmitDynamicImageJobResponseBodyDynamicImageJob
        self.request_id = request_id  # type: str

    def validate(self):
        if self.dynamic_image_job:
            self.dynamic_image_job.validate()

    def to_map(self):
        _map = super(SubmitDynamicImageJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_image_job is not None:
            result['DynamicImageJob'] = self.dynamic_image_job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DynamicImageJob') is not None:
            temp_model = SubmitDynamicImageJobResponseBodyDynamicImageJob()
            self.dynamic_image_job = temp_model.from_map(m['DynamicImageJob'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitDynamicImageJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitDynamicImageJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitDynamicImageJobResponse, self).to_map()
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
            temp_model = SubmitDynamicImageJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitMediaDNADeleteJobRequest(TeaModel):
    def __init__(self, media_id=None, owner_account=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.media_id = media_id  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMediaDNADeleteJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SubmitMediaDNADeleteJobResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        self.job_id = job_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitMediaDNADeleteJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitMediaDNADeleteJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitMediaDNADeleteJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitMediaDNADeleteJobResponse, self).to_map()
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
            temp_model = SubmitMediaDNADeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPreprocessJobsRequest(TeaModel):
    def __init__(self, preprocess_type=None, video_id=None):
        self.preprocess_type = preprocess_type  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPreprocessJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preprocess_type is not None:
            result['PreprocessType'] = self.preprocess_type
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PreprocessType') is not None:
            self.preprocess_type = m.get('PreprocessType')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class SubmitPreprocessJobsResponseBodyPreprocessJobsPreprocessJob(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitPreprocessJobsResponseBodyPreprocessJobsPreprocessJob, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(SubmitPreprocessJobsResponseBodyPreprocessJobs, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, preprocess_jobs=None, request_id=None):
        self.preprocess_jobs = preprocess_jobs  # type: SubmitPreprocessJobsResponseBodyPreprocessJobs
        self.request_id = request_id  # type: str

    def validate(self):
        if self.preprocess_jobs:
            self.preprocess_jobs.validate()

    def to_map(self):
        _map = super(SubmitPreprocessJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preprocess_jobs is not None:
            result['PreprocessJobs'] = self.preprocess_jobs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PreprocessJobs') is not None:
            temp_model = SubmitPreprocessJobsResponseBodyPreprocessJobs()
            self.preprocess_jobs = temp_model.from_map(m['PreprocessJobs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitPreprocessJobsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitPreprocessJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitPreprocessJobsResponse, self).to_map()
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
            temp_model = SubmitPreprocessJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSnapshotJobRequest(TeaModel):
    def __init__(self, count=None, height=None, interval=None, snapshot_template_id=None,
                 specified_offset_time=None, sprite_snapshot_config=None, user_data=None, video_id=None, width=None):
        self.count = count  # type: long
        self.height = height  # type: str
        self.interval = interval  # type: long
        self.snapshot_template_id = snapshot_template_id  # type: str
        self.specified_offset_time = specified_offset_time  # type: long
        self.sprite_snapshot_config = sprite_snapshot_config  # type: str
        self.user_data = user_data  # type: str
        self.video_id = video_id  # type: str
        self.width = width  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSnapshotJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.height is not None:
            result['Height'] = self.height
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.snapshot_template_id is not None:
            result['SnapshotTemplateId'] = self.snapshot_template_id
        if self.specified_offset_time is not None:
            result['SpecifiedOffsetTime'] = self.specified_offset_time
        if self.sprite_snapshot_config is not None:
            result['SpriteSnapshotConfig'] = self.sprite_snapshot_config
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('SnapshotTemplateId') is not None:
            self.snapshot_template_id = m.get('SnapshotTemplateId')
        if m.get('SpecifiedOffsetTime') is not None:
            self.specified_offset_time = m.get('SpecifiedOffsetTime')
        if m.get('SpriteSnapshotConfig') is not None:
            self.sprite_snapshot_config = m.get('SpriteSnapshotConfig')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class SubmitSnapshotJobResponseBodySnapshotJob(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSnapshotJobResponseBodySnapshotJob, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str
        self.snapshot_job = snapshot_job  # type: SubmitSnapshotJobResponseBodySnapshotJob

    def validate(self):
        if self.snapshot_job:
            self.snapshot_job.validate()

    def to_map(self):
        _map = super(SubmitSnapshotJobResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitSnapshotJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitSnapshotJobResponse, self).to_map()
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
            temp_model = SubmitSnapshotJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTranscodeJobsRequest(TeaModel):
    def __init__(self, encrypt_config=None, override_params=None, pipeline_id=None, priority=None,
                 template_group_id=None, user_data=None, video_id=None):
        self.encrypt_config = encrypt_config  # type: str
        self.override_params = override_params  # type: str
        self.pipeline_id = pipeline_id  # type: str
        self.priority = priority  # type: str
        self.template_group_id = template_group_id  # type: str
        self.user_data = user_data  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTranscodeJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_config is not None:
            result['EncryptConfig'] = self.encrypt_config
        if self.override_params is not None:
            result['OverrideParams'] = self.override_params
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptConfig') is not None:
            self.encrypt_config = m.get('EncryptConfig')
        if m.get('OverrideParams') is not None:
            self.override_params = m.get('OverrideParams')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class SubmitTranscodeJobsResponseBodyTranscodeJobsTranscodeJob(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTranscodeJobsResponseBodyTranscodeJobsTranscodeJob, self).to_map()
        if _map is not None:
            return _map

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
        _map = super(SubmitTranscodeJobsResponseBodyTranscodeJobs, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str
        self.transcode_jobs = transcode_jobs  # type: SubmitTranscodeJobsResponseBodyTranscodeJobs
        self.transcode_task_id = transcode_task_id  # type: str

    def validate(self):
        if self.transcode_jobs:
            self.transcode_jobs.validate()

    def to_map(self):
        _map = super(SubmitTranscodeJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitTranscodeJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTranscodeJobsResponse, self).to_map()
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
            temp_model = SubmitTranscodeJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitWorkflowJobRequest(TeaModel):
    def __init__(self, media_id=None, workflow_id=None):
        self.media_id = media_id  # type: str
        self.workflow_id = workflow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitWorkflowJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class SubmitWorkflowJobResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitWorkflowJobResponseBody, self).to_map()
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


class SubmitWorkflowJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitWorkflowJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitWorkflowJobResponse, self).to_map()
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
            temp_model = SubmitWorkflowJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAITemplateRequest(TeaModel):
    def __init__(self, template_config=None, template_id=None, template_name=None):
        self.template_config = template_config  # type: str
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAITemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class UpdateAITemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, template_id=None):
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAITemplateResponseBody, self).to_map()
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


class UpdateAITemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAITemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAITemplateResponse, self).to_map()
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
            temp_model = UpdateAITemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppInfoRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None, description=None, status=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.description = description  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppInfoResponseBody, self).to_map()
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


class UpdateAppInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppInfoResponse, self).to_map()
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
            temp_model = UpdateAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAttachedMediaInfosRequest(TeaModel):
    def __init__(self, update_content=None):
        self.update_content = update_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAttachedMediaInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_content is not None:
            result['UpdateContent'] = self.update_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateContent') is not None:
            self.update_content = m.get('UpdateContent')
        return self


class UpdateAttachedMediaInfosResponseBody(TeaModel):
    def __init__(self, non_exist_media_ids=None, request_id=None):
        self.non_exist_media_ids = non_exist_media_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAttachedMediaInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAttachedMediaInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAttachedMediaInfosResponse, self).to_map()
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
            temp_model = UpdateAttachedMediaInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCategoryRequest(TeaModel):
    def __init__(self, cate_id=None, cate_name=None):
        self.cate_id = cate_id  # type: long
        self.cate_name = cate_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCategoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        return self


class UpdateCategoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCategoryResponseBody, self).to_map()
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


class UpdateCategoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCategoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCategoryResponse, self).to_map()
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
            temp_model = UpdateCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEditingProjectRequest(TeaModel):
    def __init__(self, cover_url=None, description=None, owner_account=None, owner_id=None, project_id=None,
                 resource_owner_account=None, resource_owner_id=None, timeline=None, title=None):
        self.cover_url = cover_url  # type: str
        self.description = description  # type: str
        self.owner_account = owner_account  # type: str
        self.owner_id = owner_id  # type: str
        self.project_id = project_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: str
        self.timeline = timeline  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEditingProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.timeline is not None:
            result['Timeline'] = self.timeline
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateEditingProjectResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEditingProjectResponseBody, self).to_map()
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


class UpdateEditingProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEditingProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEditingProjectResponse, self).to_map()
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
            temp_model = UpdateEditingProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageInfosRequest(TeaModel):
    def __init__(self, update_content=None):
        self.update_content = update_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_content is not None:
            result['UpdateContent'] = self.update_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateContent') is not None:
            self.update_content = m.get('UpdateContent')
        return self


class UpdateImageInfosResponseBodyNonExistImageIds(TeaModel):
    def __init__(self, image_id=None):
        self.image_id = image_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateImageInfosResponseBodyNonExistImageIds, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, non_exist_image_ids=None, request_id=None):
        self.non_exist_image_ids = non_exist_image_ids  # type: UpdateImageInfosResponseBodyNonExistImageIds
        self.request_id = request_id  # type: str

    def validate(self):
        if self.non_exist_image_ids:
            self.non_exist_image_ids.validate()

    def to_map(self):
        _map = super(UpdateImageInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_exist_image_ids is not None:
            result['NonExistImageIds'] = self.non_exist_image_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NonExistImageIds') is not None:
            temp_model = UpdateImageInfosResponseBodyNonExistImageIds()
            self.non_exist_image_ids = temp_model.from_map(m['NonExistImageIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateImageInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateImageInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateImageInfosResponse, self).to_map()
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
            temp_model = UpdateImageInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTranscodeTemplateGroupRequest(TeaModel):
    def __init__(self, locked=None, name=None, transcode_template_group_id=None, transcode_template_list=None):
        self.locked = locked  # type: str
        self.name = name  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str
        self.transcode_template_list = transcode_template_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTranscodeTemplateGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.name is not None:
            result['Name'] = self.name
        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id
        if self.transcode_template_list is not None:
            result['TranscodeTemplateList'] = self.transcode_template_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')
        if m.get('TranscodeTemplateList') is not None:
            self.transcode_template_list = m.get('TranscodeTemplateList')
        return self


class UpdateTranscodeTemplateGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, transcode_template_group_id=None):
        self.request_id = request_id  # type: str
        self.transcode_template_group_id = transcode_template_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTranscodeTemplateGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTranscodeTemplateGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTranscodeTemplateGroupResponse, self).to_map()
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
            temp_model = UpdateTranscodeTemplateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVideoInfoRequest(TeaModel):
    def __init__(self, cate_id=None, cover_url=None, description=None, tags=None, title=None, video_id=None):
        self.cate_id = cate_id  # type: long
        self.cover_url = cover_url  # type: str
        self.description = description  # type: str
        self.tags = tags  # type: str
        self.title = title  # type: str
        self.video_id = video_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVideoInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url
        if self.description is not None:
            result['Description'] = self.description
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.video_id is not None:
            result['VideoId'] = self.video_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')
        return self


class UpdateVideoInfoResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVideoInfoResponseBody, self).to_map()
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


class UpdateVideoInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVideoInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVideoInfoResponse, self).to_map()
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
            temp_model = UpdateVideoInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVideoInfosRequest(TeaModel):
    def __init__(self, update_content=None):
        self.update_content = update_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVideoInfosRequest, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, forbidden_video_ids=None, non_exist_video_ids=None, request_id=None):
        self.forbidden_video_ids = forbidden_video_ids  # type: list[str]
        self.non_exist_video_ids = non_exist_video_ids  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVideoInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forbidden_video_ids is not None:
            result['ForbiddenVideoIds'] = self.forbidden_video_ids
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ForbiddenVideoIds') is not None:
            self.forbidden_video_ids = m.get('ForbiddenVideoIds')
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateVideoInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVideoInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVideoInfosResponse, self).to_map()
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
            temp_model = UpdateVideoInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVodDomainRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, security_token=None, sources=None, top_level_domain=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.security_token = security_token  # type: str
        self.sources = sources  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVodDomainRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sources is not None:
            result['Sources'] = self.sources
        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')
        return self


class UpdateVodDomainResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVodDomainResponseBody, self).to_map()
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


class UpdateVodDomainResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVodDomainResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVodDomainResponse, self).to_map()
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
            temp_model = UpdateVodDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVodTemplateRequest(TeaModel):
    def __init__(self, name=None, template_config=None, vod_template_id=None):
        self.name = name  # type: str
        self.template_config = template_config  # type: str
        self.vod_template_id = vod_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVodTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.vod_template_id is not None:
            result['VodTemplateId'] = self.vod_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('VodTemplateId') is not None:
            self.vod_template_id = m.get('VodTemplateId')
        return self


class UpdateVodTemplateResponseBody(TeaModel):
    def __init__(self, request_id=None, vod_template_id=None):
        self.request_id = request_id  # type: str
        self.vod_template_id = vod_template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVodTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVodTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVodTemplateResponse, self).to_map()
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
            temp_model = UpdateVodTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWatermarkRequest(TeaModel):
    def __init__(self, name=None, watermark_config=None, watermark_id=None):
        self.name = name  # type: str
        self.watermark_config = watermark_config  # type: str
        self.watermark_id = watermark_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWatermarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class UpdateWatermarkResponseBodyWatermarkInfo(TeaModel):
    def __init__(self, creation_time=None, file_url=None, is_default=None, name=None, type=None,
                 watermark_config=None, watermark_id=None):
        self.creation_time = creation_time  # type: str
        self.file_url = file_url  # type: str
        self.is_default = is_default  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.watermark_config = watermark_config  # type: str
        self.watermark_id = watermark_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWatermarkResponseBodyWatermarkInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config
        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')
        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')
        return self


class UpdateWatermarkResponseBody(TeaModel):
    def __init__(self, request_id=None, watermark_info=None):
        self.request_id = request_id  # type: str
        self.watermark_info = watermark_info  # type: UpdateWatermarkResponseBodyWatermarkInfo

    def validate(self):
        if self.watermark_info:
            self.watermark_info.validate()

    def to_map(self):
        _map = super(UpdateWatermarkResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateWatermarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWatermarkResponse, self).to_map()
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
            temp_model = UpdateWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadMediaByURLRequest(TeaModel):
    def __init__(self, app_id=None, storage_location=None, template_group_id=None, upload_metadatas=None,
                 upload_urls=None, user_data=None, workflow_id=None):
        self.app_id = app_id  # type: str
        self.storage_location = storage_location  # type: str
        self.template_group_id = template_group_id  # type: str
        self.upload_metadatas = upload_metadatas  # type: str
        self.upload_urls = upload_urls  # type: str
        self.user_data = user_data  # type: str
        self.workflow_id = workflow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadMediaByURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location
        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id
        if self.upload_metadatas is not None:
            result['UploadMetadatas'] = self.upload_metadatas
        if self.upload_urls is not None:
            result['UploadURLs'] = self.upload_urls
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')
        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')
        if m.get('UploadMetadatas') is not None:
            self.upload_metadatas = m.get('UploadMetadatas')
        if m.get('UploadURLs') is not None:
            self.upload_urls = m.get('UploadURLs')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')
        return self


class UploadMediaByURLResponseBodyUploadJobs(TeaModel):
    def __init__(self, job_id=None, source_url=None):
        self.job_id = job_id  # type: str
        self.source_url = source_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadMediaByURLResponseBodyUploadJobs, self).to_map()
        if _map is not None:
            return _map

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
        self.request_id = request_id  # type: str
        self.upload_jobs = upload_jobs  # type: list[UploadMediaByURLResponseBodyUploadJobs]

    def validate(self):
        if self.upload_jobs:
            for k in self.upload_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UploadMediaByURLResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadMediaByURLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadMediaByURLResponse, self).to_map()
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
            temp_model = UploadMediaByURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadStreamByURLRequest(TeaModel):
    def __init__(self, definition=None, file_extension=None, hdrtype=None, media_id=None, stream_url=None,
                 user_data=None):
        self.definition = definition  # type: str
        self.file_extension = file_extension  # type: str
        self.hdrtype = hdrtype  # type: str
        self.media_id = media_id  # type: str
        self.stream_url = stream_url  # type: str
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadStreamByURLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.file_extension is not None:
            result['FileExtension'] = self.file_extension
        if self.hdrtype is not None:
            result['HDRType'] = self.hdrtype
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('FileExtension') is not None:
            self.file_extension = m.get('FileExtension')
        if m.get('HDRType') is not None:
            self.hdrtype = m.get('HDRType')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class UploadStreamByURLResponseBody(TeaModel):
    def __init__(self, file_url=None, request_id=None, source_url=None, stream_job_id=None):
        self.file_url = file_url  # type: str
        self.request_id = request_id  # type: str
        self.source_url = source_url  # type: str
        self.stream_job_id = stream_job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadStreamByURLResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileURL'] = self.file_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_url is not None:
            result['SourceURL'] = self.source_url
        if self.stream_job_id is not None:
            result['StreamJobId'] = self.stream_job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceURL') is not None:
            self.source_url = m.get('SourceURL')
        if m.get('StreamJobId') is not None:
            self.stream_job_id = m.get('StreamJobId')
        return self


class UploadStreamByURLResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadStreamByURLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadStreamByURLResponse, self).to_map()
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
            temp_model = UploadStreamByURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyVodDomainOwnerRequest(TeaModel):
    def __init__(self, domain_name=None, owner_id=None, verify_type=None):
        self.domain_name = domain_name  # type: str
        self.owner_id = owner_id  # type: long
        self.verify_type = verify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyVodDomainOwnerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class VerifyVodDomainOwnerResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyVodDomainOwnerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyVodDomainOwnerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VerifyVodDomainOwnerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyVodDomainOwnerResponse, self).to_map()
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
            temp_model = VerifyVodDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


