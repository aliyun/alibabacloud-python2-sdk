# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddWebhookRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, description=None, enable_ssl_verification=None,
                 merge_requests_events=None, note_events=None, push_events=None, secret_token=None, tag_push_events=None, url=None):
        self.access_token = access_token  # type: str
        self.organization_id = organization_id  # type: str
        # webhook描述
        self.description = description  # type: str
        # 使用ssl认证
        self.enable_ssl_verification = enable_ssl_verification  # type: bool
        # 合并请求事件
        self.merge_requests_events = merge_requests_events  # type: bool
        # 评论事件
        self.note_events = note_events  # type: bool
        # 分支推送事件
        self.push_events = push_events  # type: bool
        self.secret_token = secret_token  # type: str
        # 标签推送事件
        self.tag_push_events = tag_push_events  # type: bool
        # hook url
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.description is not None:
            result['description'] = self.description
        if self.enable_ssl_verification is not None:
            result['enableSslVerification'] = self.enable_ssl_verification
        if self.merge_requests_events is not None:
            result['mergeRequestsEvents'] = self.merge_requests_events
        if self.note_events is not None:
            result['noteEvents'] = self.note_events
        if self.push_events is not None:
            result['pushEvents'] = self.push_events
        if self.secret_token is not None:
            result['secretToken'] = self.secret_token
        if self.tag_push_events is not None:
            result['tagPushEvents'] = self.tag_push_events
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enableSslVerification') is not None:
            self.enable_ssl_verification = m.get('enableSslVerification')
        if m.get('mergeRequestsEvents') is not None:
            self.merge_requests_events = m.get('mergeRequestsEvents')
        if m.get('noteEvents') is not None:
            self.note_events = m.get('noteEvents')
        if m.get('pushEvents') is not None:
            self.push_events = m.get('pushEvents')
        if m.get('secretToken') is not None:
            self.secret_token = m.get('secretToken')
        if m.get('tagPushEvents') is not None:
            self.tag_push_events = m.get('tagPushEvents')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class AddWebhookResponseBodyResult(TeaModel):
    def __init__(self, enable_ssl_verification=None, build_events=None, created_at=None, description=None, id=None,
                 issues_events=None, last_test_result=None, merge_requests_events=None, note_events=None, push_events=None,
                 repository_id=None, secret_token=None, tag_push_events=None, url=None):
        self.enable_ssl_verification = enable_ssl_verification  # type: bool
        self.build_events = build_events  # type: bool
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.issues_events = issues_events  # type: bool
        self.last_test_result = last_test_result  # type: str
        self.merge_requests_events = merge_requests_events  # type: bool
        self.note_events = note_events  # type: bool
        self.push_events = push_events  # type: bool
        self.repository_id = repository_id  # type: long
        self.secret_token = secret_token  # type: str
        self.tag_push_events = tag_push_events  # type: bool
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddWebhookResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_ssl_verification is not None:
            result['EnableSslVerification'] = self.enable_ssl_verification
        if self.build_events is not None:
            result['buildEvents'] = self.build_events
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.issues_events is not None:
            result['issuesEvents'] = self.issues_events
        if self.last_test_result is not None:
            result['lastTestResult'] = self.last_test_result
        if self.merge_requests_events is not None:
            result['mergeRequestsEvents'] = self.merge_requests_events
        if self.note_events is not None:
            result['noteEvents'] = self.note_events
        if self.push_events is not None:
            result['pushEvents'] = self.push_events
        if self.repository_id is not None:
            result['repositoryId'] = self.repository_id
        if self.secret_token is not None:
            result['secretToken'] = self.secret_token
        if self.tag_push_events is not None:
            result['tagPushEvents'] = self.tag_push_events
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableSslVerification') is not None:
            self.enable_ssl_verification = m.get('EnableSslVerification')
        if m.get('buildEvents') is not None:
            self.build_events = m.get('buildEvents')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('issuesEvents') is not None:
            self.issues_events = m.get('issuesEvents')
        if m.get('lastTestResult') is not None:
            self.last_test_result = m.get('lastTestResult')
        if m.get('mergeRequestsEvents') is not None:
            self.merge_requests_events = m.get('mergeRequestsEvents')
        if m.get('noteEvents') is not None:
            self.note_events = m.get('noteEvents')
        if m.get('pushEvents') is not None:
            self.push_events = m.get('pushEvents')
        if m.get('repositoryId') is not None:
            self.repository_id = m.get('repositoryId')
        if m.get('secretToken') is not None:
            self.secret_token = m.get('secretToken')
        if m.get('tagPushEvents') is not None:
            self.tag_push_events = m.get('tagPushEvents')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class AddWebhookResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: AddWebhookResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(AddWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = AddWebhookResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AddWebhookResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddWebhookResponse, self).to_map()
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
            temp_model = AddWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowTagRequest(TeaModel):
    def __init__(self, color=None, flow_tag_group_id=None, name=None):
        self.color = color  # type: str
        self.flow_tag_group_id = flow_tag_group_id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['color'] = self.color
        if self.flow_tag_group_id is not None:
            result['flowTagGroupId'] = self.flow_tag_group_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('color') is not None:
            self.color = m.get('color')
        if m.get('flowTagGroupId') is not None:
            self.flow_tag_group_id = m.get('flowTagGroupId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateFlowTagResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, id=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        self.id = id  # type: long
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateFlowTagResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFlowTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowTagResponse, self).to_map()
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
            temp_model = CreateFlowTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowTagGroupRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowTagGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateFlowTagGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, id=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 标签分类
        self.id = id  # type: long
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFlowTagGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateFlowTagGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateFlowTagGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFlowTagGroupResponse, self).to_map()
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
            temp_model = CreateFlowTagGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostGroupRequest(TeaModel):
    def __init__(self, aliyun_region=None, ecs_label_key=None, ecs_label_value=None, ecs_type=None, env_id=None,
                 machine_infos=None, name=None, service_connection_id=None, tag_ids=None, type=None):
        self.aliyun_region = aliyun_region  # type: str
        self.ecs_label_key = ecs_label_key  # type: str
        self.ecs_label_value = ecs_label_value  # type: str
        self.ecs_type = ecs_type  # type: str
        self.env_id = env_id  # type: str
        self.machine_infos = machine_infos  # type: str
        self.name = name  # type: str
        self.service_connection_id = service_connection_id  # type: long
        self.tag_ids = tag_ids  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_region is not None:
            result['aliyunRegion'] = self.aliyun_region
        if self.ecs_label_key is not None:
            result['ecsLabelKey'] = self.ecs_label_key
        if self.ecs_label_value is not None:
            result['ecsLabelValue'] = self.ecs_label_value
        if self.ecs_type is not None:
            result['ecsType'] = self.ecs_type
        if self.env_id is not None:
            result['envId'] = self.env_id
        if self.machine_infos is not None:
            result['machineInfos'] = self.machine_infos
        if self.name is not None:
            result['name'] = self.name
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        if self.tag_ids is not None:
            result['tagIds'] = self.tag_ids
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunRegion') is not None:
            self.aliyun_region = m.get('aliyunRegion')
        if m.get('ecsLabelKey') is not None:
            self.ecs_label_key = m.get('ecsLabelKey')
        if m.get('ecsLabelValue') is not None:
            self.ecs_label_value = m.get('ecsLabelValue')
        if m.get('ecsType') is not None:
            self.ecs_type = m.get('ecsType')
        if m.get('envId') is not None:
            self.env_id = m.get('envId')
        if m.get('machineInfos') is not None:
            self.machine_infos = m.get('machineInfos')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        if m.get('tagIds') is not None:
            self.tag_ids = m.get('tagIds')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateHostGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, host_group_id=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.host_group_id = host_group_id  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.host_group_id is not None:
            result['hostGroupId'] = self.host_group_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('hostGroupId') is not None:
            self.host_group_id = m.get('hostGroupId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateHostGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHostGroupResponse, self).to_map()
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
            temp_model = CreateHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, custom_code=None, name=None, scope=None, template_identifier=None):
        self.custom_code = custom_code  # type: str
        self.name = name  # type: str
        self.scope = scope  # type: str
        self.template_identifier = template_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_code is not None:
            result['customCode'] = self.custom_code
        if self.name is not None:
            result['name'] = self.name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.template_identifier is not None:
            result['templateIdentifier'] = self.template_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('customCode') is not None:
            self.custom_code = m.get('customCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('templateIdentifier') is not None:
            self.template_identifier = m.get('templateIdentifier')
        return self


class CreateProjectResponseBodyProject(TeaModel):
    def __init__(self, category_identifier=None, creator=None, custom_code=None, description=None, gmt_create=None,
                 gmt_modified=None, icon=None, identifier=None, logical_status=None, modifier=None, name=None,
                 organization_identifier=None, scope=None, status_identifier=None, status_stage_identifier=None, type_identifier=None):
        # 空间大类id
        self.category_identifier = category_identifier  # type: str
        # 创建人id
        self.creator = creator  # type: str
        # 自定义编号
        self.custom_code = custom_code  # type: str
        # 描述信息
        self.description = description  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 图标
        self.icon = icon  # type: str
        # 项目唯一标识符
        self.identifier = identifier  # type: str
        # 项目状态
        self.logical_status = logical_status  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 项目名称
        self.name = name  # type: str
        # 企业id
        self.organization_identifier = organization_identifier  # type: str
        # 可见范围
        self.scope = scope  # type: str
        # 状态id
        self.status_identifier = status_identifier  # type: str
        # 状态阶段
        self.status_stage_identifier = status_stage_identifier  # type: str
        # 空间小类id
        self.type_identifier = type_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_identifier is not None:
            result['categoryIdentifier'] = self.category_identifier
        if self.creator is not None:
            result['creator'] = self.creator
        if self.custom_code is not None:
            result['customCode'] = self.custom_code
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.icon is not None:
            result['icon'] = self.icon
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.logical_status is not None:
            result['logicalStatus'] = self.logical_status
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.organization_identifier is not None:
            result['organizationIdentifier'] = self.organization_identifier
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status_identifier is not None:
            result['statusIdentifier'] = self.status_identifier
        if self.status_stage_identifier is not None:
            result['statusStageIdentifier'] = self.status_stage_identifier
        if self.type_identifier is not None:
            result['typeIdentifier'] = self.type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('categoryIdentifier') is not None:
            self.category_identifier = m.get('categoryIdentifier')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('customCode') is not None:
            self.custom_code = m.get('customCode')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('logicalStatus') is not None:
            self.logical_status = m.get('logicalStatus')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('organizationIdentifier') is not None:
            self.organization_identifier = m.get('organizationIdentifier')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('statusIdentifier') is not None:
            self.status_identifier = m.get('statusIdentifier')
        if m.get('statusStageIdentifier') is not None:
            self.status_stage_identifier = m.get('statusStageIdentifier')
        if m.get('typeIdentifier') is not None:
            self.type_identifier = m.get('typeIdentifier')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, project=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 项目信息
        self.project = project  # type: CreateProjectResponseBodyProject
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.project is not None:
            result['project'] = self.project.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('project') is not None:
            temp_model = CreateProjectResponseBodyProject()
            self.project = temp_model.from_map(m['project'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryRequestImportSvnRepoConfig(TeaModel):
    def __init__(self, author_mapping=None, branch_mapping=None, no_branches=None, no_tags=None, password=None,
                 path=None, root_is_trunk=None, standard_layout=None, svn_import_url=None, tag_mapping=None,
                 trunk_mapping=None, username=None):
        # author 映射
        self.author_mapping = author_mapping  # type: str
        # 分支映射
        self.branch_mapping = branch_mapping  # type: str
        # 不导入branch
        self.no_branches = no_branches  # type: bool
        # 不导入tag
        self.no_tags = no_tags  # type: bool
        # svn密码
        self.password = password  # type: str
        # 导入代码库目标path
        self.path = path  # type: str
        # 根目录映射trunk
        self.root_is_trunk = root_is_trunk  # type: bool
        # 标准布局
        self.standard_layout = standard_layout  # type: bool
        # svn仓库地址
        self.svn_import_url = svn_import_url  # type: str
        # 标签映射
        self.tag_mapping = tag_mapping  # type: str
        # trunk映射
        self.trunk_mapping = trunk_mapping  # type: str
        # svn用户名
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryRequestImportSvnRepoConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_mapping is not None:
            result['authorMapping'] = self.author_mapping
        if self.branch_mapping is not None:
            result['branchMapping'] = self.branch_mapping
        if self.no_branches is not None:
            result['noBranches'] = self.no_branches
        if self.no_tags is not None:
            result['noTags'] = self.no_tags
        if self.password is not None:
            result['password'] = self.password
        if self.path is not None:
            result['path'] = self.path
        if self.root_is_trunk is not None:
            result['rootIsTrunk'] = self.root_is_trunk
        if self.standard_layout is not None:
            result['standardLayout'] = self.standard_layout
        if self.svn_import_url is not None:
            result['svnImportUrl'] = self.svn_import_url
        if self.tag_mapping is not None:
            result['tagMapping'] = self.tag_mapping
        if self.trunk_mapping is not None:
            result['trunkMapping'] = self.trunk_mapping
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authorMapping') is not None:
            self.author_mapping = m.get('authorMapping')
        if m.get('branchMapping') is not None:
            self.branch_mapping = m.get('branchMapping')
        if m.get('noBranches') is not None:
            self.no_branches = m.get('noBranches')
        if m.get('noTags') is not None:
            self.no_tags = m.get('noTags')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('rootIsTrunk') is not None:
            self.root_is_trunk = m.get('rootIsTrunk')
        if m.get('standardLayout') is not None:
            self.standard_layout = m.get('standardLayout')
        if m.get('svnImportUrl') is not None:
            self.svn_import_url = m.get('svnImportUrl')
        if m.get('tagMapping') is not None:
            self.tag_mapping = m.get('tagMapping')
        if m.get('trunkMapping') is not None:
            self.trunk_mapping = m.get('trunkMapping')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class CreateRepositoryRequest(TeaModel):
    def __init__(self, access_token=None, avatar_url=None, description=None, gitignore_type=None,
                 import_account=None, import_demo_project=None, import_repo_type=None, import_svn_repo_config=None,
                 import_token=None, import_token_encrypted=None, import_url=None, init_standard_service=None,
                 is_crypto_enabled=None, local_import_url=None, name=None, namespace_id=None, path=None, readme_type=None,
                 visibility_level=None, create_parent_path=None, organization_id=None, sync=None):
        self.access_token = access_token  # type: str
        # 代码库头像地址
        self.avatar_url = avatar_url  # type: str
        # 代码库描述
        self.description = description  # type: str
        # gitignore模板类型
        self.gitignore_type = gitignore_type  # type: str
        # 导入时使用的账号
        self.import_account = import_account  # type: str
        # 使用使用demo库内容进行初始化
        self.import_demo_project = import_demo_project  # type: bool
        # 导入代码库类型 (GIT: Git库, SVN: SVN库)
        self.import_repo_type = import_repo_type  # type: str
        # 导入SVN库的设置
        self.import_svn_repo_config = import_svn_repo_config  # type: CreateRepositoryRequestImportSvnRepoConfig
        # 导入时账号的token
        self.import_token = import_token  # type: str
        # import_token字段的传输格式，使用明文或rsa加密
        self.import_token_encrypted = import_token_encrypted  # type: str
        # 导入地址（http协议地址）
        self.import_url = import_url  # type: str
        # 初始化标准智能化服务
        self.init_standard_service = init_standard_service  # type: bool
        # 是否启用加密
        self.is_crypto_enabled = is_crypto_enabled  # type: bool
        # 本地导入代码库的远程地址
        self.local_import_url = local_import_url  # type: str
        # 代码库名称
        self.name = name  # type: str
        # 代码库父路径id
        self.namespace_id = namespace_id  # type: long
        # 代码库路径
        self.path = path  # type: str
        # 自动创建readme类型 (EMPTY: 仅创建README.md, USER_GUIDE: 包含新手引导)
        self.readme_type = readme_type  # type: str
        self.visibility_level = visibility_level  # type: int
        self.create_parent_path = create_parent_path  # type: bool
        self.organization_id = organization_id  # type: str
        self.sync = sync  # type: bool

    def validate(self):
        if self.import_svn_repo_config:
            self.import_svn_repo_config.validate()

    def to_map(self):
        _map = super(CreateRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.description is not None:
            result['description'] = self.description
        if self.gitignore_type is not None:
            result['gitignoreType'] = self.gitignore_type
        if self.import_account is not None:
            result['importAccount'] = self.import_account
        if self.import_demo_project is not None:
            result['importDemoProject'] = self.import_demo_project
        if self.import_repo_type is not None:
            result['importRepoType'] = self.import_repo_type
        if self.import_svn_repo_config is not None:
            result['importSvnRepoConfig'] = self.import_svn_repo_config.to_map()
        if self.import_token is not None:
            result['importToken'] = self.import_token
        if self.import_token_encrypted is not None:
            result['importTokenEncrypted'] = self.import_token_encrypted
        if self.import_url is not None:
            result['importUrl'] = self.import_url
        if self.init_standard_service is not None:
            result['initStandardService'] = self.init_standard_service
        if self.is_crypto_enabled is not None:
            result['isCryptoEnabled'] = self.is_crypto_enabled
        if self.local_import_url is not None:
            result['localImportUrl'] = self.local_import_url
        if self.name is not None:
            result['name'] = self.name
        if self.namespace_id is not None:
            result['namespaceId'] = self.namespace_id
        if self.path is not None:
            result['path'] = self.path
        if self.readme_type is not None:
            result['readmeType'] = self.readme_type
        if self.visibility_level is not None:
            result['visibilityLevel'] = self.visibility_level
        if self.create_parent_path is not None:
            result['createParentPath'] = self.create_parent_path
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        if self.sync is not None:
            result['sync'] = self.sync
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gitignoreType') is not None:
            self.gitignore_type = m.get('gitignoreType')
        if m.get('importAccount') is not None:
            self.import_account = m.get('importAccount')
        if m.get('importDemoProject') is not None:
            self.import_demo_project = m.get('importDemoProject')
        if m.get('importRepoType') is not None:
            self.import_repo_type = m.get('importRepoType')
        if m.get('importSvnRepoConfig') is not None:
            temp_model = CreateRepositoryRequestImportSvnRepoConfig()
            self.import_svn_repo_config = temp_model.from_map(m['importSvnRepoConfig'])
        if m.get('importToken') is not None:
            self.import_token = m.get('importToken')
        if m.get('importTokenEncrypted') is not None:
            self.import_token_encrypted = m.get('importTokenEncrypted')
        if m.get('importUrl') is not None:
            self.import_url = m.get('importUrl')
        if m.get('initStandardService') is not None:
            self.init_standard_service = m.get('initStandardService')
        if m.get('isCryptoEnabled') is not None:
            self.is_crypto_enabled = m.get('isCryptoEnabled')
        if m.get('localImportUrl') is not None:
            self.local_import_url = m.get('localImportUrl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespaceId') is not None:
            self.namespace_id = m.get('namespaceId')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('readmeType') is not None:
            self.readme_type = m.get('readmeType')
        if m.get('visibilityLevel') is not None:
            self.visibility_level = m.get('visibilityLevel')
        if m.get('createParentPath') is not None:
            self.create_parent_path = m.get('createParentPath')
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        if m.get('sync') is not None:
            self.sync = m.get('sync')
        return self


class CreateRepositoryResponseBodyResultNamespace(TeaModel):
    def __init__(self, avatar=None, created_at=None, description=None, id=None, name=None, owner_id=None, path=None,
                 public=None, updated_at=None, visibility_level=None):
        # 头像地址
        self.avatar = avatar  # type: str
        # 创建时间
        self.created_at = created_at  # type: str
        # 描述
        self.description = description  # type: str
        # id
        self.id = id  # type: long
        # 名称
        self.name = name  # type: str
        # 归属者id
        self.owner_id = owner_id  # type: long
        # 路径
        self.path = path  # type: str
        # 公开性
        self.public = public  # type: bool
        # 更新时间
        self.updated_at = updated_at  # type: str
        # 可见性。0：私有，10：内部公开
        self.visibility_level = visibility_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRepositoryResponseBodyResultNamespace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.path is not None:
            result['path'] = self.path
        if self.public is not None:
            result['public'] = self.public
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.visibility_level is not None:
            result['visibilityLevel'] = self.visibility_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('public') is not None:
            self.public = m.get('public')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('visibilityLevel') is not None:
            self.visibility_level = m.get('visibilityLevel')
        return self


class CreateRepositoryResponseBodyResult(TeaModel):
    def __init__(self, import_from_svn=None, archived=None, avatar_url=None, created_at=None, creator_id=None,
                 default_branch=None, demo_project=None, description=None, http_url_to_repo=None, id=None, last_activity_at=None,
                 name=None, name_with_namespace=None, namespace=None, path=None, path_with_namespace=None,
                 ssh_url_to_repo=None, visibility_level=None, web_url=None):
        # 从SVN导入
        self.import_from_svn = import_from_svn  # type: bool
        # 归档标识
        self.archived = archived  # type: bool
        # 代码库头像地址
        self.avatar_url = avatar_url  # type: str
        # 创建时间
        self.created_at = created_at  # type: str
        # 创建者id
        self.creator_id = creator_id  # type: long
        # 默认分支
        self.default_branch = default_branch  # type: str
        # demo库标识
        self.demo_project = demo_project  # type: bool
        # 描述
        self.description = description  # type: str
        # http地址
        self.http_url_to_repo = http_url_to_repo  # type: str
        # id
        self.id = id  # type: long
        # 最后活跃时间
        self.last_activity_at = last_activity_at  # type: str
        # 名称
        self.name = name  # type: str
        # 名称（含父路径）
        self.name_with_namespace = name_with_namespace  # type: str
        # 父路径信息
        self.namespace = namespace  # type: CreateRepositoryResponseBodyResultNamespace
        # 路径
        self.path = path  # type: str
        # 路径（含父路径）
        self.path_with_namespace = path_with_namespace  # type: str
        # ssh地址
        self.ssh_url_to_repo = ssh_url_to_repo  # type: str
        # 可见性。0：私有，10：内部公开
        self.visibility_level = visibility_level  # type: str
        # web url
        self.web_url = web_url  # type: str

    def validate(self):
        if self.namespace:
            self.namespace.validate()

    def to_map(self):
        _map = super(CreateRepositoryResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_from_svn is not None:
            result['Import_from_svn'] = self.import_from_svn
        if self.archived is not None:
            result['archived'] = self.archived
        if self.avatar_url is not None:
            result['avatar_url'] = self.avatar_url
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.default_branch is not None:
            result['defaultBranch'] = self.default_branch
        if self.demo_project is not None:
            result['demoProject'] = self.demo_project
        if self.description is not None:
            result['description'] = self.description
        if self.http_url_to_repo is not None:
            result['httpUrlToRepo'] = self.http_url_to_repo
        if self.id is not None:
            result['id'] = self.id
        if self.last_activity_at is not None:
            result['lastActivityAt'] = self.last_activity_at
        if self.name is not None:
            result['name'] = self.name
        if self.name_with_namespace is not None:
            result['nameWithNamespace'] = self.name_with_namespace
        if self.namespace is not None:
            result['namespace'] = self.namespace.to_map()
        if self.path is not None:
            result['path'] = self.path
        if self.path_with_namespace is not None:
            result['pathWithNamespace'] = self.path_with_namespace
        if self.ssh_url_to_repo is not None:
            result['sshUrlToRepo'] = self.ssh_url_to_repo
        if self.visibility_level is not None:
            result['visibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['webUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Import_from_svn') is not None:
            self.import_from_svn = m.get('Import_from_svn')
        if m.get('archived') is not None:
            self.archived = m.get('archived')
        if m.get('avatar_url') is not None:
            self.avatar_url = m.get('avatar_url')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('defaultBranch') is not None:
            self.default_branch = m.get('defaultBranch')
        if m.get('demoProject') is not None:
            self.demo_project = m.get('demoProject')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('httpUrlToRepo') is not None:
            self.http_url_to_repo = m.get('httpUrlToRepo')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastActivityAt') is not None:
            self.last_activity_at = m.get('lastActivityAt')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameWithNamespace') is not None:
            self.name_with_namespace = m.get('nameWithNamespace')
        if m.get('namespace') is not None:
            temp_model = CreateRepositoryResponseBodyResultNamespace()
            self.namespace = temp_model.from_map(m['namespace'])
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('pathWithNamespace') is not None:
            self.path_with_namespace = m.get('pathWithNamespace')
        if m.get('sshUrlToRepo') is not None:
            self.ssh_url_to_repo = m.get('sshUrlToRepo')
        if m.get('visibilityLevel') is not None:
            self.visibility_level = m.get('visibilityLevel')
        if m.get('webUrl') is not None:
            self.web_url = m.get('webUrl')
        return self


class CreateRepositoryResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateRepositoryResponseBodyResult
        # 调用是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = CreateRepositoryResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateRepositoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRepositoryResponse, self).to_map()
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
            temp_model = CreateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceMemberRequest(TeaModel):
    def __init__(self, account_id=None, role_name=None):
        # 用户id
        self.account_id = account_id  # type: str
        # 角色部署组 deployGroup   user  成员，使用权限   admin 管理员，使用编辑权限 流水线 pipeline   admin 查看、运行、编辑权限   member  运行权限   viewer 查看权限
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.role_name is not None:
            result['roleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        return self


class CreateResourceMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateResourceMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateResourceMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceMemberResponse, self).to_map()
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
            temp_model = CreateResourceMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSprintRequest(TeaModel):
    def __init__(self, end_date=None, name=None, space_identifier=None, staff_ids=None, start_date=None):
        # 结束时间
        self.end_date = end_date  # type: str
        # 迭代名
        self.name = name  # type: str
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 负责人列表
        self.staff_ids = staff_ids  # type: list[str]
        # 开始时间
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSprintRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.name is not None:
            result['name'] = self.name
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.staff_ids is not None:
            result['staffIds'] = self.staff_ids
        if self.start_date is not None:
            result['startDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('staffIds') is not None:
            self.staff_ids = m.get('staffIds')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        return self


class CreateSprintResponseBodySprint(TeaModel):
    def __init__(self, creator=None, description=None, end_date=None, gmt_create=None, gmt_modified=None,
                 identifier=None, modifier=None, name=None, scope=None, space_identifier=None, start_date=None, status=None):
        # 创建人id
        self.creator = creator  # type: str
        # 描述信息
        self.description = description  # type: str
        # 结束时间
        self.end_date = end_date  # type: long
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 迭代唯一标识符
        self.identifier = identifier  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 迭代名称
        self.name = name  # type: str
        # 可见范围
        self.scope = scope  # type: str
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 开始时间
        self.start_date = start_date  # type: long
        # 状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSprintResponseBodySprint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateSprintResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, sprint=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 迭代信息
        self.sprint = sprint  # type: CreateSprintResponseBodySprint
        # true或者false
        self.success = success  # type: bool

    def validate(self):
        if self.sprint:
            self.sprint.validate()

    def to_map(self):
        _map = super(CreateSprintResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.sprint is not None:
            result['sprint'] = self.sprint.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sprint') is not None:
            temp_model = CreateSprintResponseBodySprint()
            self.sprint = temp_model.from_map(m['sprint'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSprintResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSprintResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSprintResponse, self).to_map()
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
            temp_model = CreateSprintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSshKeyResponseBodySshKey(TeaModel):
    def __init__(self, id=None, public_key=None):
        # 企业公钥id
        self.id = id  # type: long
        # 企业公钥
        self.public_key = public_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSshKeyResponseBodySshKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.public_key is not None:
            result['publicKey'] = self.public_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('publicKey') is not None:
            self.public_key = m.get('publicKey')
        return self


class CreateSshKeyResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, ssh_key=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 企业公钥
        self.ssh_key = ssh_key  # type: CreateSshKeyResponseBodySshKey
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.ssh_key:
            self.ssh_key.validate()

    def to_map(self):
        _map = super(CreateSshKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.ssh_key is not None:
            result['sshKey'] = self.ssh_key.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sshKey') is not None:
            temp_model = CreateSshKeyResponseBodySshKey()
            self.ssh_key = temp_model.from_map(m['sshKey'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSshKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSshKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSshKeyResponse, self).to_map()
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
            temp_model = CreateSshKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVariableGroupRequest(TeaModel):
    def __init__(self, description=None, name=None, variables=None):
        # 变量组描述
        self.description = description  # type: str
        # 变量组名称
        self.name = name  # type: str
        # 变量信息json字符串 isEncrypted 是否加密 name 变量名称 value 变量值
        self.variables = variables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVariableGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.variables is not None:
            result['variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('variables') is not None:
            self.variables = m.get('variables')
        return self


class CreateVariableGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None, variable_group_id=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 新建的变量组id
        self.variable_group_id = variable_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVariableGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.variable_group_id is not None:
            result['variableGroupId'] = self.variable_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('variableGroupId') is not None:
            self.variable_group_id = m.get('variableGroupId')
        return self


class CreateVariableGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVariableGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVariableGroupResponse, self).to_map()
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
            temp_model = CreateVariableGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkitemRequestFieldValueList(TeaModel):
    def __init__(self, field_identifier=None, value=None, workitem_identifier=None):
        # 字段唯一标识
        self.field_identifier = field_identifier  # type: str
        # 字段值，写入时使用
        self.value = value  # type: str
        # 工作项的唯一标识
        self.workitem_identifier = workitem_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkitemRequestFieldValueList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_identifier is not None:
            result['fieldIdentifier'] = self.field_identifier
        if self.value is not None:
            result['value'] = self.value
        if self.workitem_identifier is not None:
            result['workitemIdentifier'] = self.workitem_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fieldIdentifier') is not None:
            self.field_identifier = m.get('fieldIdentifier')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('workitemIdentifier') is not None:
            self.workitem_identifier = m.get('workitemIdentifier')
        return self


class CreateWorkitemRequest(TeaModel):
    def __init__(self, assigned_to=None, category=None, description=None, description_format=None,
                 field_value_list=None, participant=None, space=None, space_identifier=None, space_type=None, sprint=None,
                 subject=None, tracker=None, verifier=None, workitem_type=None):
        # 工作项负责人的id，或者企业中的用户名
        self.assigned_to = assigned_to  # type: str
        # 工作项的类型id，比如：Bug、Task对应id
        self.category = category  # type: str
        # 工作项内容
        self.description = description  # type: str
        # 内容格式
        self.description_format = description_format  # type: str
        # 自定义字段
        self.field_value_list = field_value_list  # type: list[CreateWorkitemRequestFieldValueList]
        # 参与人id列表，或者企业名称列表
        self.participant = participant  # type: list[str]
        # 项目id
        self.space = space  # type: str
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 资源类型
        self.space_type = space_type  # type: str
        # 要关联迭代
        self.sprint = sprint  # type: list[str]
        # 标题
        self.subject = subject  # type: str
        # 抄送人id列表
        self.tracker = tracker  # type: list[str]
        # 验证者id列表，或者企业名称列表
        self.verifier = verifier  # type: list[str]
        # 工作项小类型id
        self.workitem_type = workitem_type  # type: str

    def validate(self):
        if self.field_value_list:
            for k in self.field_value_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateWorkitemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assigned_to is not None:
            result['assignedTo'] = self.assigned_to
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.description_format is not None:
            result['descriptionFormat'] = self.description_format
        result['fieldValueList'] = []
        if self.field_value_list is not None:
            for k in self.field_value_list:
                result['fieldValueList'].append(k.to_map() if k else None)
        if self.participant is not None:
            result['participant'] = self.participant
        if self.space is not None:
            result['space'] = self.space
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.sprint is not None:
            result['sprint'] = self.sprint
        if self.subject is not None:
            result['subject'] = self.subject
        if self.tracker is not None:
            result['tracker'] = self.tracker
        if self.verifier is not None:
            result['verifier'] = self.verifier
        if self.workitem_type is not None:
            result['workitemType'] = self.workitem_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignedTo') is not None:
            self.assigned_to = m.get('assignedTo')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('descriptionFormat') is not None:
            self.description_format = m.get('descriptionFormat')
        self.field_value_list = []
        if m.get('fieldValueList') is not None:
            for k in m.get('fieldValueList'):
                temp_model = CreateWorkitemRequestFieldValueList()
                self.field_value_list.append(temp_model.from_map(k))
        if m.get('participant') is not None:
            self.participant = m.get('participant')
        if m.get('space') is not None:
            self.space = m.get('space')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('sprint') is not None:
            self.sprint = m.get('sprint')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('tracker') is not None:
            self.tracker = m.get('tracker')
        if m.get('verifier') is not None:
            self.verifier = m.get('verifier')
        if m.get('workitemType') is not None:
            self.workitem_type = m.get('workitemType')
        return self


class CreateWorkitemResponseBodyWorkitem(TeaModel):
    def __init__(self, assigned_to=None, category_identifier=None, creator=None, document=None, gmt_create=None,
                 gmt_modified=None, identifier=None, logical_status=None, modifier=None, parent_identifier=None,
                 serial_number=None, space_identifier=None, space_name=None, space_type=None, status=None, status_identifier=None,
                 status_stage_identifier=None, subject=None, update_status_at=None, workitem_type_identifier=None):
        # 负责人
        self.assigned_to = assigned_to  # type: str
        # 工作项的类型id
        self.category_identifier = category_identifier  # type: str
        # 创建人
        self.creator = creator  # type: str
        # 工作项内容
        self.document = document  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 工作项唯一标识
        self.identifier = identifier  # type: str
        # 逻辑状态
        self.logical_status = logical_status  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 父工作项id
        self.parent_identifier = parent_identifier  # type: str
        # 编号
        self.serial_number = serial_number  # type: str
        # 所属项目id
        self.space_identifier = space_identifier  # type: str
        # 所属项目名称
        self.space_name = space_name  # type: str
        # 项目类型
        self.space_type = space_type  # type: str
        # 状态名称
        self.status = status  # type: str
        # 状态唯一标识id
        self.status_identifier = status_identifier  # type: str
        # 状态阶段id
        self.status_stage_identifier = status_stage_identifier  # type: str
        # 工作项标题
        self.subject = subject  # type: str
        # 状态更新时间
        self.update_status_at = update_status_at  # type: long
        # 工作项类型id
        self.workitem_type_identifier = workitem_type_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkitemResponseBodyWorkitem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assigned_to is not None:
            result['assignedTo'] = self.assigned_to
        if self.category_identifier is not None:
            result['categoryIdentifier'] = self.category_identifier
        if self.creator is not None:
            result['creator'] = self.creator
        if self.document is not None:
            result['document'] = self.document
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.logical_status is not None:
            result['logicalStatus'] = self.logical_status
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.parent_identifier is not None:
            result['parentIdentifier'] = self.parent_identifier
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.status is not None:
            result['status'] = self.status
        if self.status_identifier is not None:
            result['statusIdentifier'] = self.status_identifier
        if self.status_stage_identifier is not None:
            result['statusStageIdentifier'] = self.status_stage_identifier
        if self.subject is not None:
            result['subject'] = self.subject
        if self.update_status_at is not None:
            result['updateStatusAt'] = self.update_status_at
        if self.workitem_type_identifier is not None:
            result['workitemTypeIdentifier'] = self.workitem_type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignedTo') is not None:
            self.assigned_to = m.get('assignedTo')
        if m.get('categoryIdentifier') is not None:
            self.category_identifier = m.get('categoryIdentifier')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('logicalStatus') is not None:
            self.logical_status = m.get('logicalStatus')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('parentIdentifier') is not None:
            self.parent_identifier = m.get('parentIdentifier')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusIdentifier') is not None:
            self.status_identifier = m.get('statusIdentifier')
        if m.get('statusStageIdentifier') is not None:
            self.status_stage_identifier = m.get('statusStageIdentifier')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('updateStatusAt') is not None:
            self.update_status_at = m.get('updateStatusAt')
        if m.get('workitemTypeIdentifier') is not None:
            self.workitem_type_identifier = m.get('workitemTypeIdentifier')
        return self


class CreateWorkitemResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None, workitem=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool
        # 工作项信息
        self.workitem = workitem  # type: CreateWorkitemResponseBodyWorkitem

    def validate(self):
        if self.workitem:
            self.workitem.validate()

    def to_map(self):
        _map = super(CreateWorkitemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.workitem is not None:
            result['workitem'] = self.workitem.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('workitem') is not None:
            temp_model = CreateWorkitemResponseBodyWorkitem()
            self.workitem = temp_model.from_map(m['workitem'])
        return self


class CreateWorkitemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateWorkitemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWorkitemResponse, self).to_map()
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
            temp_model = CreateWorkitemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkspaceRequest(TeaModel):
    def __init__(self, code_url=None, code_version=None, file_path=None, name=None, request_from=None,
                 resource_identifier=None, reuse=None, workspace_template=None):
        # 代码来源URL（当前仅支持云效 Codeup 来源）
        self.code_url = code_url  # type: str
        # 代码版本，支持 commitSHA、分支、标签
        self.code_version = code_version  # type: str
        # 打开空间默认打开的文件相对路径
        self.file_path = file_path  # type: str
        # 工作空间名称
        self.name = name  # type: str
        # 请求来源（用于统计，云产品集成时需要传入）
        self.request_from = request_from  # type: str
        # 资源标识，提供给非标代码源作为空间复用的唯一标识
        self.resource_identifier = resource_identifier  # type: str
        # 工作空间复用标识，按照"用户+技术栈+代码地址+版本"进行复用 true - 复用 false - 不复用，每次均为新创建
        self.reuse = reuse  # type: bool
        # 技术栈
        self.workspace_template = workspace_template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_url is not None:
            result['codeUrl'] = self.code_url
        if self.code_version is not None:
            result['codeVersion'] = self.code_version
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.name is not None:
            result['name'] = self.name
        if self.request_from is not None:
            result['requestFrom'] = self.request_from
        if self.resource_identifier is not None:
            result['resourceIdentifier'] = self.resource_identifier
        if self.reuse is not None:
            result['reuse'] = self.reuse
        if self.workspace_template is not None:
            result['workspaceTemplate'] = self.workspace_template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('codeUrl') is not None:
            self.code_url = m.get('codeUrl')
        if m.get('codeVersion') is not None:
            self.code_version = m.get('codeVersion')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestFrom') is not None:
            self.request_from = m.get('requestFrom')
        if m.get('resourceIdentifier') is not None:
            self.resource_identifier = m.get('resourceIdentifier')
        if m.get('reuse') is not None:
            self.reuse = m.get('reuse')
        if m.get('workspaceTemplate') is not None:
            self.workspace_template = m.get('workspaceTemplate')
        return self


class CreateWorkspaceResponseBodyWorkspace(TeaModel):
    def __init__(self, create_time=None, creator=None, id=None, name=None, status=None, template=None):
        # 创建时间戳
        self.create_time = create_time  # type: str
        # 创建者，阿里云PK
        self.creator = creator  # type: str
        # 工作空间唯一标识，字符串形式，可在云效DevStudio访问空间链接中获取
        self.id = id  # type: str
        # 工作空间名称
        self.name = name  # type: str
        # 空间状态，枚举：CREATING-创建中, SUCCESS-运行中, FROZEN-冻结中, RECOVERING-恢复中
        self.status = status  # type: str
        # 工作空间模板
        self.template = template  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceResponseBodyWorkspace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.template is not None:
            result['template'] = self.template
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template') is not None:
            self.template = m.get('template')
        return self


class CreateWorkspaceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None, workspace=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool
        # 工作空间信息
        self.workspace = workspace  # type: CreateWorkspaceResponseBodyWorkspace

    def validate(self):
        if self.workspace:
            self.workspace.validate()

    def to_map(self):
        _map = super(CreateWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.workspace is not None:
            result['workspace'] = self.workspace.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('workspace') is not None:
            temp_model = CreateWorkspaceResponseBodyWorkspace()
            self.workspace = temp_model.from_map(m['workspace'])
        return self


class CreateWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateWorkspaceResponse, self).to_map()
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
            temp_model = CreateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowTagResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteFlowTagResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFlowTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowTagResponse, self).to_map()
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
            temp_model = DeleteFlowTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowTagGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFlowTagGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteFlowTagGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteFlowTagGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFlowTagGroupResponse, self).to_map()
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
            temp_model = DeleteFlowTagGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteHostGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHostGroupResponse, self).to_map()
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
            temp_model = DeleteHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePipelineResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeletePipelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeletePipelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePipelineResponse, self).to_map()
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
            temp_model = DeletePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(self, identifier=None):
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['identifier'] = self.identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, result=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.result = result  # type: bool
        # true或者false
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteResourceMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteResourceMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceMemberResponse, self).to_map()
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
            temp_model = DeleteResourceMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVariableGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVariableGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteVariableGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteVariableGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVariableGroupResponse, self).to_map()
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
            temp_model = DeleteVariableGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FrozenWorkspaceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(FrozenWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class FrozenWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FrozenWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FrozenWorkspaceResponse, self).to_map()
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
            temp_model = FrozenWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeupOrganizationRequest(TeaModel):
    def __init__(self, access_token=None):
        self.access_token = access_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeupOrganizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        return self


class GetCodeupOrganizationResponseBodyResult(TeaModel):
    def __init__(self, created_at=None, id=None, namespace_id=None, organization_id=None, path=None, updated_at=None,
                 user_role=None):
        self.created_at = created_at  # type: str
        self.id = id  # type: long
        self.namespace_id = namespace_id  # type: long
        self.organization_id = organization_id  # type: str
        self.path = path  # type: str
        self.updated_at = updated_at  # type: str
        self.user_role = user_role  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCodeupOrganizationResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.path is not None:
            result['Path'] = self.path
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.user_role is not None:
            result['UserRole'] = self.user_role
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('UserRole') is not None:
            self.user_role = m.get('UserRole')
        return self


class GetCodeupOrganizationResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetCodeupOrganizationResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetCodeupOrganizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetCodeupOrganizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCodeupOrganizationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCodeupOrganizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCodeupOrganizationResponse, self).to_map()
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
            temp_model = GetCodeupOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomFieldOptionRequest(TeaModel):
    def __init__(self, space_identifier=None, space_type=None, workitem_type_identifier=None):
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 类型
        self.space_type = space_type  # type: str
        # 工作项类型id
        self.workitem_type_identifier = workitem_type_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomFieldOptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.workitem_type_identifier is not None:
            result['workitemTypeIdentifier'] = self.workitem_type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('workitemTypeIdentifier') is not None:
            self.workitem_type_identifier = m.get('workitemTypeIdentifier')
        return self


class GetCustomFieldOptionResponseBodyFileds(TeaModel):
    def __init__(self, display_value=None, field_identifier=None, identifier=None, level=None, position=None,
                 value=None, value_en=None):
        # 展示的值
        self.display_value = display_value  # type: str
        # 字段唯一标识
        self.field_identifier = field_identifier  # type: str
        # 迭代唯一标识符
        self.identifier = identifier  # type: str
        # 展示级别，数字范围1~9，数字越大，颜色越浅
        self.level = level  # type: long
        # 待选值顺序
        self.position = position  # type: long
        # 字段中文名称
        self.value = value  # type: str
        # 字段英文名称
        self.value_en = value_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomFieldOptionResponseBodyFileds, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_value is not None:
            result['displayValue'] = self.display_value
        if self.field_identifier is not None:
            result['fieldIdentifier'] = self.field_identifier
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.level is not None:
            result['level'] = self.level
        if self.position is not None:
            result['position'] = self.position
        if self.value is not None:
            result['value'] = self.value
        if self.value_en is not None:
            result['valueEn'] = self.value_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayValue') is not None:
            self.display_value = m.get('displayValue')
        if m.get('fieldIdentifier') is not None:
            self.field_identifier = m.get('fieldIdentifier')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueEn') is not None:
            self.value_en = m.get('valueEn')
        return self


class GetCustomFieldOptionResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, fileds=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 字段值信息
        self.fileds = fileds  # type: list[GetCustomFieldOptionResponseBodyFileds]
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool

    def validate(self):
        if self.fileds:
            for k in self.fileds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCustomFieldOptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        result['fileds'] = []
        if self.fileds is not None:
            for k in self.fileds:
                result['fileds'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        self.fileds = []
        if m.get('fileds') is not None:
            for k in m.get('fileds'):
                temp_model = GetCustomFieldOptionResponseBodyFileds()
                self.fileds.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetCustomFieldOptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCustomFieldOptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCustomFieldOptionResponse, self).to_map()
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
            temp_model = GetCustomFieldOptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileLastCommitRequest(TeaModel):
    def __init__(self, access_token=None, filepath=None, organization_id=None, sha=None):
        # 个人访问令牌
        self.access_token = access_token  # type: str
        # 文件路径
        self.filepath = filepath  # type: str
        # 云效企业ID
        self.organization_id = organization_id  # type: str
        # 分支名称、标签名称或Commit ID
        self.sha = sha  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileLastCommitRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.filepath is not None:
            result['filepath'] = self.filepath
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        if self.sha is not None:
            result['sha'] = self.sha
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('filepath') is not None:
            self.filepath = m.get('filepath')
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        if m.get('sha') is not None:
            self.sha = m.get('sha')
        return self


class GetFileLastCommitResponseBodyResultSignature(TeaModel):
    def __init__(self, gpg_key_id=None, verification_status=None):
        # GPG密钥ID
        self.gpg_key_id = gpg_key_id  # type: str
        # 验证状态
        self.verification_status = verification_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileLastCommitResponseBodyResultSignature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpg_key_id is not None:
            result['GpgKeyId'] = self.gpg_key_id
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpgKeyId') is not None:
            self.gpg_key_id = m.get('GpgKeyId')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class GetFileLastCommitResponseBodyResult(TeaModel):
    def __init__(self, author_date=None, author_email=None, author_name=None, committed_date=None,
                 committer_email=None, committer_name=None, created_at=None, id=None, message=None, parent_ids=None, short_id=None,
                 signature=None, title=None):
        # 作者提交时间
        self.author_date = author_date  # type: str
        # 提交者邮箱
        self.author_email = author_email  # type: str
        # 作者姓名
        self.author_name = author_name  # type: str
        # 提交者提交时间
        self.committed_date = committed_date  # type: str
        # 提交者邮箱
        self.committer_email = committer_email  # type: str
        # 提交者姓名
        self.committer_name = committer_name  # type: str
        # 创建时间
        self.created_at = created_at  # type: str
        # Commit ID
        self.id = id  # type: str
        # 提交内容
        self.message = message  # type: str
        # 父提交ID
        self.parent_ids = parent_ids  # type: list[str]
        # Commit短ID
        self.short_id = short_id  # type: str
        # 签名
        self.signature = signature  # type: GetFileLastCommitResponseBodyResultSignature
        # 标题，提交的第一行内容
        self.title = title  # type: str

    def validate(self):
        if self.signature:
            self.signature.validate()

    def to_map(self):
        _map = super(GetFileLastCommitResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_date is not None:
            result['AuthorDate'] = self.author_date
        if self.author_email is not None:
            result['AuthorEmail'] = self.author_email
        if self.author_name is not None:
            result['AuthorName'] = self.author_name
        if self.committed_date is not None:
            result['CommittedDate'] = self.committed_date
        if self.committer_email is not None:
            result['CommitterEmail'] = self.committer_email
        if self.committer_name is not None:
            result['CommitterName'] = self.committer_name
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_ids is not None:
            result['ParentIds'] = self.parent_ids
        if self.short_id is not None:
            result['ShortId'] = self.short_id
        if self.signature is not None:
            result['Signature'] = self.signature.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorDate') is not None:
            self.author_date = m.get('AuthorDate')
        if m.get('AuthorEmail') is not None:
            self.author_email = m.get('AuthorEmail')
        if m.get('AuthorName') is not None:
            self.author_name = m.get('AuthorName')
        if m.get('CommittedDate') is not None:
            self.committed_date = m.get('CommittedDate')
        if m.get('CommitterEmail') is not None:
            self.committer_email = m.get('CommitterEmail')
        if m.get('CommitterName') is not None:
            self.committer_name = m.get('CommitterName')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentIds') is not None:
            self.parent_ids = m.get('ParentIds')
        if m.get('ShortId') is not None:
            self.short_id = m.get('ShortId')
        if m.get('Signature') is not None:
            temp_model = GetFileLastCommitResponseBodyResultSignature()
            self.signature = temp_model.from_map(m['Signature'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetFileLastCommitResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 响应结果
        self.result = result  # type: GetFileLastCommitResponseBodyResult
        # 请求结果
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetFileLastCommitResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetFileLastCommitResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFileLastCommitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFileLastCommitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileLastCommitResponse, self).to_map()
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
            temp_model = GetFileLastCommitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFlowTagGroupResponseBodyFlowTagGroupFlowTagList(TeaModel):
    def __init__(self, color=None, creator_account_id=None, id=None, modifer_account_id=None, name=None):
        self.color = color  # type: str
        self.creator_account_id = creator_account_id  # type: str
        self.id = id  # type: long
        self.modifer_account_id = modifer_account_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFlowTagGroupResponseBodyFlowTagGroupFlowTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['color'] = self.color
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.id is not None:
            result['id'] = self.id
        if self.modifer_account_id is not None:
            result['modiferAccountId'] = self.modifer_account_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('color') is not None:
            self.color = m.get('color')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modiferAccountId') is not None:
            self.modifer_account_id = m.get('modiferAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetFlowTagGroupResponseBodyFlowTagGroup(TeaModel):
    def __init__(self, creator_account_id=None, flow_tag_list=None, id=None, modifer_account_id=None, name=None):
        self.creator_account_id = creator_account_id  # type: str
        self.flow_tag_list = flow_tag_list  # type: list[GetFlowTagGroupResponseBodyFlowTagGroupFlowTagList]
        self.id = id  # type: long
        self.modifer_account_id = modifer_account_id  # type: str
        self.name = name  # type: str

    def validate(self):
        if self.flow_tag_list:
            for k in self.flow_tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetFlowTagGroupResponseBodyFlowTagGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        result['flowTagList'] = []
        if self.flow_tag_list is not None:
            for k in self.flow_tag_list:
                result['flowTagList'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.modifer_account_id is not None:
            result['modiferAccountId'] = self.modifer_account_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        self.flow_tag_list = []
        if m.get('flowTagList') is not None:
            for k in m.get('flowTagList'):
                temp_model = GetFlowTagGroupResponseBodyFlowTagGroupFlowTagList()
                self.flow_tag_list.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modiferAccountId') is not None:
            self.modifer_account_id = m.get('modiferAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetFlowTagGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, flow_tag_group=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        self.flow_tag_group = flow_tag_group  # type: GetFlowTagGroupResponseBodyFlowTagGroup
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.flow_tag_group:
            self.flow_tag_group.validate()

    def to_map(self):
        _map = super(GetFlowTagGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.flow_tag_group is not None:
            result['flowTagGroup'] = self.flow_tag_group.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('flowTagGroup') is not None:
            temp_model = GetFlowTagGroupResponseBodyFlowTagGroup()
            self.flow_tag_group = temp_model.from_map(m['flowTagGroup'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetFlowTagGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetFlowTagGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFlowTagGroupResponse, self).to_map()
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
            temp_model = GetFlowTagGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostGroupResponseBodyHostGroupHostInfos(TeaModel):
    def __init__(self, aliyun_region_id=None, create_time=None, creator_account_id=None, instance_name=None,
                 ip=None, machine_sn=None, modifier_account_id=None, object_type=None, update_time=None):
        self.aliyun_region_id = aliyun_region_id  # type: str
        self.create_time = create_time  # type: long
        self.creator_account_id = creator_account_id  # type: str
        self.instance_name = instance_name  # type: str
        self.ip = ip  # type: str
        self.machine_sn = machine_sn  # type: str
        self.modifier_account_id = modifier_account_id  # type: str
        self.object_type = object_type  # type: str
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostGroupResponseBodyHostGroupHostInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_region_id is not None:
            result['aliyunRegionId'] = self.aliyun_region_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.ip is not None:
            result['ip'] = self.ip
        if self.machine_sn is not None:
            result['machineSn'] = self.machine_sn
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunRegionId') is not None:
            self.aliyun_region_id = m.get('aliyunRegionId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('machineSn') is not None:
            self.machine_sn = m.get('machineSn')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetHostGroupResponseBodyHostGroup(TeaModel):
    def __init__(self, aliyun_region=None, create_time=None, creator_account_id=None, description=None,
                 ecs_label_key=None, ecs_label_value=None, ecs_type=None, host_infos=None, host_num=None, id=None,
                 modifier_account_id=None, name=None, service_connection_id=None, type=None, upate_time=None):
        self.aliyun_region = aliyun_region  # type: str
        self.create_time = create_time  # type: long
        self.creator_account_id = creator_account_id  # type: str
        self.description = description  # type: str
        self.ecs_label_key = ecs_label_key  # type: str
        self.ecs_label_value = ecs_label_value  # type: str
        self.ecs_type = ecs_type  # type: str
        self.host_infos = host_infos  # type: list[GetHostGroupResponseBodyHostGroupHostInfos]
        self.host_num = host_num  # type: long
        self.id = id  # type: long
        self.modifier_account_id = modifier_account_id  # type: str
        self.name = name  # type: str
        self.service_connection_id = service_connection_id  # type: long
        self.type = type  # type: str
        self.upate_time = upate_time  # type: long

    def validate(self):
        if self.host_infos:
            for k in self.host_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHostGroupResponseBodyHostGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_region is not None:
            result['aliyunRegion'] = self.aliyun_region
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.description is not None:
            result['description'] = self.description
        if self.ecs_label_key is not None:
            result['ecsLabelKey'] = self.ecs_label_key
        if self.ecs_label_value is not None:
            result['ecsLabelValue'] = self.ecs_label_value
        if self.ecs_type is not None:
            result['ecsType'] = self.ecs_type
        result['hostInfos'] = []
        if self.host_infos is not None:
            for k in self.host_infos:
                result['hostInfos'].append(k.to_map() if k else None)
        if self.host_num is not None:
            result['hostNum'] = self.host_num
        if self.id is not None:
            result['id'] = self.id
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.name is not None:
            result['name'] = self.name
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        if self.type is not None:
            result['type'] = self.type
        if self.upate_time is not None:
            result['upateTIme'] = self.upate_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunRegion') is not None:
            self.aliyun_region = m.get('aliyunRegion')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('ecsLabelKey') is not None:
            self.ecs_label_key = m.get('ecsLabelKey')
        if m.get('ecsLabelValue') is not None:
            self.ecs_label_value = m.get('ecsLabelValue')
        if m.get('ecsType') is not None:
            self.ecs_type = m.get('ecsType')
        self.host_infos = []
        if m.get('hostInfos') is not None:
            for k in m.get('hostInfos'):
                temp_model = GetHostGroupResponseBodyHostGroupHostInfos()
                self.host_infos.append(temp_model.from_map(k))
        if m.get('hostNum') is not None:
            self.host_num = m.get('hostNum')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('upateTIme') is not None:
            self.upate_time = m.get('upateTIme')
        return self


class GetHostGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, host_group=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        self.host_group = host_group  # type: GetHostGroupResponseBodyHostGroup
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.host_group:
            self.host_group.validate()

    def to_map(self):
        _map = super(GetHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.host_group is not None:
            result['hostGroup'] = self.host_group.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('hostGroup') is not None:
            temp_model = GetHostGroupResponseBodyHostGroup()
            self.host_group = temp_model.from_map(m['hostGroup'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetHostGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHostGroupResponse, self).to_map()
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
            temp_model = GetHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationMemberResponseBodyMemberIdentities(TeaModel):
    def __init__(self, extern_uid=None, provider=None):
        # 第三方系统的用户 id
        self.extern_uid = extern_uid  # type: str
        # 第三方系统
        self.provider = provider  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrganizationMemberResponseBodyMemberIdentities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_uid is not None:
            result['externUid'] = self.extern_uid
        if self.provider is not None:
            result['provider'] = self.provider
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externUid') is not None:
            self.extern_uid = m.get('externUid')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        return self


class GetOrganizationMemberResponseBodyMember(TeaModel):
    def __init__(self, account_id=None, birthday=None, dept_lists=None, email=None, hired_date=None, identities=None,
                 join_time=None, last_visit_time=None, mobile=None, organization_member_name=None, organization_role_id=None,
                 organization_role_name=None, state=None):
        # 阿里云用户PK
        self.account_id = account_id  # type: str
        # 生日
        self.birthday = birthday  # type: long
        # 部门名称列表
        self.dept_lists = dept_lists  # type: list[str]
        # 邮箱
        self.email = email  # type: str
        # 入职时间
        self.hired_date = hired_date  # type: long
        # 第三方信息
        self.identities = identities  # type: GetOrganizationMemberResponseBodyMemberIdentities
        # 加入云效企业时间
        self.join_time = join_time  # type: long
        # 最近一次访问时间
        self.last_visit_time = last_visit_time  # type: long
        # 手机号
        self.mobile = mobile  # type: str
        # 企业成员名
        self.organization_member_name = organization_member_name  # type: str
        # 企业角色Id
        self.organization_role_id = organization_role_id  # type: str
        # 企业角色名字
        self.organization_role_name = organization_role_name  # type: str
        # 用户状态
        self.state = state  # type: str

    def validate(self):
        if self.identities:
            self.identities.validate()

    def to_map(self):
        _map = super(GetOrganizationMemberResponseBodyMember, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.dept_lists is not None:
            result['deptLists'] = self.dept_lists
        if self.email is not None:
            result['email'] = self.email
        if self.hired_date is not None:
            result['hiredDate'] = self.hired_date
        if self.identities is not None:
            result['identities'] = self.identities.to_map()
        if self.join_time is not None:
            result['joinTime'] = self.join_time
        if self.last_visit_time is not None:
            result['lastVisitTime'] = self.last_visit_time
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.organization_member_name is not None:
            result['organizationMemberName'] = self.organization_member_name
        if self.organization_role_id is not None:
            result['organizationRoleId'] = self.organization_role_id
        if self.organization_role_name is not None:
            result['organizationRoleName'] = self.organization_role_name
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('deptLists') is not None:
            self.dept_lists = m.get('deptLists')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('hiredDate') is not None:
            self.hired_date = m.get('hiredDate')
        if m.get('identities') is not None:
            temp_model = GetOrganizationMemberResponseBodyMemberIdentities()
            self.identities = temp_model.from_map(m['identities'])
        if m.get('joinTime') is not None:
            self.join_time = m.get('joinTime')
        if m.get('lastVisitTime') is not None:
            self.last_visit_time = m.get('lastVisitTime')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('organizationMemberName') is not None:
            self.organization_member_name = m.get('organizationMemberName')
        if m.get('organizationRoleId') is not None:
            self.organization_role_id = m.get('organizationRoleId')
        if m.get('organizationRoleName') is not None:
            self.organization_role_name = m.get('organizationRoleName')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class GetOrganizationMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, member=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 成员
        self.member = member  # type: GetOrganizationMemberResponseBodyMember
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super(GetOrganizationMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.member is not None:
            result['member'] = self.member.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('member') is not None:
            temp_model = GetOrganizationMemberResponseBodyMember()
            self.member = temp_model.from_map(m['member'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetOrganizationMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOrganizationMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrganizationMemberResponse, self).to_map()
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
            temp_model = GetOrganizationMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineResponseBodyPipelinePipelineConfigSourcesData(TeaModel):
    def __init__(self, branch=None, clone_depth=None, credential_id=None, credential_label=None,
                 credential_type=None, events=None, is_branch_mode=None, is_clone_depth=None, is_submodule=None, is_trigger=None,
                 label=None, namespace=None, repo=None, service_connection_id=None, trigger_filter=None, webhook=None):
        # 分支
        self.branch = branch  # type: str
        # 克隆深度
        self.clone_depth = clone_depth  # type: long
        # Credential Id
        self.credential_id = credential_id  # type: long
        # Credential Label
        self.credential_label = credential_label  # type: str
        # Credential Type
        self.credential_type = credential_type  # type: str
        # 触发事件
        self.events = events  # type: list[str]
        # 是否分支模式
        self.is_branch_mode = is_branch_mode  # type: bool
        # 是否设置clone深度
        self.is_clone_depth = is_clone_depth  # type: bool
        # 是否子模块
        self.is_submodule = is_submodule  # type: bool
        # 是否提交触发
        self.is_trigger = is_trigger  # type: bool
        # 代码源显示标签
        self.label = label  # type: str
        # github命名空间
        self.namespace = namespace  # type: str
        # 代码库地址
        self.repo = repo  # type: str
        # 服务连接Id
        self.service_connection_id = service_connection_id  # type: long
        # 触发过滤条件
        self.trigger_filter = trigger_filter  # type: str
        # webhhook地址
        self.webhook = webhook  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineResponseBodyPipelinePipelineConfigSourcesData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.clone_depth is not None:
            result['cloneDepth'] = self.clone_depth
        if self.credential_id is not None:
            result['credentialId'] = self.credential_id
        if self.credential_label is not None:
            result['credentialLabel'] = self.credential_label
        if self.credential_type is not None:
            result['credentialType'] = self.credential_type
        if self.events is not None:
            result['events'] = self.events
        if self.is_branch_mode is not None:
            result['isBranchMode'] = self.is_branch_mode
        if self.is_clone_depth is not None:
            result['isCloneDepth'] = self.is_clone_depth
        if self.is_submodule is not None:
            result['isSubmodule'] = self.is_submodule
        if self.is_trigger is not None:
            result['isTrigger'] = self.is_trigger
        if self.label is not None:
            result['label'] = self.label
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.repo is not None:
            result['repo'] = self.repo
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        if self.trigger_filter is not None:
            result['triggerFilter'] = self.trigger_filter
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('cloneDepth') is not None:
            self.clone_depth = m.get('cloneDepth')
        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')
        if m.get('credentialLabel') is not None:
            self.credential_label = m.get('credentialLabel')
        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')
        if m.get('events') is not None:
            self.events = m.get('events')
        if m.get('isBranchMode') is not None:
            self.is_branch_mode = m.get('isBranchMode')
        if m.get('isCloneDepth') is not None:
            self.is_clone_depth = m.get('isCloneDepth')
        if m.get('isSubmodule') is not None:
            self.is_submodule = m.get('isSubmodule')
        if m.get('isTrigger') is not None:
            self.is_trigger = m.get('isTrigger')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('repo') is not None:
            self.repo = m.get('repo')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        if m.get('triggerFilter') is not None:
            self.trigger_filter = m.get('triggerFilter')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self


class GetPipelineResponseBodyPipelinePipelineConfigSources(TeaModel):
    def __init__(self, data=None, sign=None, type=None):
        # 代码数据
        self.data = data  # type: GetPipelineResponseBodyPipelinePipelineConfigSourcesData
        # 代码源唯一标识
        self.sign = sign  # type: str
        # 代码源类型aliyunGit 阿里云代码库 customGitlab  自建git giteeGit 码云 codeup Codeup git 通用git gitlab gitlab bitbucket bitbucket githubOAuth github
        self.type = type  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPipelineResponseBodyPipelinePipelineConfigSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.sign is not None:
            result['sign'] = self.sign
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPipelineResponseBodyPipelinePipelineConfigSourcesData()
            self.data = temp_model.from_map(m['data'])
        if m.get('sign') is not None:
            self.sign = m.get('sign')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetPipelineResponseBodyPipelinePipelineConfig(TeaModel):
    def __init__(self, flow=None, settings=None, sources=None):
        # 流水线配置信息
        self.flow = flow  # type: str
        # 流水线环境变量等
        self.settings = settings  # type: str
        # 代码源
        self.sources = sources  # type: list[GetPipelineResponseBodyPipelinePipelineConfigSources]

    def validate(self):
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineResponseBodyPipelinePipelineConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['flow'] = self.flow
        if self.settings is not None:
            result['settings'] = self.settings
        result['sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['sources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('flow') is not None:
            self.flow = m.get('flow')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        self.sources = []
        if m.get('sources') is not None:
            for k in m.get('sources'):
                temp_model = GetPipelineResponseBodyPipelinePipelineConfigSources()
                self.sources.append(temp_model.from_map(k))
        return self


class GetPipelineResponseBodyPipelineTagList(TeaModel):
    def __init__(self, id=None, name=None):
        # 标签id
        self.id = id  # type: long
        # 标签名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineResponseBodyPipelineTagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetPipelineResponseBodyPipeline(TeaModel):
    def __init__(self, create_time=None, creator_account_id=None, env_id=None, env_name=None, group_id=None,
                 modifier_account_id=None, name=None, pipeline_config=None, tag_list=None, update_time=None):
        # 创建时间
        self.create_time = create_time  # type: long
        # 创建者阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 环境id 0 日常环境  1预发环境 2正式环境
        self.env_id = env_id  # type: int
        # 环境名称
        self.env_name = env_name  # type: str
        # 流水线分组id
        self.group_id = group_id  # type: long
        # 更新人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 流水线名称
        self.name = name  # type: str
        # 流水线配置
        self.pipeline_config = pipeline_config  # type: GetPipelineResponseBodyPipelinePipelineConfig
        # 标签
        self.tag_list = tag_list  # type: list[GetPipelineResponseBodyPipelineTagList]
        # 更新时间
        self.update_time = update_time  # type: long

    def validate(self):
        if self.pipeline_config:
            self.pipeline_config.validate()
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineResponseBodyPipeline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.env_id is not None:
            result['envId'] = self.env_id
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.name is not None:
            result['name'] = self.name
        if self.pipeline_config is not None:
            result['pipelineConfig'] = self.pipeline_config.to_map()
        result['tagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['tagList'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('envId') is not None:
            self.env_id = m.get('envId')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pipelineConfig') is not None:
            temp_model = GetPipelineResponseBodyPipelinePipelineConfig()
            self.pipeline_config = temp_model.from_map(m['pipelineConfig'])
        self.tag_list = []
        if m.get('tagList') is not None:
            for k in m.get('tagList'):
                temp_model = GetPipelineResponseBodyPipelineTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetPipelineResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, pipeline=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 流水线
        self.pipeline = pipeline  # type: GetPipelineResponseBodyPipeline
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.pipeline:
            self.pipeline.validate()

    def to_map(self):
        _map = super(GetPipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.pipeline is not None:
            result['pipeline'] = self.pipeline.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('pipeline') is not None:
            temp_model = GetPipelineResponseBodyPipeline()
            self.pipeline = temp_model.from_map(m['pipeline'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPipelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineResponse, self).to_map()
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
            temp_model = GetPipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineArtifactUrlRequest(TeaModel):
    def __init__(self, file_name=None, file_path=None):
        self.file_name = file_name  # type: str
        self.file_path = file_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineArtifactUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_path is not None:
            result['filePath'] = self.file_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        return self


class GetPipelineArtifactUrlResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, file_url=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        self.file_url = file_url  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineArtifactUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPipelineArtifactUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineArtifactUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineArtifactUrlResponse, self).to_map()
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
            temp_model = GetPipelineArtifactUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineEmasArtifactUrlRequest(TeaModel):
    def __init__(self, service_connection_id=None):
        self.service_connection_id = service_connection_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineEmasArtifactUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        return self


class GetPipelineEmasArtifactUrlResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, file_url=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        self.file_url = file_url  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineEmasArtifactUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPipelineEmasArtifactUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineEmasArtifactUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineEmasArtifactUrlResponse, self).to_map()
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
            temp_model = GetPipelineEmasArtifactUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineRunResponseBodyPipelineRunSourcesData(TeaModel):
    def __init__(self, branch=None, commint=None, repo=None):
        # 分支
        self.branch = branch  # type: str
        # 提交信息 json数据
        self.commint = commint  # type: str
        # 代码库地址
        self.repo = repo  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineRunResponseBodyPipelineRunSourcesData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.commint is not None:
            result['commint'] = self.commint
        if self.repo is not None:
            result['repo'] = self.repo
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('commint') is not None:
            self.commint = m.get('commint')
        if m.get('repo') is not None:
            self.repo = m.get('repo')
        return self


class GetPipelineRunResponseBodyPipelineRunSources(TeaModel):
    def __init__(self, data=None, sign=None, type=None):
        # 代码源信息
        self.data = data  # type: GetPipelineRunResponseBodyPipelineRunSourcesData
        # 代码源唯一标识
        self.sign = sign  # type: str
        # 代码库类型
        self.type = type  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPipelineRunResponseBodyPipelineRunSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.sign is not None:
            result['sign'] = self.sign
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPipelineRunResponseBodyPipelineRunSourcesData()
            self.data = temp_model.from_map(m['data'])
        if m.get('sign') is not None:
            self.sign = m.get('sign')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobsActions(TeaModel):
    def __init__(self, disable=None, params=None, type=None):
        # 是否可用
        self.disable = disable  # type: bool
        # API参数
        self.params = params  # type: dict[str, any]
        # API名称
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobsActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable is not None:
            result['disable'] = self.disable
        if self.params is not None:
            result['params'] = self.params
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('disable') is not None:
            self.disable = m.get('disable')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobs(TeaModel):
    def __init__(self, actions=None, end_time=None, id=None, name=None, params=None, start_time=None, status=None):
        # 后续操作
        self.actions = actions  # type: list[GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobsActions]
        # 结束时间
        self.end_time = end_time  # type: long
        # 任务Id
        self.id = id  # type: long
        # 任务名称
        self.name = name  # type: str
        # 触发参数
        self.params = params  # type: str
        # 开始时间
        self.start_time = start_time  # type: long
        # 状态
        self.status = status  # type: str

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['actions'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.params is not None:
            result['params'] = self.params
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('actions') is not None:
            for k in m.get('actions'):
                temp_model = GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobsActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetPipelineRunResponseBodyPipelineRunStagesStageInfo(TeaModel):
    def __init__(self, end_time=None, jobs=None, name=None, start_time=None, status=None):
        # 结束时间
        self.end_time = end_time  # type: long
        # 任务
        self.jobs = jobs  # type: list[GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobs]
        # 阶段名称
        self.name = name  # type: str
        # 开始时间
        self.start_time = start_time  # type: long
        # 状态
        self.status = status  # type: str

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineRunResponseBodyPipelineRunStagesStageInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        result['jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['jobs'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetPipelineRunResponseBodyPipelineRunStages(TeaModel):
    def __init__(self, name=None, stage_info=None):
        # 阶段名称
        self.name = name  # type: str
        # 阶段详情
        self.stage_info = stage_info  # type: GetPipelineRunResponseBodyPipelineRunStagesStageInfo

    def validate(self):
        if self.stage_info:
            self.stage_info.validate()

    def to_map(self):
        _map = super(GetPipelineRunResponseBodyPipelineRunStages, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.stage_info is not None:
            result['stageInfo'] = self.stage_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('stageInfo') is not None:
            temp_model = GetPipelineRunResponseBodyPipelineRunStagesStageInfo()
            self.stage_info = temp_model.from_map(m['stageInfo'])
        return self


class GetPipelineRunResponseBodyPipelineRun(TeaModel):
    def __init__(self, create_time=None, creator_account_id=None, modifier_account_id=None, pipeline_id=None,
                 pipeline_run_id=None, sources=None, stage_group=None, stages=None, status=None, trigger_mode=None, update_time=None):
        # 创建时间
        self.create_time = create_time  # type: long
        # 创建者阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 更新人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 流水线Id
        self.pipeline_id = pipeline_id  # type: long
        # 流水线运行实例id
        self.pipeline_run_id = pipeline_run_id  # type: long
        # 代码源
        self.sources = sources  # type: list[GetPipelineRunResponseBodyPipelineRunSources]
        # 阶段拓扑信息
        self.stage_group = stage_group  # type: list[list[str]]
        # 阶段信息
        self.stages = stages  # type: list[GetPipelineRunResponseBodyPipelineRunStages]
        # 状态 FAIL 运行失败 SUCCESS 运行成功 RUNNING 运行中
        self.status = status  # type: str
        # 触发模式 1人工触发 2定时触发 3代码提交触发
        self.trigger_mode = trigger_mode  # type: int
        # 更新时间
        self.update_time = update_time  # type: long

    def validate(self):
        if self.sources:
            for k in self.sources:
                if k:
                    k.validate()
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPipelineRunResponseBodyPipelineRun, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.pipeline_run_id is not None:
            result['pipelineRunId'] = self.pipeline_run_id
        result['sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['sources'].append(k.to_map() if k else None)
        if self.stage_group is not None:
            result['stageGroup'] = self.stage_group
        result['stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['stages'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('pipelineRunId') is not None:
            self.pipeline_run_id = m.get('pipelineRunId')
        self.sources = []
        if m.get('sources') is not None:
            for k in m.get('sources'):
                temp_model = GetPipelineRunResponseBodyPipelineRunSources()
                self.sources.append(temp_model.from_map(k))
        if m.get('stageGroup') is not None:
            self.stage_group = m.get('stageGroup')
        self.stages = []
        if m.get('stages') is not None:
            for k in m.get('stages'):
                temp_model = GetPipelineRunResponseBodyPipelineRunStages()
                self.stages.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetPipelineRunResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, pipeline_run=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 流水线运行实例
        self.pipeline_run = pipeline_run  # type: GetPipelineRunResponseBodyPipelineRun
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.pipeline_run:
            self.pipeline_run.validate()

    def to_map(self):
        _map = super(GetPipelineRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.pipeline_run is not None:
            result['pipelineRun'] = self.pipeline_run.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('pipelineRun') is not None:
            temp_model = GetPipelineRunResponseBodyPipelineRun()
            self.pipeline_run = temp_model.from_map(m['pipelineRun'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPipelineRunResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineRunResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineRunResponse, self).to_map()
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
            temp_model = GetPipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPipelineScanReportUrlRequest(TeaModel):
    def __init__(self, report_path=None):
        self.report_path = report_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineScanReportUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_path is not None:
            result['reportPath'] = self.report_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('reportPath') is not None:
            self.report_path = m.get('reportPath')
        return self


class GetPipelineScanReportUrlResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, report_url=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        self.report_url = report_url  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineScanReportUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.report_url is not None:
            result['reportUrl'] = self.report_url
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('reportUrl') is not None:
            self.report_url = m.get('reportUrl')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPipelineScanReportUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPipelineScanReportUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPipelineScanReportUrlResponse, self).to_map()
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
            temp_model = GetPipelineScanReportUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectInfoResponseBodyProject(TeaModel):
    def __init__(self, category=None, category_identifier=None, creator=None, custom_code=None, description=None,
                 gmt_create=None, gmt_modified=None, icon=None, icon_big=None, icon_group=None, icon_small=None, id=None,
                 identifier=None, identifier_path=None, logical_status=None, modifier=None, name=None,
                 organization_identifier=None, parent_identifier=None, scope=None, status_identifier=None, status_stage_identifier=None,
                 sub_type=None, type_identifier=None):
        self.category = category  # type: str
        self.category_identifier = category_identifier  # type: str
        self.creator = creator  # type: str
        self.custom_code = custom_code  # type: str
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.icon = icon  # type: str
        self.icon_big = icon_big  # type: str
        self.icon_group = icon_group  # type: str
        self.icon_small = icon_small  # type: str
        self.id = id  # type: str
        self.identifier = identifier  # type: str
        self.identifier_path = identifier_path  # type: str
        self.logical_status = logical_status  # type: str
        self.modifier = modifier  # type: str
        self.name = name  # type: str
        self.organization_identifier = organization_identifier  # type: str
        self.parent_identifier = parent_identifier  # type: str
        self.scope = scope  # type: str
        self.status_identifier = status_identifier  # type: str
        self.status_stage_identifier = status_stage_identifier  # type: str
        self.sub_type = sub_type  # type: str
        self.type_identifier = type_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectInfoResponseBodyProject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.category_identifier is not None:
            result['categoryIdentifier'] = self.category_identifier
        if self.creator is not None:
            result['creator'] = self.creator
        if self.custom_code is not None:
            result['customCode'] = self.custom_code
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.icon is not None:
            result['icon'] = self.icon
        if self.icon_big is not None:
            result['iconBig'] = self.icon_big
        if self.icon_group is not None:
            result['iconGroup'] = self.icon_group
        if self.icon_small is not None:
            result['iconSmall'] = self.icon_small
        if self.id is not None:
            result['id'] = self.id
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.identifier_path is not None:
            result['identifierPath'] = self.identifier_path
        if self.logical_status is not None:
            result['logicalStatus'] = self.logical_status
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.organization_identifier is not None:
            result['organizationIdentifier'] = self.organization_identifier
        if self.parent_identifier is not None:
            result['parentIdentifier'] = self.parent_identifier
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status_identifier is not None:
            result['statusIdentifier'] = self.status_identifier
        if self.status_stage_identifier is not None:
            result['statusStageIdentifier'] = self.status_stage_identifier
        if self.sub_type is not None:
            result['subType'] = self.sub_type
        if self.type_identifier is not None:
            result['typeIdentifier'] = self.type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('categoryIdentifier') is not None:
            self.category_identifier = m.get('categoryIdentifier')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('customCode') is not None:
            self.custom_code = m.get('customCode')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('iconBig') is not None:
            self.icon_big = m.get('iconBig')
        if m.get('iconGroup') is not None:
            self.icon_group = m.get('iconGroup')
        if m.get('iconSmall') is not None:
            self.icon_small = m.get('iconSmall')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('identifierPath') is not None:
            self.identifier_path = m.get('identifierPath')
        if m.get('logicalStatus') is not None:
            self.logical_status = m.get('logicalStatus')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('organizationIdentifier') is not None:
            self.organization_identifier = m.get('organizationIdentifier')
        if m.get('parentIdentifier') is not None:
            self.parent_identifier = m.get('parentIdentifier')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('statusIdentifier') is not None:
            self.status_identifier = m.get('statusIdentifier')
        if m.get('statusStageIdentifier') is not None:
            self.status_stage_identifier = m.get('statusStageIdentifier')
        if m.get('subType') is not None:
            self.sub_type = m.get('subType')
        if m.get('typeIdentifier') is not None:
            self.type_identifier = m.get('typeIdentifier')
        return self


class GetProjectInfoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, project=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        # 项目信息
        self.project = project  # type: GetProjectInfoResponseBodyProject
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super(GetProjectInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.project is not None:
            result['project'] = self.project.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('project') is not None:
            temp_model = GetProjectInfoResponseBodyProject()
            self.project = temp_model.from_map(m['project'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProjectInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProjectInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectInfoResponse, self).to_map()
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
            temp_model = GetProjectInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectMemberRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, repository_id=None, user_aliyun_pk=None):
        # accessToken（选填），使用AK方式调用时无需填accessToken
        self.access_token = access_token  # type: str
        # 企业ID
        self.organization_id = organization_id  # type: str
        # 代码仓库Id
        self.repository_id = repository_id  # type: long
        # 用户阿里云PK
        self.user_aliyun_pk = user_aliyun_pk  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.repository_id is not None:
            result['repositoryId'] = self.repository_id
        if self.user_aliyun_pk is not None:
            result['userAliyunPk'] = self.user_aliyun_pk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('repositoryId') is not None:
            self.repository_id = m.get('repositoryId')
        if m.get('userAliyunPk') is not None:
            self.user_aliyun_pk = m.get('userAliyunPk')
        return self


class GetProjectMemberResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, extern_user_id=None, id=None, name=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectMemberResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['accessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.extern_user_id is not None:
            result['externUserId'] = self.extern_user_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessLevel') is not None:
            self.access_level = m.get('accessLevel')
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('externUserId') is not None:
            self.extern_user_id = m.get('externUserId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetProjectMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: GetProjectMemberResponseBodyResult
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetProjectMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetProjectMemberResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetProjectMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProjectMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectMemberResponse, self).to_map()
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
            temp_model = GetProjectMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryRequest(TeaModel):
    def __init__(self, access_token=None, identity=None, organization_id=None):
        # 个人访问令牌
        self.access_token = access_token  # type: str
        # 代码库ID或路径
        self.identity = identity  # type: str
        # 企业ID
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.identity is not None:
            result['identity'] = self.identity
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        return self


class GetRepositoryResponseBodyRepositoryNamespace(TeaModel):
    def __init__(self, avatar=None, created_at=None, description=None, id=None, name=None, owner_id=None, path=None,
                 updated_at=None, visibility_level=None):
        # 头像地址
        self.avatar = avatar  # type: str
        # 创建时间
        self.created_at = created_at  # type: str
        # 描述
        self.description = description  # type: str
        # id
        self.id = id  # type: long
        # 名称
        self.name = name  # type: str
        # 归属者ID
        self.owner_id = owner_id  # type: long
        # 路径
        self.path = path  # type: str
        # 更新时间
        self.updated_at = updated_at  # type: str
        # 可见性。0：私有，10：内部公开
        self.visibility_level = visibility_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRepositoryResponseBodyRepositoryNamespace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.path is not None:
            result['path'] = self.path
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.visibility_level is not None:
            result['visibilityLevel'] = self.visibility_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('visibilityLevel') is not None:
            self.visibility_level = m.get('visibilityLevel')
        return self


class GetRepositoryResponseBodyRepository(TeaModel):
    def __init__(self, archive=None, avatar_url=None, created_at=None, creator_id=None, default_branch=None,
                 demo_project_status=None, description=None, http_url_to_repository=None, id=None, last_activity_at=None, name=None,
                 name_with_namespace=None, namespace=None, path=None, path_with_namespace=None, ssh_url_to_repository=None,
                 visibility_level=None, web_url=None):
        # 归档标识
        self.archive = archive  # type: bool
        # 代码库头像地址
        self.avatar_url = avatar_url  # type: str
        # 创建时间
        self.created_at = created_at  # type: str
        # 创建者ID
        self.creator_id = creator_id  # type: long
        # 默认分支
        self.default_branch = default_branch  # type: str
        # DEMO库标识
        self.demo_project_status = demo_project_status  # type: bool
        # 描述
        self.description = description  # type: str
        # HTTP克隆地址
        self.http_url_to_repository = http_url_to_repository  # type: str
        # 代码库ID
        self.id = id  # type: long
        # 最后活跃时间
        self.last_activity_at = last_activity_at  # type: str
        # 名称
        self.name = name  # type: str
        # 名称（含父名称）
        self.name_with_namespace = name_with_namespace  # type: str
        # 父空间
        self.namespace = namespace  # type: GetRepositoryResponseBodyRepositoryNamespace
        # 路径
        self.path = path  # type: str
        # 路径（含父路径）
        self.path_with_namespace = path_with_namespace  # type: str
        # SSH克隆地址
        self.ssh_url_to_repository = ssh_url_to_repository  # type: str
        # 可见性。0：私有，10：内部公开
        self.visibility_level = visibility_level  # type: int
        # 页面访问地址
        self.web_url = web_url  # type: str

    def validate(self):
        if self.namespace:
            self.namespace.validate()

    def to_map(self):
        _map = super(GetRepositoryResponseBodyRepository, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive is not None:
            result['archive'] = self.archive
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.default_branch is not None:
            result['defaultBranch'] = self.default_branch
        if self.demo_project_status is not None:
            result['demoProjectStatus'] = self.demo_project_status
        if self.description is not None:
            result['description'] = self.description
        if self.http_url_to_repository is not None:
            result['httpUrlToRepository'] = self.http_url_to_repository
        if self.id is not None:
            result['id'] = self.id
        if self.last_activity_at is not None:
            result['lastActivityAt'] = self.last_activity_at
        if self.name is not None:
            result['name'] = self.name
        if self.name_with_namespace is not None:
            result['nameWithNamespace'] = self.name_with_namespace
        if self.namespace is not None:
            result['namespace'] = self.namespace.to_map()
        if self.path is not None:
            result['path'] = self.path
        if self.path_with_namespace is not None:
            result['pathWithNamespace'] = self.path_with_namespace
        if self.ssh_url_to_repository is not None:
            result['sshUrlToRepository'] = self.ssh_url_to_repository
        if self.visibility_level is not None:
            result['visibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['webUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('archive') is not None:
            self.archive = m.get('archive')
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('defaultBranch') is not None:
            self.default_branch = m.get('defaultBranch')
        if m.get('demoProjectStatus') is not None:
            self.demo_project_status = m.get('demoProjectStatus')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('httpUrlToRepository') is not None:
            self.http_url_to_repository = m.get('httpUrlToRepository')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastActivityAt') is not None:
            self.last_activity_at = m.get('lastActivityAt')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameWithNamespace') is not None:
            self.name_with_namespace = m.get('nameWithNamespace')
        if m.get('namespace') is not None:
            temp_model = GetRepositoryResponseBodyRepositoryNamespace()
            self.namespace = temp_model.from_map(m['namespace'])
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('pathWithNamespace') is not None:
            self.path_with_namespace = m.get('pathWithNamespace')
        if m.get('sshUrlToRepository') is not None:
            self.ssh_url_to_repository = m.get('sshUrlToRepository')
        if m.get('visibilityLevel') is not None:
            self.visibility_level = m.get('visibilityLevel')
        if m.get('webUrl') is not None:
            self.web_url = m.get('webUrl')
        return self


class GetRepositoryResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, repository=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 代码库信息
        self.repository = repository  # type: GetRepositoryResponseBodyRepository
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.repository:
            self.repository.validate()

    def to_map(self):
        _map = super(GetRepositoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.repository is not None:
            result['repository'] = self.repository.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('repository') is not None:
            temp_model = GetRepositoryResponseBodyRepository()
            self.repository = temp_model.from_map(m['repository'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetRepositoryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRepositoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRepositoryResponse, self).to_map()
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
            temp_model = GetRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSprintInfoResponseBodySprint(TeaModel):
    def __init__(self, creator=None, description=None, end_date=None, gmt_create=None, gmt_modified=None,
                 identifier=None, modifier=None, name=None, scope=None, space_identifier=None, start_date=None, status=None):
        # 创建人id
        self.creator = creator  # type: str
        # 描述信息
        self.description = description  # type: str
        # 结束时间
        self.end_date = end_date  # type: long
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 迭代唯一标识符
        self.identifier = identifier  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 迭代名称
        self.name = name  # type: str
        # 可见范围
        self.scope = scope  # type: str
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 开始时间
        self.start_date = start_date  # type: long
        # 状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSprintInfoResponseBodySprint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetSprintInfoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, sprint=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        # 迭代信息
        self.sprint = sprint  # type: GetSprintInfoResponseBodySprint
        self.success = success  # type: bool

    def validate(self):
        if self.sprint:
            self.sprint.validate()

    def to_map(self):
        _map = super(GetSprintInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.sprint is not None:
            result['sprint'] = self.sprint.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sprint') is not None:
            temp_model = GetSprintInfoResponseBodySprint()
            self.sprint = temp_model.from_map(m['sprint'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetSprintInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSprintInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSprintInfoResponse, self).to_map()
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
            temp_model = GetSprintInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVMDeployOrderResponseBodyDeployOrderActions(TeaModel):
    def __init__(self, disable=None, params=None, type=None):
        # 是否可用
        self.disable = disable  # type: bool
        # 参数
        self.params = params  # type: dict[str, any]
        # Action
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVMDeployOrderResponseBodyDeployOrderActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable is not None:
            result['disable'] = self.disable
        if self.params is not None:
            result['params'] = self.params
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('disable') is not None:
            self.disable = m.get('disable')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfoDeployMachinesActions(TeaModel):
    def __init__(self, disable=None, params=None, type=None):
        # 是否可用
        self.disable = disable  # type: bool
        # 参数
        self.params = params  # type: dict[str, any]
        # Action
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfoDeployMachinesActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable is not None:
            result['disable'] = self.disable
        if self.params is not None:
            result['params'] = self.params
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('disable') is not None:
            self.disable = m.get('disable')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfoDeployMachines(TeaModel):
    def __init__(self, actions=None, batch_num=None, client_status=None, create_time=None, ip=None, machine_sn=None,
                 status=None, update_time=None):
        # 后续action
        self.actions = actions  # type: list[GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfoDeployMachinesActions]
        # 部署批次
        self.batch_num = batch_num  # type: int
        # 机器状态
        self.client_status = client_status  # type: str
        # 开始时间
        self.create_time = create_time  # type: long
        # 机器IP
        self.ip = ip  # type: str
        # 机器sn
        self.machine_sn = machine_sn  # type: str
        # 部署状态
        self.status = status  # type: str
        # 修改时间
        self.update_time = update_time  # type: long

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfoDeployMachines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['actions'].append(k.to_map() if k else None)
        if self.batch_num is not None:
            result['batchNum'] = self.batch_num
        if self.client_status is not None:
            result['clientStatus'] = self.client_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.ip is not None:
            result['ip'] = self.ip
        if self.machine_sn is not None:
            result['machineSn'] = self.machine_sn
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('actions') is not None:
            for k in m.get('actions'):
                temp_model = GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfoDeployMachinesActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('batchNum') is not None:
            self.batch_num = m.get('batchNum')
        if m.get('clientStatus') is not None:
            self.client_status = m.get('clientStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('machineSn') is not None:
            self.machine_sn = m.get('machineSn')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfo(TeaModel):
    def __init__(self, batch_num=None, deploy_machines=None, host_group_id=None):
        # 发布批次
        self.batch_num = batch_num  # type: int
        # 部署机器列表
        self.deploy_machines = deploy_machines  # type: list[GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfoDeployMachines]
        # 主机组ID
        self.host_group_id = host_group_id  # type: long

    def validate(self):
        if self.deploy_machines:
            for k in self.deploy_machines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_num is not None:
            result['batchNum'] = self.batch_num
        result['deployMachines'] = []
        if self.deploy_machines is not None:
            for k in self.deploy_machines:
                result['deployMachines'].append(k.to_map() if k else None)
        if self.host_group_id is not None:
            result['hostGroupId'] = self.host_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('batchNum') is not None:
            self.batch_num = m.get('batchNum')
        self.deploy_machines = []
        if m.get('deployMachines') is not None:
            for k in m.get('deployMachines'):
                temp_model = GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfoDeployMachines()
                self.deploy_machines.append(temp_model.from_map(k))
        if m.get('hostGroupId') is not None:
            self.host_group_id = m.get('hostGroupId')
        return self


class GetVMDeployOrderResponseBodyDeployOrder(TeaModel):
    def __init__(self, actions=None, create_time=None, creator=None, current_batch=None, deploy_machine_info=None,
                 deploy_order_id=None, exception_code=None, status=None, total_batch=None, update_time=None):
        # 后续action
        self.actions = actions  # type: list[GetVMDeployOrderResponseBodyDeployOrderActions]
        # 创建时时间
        self.create_time = create_time  # type: long
        # 创建人
        self.creator = creator  # type: str
        # 当前发布批次
        self.current_batch = current_batch  # type: int
        # 部署机器信息
        self.deploy_machine_info = deploy_machine_info  # type: GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfo
        # 部署单ID
        self.deploy_order_id = deploy_order_id  # type: str
        # 错误码
        self.exception_code = exception_code  # type: str
        # 发布状态
        self.status = status  # type: str
        # 总发布批次
        self.total_batch = total_batch  # type: int
        # 修改时间
        self.update_time = update_time  # type: long

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.deploy_machine_info:
            self.deploy_machine_info.validate()

    def to_map(self):
        _map = super(GetVMDeployOrderResponseBodyDeployOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['actions'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.current_batch is not None:
            result['currentBatch'] = self.current_batch
        if self.deploy_machine_info is not None:
            result['deployMachineInfo'] = self.deploy_machine_info.to_map()
        if self.deploy_order_id is not None:
            result['deployOrderId'] = self.deploy_order_id
        if self.exception_code is not None:
            result['exceptionCode'] = self.exception_code
        if self.status is not None:
            result['status'] = self.status
        if self.total_batch is not None:
            result['totalBatch'] = self.total_batch
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.actions = []
        if m.get('actions') is not None:
            for k in m.get('actions'):
                temp_model = GetVMDeployOrderResponseBodyDeployOrderActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('currentBatch') is not None:
            self.current_batch = m.get('currentBatch')
        if m.get('deployMachineInfo') is not None:
            temp_model = GetVMDeployOrderResponseBodyDeployOrderDeployMachineInfo()
            self.deploy_machine_info = temp_model.from_map(m['deployMachineInfo'])
        if m.get('deployOrderId') is not None:
            self.deploy_order_id = m.get('deployOrderId')
        if m.get('exceptionCode') is not None:
            self.exception_code = m.get('exceptionCode')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('totalBatch') is not None:
            self.total_batch = m.get('totalBatch')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetVMDeployOrderResponseBody(TeaModel):
    def __init__(self, deploy_order=None, error_code=None, error_message=None, request_id=None, success=None):
        # 部署单
        self.deploy_order = deploy_order  # type: GetVMDeployOrderResponseBodyDeployOrder
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.deploy_order:
            self.deploy_order.validate()

    def to_map(self):
        _map = super(GetVMDeployOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_order is not None:
            result['deployOrder'] = self.deploy_order.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deployOrder') is not None:
            temp_model = GetVMDeployOrderResponseBodyDeployOrder()
            self.deploy_order = temp_model.from_map(m['deployOrder'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetVMDeployOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVMDeployOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVMDeployOrderResponse, self).to_map()
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
            temp_model = GetVMDeployOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVariableGroupResponseBodyVariableGroupRelatedPipelines(TeaModel):
    def __init__(self, id=None, name=None):
        # 关联的流水线Id
        self.id = id  # type: long
        # 关联的流水线名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVariableGroupResponseBodyVariableGroupRelatedPipelines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetVariableGroupResponseBodyVariableGroupVariables(TeaModel):
    def __init__(self, is_encrypted=None, name=None, value=None):
        # 是否加密
        self.is_encrypted = is_encrypted  # type: bool
        # 变量名
        self.name = name  # type: str
        # 变量值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVariableGroupResponseBodyVariableGroupVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_encrypted is not None:
            result['isEncrypted'] = self.is_encrypted
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('isEncrypted') is not None:
            self.is_encrypted = m.get('isEncrypted')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetVariableGroupResponseBodyVariableGroup(TeaModel):
    def __init__(self, ccreator_account_id=None, create_time=None, description=None, id=None,
                 modifier_account_id=None, name=None, related_pipelines=None, update_time=None, variables=None):
        # 创建人阿里云账号id
        self.ccreator_account_id = ccreator_account_id  # type: str
        # 创建时间
        self.create_time = create_time  # type: long
        # 变量组描述
        self.description = description  # type: str
        # 变量组id
        self.id = id  # type: long
        # 更新人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 变量组名称
        self.name = name  # type: str
        # 关联的流水线
        self.related_pipelines = related_pipelines  # type: list[GetVariableGroupResponseBodyVariableGroupRelatedPipelines]
        # 更新时间
        self.update_time = update_time  # type: long
        # 变量
        self.variables = variables  # type: list[GetVariableGroupResponseBodyVariableGroupVariables]

    def validate(self):
        if self.related_pipelines:
            for k in self.related_pipelines:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVariableGroupResponseBodyVariableGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ccreator_account_id is not None:
            result['ccreatorAccountId'] = self.ccreator_account_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.name is not None:
            result['name'] = self.name
        result['relatedPipelines'] = []
        if self.related_pipelines is not None:
            for k in self.related_pipelines:
                result['relatedPipelines'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ccreatorAccountId') is not None:
            self.ccreator_account_id = m.get('ccreatorAccountId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.related_pipelines = []
        if m.get('relatedPipelines') is not None:
            for k in m.get('relatedPipelines'):
                temp_model = GetVariableGroupResponseBodyVariableGroupRelatedPipelines()
                self.related_pipelines.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = GetVariableGroupResponseBodyVariableGroupVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class GetVariableGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None, variable_group=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 变量组
        self.variable_group = variable_group  # type: GetVariableGroupResponseBodyVariableGroup

    def validate(self):
        if self.variable_group:
            self.variable_group.validate()

    def to_map(self):
        _map = super(GetVariableGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.variable_group is not None:
            result['variableGroup'] = self.variable_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('variableGroup') is not None:
            temp_model = GetVariableGroupResponseBodyVariableGroup()
            self.variable_group = temp_model.from_map(m['variableGroup'])
        return self


class GetVariableGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVariableGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVariableGroupResponse, self).to_map()
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
            temp_model = GetVariableGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkItemActivityResponseBodyActivitiesProperty(TeaModel):
    def __init__(self, display_name=None, property_identifier=None, property_name=None, property_type=None):
        # 属性的展示名
        self.display_name = display_name  # type: str
        # 资源id
        self.property_identifier = property_identifier  # type: str
        # 属性key
        self.property_name = property_name  # type: str
        # 类型
        self.property_type = property_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkItemActivityResponseBodyActivitiesProperty, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.property_identifier is not None:
            result['propertyIdentifier'] = self.property_identifier
        if self.property_name is not None:
            result['propertyName'] = self.property_name
        if self.property_type is not None:
            result['propertyType'] = self.property_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('propertyIdentifier') is not None:
            self.property_identifier = m.get('propertyIdentifier')
        if m.get('propertyName') is not None:
            self.property_name = m.get('propertyName')
        if m.get('propertyType') is not None:
            self.property_type = m.get('propertyType')
        return self


class GetWorkItemActivityResponseBodyActivities(TeaModel):
    def __init__(self, action_type=None, event_id=None, event_time=None, event_type=None, operator=None,
                 parent_event_id=None, property=None, resource_identifier=None):
        # 动作类型
        self.action_type = action_type  # type: str
        # 事件id
        self.event_id = event_id  # type: long
        # 事件时间
        self.event_time = event_time  # type: long
        # 事件类型
        self.event_type = event_type  # type: str
        # 操作者
        self.operator = operator  # type: str
        # 父事件id
        self.parent_event_id = parent_event_id  # type: long
        # 修改属性
        self.property = property  # type: GetWorkItemActivityResponseBodyActivitiesProperty
        # 操作对象
        self.resource_identifier = resource_identifier  # type: str

    def validate(self):
        if self.property:
            self.property.validate()

    def to_map(self):
        _map = super(GetWorkItemActivityResponseBodyActivities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['actionType'] = self.action_type
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.event_time is not None:
            result['eventTime'] = self.event_time
        if self.event_type is not None:
            result['eventType'] = self.event_type
        if self.operator is not None:
            result['operator'] = self.operator
        if self.parent_event_id is not None:
            result['parentEventId'] = self.parent_event_id
        if self.property is not None:
            result['property'] = self.property.to_map()
        if self.resource_identifier is not None:
            result['resourceIdentifier'] = self.resource_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')
        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('parentEventId') is not None:
            self.parent_event_id = m.get('parentEventId')
        if m.get('property') is not None:
            temp_model = GetWorkItemActivityResponseBodyActivitiesProperty()
            self.property = temp_model.from_map(m['property'])
        if m.get('resourceIdentifier') is not None:
            self.resource_identifier = m.get('resourceIdentifier')
        return self


class GetWorkItemActivityResponseBody(TeaModel):
    def __init__(self, activities=None, error_code=None, error_msg=None, request_id=None, success=None):
        # 动态信息
        self.activities = activities  # type: list[GetWorkItemActivityResponseBodyActivities]
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool

    def validate(self):
        if self.activities:
            for k in self.activities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWorkItemActivityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['activities'] = []
        if self.activities is not None:
            for k in self.activities:
                result['activities'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.activities = []
        if m.get('activities') is not None:
            for k in m.get('activities'):
                temp_model = GetWorkItemActivityResponseBodyActivities()
                self.activities.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetWorkItemActivityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetWorkItemActivityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkItemActivityResponse, self).to_map()
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
            temp_model = GetWorkItemActivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkItemInfoResponseBodyWorkitemCustomFieldsValueList(TeaModel):
    def __init__(self, display_value=None, identifier=None, level=None, value=None, value_en=None):
        # 根据语言环境获取当前展示的值
        self.display_value = display_value  # type: str
        # 字段值为对象类型时，值所对应的对象的唯一标识 例如：option表中的id
        self.identifier = identifier  # type: str
        # 展示级别，数字范围1~9，数字越大，颜色越浅。
        self.level = level  # type: long
        # 字段值
        self.value = value  # type: str
        # 字段英文值，目前只有列表类有英文值
        self.value_en = value_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkItemInfoResponseBodyWorkitemCustomFieldsValueList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_value is not None:
            result['displayValue'] = self.display_value
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.level is not None:
            result['level'] = self.level
        if self.value is not None:
            result['value'] = self.value
        if self.value_en is not None:
            result['valueEn'] = self.value_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayValue') is not None:
            self.display_value = m.get('displayValue')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueEn') is not None:
            self.value_en = m.get('valueEn')
        return self


class GetWorkItemInfoResponseBodyWorkitemCustomFields(TeaModel):
    def __init__(self, field_class_name=None, field_format=None, field_identifier=None, level=None,
                 object_value=None, position=None, value=None, value_list=None, workitem_identifier=None):
        # 字段的className，便于数据查询
        self.field_class_name = field_class_name  # type: str
        # 字段格式，便于查询数据
        self.field_format = field_format  # type: str
        # 字段的唯一标识
        self.field_identifier = field_identifier  # type: str
        # 展示级别，数字范围1~9，数字越大，颜色越浅。
        self.level = level  # type: long
        # 值对象列表
        self.object_value = object_value  # type: str
        # 自定义字段值的position
        self.position = position  # type: long
        # 字段值，写入时使用
        self.value = value  # type: str
        # 值对象列表，查询时使用
        self.value_list = value_list  # type: list[GetWorkItemInfoResponseBodyWorkitemCustomFieldsValueList]
        # 工作项的唯一标识
        self.workitem_identifier = workitem_identifier  # type: str

    def validate(self):
        if self.value_list:
            for k in self.value_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWorkItemInfoResponseBodyWorkitemCustomFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_class_name is not None:
            result['fieldClassName'] = self.field_class_name
        if self.field_format is not None:
            result['fieldFormat'] = self.field_format
        if self.field_identifier is not None:
            result['fieldIdentifier'] = self.field_identifier
        if self.level is not None:
            result['level'] = self.level
        if self.object_value is not None:
            result['objectValue'] = self.object_value
        if self.position is not None:
            result['position'] = self.position
        if self.value is not None:
            result['value'] = self.value
        result['valueList'] = []
        if self.value_list is not None:
            for k in self.value_list:
                result['valueList'].append(k.to_map() if k else None)
        if self.workitem_identifier is not None:
            result['workitemIdentifier'] = self.workitem_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fieldClassName') is not None:
            self.field_class_name = m.get('fieldClassName')
        if m.get('fieldFormat') is not None:
            self.field_format = m.get('fieldFormat')
        if m.get('fieldIdentifier') is not None:
            self.field_identifier = m.get('fieldIdentifier')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('objectValue') is not None:
            self.object_value = m.get('objectValue')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('value') is not None:
            self.value = m.get('value')
        self.value_list = []
        if m.get('valueList') is not None:
            for k in m.get('valueList'):
                temp_model = GetWorkItemInfoResponseBodyWorkitemCustomFieldsValueList()
                self.value_list.append(temp_model.from_map(k))
        if m.get('workitemIdentifier') is not None:
            self.workitem_identifier = m.get('workitemIdentifier')
        return self


class GetWorkItemInfoResponseBodyWorkitem(TeaModel):
    def __init__(self, assigned_to=None, category_identifier=None, creator=None, custom_fields=None, document=None,
                 gmt_create=None, gmt_modified=None, identifier=None, logical_status=None, modifier=None,
                 parent_identifier=None, participant=None, serial_number=None, space_identifier=None, space_name=None,
                 space_type=None, sprint=None, status=None, status_identifier=None, status_stage_identifier=None, subject=None,
                 tag=None, tracker=None, update_status_at=None, verifier=None, workitem_type_identifier=None):
        # 负责人
        self.assigned_to = assigned_to  # type: str
        # 工作项的类型id
        self.category_identifier = category_identifier  # type: str
        # 创建人
        self.creator = creator  # type: str
        # 自定义字段列表
        self.custom_fields = custom_fields  # type: list[GetWorkItemInfoResponseBodyWorkitemCustomFields]
        # 工作项内容
        self.document = document  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 工作项唯一标识
        self.identifier = identifier  # type: str
        # 逻辑状态
        self.logical_status = logical_status  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 父工作项id
        self.parent_identifier = parent_identifier  # type: str
        # 参与人aliyunPk id列表
        self.participant = participant  # type: list[str]
        # 编号
        self.serial_number = serial_number  # type: str
        # 所属项目id
        self.space_identifier = space_identifier  # type: str
        # 所属项目名称
        self.space_name = space_name  # type: str
        # 项目类型
        self.space_type = space_type  # type: str
        # 关联的迭代id
        self.sprint = sprint  # type: list[str]
        # 状态名称
        self.status = status  # type: str
        # 状态id
        self.status_identifier = status_identifier  # type: str
        # 状态阶段id
        self.status_stage_identifier = status_stage_identifier  # type: str
        # 工作项标题
        self.subject = subject  # type: str
        # 标签id列表
        self.tag = tag  # type: list[str]
        # 抄送人的aliyunPk id列表
        self.tracker = tracker  # type: list[str]
        # 状态更新时间
        self.update_status_at = update_status_at  # type: long
        # 验证者的aliyunPk id列表
        self.verifier = verifier  # type: list[str]
        # 工作项类型id
        self.workitem_type_identifier = workitem_type_identifier  # type: str

    def validate(self):
        if self.custom_fields:
            for k in self.custom_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWorkItemInfoResponseBodyWorkitem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assigned_to is not None:
            result['assignedTo'] = self.assigned_to
        if self.category_identifier is not None:
            result['categoryIdentifier'] = self.category_identifier
        if self.creator is not None:
            result['creator'] = self.creator
        result['customFields'] = []
        if self.custom_fields is not None:
            for k in self.custom_fields:
                result['customFields'].append(k.to_map() if k else None)
        if self.document is not None:
            result['document'] = self.document
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.logical_status is not None:
            result['logicalStatus'] = self.logical_status
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.parent_identifier is not None:
            result['parentIdentifier'] = self.parent_identifier
        if self.participant is not None:
            result['participant'] = self.participant
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.sprint is not None:
            result['sprint'] = self.sprint
        if self.status is not None:
            result['status'] = self.status
        if self.status_identifier is not None:
            result['statusIdentifier'] = self.status_identifier
        if self.status_stage_identifier is not None:
            result['statusStageIdentifier'] = self.status_stage_identifier
        if self.subject is not None:
            result['subject'] = self.subject
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tracker is not None:
            result['tracker'] = self.tracker
        if self.update_status_at is not None:
            result['updateStatusAt'] = self.update_status_at
        if self.verifier is not None:
            result['verifier'] = self.verifier
        if self.workitem_type_identifier is not None:
            result['workitemTypeIdentifier'] = self.workitem_type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignedTo') is not None:
            self.assigned_to = m.get('assignedTo')
        if m.get('categoryIdentifier') is not None:
            self.category_identifier = m.get('categoryIdentifier')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        self.custom_fields = []
        if m.get('customFields') is not None:
            for k in m.get('customFields'):
                temp_model = GetWorkItemInfoResponseBodyWorkitemCustomFields()
                self.custom_fields.append(temp_model.from_map(k))
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('logicalStatus') is not None:
            self.logical_status = m.get('logicalStatus')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('parentIdentifier') is not None:
            self.parent_identifier = m.get('parentIdentifier')
        if m.get('participant') is not None:
            self.participant = m.get('participant')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('sprint') is not None:
            self.sprint = m.get('sprint')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusIdentifier') is not None:
            self.status_identifier = m.get('statusIdentifier')
        if m.get('statusStageIdentifier') is not None:
            self.status_stage_identifier = m.get('statusStageIdentifier')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tracker') is not None:
            self.tracker = m.get('tracker')
        if m.get('updateStatusAt') is not None:
            self.update_status_at = m.get('updateStatusAt')
        if m.get('verifier') is not None:
            self.verifier = m.get('verifier')
        if m.get('workitemTypeIdentifier') is not None:
            self.workitem_type_identifier = m.get('workitemTypeIdentifier')
        return self


class GetWorkItemInfoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None, workitem=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool
        # 工作项信息
        self.workitem = workitem  # type: GetWorkItemInfoResponseBodyWorkitem

    def validate(self):
        if self.workitem:
            self.workitem.validate()

    def to_map(self):
        _map = super(GetWorkItemInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.workitem is not None:
            result['workitem'] = self.workitem.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('workitem') is not None:
            temp_model = GetWorkItemInfoResponseBodyWorkitem()
            self.workitem = temp_model.from_map(m['workitem'])
        return self


class GetWorkItemInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetWorkItemInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkItemInfoResponse, self).to_map()
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
            temp_model = GetWorkItemInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkItemWorkFlowInfoRequest(TeaModel):
    def __init__(self, configuration_id=None):
        # 项目id
        self.configuration_id = configuration_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkItemWorkFlowInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration_id is not None:
            result['configurationId'] = self.configuration_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('configurationId') is not None:
            self.configuration_id = m.get('configurationId')
        return self


class GetWorkItemWorkFlowInfoResponseBodyWorkflowStatuses(TeaModel):
    def __init__(self, creator=None, description=None, gmt_create=None, gmt_modified=None, identifier=None,
                 modifier=None, name=None, resource_type=None, source=None, workflow_stage_identifier=None,
                 workflow_stage_name=None):
        # 创建人
        self.creator = creator  # type: str
        # 描述信息
        self.description = description  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 状态唯一标识
        self.identifier = identifier  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 状态名
        self.name = name  # type: str
        # 资源来源
        self.resource_type = resource_type  # type: str
        # 状态来源
        self.source = source  # type: str
        # 阶段信息-阶段的唯一标识
        self.workflow_stage_identifier = workflow_stage_identifier  # type: str
        # 阶段信息-名称
        self.workflow_stage_name = workflow_stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkItemWorkFlowInfoResponseBodyWorkflowStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.source is not None:
            result['source'] = self.source
        if self.workflow_stage_identifier is not None:
            result['workflowStageIdentifier'] = self.workflow_stage_identifier
        if self.workflow_stage_name is not None:
            result['workflowStageName'] = self.workflow_stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('workflowStageIdentifier') is not None:
            self.workflow_stage_identifier = m.get('workflowStageIdentifier')
        if m.get('workflowStageName') is not None:
            self.workflow_stage_name = m.get('workflowStageName')
        return self


class GetWorkItemWorkFlowInfoResponseBodyWorkflowWorkflowActions(TeaModel):
    def __init__(self, id=None, name=None, next_workflow_status_identifier=None, workflow_identifier=None,
                 workflow_status_identifier=None):
        # 流转步骤的id
        self.id = id  # type: long
        # action的名称
        self.name = name  # type: str
        # action对应的下个状态的信息id
        self.next_workflow_status_identifier = next_workflow_status_identifier  # type: str
        # action对应的工作流
        self.workflow_identifier = workflow_identifier  # type: str
        # action对应的当前状态id
        self.workflow_status_identifier = workflow_status_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkItemWorkFlowInfoResponseBodyWorkflowWorkflowActions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.next_workflow_status_identifier is not None:
            result['nextWorkflowStatusIdentifier'] = self.next_workflow_status_identifier
        if self.workflow_identifier is not None:
            result['workflowIdentifier'] = self.workflow_identifier
        if self.workflow_status_identifier is not None:
            result['workflowStatusIdentifier'] = self.workflow_status_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nextWorkflowStatusIdentifier') is not None:
            self.next_workflow_status_identifier = m.get('nextWorkflowStatusIdentifier')
        if m.get('workflowIdentifier') is not None:
            self.workflow_identifier = m.get('workflowIdentifier')
        if m.get('workflowStatusIdentifier') is not None:
            self.workflow_status_identifier = m.get('workflowStatusIdentifier')
        return self


class GetWorkItemWorkFlowInfoResponseBodyWorkflow(TeaModel):
    def __init__(self, creator=None, default_status_identifier=None, description=None, gmt_create=None,
                 gmt_modified=None, identifier=None, modifier=None, name=None, owner_space_identifier=None,
                 owner_space_type=None, resource_type=None, source=None, status_order=None, statuses=None, workflow_actions=None):
        # 创建人
        self.creator = creator  # type: str
        # 工作流的默认状态
        self.default_status_identifier = default_status_identifier  # type: str
        # 工作流的描述
        self.description = description  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 工作流唯一标识
        self.identifier = identifier  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 工作流名称
        self.name = name  # type: str
        # 工作流所属的团队空间或项目的identifier
        self.owner_space_identifier = owner_space_identifier  # type: str
        # 工作流所属的团队项目类型
        self.owner_space_type = owner_space_type  # type: str
        # 资源类型
        self.resource_type = resource_type  # type: str
        # 工作流来源
        self.source = source  # type: str
        # 工作流的状态顺序
        self.status_order = status_order  # type: str
        # 状态列表
        self.statuses = statuses  # type: list[GetWorkItemWorkFlowInfoResponseBodyWorkflowStatuses]
        # 工作流的流转步骤
        self.workflow_actions = workflow_actions  # type: list[GetWorkItemWorkFlowInfoResponseBodyWorkflowWorkflowActions]

    def validate(self):
        if self.statuses:
            for k in self.statuses:
                if k:
                    k.validate()
        if self.workflow_actions:
            for k in self.workflow_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetWorkItemWorkFlowInfoResponseBodyWorkflow, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_status_identifier is not None:
            result['defaultStatusIdentifier'] = self.default_status_identifier
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.owner_space_identifier is not None:
            result['ownerSpaceIdentifier'] = self.owner_space_identifier
        if self.owner_space_type is not None:
            result['ownerSpaceType'] = self.owner_space_type
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.source is not None:
            result['source'] = self.source
        if self.status_order is not None:
            result['statusOrder'] = self.status_order
        result['statuses'] = []
        if self.statuses is not None:
            for k in self.statuses:
                result['statuses'].append(k.to_map() if k else None)
        result['workflowActions'] = []
        if self.workflow_actions is not None:
            for k in self.workflow_actions:
                result['workflowActions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('defaultStatusIdentifier') is not None:
            self.default_status_identifier = m.get('defaultStatusIdentifier')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ownerSpaceIdentifier') is not None:
            self.owner_space_identifier = m.get('ownerSpaceIdentifier')
        if m.get('ownerSpaceType') is not None:
            self.owner_space_type = m.get('ownerSpaceType')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('statusOrder') is not None:
            self.status_order = m.get('statusOrder')
        self.statuses = []
        if m.get('statuses') is not None:
            for k in m.get('statuses'):
                temp_model = GetWorkItemWorkFlowInfoResponseBodyWorkflowStatuses()
                self.statuses.append(temp_model.from_map(k))
        self.workflow_actions = []
        if m.get('workflowActions') is not None:
            for k in m.get('workflowActions'):
                temp_model = GetWorkItemWorkFlowInfoResponseBodyWorkflowWorkflowActions()
                self.workflow_actions.append(temp_model.from_map(k))
        return self


class GetWorkItemWorkFlowInfoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None, workflow=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool
        # 工作项信息
        self.workflow = workflow  # type: GetWorkItemWorkFlowInfoResponseBodyWorkflow

    def validate(self):
        if self.workflow:
            self.workflow.validate()

    def to_map(self):
        _map = super(GetWorkItemWorkFlowInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.workflow is not None:
            result['workflow'] = self.workflow.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('workflow') is not None:
            temp_model = GetWorkItemWorkFlowInfoResponseBodyWorkflow()
            self.workflow = temp_model.from_map(m['workflow'])
        return self


class GetWorkItemWorkFlowInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetWorkItemWorkFlowInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkItemWorkFlowInfoResponse, self).to_map()
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
            temp_model = GetWorkItemWorkFlowInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkspaceResponseBodyWorkspace(TeaModel):
    def __init__(self, code_url=None, code_version=None, create_time=None, id=None, name=None, spec=None, status=None,
                 template=None, user_id=None):
        # 代码来源URL
        self.code_url = code_url  # type: str
        # 代码版本，支持 commitSHA、分支、标签
        self.code_version = code_version  # type: str
        # 创建时间戳
        self.create_time = create_time  # type: str
        # 工作空间唯一标识，字符串形式，可在云效DevStudio访问空间链接中获取
        self.id = id  # type: str
        # 工作空间名称
        self.name = name  # type: str
        # 机器规格
        self.spec = spec  # type: str
        # 空间状态，枚举：CREATING-创建中, SUCCESS-运行中, FROZEN-冻结中, RECOVERING-恢复中
        self.status = status  # type: str
        # 工作空间模板
        self.template = template  # type: str
        # 用户阿里云PK
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkspaceResponseBodyWorkspace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_url is not None:
            result['codeUrl'] = self.code_url
        if self.code_version is not None:
            result['codeVersion'] = self.code_version
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        if self.template is not None:
            result['template'] = self.template
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('codeUrl') is not None:
            self.code_url = m.get('codeUrl')
        if m.get('codeVersion') is not None:
            self.code_version = m.get('codeVersion')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetWorkspaceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None, workspace=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool
        # 工作空间信息
        self.workspace = workspace  # type: GetWorkspaceResponseBodyWorkspace

    def validate(self):
        if self.workspace:
            self.workspace.validate()

    def to_map(self):
        _map = super(GetWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.workspace is not None:
            result['workspace'] = self.workspace.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('workspace') is not None:
            temp_model = GetWorkspaceResponseBodyWorkspace()
            self.workspace = temp_model.from_map(m['workspace'])
        return self


class GetWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetWorkspaceResponse, self).to_map()
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
            temp_model = GetWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowTagGroupsResponseBodyFlowTagGroups(TeaModel):
    def __init__(self, creator_account_id=None, id=None, modifer_account_id=None, name=None):
        # 创建人
        self.creator_account_id = creator_account_id  # type: str
        # 标签分类id
        self.id = id  # type: long
        # 修改人
        self.modifer_account_id = modifer_account_id  # type: str
        # 标签分类名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFlowTagGroupsResponseBodyFlowTagGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.id is not None:
            result['id'] = self.id
        if self.modifer_account_id is not None:
            result['modiferAccountId'] = self.modifer_account_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modiferAccountId') is not None:
            self.modifer_account_id = m.get('modiferAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListFlowTagGroupsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, flow_tag_groups=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 标签分类
        self.flow_tag_groups = flow_tag_groups  # type: list[ListFlowTagGroupsResponseBodyFlowTagGroups]
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.flow_tag_groups:
            for k in self.flow_tag_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFlowTagGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['flowTagGroups'] = []
        if self.flow_tag_groups is not None:
            for k in self.flow_tag_groups:
                result['flowTagGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.flow_tag_groups = []
        if m.get('flowTagGroups') is not None:
            for k in m.get('flowTagGroups'):
                temp_model = ListFlowTagGroupsResponseBodyFlowTagGroups()
                self.flow_tag_groups.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListFlowTagGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListFlowTagGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFlowTagGroupsResponse, self).to_map()
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
            temp_model = ListFlowTagGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsRequest(TeaModel):
    def __init__(self, create_end_time=None, create_start_time=None, creator_account_ids=None, ids=None,
                 max_results=None, name=None, next_token=None, page_order=None, page_sort=None):
        # 主机组结束时间
        self.create_end_time = create_end_time  # type: long
        # 主机组创建时间
        self.create_start_time = create_start_time  # type: long
        # 创建阿里云账号id，多个逗号分割
        self.creator_account_ids = creator_account_ids  # type: str
        # 主机组id，多个逗号分割
        self.ids = ids  # type: str
        # 结果返回个数
        self.max_results = max_results  # type: long
        # 主机组名称
        self.name = name  # type: str
        # 分页token
        self.next_token = next_token  # type: str
        # 排序顺序
        self.page_order = page_order  # type: str
        # 排序条件ID
        self.page_sort = page_sort  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_end_time is not None:
            result['createEndTime'] = self.create_end_time
        if self.create_start_time is not None:
            result['createStartTime'] = self.create_start_time
        if self.creator_account_ids is not None:
            result['creatorAccountIds'] = self.creator_account_ids
        if self.ids is not None:
            result['ids'] = self.ids
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.name is not None:
            result['name'] = self.name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page_order is not None:
            result['pageOrder'] = self.page_order
        if self.page_sort is not None:
            result['pageSort'] = self.page_sort
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createEndTime') is not None:
            self.create_end_time = m.get('createEndTime')
        if m.get('createStartTime') is not None:
            self.create_start_time = m.get('createStartTime')
        if m.get('creatorAccountIds') is not None:
            self.creator_account_ids = m.get('creatorAccountIds')
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pageOrder') is not None:
            self.page_order = m.get('pageOrder')
        if m.get('pageSort') is not None:
            self.page_sort = m.get('pageSort')
        return self


class ListHostGroupsResponseBodyHostGroups(TeaModel):
    def __init__(self, aliyun_region=None, create_time=None, creator_account_id=None, description=None,
                 ecs_label_key=None, ecs_label_value=None, ecs_type=None, host_num=None, id=None, modifier_account_id=None,
                 name=None, service_connection_id=None, type=None, update_time=None):
        # 阿里云区域
        self.aliyun_region = aliyun_region  # type: str
        # 主机时间
        self.create_time = create_time  # type: long
        # 创建人阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 描述
        self.description = description  # type: str
        # ecs标签Key
        self.ecs_label_key = ecs_label_key  # type: str
        # Ecs标签值
        self.ecs_label_value = ecs_label_value  # type: str
        # 主机类型
        self.ecs_type = ecs_type  # type: str
        # 主机个数
        self.host_num = host_num  # type: long
        # 323232
        self.id = id  # type: long
        # 修改人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 部署组名称
        self.name = name  # type: str
        # 服务连接Id
        self.service_connection_id = service_connection_id  # type: long
        # 类型
        self.type = type  # type: str
        # 更新时间
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsResponseBodyHostGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_region is not None:
            result['aliyunRegion'] = self.aliyun_region
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.description is not None:
            result['description'] = self.description
        if self.ecs_label_key is not None:
            result['ecsLabelKey'] = self.ecs_label_key
        if self.ecs_label_value is not None:
            result['ecsLabelValue'] = self.ecs_label_value
        if self.ecs_type is not None:
            result['ecsType'] = self.ecs_type
        if self.host_num is not None:
            result['hostNum'] = self.host_num
        if self.id is not None:
            result['id'] = self.id
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.name is not None:
            result['name'] = self.name
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        if self.type is not None:
            result['type'] = self.type
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunRegion') is not None:
            self.aliyun_region = m.get('aliyunRegion')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('ecsLabelKey') is not None:
            self.ecs_label_key = m.get('ecsLabelKey')
        if m.get('ecsLabelValue') is not None:
            self.ecs_label_value = m.get('ecsLabelValue')
        if m.get('ecsType') is not None:
            self.ecs_type = m.get('ecsType')
        if m.get('hostNum') is not None:
            self.host_num = m.get('hostNum')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListHostGroupsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, host_groups=None, next_token=None, request_id=None,
                 success=None, total_count=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 主机组
        self.host_groups = host_groups  # type: list[ListHostGroupsResponseBodyHostGroups]
        # 分页token,空表示最后一页
        self.next_token = next_token  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['hostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['hostGroups'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.host_groups = []
        if m.get('hostGroups') is not None:
            for k in m.get('hostGroups'):
                temp_model = ListHostGroupsResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListHostGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostGroupsResponse, self).to_map()
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
            temp_model = ListHostGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationMembersRequest(TeaModel):
    def __init__(self, extern_uid=None, join_time_from=None, join_time_to=None, max_results=None, next_token=None,
                 organization_member_name=None, provider=None, state=None):
        self.extern_uid = extern_uid  # type: str
        self.join_time_from = join_time_from  # type: long
        self.join_time_to = join_time_to  # type: long
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.organization_member_name = organization_member_name  # type: str
        self.provider = provider  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_uid is not None:
            result['externUid'] = self.extern_uid
        if self.join_time_from is not None:
            result['joinTimeFrom'] = self.join_time_from
        if self.join_time_to is not None:
            result['joinTimeTo'] = self.join_time_to
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.organization_member_name is not None:
            result['organizationMemberName'] = self.organization_member_name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externUid') is not None:
            self.extern_uid = m.get('externUid')
        if m.get('joinTimeFrom') is not None:
            self.join_time_from = m.get('joinTimeFrom')
        if m.get('joinTimeTo') is not None:
            self.join_time_to = m.get('joinTimeTo')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('organizationMemberName') is not None:
            self.organization_member_name = m.get('organizationMemberName')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class ListOrganizationMembersResponseBodyMembersIdentities(TeaModel):
    def __init__(self, extern_uid=None, provider=None):
        # 第三方系统的用户Id
        self.extern_uid = extern_uid  # type: str
        # 第三方系统
        self.provider = provider  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrganizationMembersResponseBodyMembersIdentities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extern_uid is not None:
            result['externUid'] = self.extern_uid
        if self.provider is not None:
            result['provider'] = self.provider
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('externUid') is not None:
            self.extern_uid = m.get('externUid')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        return self


class ListOrganizationMembersResponseBodyMembers(TeaModel):
    def __init__(self, account_id=None, birthday=None, dept_lists=None, email=None, hired_date=None, identities=None,
                 join_time=None, last_visit_time=None, mobile=None, organization_member_name=None, organization_role_id=None,
                 organization_role_name=None, state=None):
        # 阿里云用户ID
        self.account_id = account_id  # type: str
        # 生日
        self.birthday = birthday  # type: long
        # 部门名称列表
        self.dept_lists = dept_lists  # type: list[str]
        # 邮箱
        self.email = email  # type: str
        # 入职时间
        self.hired_date = hired_date  # type: long
        # 第三方信息
        self.identities = identities  # type: ListOrganizationMembersResponseBodyMembersIdentities
        # 加入云效企业时间
        self.join_time = join_time  # type: long
        # 最近一次访问时间
        self.last_visit_time = last_visit_time  # type: long
        # 手机号
        self.mobile = mobile  # type: str
        # 企业成员名
        self.organization_member_name = organization_member_name  # type: str
        # 企业角色Id
        self.organization_role_id = organization_role_id  # type: str
        # 企业角色名字
        self.organization_role_name = organization_role_name  # type: str
        # 用户状态
        self.state = state  # type: str

    def validate(self):
        if self.identities:
            self.identities.validate()

    def to_map(self):
        _map = super(ListOrganizationMembersResponseBodyMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.birthday is not None:
            result['birthday'] = self.birthday
        if self.dept_lists is not None:
            result['deptLists'] = self.dept_lists
        if self.email is not None:
            result['email'] = self.email
        if self.hired_date is not None:
            result['hiredDate'] = self.hired_date
        if self.identities is not None:
            result['identities'] = self.identities.to_map()
        if self.join_time is not None:
            result['joinTime'] = self.join_time
        if self.last_visit_time is not None:
            result['lastVisitTime'] = self.last_visit_time
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.organization_member_name is not None:
            result['organizationMemberName'] = self.organization_member_name
        if self.organization_role_id is not None:
            result['organizationRoleId'] = self.organization_role_id
        if self.organization_role_name is not None:
            result['organizationRoleName'] = self.organization_role_name
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')
        if m.get('deptLists') is not None:
            self.dept_lists = m.get('deptLists')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('hiredDate') is not None:
            self.hired_date = m.get('hiredDate')
        if m.get('identities') is not None:
            temp_model = ListOrganizationMembersResponseBodyMembersIdentities()
            self.identities = temp_model.from_map(m['identities'])
        if m.get('joinTime') is not None:
            self.join_time = m.get('joinTime')
        if m.get('lastVisitTime') is not None:
            self.last_visit_time = m.get('lastVisitTime')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('organizationMemberName') is not None:
            self.organization_member_name = m.get('organizationMemberName')
        if m.get('organizationRoleId') is not None:
            self.organization_role_id = m.get('organizationRoleId')
        if m.get('organizationRoleName') is not None:
            self.organization_role_name = m.get('organizationRoleName')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class ListOrganizationMembersResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, members=None, next_token=None, request_id=None,
                 success=None, total_count=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 成员列表
        self.members = members  # type: list[ListOrganizationMembersResponseBodyMembers]
        # 分页Token
        self.next_token = next_token  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOrganizationMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = ListOrganizationMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListOrganizationMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOrganizationMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOrganizationMembersResponse, self).to_map()
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
            temp_model = ListOrganizationMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineJobHistorysRequest(TeaModel):
    def __init__(self, category=None, identifier=None, max_results=None, next_token=None):
        self.category = category  # type: str
        self.identifier = identifier  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineJobHistorysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListPipelineJobHistorysResponseBodyJobs(TeaModel):
    def __init__(self, execute_number=None, identifier=None, job_id=None, job_name=None, operator_account_id=None,
                 pipeline_id=None, pipeline_run_id=None, sources=None, status=None):
        self.execute_number = execute_number  # type: int
        self.identifier = identifier  # type: str
        self.job_id = job_id  # type: long
        self.job_name = job_name  # type: str
        self.operator_account_id = operator_account_id  # type: str
        self.pipeline_id = pipeline_id  # type: long
        self.pipeline_run_id = pipeline_run_id  # type: long
        self.sources = sources  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineJobHistorysResponseBodyJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execute_number is not None:
            result['executeNumber'] = self.execute_number
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.job_name is not None:
            result['jobName'] = self.job_name
        if self.operator_account_id is not None:
            result['operatorAccountId'] = self.operator_account_id
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.pipeline_run_id is not None:
            result['pipelineRunId'] = self.pipeline_run_id
        if self.sources is not None:
            result['sources'] = self.sources
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('executeNumber') is not None:
            self.execute_number = m.get('executeNumber')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')
        if m.get('operatorAccountId') is not None:
            self.operator_account_id = m.get('operatorAccountId')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('pipelineRunId') is not None:
            self.pipeline_run_id = m.get('pipelineRunId')
        if m.get('sources') is not None:
            self.sources = m.get('sources')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListPipelineJobHistorysResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, jobs=None, next_token=None, request_id=None,
                 success=None, total_count=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        self.jobs = jobs  # type: list[ListPipelineJobHistorysResponseBodyJobs]
        self.next_token = next_token  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPipelineJobHistorysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['jobs'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = ListPipelineJobHistorysResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListPipelineJobHistorysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPipelineJobHistorysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPipelineJobHistorysResponse, self).to_map()
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
            temp_model = ListPipelineJobHistorysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineJobsRequest(TeaModel):
    def __init__(self, category=None):
        self.category = category  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineJobsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        return self


class ListPipelineJobsResponseBodyJobs(TeaModel):
    def __init__(self, identifier=None, job_name=None, last_job_id=None, last_job_params=None):
        self.identifier = identifier  # type: str
        self.job_name = job_name  # type: str
        self.last_job_id = last_job_id  # type: long
        self.last_job_params = last_job_params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineJobsResponseBodyJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.job_name is not None:
            result['jobName'] = self.job_name
        if self.last_job_id is not None:
            result['lastJobId'] = self.last_job_id
        if self.last_job_params is not None:
            result['lastJobParams'] = self.last_job_params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')
        if m.get('lastJobId') is not None:
            self.last_job_id = m.get('lastJobId')
        if m.get('lastJobParams') is not None:
            self.last_job_params = m.get('lastJobParams')
        return self


class ListPipelineJobsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, jobs=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        self.jobs = jobs  # type: list[ListPipelineJobsResponseBodyJobs]
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPipelineJobsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        result['jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['jobs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = ListPipelineJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListPipelineJobsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPipelineJobsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPipelineJobsResponse, self).to_map()
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
            temp_model = ListPipelineJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelineRunsRequest(TeaModel):
    def __init__(self, end_time=None, max_results=None, next_token=None, start_time=None, status=None,
                 trigger_mode=None):
        # 结束时间
        self.end_time = end_time  # type: long
        # 最大返回数量
        self.max_results = max_results  # type: long
        # 分页Token
        self.next_token = next_token  # type: str
        # 开始时间
        self.start_time = start_time  # type: long
        # 状态 状态 FAIL 运行失败 SUCCESS 运行成功 RUNNING 运行中
        self.status = status  # type: str
        # 触发模式 1人工触发 2定时触发 3代码提交触发
        self.trigger_mode = trigger_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineRunsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')
        return self


class ListPipelineRunsResponseBodyPipelineRuns(TeaModel):
    def __init__(self, creator_account_id=None, end_time=None, pipeline_id=None, pipeline_run_id=None,
                 start_time=None, status=None, trigger_mode=None):
        # 运行人阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 结束时间
        self.end_time = end_time  # type: long
        # 流水线id
        self.pipeline_id = pipeline_id  # type: long
        # 流水线实例id
        self.pipeline_run_id = pipeline_run_id  # type: long
        # 开始时间
        self.start_time = start_time  # type: long
        # 运行状态
        self.status = status  # type: str
        # 触发模式
        self.trigger_mode = trigger_mode  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineRunsResponseBodyPipelineRuns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.pipeline_run_id is not None:
            result['pipelineRunId'] = self.pipeline_run_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('pipelineRunId') is not None:
            self.pipeline_run_id = m.get('pipelineRunId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')
        return self


class ListPipelineRunsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, next_token=None, pipeline_runs=None, request_id=None,
                 success=None, total_count=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 下一个分页token，为空时，表示没有下一页
        self.next_token = next_token  # type: str
        # 流水线运行实例
        self.pipeline_runs = pipeline_runs  # type: list[ListPipelineRunsResponseBodyPipelineRuns]
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.pipeline_runs:
            for k in self.pipeline_runs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPipelineRunsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['pipelineRuns'] = []
        if self.pipeline_runs is not None:
            for k in self.pipeline_runs:
                result['pipelineRuns'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.pipeline_runs = []
        if m.get('pipelineRuns') is not None:
            for k in m.get('pipelineRuns'):
                temp_model = ListPipelineRunsResponseBodyPipelineRuns()
                self.pipeline_runs.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListPipelineRunsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPipelineRunsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPipelineRunsResponse, self).to_map()
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
            temp_model = ListPipelineRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPipelinesRequest(TeaModel):
    def __init__(self, create_end_time=None, create_start_time=None, creator_account_ids=None,
                 execute_account_ids=None, execute_end_time=None, execute_start_time=None, max_results=None, next_token=None,
                 pipeline_name=None, status_list=None):
        # 创建结束时间
        self.create_end_time = create_end_time  # type: long
        # 创建开始时间
        self.create_start_time = create_start_time  # type: long
        # 创建人阿里云账号Id
        self.creator_account_ids = creator_account_ids  # type: str
        # 执行人阿里云账号id
        self.execute_account_ids = execute_account_ids  # type: str
        # 执行结束时间
        self.execute_end_time = execute_end_time  # type: long
        # 执行开始时间
        self.execute_start_time = execute_start_time  # type: long
        # 返回的总数
        self.max_results = max_results  # type: long
        # 分页Token
        self.next_token = next_token  # type: str
        # 流水线名称
        self.pipeline_name = pipeline_name  # type: str
        # 状态列表，多个逗号分割
        self.status_list = status_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_end_time is not None:
            result['createEndTime'] = self.create_end_time
        if self.create_start_time is not None:
            result['createStartTime'] = self.create_start_time
        if self.creator_account_ids is not None:
            result['creatorAccountIds'] = self.creator_account_ids
        if self.execute_account_ids is not None:
            result['executeAccountIds'] = self.execute_account_ids
        if self.execute_end_time is not None:
            result['executeEndTime'] = self.execute_end_time
        if self.execute_start_time is not None:
            result['executeStartTime'] = self.execute_start_time
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        if self.status_list is not None:
            result['statusList'] = self.status_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createEndTime') is not None:
            self.create_end_time = m.get('createEndTime')
        if m.get('createStartTime') is not None:
            self.create_start_time = m.get('createStartTime')
        if m.get('creatorAccountIds') is not None:
            self.creator_account_ids = m.get('creatorAccountIds')
        if m.get('executeAccountIds') is not None:
            self.execute_account_ids = m.get('executeAccountIds')
        if m.get('executeEndTime') is not None:
            self.execute_end_time = m.get('executeEndTime')
        if m.get('executeStartTime') is not None:
            self.execute_start_time = m.get('executeStartTime')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        return self


class ListPipelinesResponseBodyPipelines(TeaModel):
    def __init__(self, create_time=None, creator_account_id=None, pipeline_id=None, pipeline_name=None):
        # 创建时间
        self.create_time = create_time  # type: long
        # 创建人阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 流水线id
        self.pipeline_id = pipeline_id  # type: long
        # 流水线名称
        self.pipeline_name = pipeline_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelinesResponseBodyPipelines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        return self


class ListPipelinesResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, next_token=None, pipelines=None, request_id=None,
                 success=None, total_count=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 分页Token
        self.next_token = next_token  # type: str
        # 流水线
        self.pipelines = pipelines  # type: list[ListPipelinesResponseBodyPipelines]
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.pipelines:
            for k in self.pipelines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPipelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['pipelines'] = []
        if self.pipelines is not None:
            for k in self.pipelines:
                result['pipelines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.pipelines = []
        if m.get('pipelines') is not None:
            for k in m.get('pipelines'):
                temp_model = ListPipelinesResponseBodyPipelines()
                self.pipelines.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListPipelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListPipelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPipelinesResponse, self).to_map()
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
            temp_model = ListPipelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectMembersRequest(TeaModel):
    def __init__(self, target_type=None):
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_type is not None:
            result['targetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        return self


class ListProjectMembersResponseBodyMembersDivision(TeaModel):
    def __init__(self, identifier=None):
        # 部门唯一标识
        self.identifier = identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectMembersResponseBodyMembersDivision, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['identifier'] = self.identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        return self


class ListProjectMembersResponseBodyMembersOrganizationUserInfo(TeaModel):
    def __init__(self, organization_identifier=None):
        # 企业唯一标识符
        self.organization_identifier = organization_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectMembersResponseBodyMembersOrganizationUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_identifier is not None:
            result['organizationIdentifier'] = self.organization_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('organizationIdentifier') is not None:
            self.organization_identifier = m.get('organizationIdentifier')
        return self


class ListProjectMembersResponseBodyMembers(TeaModel):
    def __init__(self, account=None, avatar=None, ding_talk_id=None, display_name=None, display_nick_name=None,
                 display_real_name=None, division=None, email=None, gender=None, identifier=None, mobile=None, name_en=None,
                 nick_name=None, nick_name_pinyin=None, organization_user_info=None, real_name=None, real_name_pinyin=None,
                 stamp=None, tb_role_id=None):
        # 登陆账号
        self.account = account  # type: str
        # 用户头像
        self.avatar = avatar  # type: str
        # 钉钉id
        self.ding_talk_id = ding_talk_id  # type: str
        # 展示名
        self.display_name = display_name  # type: str
        # 展示昵称
        self.display_nick_name = display_nick_name  # type: str
        # 展示真名
        self.display_real_name = display_real_name  # type: str
        # 部门信息
        self.division = division  # type: ListProjectMembersResponseBodyMembersDivision
        # 邮箱
        self.email = email  # type: str
        # 性别
        self.gender = gender  # type: str
        # 用户唯一 标识符
        self.identifier = identifier  # type: str
        # 手机号
        self.mobile = mobile  # type: str
        # 英文名
        self.name_en = name_en  # type: str
        # 昵称
        self.nick_name = nick_name  # type: str
        # 昵称拼音
        self.nick_name_pinyin = nick_name_pinyin  # type: str
        # 企业信息
        self.organization_user_info = organization_user_info  # type: ListProjectMembersResponseBodyMembersOrganizationUserInfo
        # 真名
        self.real_name = real_name  # type: str
        # 真名拼音
        self.real_name_pinyin = real_name_pinyin  # type: str
        # 用户类型
        self.stamp = stamp  # type: str
        # 角色id
        self.tb_role_id = tb_role_id  # type: str

    def validate(self):
        if self.division:
            self.division.validate()
        if self.organization_user_info:
            self.organization_user_info.validate()

    def to_map(self):
        _map = super(ListProjectMembersResponseBodyMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.ding_talk_id is not None:
            result['dingTalkId'] = self.ding_talk_id
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.display_nick_name is not None:
            result['displayNickName'] = self.display_nick_name
        if self.display_real_name is not None:
            result['displayRealName'] = self.display_real_name
        if self.division is not None:
            result['division'] = self.division.to_map()
        if self.email is not None:
            result['email'] = self.email
        if self.gender is not None:
            result['gender'] = self.gender
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.mobile is not None:
            result['mobile'] = self.mobile
        if self.name_en is not None:
            result['nameEn'] = self.name_en
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.nick_name_pinyin is not None:
            result['nickNamePinyin'] = self.nick_name_pinyin
        if self.organization_user_info is not None:
            result['organizationUserInfo'] = self.organization_user_info.to_map()
        if self.real_name is not None:
            result['realName'] = self.real_name
        if self.real_name_pinyin is not None:
            result['realNamePinyin'] = self.real_name_pinyin
        if self.stamp is not None:
            result['stamp'] = self.stamp
        if self.tb_role_id is not None:
            result['tbRoleId'] = self.tb_role_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('dingTalkId') is not None:
            self.ding_talk_id = m.get('dingTalkId')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('displayNickName') is not None:
            self.display_nick_name = m.get('displayNickName')
        if m.get('displayRealName') is not None:
            self.display_real_name = m.get('displayRealName')
        if m.get('division') is not None:
            temp_model = ListProjectMembersResponseBodyMembersDivision()
            self.division = temp_model.from_map(m['division'])
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        if m.get('nameEn') is not None:
            self.name_en = m.get('nameEn')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('nickNamePinyin') is not None:
            self.nick_name_pinyin = m.get('nickNamePinyin')
        if m.get('organizationUserInfo') is not None:
            temp_model = ListProjectMembersResponseBodyMembersOrganizationUserInfo()
            self.organization_user_info = temp_model.from_map(m['organizationUserInfo'])
        if m.get('realName') is not None:
            self.real_name = m.get('realName')
        if m.get('realNamePinyin') is not None:
            self.real_name_pinyin = m.get('realNamePinyin')
        if m.get('stamp') is not None:
            self.stamp = m.get('stamp')
        if m.get('tbRoleId') is not None:
            self.tb_role_id = m.get('tbRoleId')
        return self


class ListProjectMembersResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, members=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # member信息
        self.members = members  # type: list[ListProjectMembersResponseBodyMembers]
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        result['members'] = []
        if self.members is not None:
            for k in self.members:
                result['members'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        self.members = []
        if m.get('members') is not None:
            for k in m.get('members'):
                temp_model = ListProjectMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListProjectMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProjectMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectMembersResponse, self).to_map()
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
            temp_model = ListProjectMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectTemplatesRequest(TeaModel):
    def __init__(self, category=None):
        # 模板类型
        self.category = category  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        return self


class ListProjectTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, copy_from=None, creator=None, description=None, gmt_create=None, gmt_modified=None, icon=None,
                 identifier=None, modifier=None, name=None, name_en=None, resource_category=None, resource_type=None,
                 space_identifier=None, space_type=None, type=None):
        self.copy_from = copy_from  # type: str
        # 创建人id
        self.creator = creator  # type: str
        # 描述信息
        self.description = description  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 模板封面
        self.icon = icon  # type: str
        # 模板唯一标识符
        self.identifier = identifier  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 模板名称
        self.name = name  # type: str
        # 模板英文名称
        self.name_en = name_en  # type: str
        # 所属资源类型
        self.resource_category = resource_category  # type: str
        self.resource_type = resource_type  # type: str
        self.space_identifier = space_identifier  # type: str
        self.space_type = space_type  # type: str
        # 模板类型 0-system/4-custom/16-instance
        self.type = type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectTemplatesResponseBodyTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy_from is not None:
            result['copyFrom'] = self.copy_from
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.icon is not None:
            result['icon'] = self.icon
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.name_en is not None:
            result['nameEn'] = self.name_en
        if self.resource_category is not None:
            result['resourceCategory'] = self.resource_category
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('copyFrom') is not None:
            self.copy_from = m.get('copyFrom')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameEn') is not None:
            self.name_en = m.get('nameEn')
        if m.get('resourceCategory') is not None:
            self.resource_category = m.get('resourceCategory')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListProjectTemplatesResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, request_id=None, success=None, templates=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool
        # 项目模板信息
        self.templates = templates  # type: list[ListProjectTemplatesResponseBodyTemplates]

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        result['templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        self.templates = []
        if m.get('templates') is not None:
            for k in m.get('templates'):
                temp_model = ListProjectTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListProjectTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProjectTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectTemplatesResponse, self).to_map()
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
            temp_model = ListProjectTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectWorkitemTypesRequest(TeaModel):
    def __init__(self, category=None, space_type=None):
        # 工作项类型
        self.category = category  # type: str
        # 空间类型
        self.space_type = space_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectWorkitemTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        return self


class ListProjectWorkitemTypesResponseBodyWorkitemTypes(TeaModel):
    def __init__(self, add_user=None, category_identifier=None, creator=None, default_type=None, description=None,
                 enable=None, gmt_add=None, gmt_create=None, identifier=None, name=None, name_en=None, system_default=None):
        # 添加到项目中的添加人
        self.add_user = add_user  # type: str
        # 工作项类型
        self.category_identifier = category_identifier  # type: str
        # 工作项类型创建人
        self.creator = creator  # type: str
        # 在项目中是否为默认类型
        self.default_type = default_type  # type: bool
        # 描述
        self.description = description  # type: str
        # 是否启用
        self.enable = enable  # type: bool
        # 添加到项目中的时间
        self.gmt_add = gmt_add  # type: long
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 工作项类型id
        self.identifier = identifier  # type: str
        # 工作项类型的名称
        self.name = name  # type: str
        # 工作项类型的英文名称
        self.name_en = name_en  # type: str
        # 是否系统默认
        self.system_default = system_default  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectWorkitemTypesResponseBodyWorkitemTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_user is not None:
            result['addUser'] = self.add_user
        if self.category_identifier is not None:
            result['categoryIdentifier'] = self.category_identifier
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_type is not None:
            result['defaultType'] = self.default_type
        if self.description is not None:
            result['description'] = self.description
        if self.enable is not None:
            result['enable'] = self.enable
        if self.gmt_add is not None:
            result['gmtAdd'] = self.gmt_add
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.name is not None:
            result['name'] = self.name
        if self.name_en is not None:
            result['nameEn'] = self.name_en
        if self.system_default is not None:
            result['systemDefault'] = self.system_default
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('addUser') is not None:
            self.add_user = m.get('addUser')
        if m.get('categoryIdentifier') is not None:
            self.category_identifier = m.get('categoryIdentifier')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('defaultType') is not None:
            self.default_type = m.get('defaultType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('gmtAdd') is not None:
            self.gmt_add = m.get('gmtAdd')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameEn') is not None:
            self.name_en = m.get('nameEn')
        if m.get('systemDefault') is not None:
            self.system_default = m.get('systemDefault')
        return self


class ListProjectWorkitemTypesResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None, workitem_types=None):
        # 错误返回码
        self.error_code = error_code  # type: str
        # 错误返回信息
        self.error_message = error_message  # type: str
        # openapi平台的request id
        self.request_id = request_id  # type: str
        # 接口是否正常返回
        self.success = success  # type: bool
        # 工作项类型
        self.workitem_types = workitem_types  # type: list[ListProjectWorkitemTypesResponseBodyWorkitemTypes]

    def validate(self):
        if self.workitem_types:
            for k in self.workitem_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectWorkitemTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        result['workitemTypes'] = []
        if self.workitem_types is not None:
            for k in self.workitem_types:
                result['workitemTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        self.workitem_types = []
        if m.get('workitemTypes') is not None:
            for k in m.get('workitemTypes'):
                temp_model = ListProjectWorkitemTypesResponseBodyWorkitemTypes()
                self.workitem_types.append(temp_model.from_map(k))
        return self


class ListProjectWorkitemTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProjectWorkitemTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectWorkitemTypesResponse, self).to_map()
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
            temp_model = ListProjectWorkitemTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(self, category=None, conditions=None, extra_conditions=None, max_results=None, next_token=None,
                 scope=None):
        # 项目类型
        self.category = category  # type: str
        self.conditions = conditions  # type: str
        self.extra_conditions = extra_conditions  # type: str
        # 每页最大返回数量，0-200，默认值20
        self.max_results = max_results  # type: long
        # 分页中的起始序列
        self.next_token = next_token  # type: str
        # 公开类型
        self.scope = scope  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.conditions is not None:
            result['conditions'] = self.conditions
        if self.extra_conditions is not None:
            result['extraConditions'] = self.extra_conditions
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.scope is not None:
            result['scope'] = self.scope
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('conditions') is not None:
            self.conditions = m.get('conditions')
        if m.get('extraConditions') is not None:
            self.extra_conditions = m.get('extraConditions')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        return self


class ListProjectsResponseBodyProjects(TeaModel):
    def __init__(self, category_identifier=None, creator=None, custom_code=None, delete_time=None, description=None,
                 gmt_create=None, icon=None, identifier=None, logical_status=None, name=None, scope=None,
                 status_stage_identifier=None, type_identifier=None):
        # 类型
        self.category_identifier = category_identifier  # type: str
        # 创建人
        self.creator = creator  # type: str
        # 自定义编号
        self.custom_code = custom_code  # type: str
        # 删除时间
        self.delete_time = delete_time  # type: long
        # 描述信息
        self.description = description  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 项目封面
        self.icon = icon  # type: str
        # 项目唯一标识符
        self.identifier = identifier  # type: str
        # 逻辑状态
        self.logical_status = logical_status  # type: str
        # 项目名称
        self.name = name  # type: str
        # 公开还是私有
        self.scope = scope  # type: str
        # 状态阶段
        self.status_stage_identifier = status_stage_identifier  # type: str
        # 类型id
        self.type_identifier = type_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyProjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_identifier is not None:
            result['categoryIdentifier'] = self.category_identifier
        if self.creator is not None:
            result['creator'] = self.creator
        if self.custom_code is not None:
            result['customCode'] = self.custom_code
        if self.delete_time is not None:
            result['deleteTime'] = self.delete_time
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.icon is not None:
            result['icon'] = self.icon
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.logical_status is not None:
            result['logicalStatus'] = self.logical_status
        if self.name is not None:
            result['name'] = self.name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.status_stage_identifier is not None:
            result['statusStageIdentifier'] = self.status_stage_identifier
        if self.type_identifier is not None:
            result['typeIdentifier'] = self.type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('categoryIdentifier') is not None:
            self.category_identifier = m.get('categoryIdentifier')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('customCode') is not None:
            self.custom_code = m.get('customCode')
        if m.get('deleteTime') is not None:
            self.delete_time = m.get('deleteTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('logicalStatus') is not None:
            self.logical_status = m.get('logicalStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('statusStageIdentifier') is not None:
            self.status_stage_identifier = m.get('statusStageIdentifier')
        if m.get('typeIdentifier') is not None:
            self.type_identifier = m.get('typeIdentifier')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, max_results=None, next_token=None, projects=None,
                 request_id=None, success=None, total_count=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 每页数量
        self.max_results = max_results  # type: long
        # 分页Token，没有下一页则为空
        self.next_token = next_token  # type: str
        # 项目信息
        self.projects = projects  # type: list[ListProjectsResponseBodyProjects]
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool
        # 总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = ListProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectsResponse, self).to_map()
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoriesRequest(TeaModel):
    def __init__(self, access_token=None, archived=None, order_by=None, organization_id=None, page=None,
                 per_page=None, search=None, sort=None):
        # accessToken
        self.access_token = access_token  # type: str
        # 是否列出归档项目
        self.archived = archived  # type: bool
        # 排序字段
        self.order_by = order_by  # type: str
        # 企业ID
        self.organization_id = organization_id  # type: str
        # 页码
        self.page = page  # type: long
        # 每页大小
        self.per_page = per_page  # type: long
        # 搜索关键字
        self.search = search  # type: str
        # 排序方式 (desc: 降序, asc: 升序)
        self.sort = sort  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoriesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.archived is not None:
            result['archived'] = self.archived
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        if self.page is not None:
            result['page'] = self.page
        if self.per_page is not None:
            result['perPage'] = self.per_page
        if self.search is not None:
            result['search'] = self.search
        if self.sort is not None:
            result['sort'] = self.sort
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('archived') is not None:
            self.archived = m.get('archived')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('perPage') is not None:
            self.per_page = m.get('perPage')
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        return self


class ListRepositoriesResponseBodyResult(TeaModel):
    def __init__(self, id=None, access_level=None, archive=None, avatar_url=None, created_at=None, description=None,
                 import_status=None, last_activity_at=None, name=None, name_with_namespace=None, namespace_id=None, path=None,
                 path_with_namespace=None, star=None, star_count=None, updated_at=None, visibility_level=None, web_url=None):
        # 代码库Id
        self.id = id  # type: long
        # 当前用户在该代码库上的权限类型
        self.access_level = access_level  # type: int
        # 代码库是否归档
        self.archive = archive  # type: bool
        # 头像地址
        self.avatar_url = avatar_url  # type: str
        # 创建时间
        self.created_at = created_at  # type: str
        # 代码库描述
        self.description = description  # type: str
        # 代码库导入状态
        self.import_status = import_status  # type: str
        # 最后活跃时间
        self.last_activity_at = last_activity_at  # type: str
        # 代码库名称
        self.name = name  # type: str
        # 代码库完整名称（含完整组名称）
        self.name_with_namespace = name_with_namespace  # type: str
        # 上级路径的id
        self.namespace_id = namespace_id  # type: long
        # 代码库路径
        self.path = path  # type: str
        # 代码库完整路径（含完整组路径）
        self.path_with_namespace = path_with_namespace  # type: str
        # 是否被收藏
        self.star = star  # type: bool
        # 被收藏的数量
        self.star_count = star_count  # type: long
        # 更新时间
        self.updated_at = updated_at  # type: str
        # 可见性;0标识私有的/10标识企业内公开
        self.visibility_level = visibility_level  # type: str
        # 页面访问时的URL
        self.web_url = web_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoriesResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.access_level is not None:
            result['accessLevel'] = self.access_level
        if self.archive is not None:
            result['archive'] = self.archive
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.import_status is not None:
            result['importStatus'] = self.import_status
        if self.last_activity_at is not None:
            result['lastActivityAt'] = self.last_activity_at
        if self.name is not None:
            result['name'] = self.name
        if self.name_with_namespace is not None:
            result['nameWithNamespace'] = self.name_with_namespace
        if self.namespace_id is not None:
            result['namespaceId'] = self.namespace_id
        if self.path is not None:
            result['path'] = self.path
        if self.path_with_namespace is not None:
            result['pathWithNamespace'] = self.path_with_namespace
        if self.star is not None:
            result['star'] = self.star
        if self.star_count is not None:
            result['starCount'] = self.star_count
        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at
        if self.visibility_level is not None:
            result['visibilityLevel'] = self.visibility_level
        if self.web_url is not None:
            result['webUrl'] = self.web_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('accessLevel') is not None:
            self.access_level = m.get('accessLevel')
        if m.get('archive') is not None:
            self.archive = m.get('archive')
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('importStatus') is not None:
            self.import_status = m.get('importStatus')
        if m.get('lastActivityAt') is not None:
            self.last_activity_at = m.get('lastActivityAt')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameWithNamespace') is not None:
            self.name_with_namespace = m.get('nameWithNamespace')
        if m.get('namespaceId') is not None:
            self.namespace_id = m.get('namespaceId')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('pathWithNamespace') is not None:
            self.path_with_namespace = m.get('pathWithNamespace')
        if m.get('star') is not None:
            self.star = m.get('star')
        if m.get('starCount') is not None:
            self.star_count = m.get('starCount')
        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')
        if m.get('visibilityLevel') is not None:
            self.visibility_level = m.get('visibilityLevel')
        if m.get('webUrl') is not None:
            self.web_url = m.get('webUrl')
        return self


class ListRepositoriesResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        # 错误码
        self.error_code = error_code  # type: int
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求requestId
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoriesResponseBodyResult]
        # 调用是否成功
        self.success = success  # type: bool
        # 总数量
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoriesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRepositoriesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListRepositoriesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRepositoriesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoriesResponse, self).to_map()
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
            temp_model = ListRepositoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryMemberWithInheritedRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None):
        # accessToken
        self.access_token = access_token  # type: str
        # 企业Id
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        return self


class ListRepositoryMemberWithInheritedResponseBodyResultInherited(TeaModel):
    def __init__(self, id=None, name=None, name_with_namespace=None, path=None, path_with_namespace=None, type=None,
                 visibility_level=None):
        self.id = id  # type: long
        self.name = name  # type: str
        self.name_with_namespace = name_with_namespace  # type: str
        self.path = path  # type: str
        self.path_with_namespace = path_with_namespace  # type: str
        self.type = type  # type: str
        self.visibility_level = visibility_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedResponseBodyResultInherited, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.name_with_namespace is not None:
            result['nameWithNamespace'] = self.name_with_namespace
        if self.path is not None:
            result['path'] = self.path
        if self.path_with_namespace is not None:
            result['pathWithNamespace'] = self.path_with_namespace
        if self.type is not None:
            result['type'] = self.type
        if self.visibility_level is not None:
            result['visibilityLevel'] = self.visibility_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameWithNamespace') is not None:
            self.name_with_namespace = m.get('nameWithNamespace')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('pathWithNamespace') is not None:
            self.path_with_namespace = m.get('pathWithNamespace')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('visibilityLevel') is not None:
            self.visibility_level = m.get('visibilityLevel')
        return self


class ListRepositoryMemberWithInheritedResponseBodyResult(TeaModel):
    def __init__(self, access_level=None, avatar_url=None, email=None, extern_user_id=None, id=None, inherited=None,
                 name=None, state=None, username=None):
        self.access_level = access_level  # type: int
        self.avatar_url = avatar_url  # type: str
        self.email = email  # type: str
        self.extern_user_id = extern_user_id  # type: str
        self.id = id  # type: long
        self.inherited = inherited  # type: ListRepositoryMemberWithInheritedResponseBodyResultInherited
        self.name = name  # type: str
        self.state = state  # type: str
        self.username = username  # type: str

    def validate(self):
        if self.inherited:
            self.inherited.validate()

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level is not None:
            result['accessLevel'] = self.access_level
        if self.avatar_url is not None:
            result['avatarUrl'] = self.avatar_url
        if self.email is not None:
            result['email'] = self.email
        if self.extern_user_id is not None:
            result['externUserId'] = self.extern_user_id
        if self.id is not None:
            result['id'] = self.id
        if self.inherited is not None:
            result['inherited'] = self.inherited.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.state is not None:
            result['state'] = self.state
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessLevel') is not None:
            self.access_level = m.get('accessLevel')
        if m.get('avatarUrl') is not None:
            self.avatar_url = m.get('avatarUrl')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('externUserId') is not None:
            self.extern_user_id = m.get('externUserId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('inherited') is not None:
            temp_model = ListRepositoryMemberWithInheritedResponseBodyResultInherited()
            self.inherited = temp_model.from_map(m['inherited'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListRepositoryMemberWithInheritedResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryMemberWithInheritedResponseBodyResult]
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRepositoryMemberWithInheritedResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListRepositoryMemberWithInheritedResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRepositoryMemberWithInheritedResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryMemberWithInheritedResponse, self).to_map()
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
            temp_model = ListRepositoryMemberWithInheritedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryWebhookRequest(TeaModel):
    def __init__(self, access_token=None, organization_id=None, page=None, page_size=None):
        # accessToken
        self.access_token = access_token  # type: str
        # 企业Id
        self.organization_id = organization_id  # type: str
        # 页码
        self.page = page  # type: long
        # 每页数据量
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListRepositoryWebhookResponseBodyResult(TeaModel):
    def __init__(self, created_at=None, description=None, enable_ssl_verification=None, id=None,
                 last_test_result=None, merge_requests_events=None, note_events=None, project_id=None, push_events=None,
                 secret_token=None, tag_push_events=None, url=None):
        self.created_at = created_at  # type: str
        self.description = description  # type: str
        self.enable_ssl_verification = enable_ssl_verification  # type: bool
        self.id = id  # type: long
        self.last_test_result = last_test_result  # type: str
        self.merge_requests_events = merge_requests_events  # type: bool
        self.note_events = note_events  # type: bool
        self.project_id = project_id  # type: long
        self.push_events = push_events  # type: bool
        self.secret_token = secret_token  # type: str
        self.tag_push_events = tag_push_events  # type: bool
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRepositoryWebhookResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.enable_ssl_verification is not None:
            result['enableSslVerification'] = self.enable_ssl_verification
        if self.id is not None:
            result['id'] = self.id
        if self.last_test_result is not None:
            result['lastTestResult'] = self.last_test_result
        if self.merge_requests_events is not None:
            result['mergeRequestsEvents'] = self.merge_requests_events
        if self.note_events is not None:
            result['noteEvents'] = self.note_events
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.push_events is not None:
            result['pushEvents'] = self.push_events
        if self.secret_token is not None:
            result['secretToken'] = self.secret_token
        if self.tag_push_events is not None:
            result['tagPushEvents'] = self.tag_push_events
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enableSslVerification') is not None:
            self.enable_ssl_verification = m.get('enableSslVerification')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastTestResult') is not None:
            self.last_test_result = m.get('lastTestResult')
        if m.get('mergeRequestsEvents') is not None:
            self.merge_requests_events = m.get('mergeRequestsEvents')
        if m.get('noteEvents') is not None:
            self.note_events = m.get('noteEvents')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('pushEvents') is not None:
            self.push_events = m.get('pushEvents')
        if m.get('secretToken') is not None:
            self.secret_token = m.get('secretToken')
        if m.get('tagPushEvents') is not None:
            self.tag_push_events = m.get('tagPushEvents')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListRepositoryWebhookResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None, total=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: list[ListRepositoryWebhookResponseBodyResult]
        self.success = success  # type: bool
        self.total = total  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRepositoryWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListRepositoryWebhookResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListRepositoryWebhookResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRepositoryWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRepositoryWebhookResponse, self).to_map()
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
            temp_model = ListRepositoryWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceMembersResponseBodyResourceMembers(TeaModel):
    def __init__(self, account_id=None, role_name=None, username=None):
        # 账号id
        self.account_id = account_id  # type: str
        # 角色
        self.role_name = role_name  # type: str
        # 用户名称
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceMembersResponseBodyResourceMembers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.role_name is not None:
            result['roleName'] = self.role_name
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListResourceMembersResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, resource_members=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 成员
        self.resource_members = resource_members  # type: list[ListResourceMembersResponseBodyResourceMembers]
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.success = success  # type: bool

    def validate(self):
        if self.resource_members:
            for k in self.resource_members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resourceMembers'] = []
        if self.resource_members is not None:
            for k in self.resource_members:
                result['resourceMembers'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resource_members = []
        if m.get('resourceMembers') is not None:
            for k in m.get('resourceMembers'):
                temp_model = ListResourceMembersResponseBodyResourceMembers()
                self.resource_members.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListResourceMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListResourceMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceMembersResponse, self).to_map()
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
            temp_model = ListResourceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceConnectionsRequest(TeaModel):
    def __init__(self, serice_connection_type=None):
        # aliyun_code  阿里云代码 Codeup       Codeup  Gitee        码云 github       Github ack       容器服务Kubernetes(ACK) docker_register_aliyun    容器镜像服务(ACR) ecs          对象存储(OSS) edas          企业级分布式应用(EDAS) emas         移动研发平台(EMAS) fc            阿里云函数计算(FC) kubernetes     自建k8s集群 oss            对象存储(OSS) PACKAGES       制品仓库 ros   资源编排服务(ROS) sae       Serverless应用引擎(SAE)
        self.serice_connection_type = serice_connection_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceConnectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serice_connection_type is not None:
            result['sericeConnectionType'] = self.serice_connection_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sericeConnectionType') is not None:
            self.serice_connection_type = m.get('sericeConnectionType')
        return self


class ListServiceConnectionsResponseBodyServiceConnections(TeaModel):
    def __init__(self, create_time=None, id=None, name=None, owner_account_id=None, type=None):
        # 创建时间
        self.create_time = create_time  # type: long
        # 服务连接Id
        self.id = id  # type: long
        # 服务连接名称
        self.name = name  # type: str
        # 拥有者阿里云账号id
        self.owner_account_id = owner_account_id  # type: long
        # 服务连接类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceConnectionsResponseBodyServiceConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.owner_account_id is not None:
            result['ownerAccountId'] = self.owner_account_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ownerAccountId') is not None:
            self.owner_account_id = m.get('ownerAccountId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListServiceConnectionsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, service_connections=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 服务连接
        self.service_connections = service_connections  # type: list[ListServiceConnectionsResponseBodyServiceConnections]
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.service_connections:
            for k in self.service_connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceConnectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['serviceConnections'] = []
        if self.service_connections is not None:
            for k in self.service_connections:
                result['serviceConnections'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.service_connections = []
        if m.get('serviceConnections') is not None:
            for k in m.get('serviceConnections'):
                temp_model = ListServiceConnectionsResponseBodyServiceConnections()
                self.service_connections.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListServiceConnectionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceConnectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceConnectionsResponse, self).to_map()
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
            temp_model = ListServiceConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSprintsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, space_identifier=None, space_type=None):
        # 每页最大返回数量，0-200，默认值20
        self.max_results = max_results  # type: long
        # 分页中的起始序列
        self.next_token = next_token  # type: str
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 类型
        self.space_type = space_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSprintsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        return self


class ListSprintsResponseBodySprints(TeaModel):
    def __init__(self, creator=None, description=None, end_date=None, gmt_create=None, gmt_modified=None,
                 identifier=None, modifier=None, name=None, scope=None, space_identifier=None, start_date=None, status=None):
        # 创建人id
        self.creator = creator  # type: str
        # 描述信息
        self.description = description  # type: str
        # 结束时间
        self.end_date = end_date  # type: long
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 迭代唯一标识符
        self.identifier = identifier  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 迭代名称
        self.name = name  # type: str
        # 可见范围
        self.scope = scope  # type: str
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 开始时间
        self.start_date = start_date  # type: long
        # 状态，未开始:Todo, 进行中:Doing, 已完成:Done
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSprintsResponseBodySprints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.scope is not None:
            result['scope'] = self.scope
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListSprintsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, max_results=None, next_token=None, request_id=None,
                 sprints=None, success=None, total_count=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 每页数量
        self.max_results = max_results  # type: long
        # 分页Token，没有下一页则为空
        self.next_token = next_token  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 迭代信息
        self.sprints = sprints  # type: list[ListSprintsResponseBodySprints]
        # true或者false
        self.success = success  # type: bool
        # 总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.sprints:
            for k in self.sprints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSprintsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['sprints'] = []
        if self.sprints is not None:
            for k in self.sprints:
                result['sprints'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.sprints = []
        if m.get('sprints') is not None:
            for k in m.get('sprints'):
                temp_model = ListSprintsResponseBodySprints()
                self.sprints.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListSprintsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSprintsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSprintsResponse, self).to_map()
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
            temp_model = ListSprintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVariableGroupsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, page_order=None, page_sort=None):
        # 最大返回数，默认30
        self.max_results = max_results  # type: int
        # 分页token，上一次请求的出参nextToken
        self.next_token = next_token  # type: str
        # 排序顺序
        self.page_order = page_order  # type: str
        # 排序条件
        self.page_sort = page_sort  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVariableGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page_order is not None:
            result['pageOrder'] = self.page_order
        if self.page_sort is not None:
            result['pageSort'] = self.page_sort
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pageOrder') is not None:
            self.page_order = m.get('pageOrder')
        if m.get('pageSort') is not None:
            self.page_sort = m.get('pageSort')
        return self


class ListVariableGroupsResponseBodyVariableGroupsRelatedPipelines(TeaModel):
    def __init__(self, id=None, name=None):
        # 关联的流水线Id
        self.id = id  # type: long
        # 关联的流水线名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVariableGroupsResponseBodyVariableGroupsRelatedPipelines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListVariableGroupsResponseBodyVariableGroupsVariables(TeaModel):
    def __init__(self, is_encrypted=None, name=None, value=None):
        # 是否加密
        self.is_encrypted = is_encrypted  # type: bool
        # 变量名
        self.name = name  # type: str
        # 变量值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVariableGroupsResponseBodyVariableGroupsVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_encrypted is not None:
            result['isEncrypted'] = self.is_encrypted
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('isEncrypted') is not None:
            self.is_encrypted = m.get('isEncrypted')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListVariableGroupsResponseBodyVariableGroups(TeaModel):
    def __init__(self, create_time=None, creator_account_id=None, description=None, id=None,
                 modifier_account_id=None, name=None, related_pipelines=None, update_time=None, variables=None):
        # 创建时间
        self.create_time = create_time  # type: long
        # 创建人阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 变量组描述
        self.description = description  # type: str
        # 变量组id
        self.id = id  # type: long
        # 更新人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 变量组名称
        self.name = name  # type: str
        # 关联的流水线
        self.related_pipelines = related_pipelines  # type: list[ListVariableGroupsResponseBodyVariableGroupsRelatedPipelines]
        # 更新时间
        self.update_time = update_time  # type: long
        # 变量
        self.variables = variables  # type: list[ListVariableGroupsResponseBodyVariableGroupsVariables]

    def validate(self):
        if self.related_pipelines:
            for k in self.related_pipelines:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVariableGroupsResponseBodyVariableGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.name is not None:
            result['name'] = self.name
        result['relatedPipelines'] = []
        if self.related_pipelines is not None:
            for k in self.related_pipelines:
                result['relatedPipelines'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.related_pipelines = []
        if m.get('relatedPipelines') is not None:
            for k in m.get('relatedPipelines'):
                temp_model = ListVariableGroupsResponseBodyVariableGroupsRelatedPipelines()
                self.related_pipelines.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = ListVariableGroupsResponseBodyVariableGroupsVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListVariableGroupsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, next_token=None, request_id=None, success=None,
                 total_count=None, variable_groups=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 下一次查询的token，为空表示最后一页
        self.next_token = next_token  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 变量组总数
        self.total_count = total_count  # type: long
        # 变量组
        self.variable_groups = variable_groups  # type: list[ListVariableGroupsResponseBodyVariableGroups]

    def validate(self):
        if self.variable_groups:
            for k in self.variable_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVariableGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['variableGroups'] = []
        if self.variable_groups is not None:
            for k in self.variable_groups:
                result['variableGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.variable_groups = []
        if m.get('variableGroups') is not None:
            for k in m.get('variableGroups'):
                temp_model = ListVariableGroupsResponseBodyVariableGroups()
                self.variable_groups.append(temp_model.from_map(k))
        return self


class ListVariableGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVariableGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVariableGroupsResponse, self).to_map()
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
            temp_model = ListVariableGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkItemAllFieldsRequest(TeaModel):
    def __init__(self, space_identifier=None, space_type=None, workitem_type_identifier=None):
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 资源类型
        self.space_type = space_type  # type: str
        # 工作项类型id，工作项类型的列表和id可以从ListProjectWorkitemType中获取
        self.workitem_type_identifier = workitem_type_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkItemAllFieldsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.workitem_type_identifier is not None:
            result['workitemTypeIdentifier'] = self.workitem_type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('workitemTypeIdentifier') is not None:
            self.workitem_type_identifier = m.get('workitemTypeIdentifier')
        return self


class ListWorkItemAllFieldsResponseBodyFieldsOptions(TeaModel):
    def __init__(self, display_value=None, field_identifier=None, identifier=None, level=None, position=None,
                 value=None, value_en=None):
        # 根据语言环境获取当前展示的值
        self.display_value = display_value  # type: str
        # 字段唯一标识
        self.field_identifier = field_identifier  # type: str
        # 待选值的唯一标识
        self.identifier = identifier  # type: str
        # 展示级别，数字范围1~9，数字越大，颜色越浅。
        self.level = level  # type: long
        # 待选值顺序
        self.position = position  # type: long
        # 待选值中文名称
        self.value = value  # type: str
        # 待选值英文名称
        self.value_en = value_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkItemAllFieldsResponseBodyFieldsOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_value is not None:
            result['displayValue'] = self.display_value
        if self.field_identifier is not None:
            result['fieldIdentifier'] = self.field_identifier
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.level is not None:
            result['level'] = self.level
        if self.position is not None:
            result['position'] = self.position
        if self.value is not None:
            result['value'] = self.value
        if self.value_en is not None:
            result['valueEn'] = self.value_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('displayValue') is not None:
            self.display_value = m.get('displayValue')
        if m.get('fieldIdentifier') is not None:
            self.field_identifier = m.get('fieldIdentifier')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('valueEn') is not None:
            self.value_en = m.get('valueEn')
        return self


class ListWorkItemAllFieldsResponseBodyFields(TeaModel):
    def __init__(self, class_name=None, creator=None, default_value=None, description=None, format=None,
                 gmt_create=None, gmt_modified=None, identifier=None, is_required=None, is_show_when_create=None,
                 is_system_required=None, link_with_service=None, modifier=None, name=None, options=None, resource_type=None, type=None):
        # 字段类型
        self.class_name = class_name  # type: str
        # 创建人id
        self.creator = creator  # type: str
        # 默认值
        self.default_value = default_value  # type: str
        # 描述信息
        self.description = description  # type: str
        # 字段格式
        self.format = format  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 字段唯一标识符
        self.identifier = identifier  # type: str
        # 是否必填
        self.is_required = is_required  # type: bool
        # 创建时是否展示
        self.is_show_when_create = is_show_when_create  # type: bool
        # 是否是系统必须字段，比如：负责人、状态等。
        self.is_system_required = is_system_required  # type: bool
        # 联动的服务，比如：迭代 迭代服务开启/关闭，这个字段字段加进/剔除出对应的模板； 字段模板里，这类字段不能手动添加或删除
        self.link_with_service = link_with_service  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 字段名称
        self.name = name  # type: str
        # 待选值
        self.options = options  # type: list[ListWorkItemAllFieldsResponseBodyFieldsOptions]
        # 区分不同的适用对象
        self.resource_type = resource_type  # type: str
        # 区分不同的类型，如系统字段、用户自定义字段
        self.type = type  # type: str

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWorkItemAllFieldsResponseBodyFields, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.description is not None:
            result['description'] = self.description
        if self.format is not None:
            result['format'] = self.format
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.is_required is not None:
            result['isRequired'] = self.is_required
        if self.is_show_when_create is not None:
            result['isShowWhenCreate'] = self.is_show_when_create
        if self.is_system_required is not None:
            result['isSystemRequired'] = self.is_system_required
        if self.link_with_service is not None:
            result['linkWithService'] = self.link_with_service
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        result['options'] = []
        if self.options is not None:
            for k in self.options:
                result['options'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('isRequired') is not None:
            self.is_required = m.get('isRequired')
        if m.get('isShowWhenCreate') is not None:
            self.is_show_when_create = m.get('isShowWhenCreate')
        if m.get('isSystemRequired') is not None:
            self.is_system_required = m.get('isSystemRequired')
        if m.get('linkWithService') is not None:
            self.link_with_service = m.get('linkWithService')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.options = []
        if m.get('options') is not None:
            for k in m.get('options'):
                temp_model = ListWorkItemAllFieldsResponseBodyFieldsOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListWorkItemAllFieldsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, fields=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 字段信息
        self.fields = fields  # type: list[ListWorkItemAllFieldsResponseBodyFields]
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWorkItemAllFieldsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = ListWorkItemAllFieldsResponseBodyFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListWorkItemAllFieldsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListWorkItemAllFieldsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkItemAllFieldsResponse, self).to_map()
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
            temp_model = ListWorkItemAllFieldsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkItemWorkFlowStatusRequest(TeaModel):
    def __init__(self, space_identifier=None, space_type=None, workitem_category_identifier=None,
                 workitem_type_identifier=None):
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 空间类型
        self.space_type = space_type  # type: str
        # 工作项大类型
        self.workitem_category_identifier = workitem_category_identifier  # type: str
        # 工作项小类型id
        self.workitem_type_identifier = workitem_type_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkItemWorkFlowStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.workitem_category_identifier is not None:
            result['workitemCategoryIdentifier'] = self.workitem_category_identifier
        if self.workitem_type_identifier is not None:
            result['workitemTypeIdentifier'] = self.workitem_type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('workitemCategoryIdentifier') is not None:
            self.workitem_category_identifier = m.get('workitemCategoryIdentifier')
        if m.get('workitemTypeIdentifier') is not None:
            self.workitem_type_identifier = m.get('workitemTypeIdentifier')
        return self


class ListWorkItemWorkFlowStatusResponseBodyStatuses(TeaModel):
    def __init__(self, creator=None, description=None, gmt_create=None, gmt_modified=None, identifier=None,
                 modifier=None, name=None, resource_type=None, source=None, workflow_stage_identifier=None,
                 workflow_stage_name=None):
        # 状态的创建人
        self.creator = creator  # type: str
        # 描述
        self.description = description  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 更新时间
        self.gmt_modified = gmt_modified  # type: long
        # 工作流状态id
        self.identifier = identifier  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 工作流状态名称
        self.name = name  # type: str
        # 状态作用的资源类型
        self.resource_type = resource_type  # type: str
        # 状态来源
        self.source = source  # type: str
        # 阶段信息-阶段的唯一标识
        self.workflow_stage_identifier = workflow_stage_identifier  # type: str
        # 阶段信息-名称
        self.workflow_stage_name = workflow_stage_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkItemWorkFlowStatusResponseBodyStatuses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.source is not None:
            result['source'] = self.source
        if self.workflow_stage_identifier is not None:
            result['workflowStageIdentifier'] = self.workflow_stage_identifier
        if self.workflow_stage_name is not None:
            result['workflowStageName'] = self.workflow_stage_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('workflowStageIdentifier') is not None:
            self.workflow_stage_identifier = m.get('workflowStageIdentifier')
        if m.get('workflowStageName') is not None:
            self.workflow_stage_name = m.get('workflowStageName')
        return self


class ListWorkItemWorkFlowStatusResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, statuses=None, success=None):
        # 错误返回码
        self.error_code = error_code  # type: str
        # 错误返回信息
        self.error_message = error_message  # type: str
        # openapi平台的request id
        self.request_id = request_id  # type: str
        # 工作流状态
        self.statuses = statuses  # type: list[ListWorkItemWorkFlowStatusResponseBodyStatuses]
        # 接口是否正常返回
        self.success = success  # type: bool

    def validate(self):
        if self.statuses:
            for k in self.statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWorkItemWorkFlowStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['statuses'] = []
        if self.statuses is not None:
            for k in self.statuses:
                result['statuses'].append(k.to_map() if k else None)
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.statuses = []
        if m.get('statuses') is not None:
            for k in m.get('statuses'):
                temp_model = ListWorkItemWorkFlowStatusResponseBodyStatuses()
                self.statuses.append(temp_model.from_map(k))
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListWorkItemWorkFlowStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListWorkItemWorkFlowStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkItemWorkFlowStatusResponse, self).to_map()
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
            temp_model = ListWorkItemWorkFlowStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkitemsRequest(TeaModel):
    def __init__(self, category=None, max_results=None, next_token=None, space_identifier=None, space_type=None):
        # 工作项类型，需求为Req，缺陷为Bug，任务为Task，风险为Risk
        self.category = category  # type: str
        # 每页最大返回数量，0-200，默认值20
        self.max_results = max_results  # type: str
        # 分页中的起始序列
        self.next_token = next_token  # type: str
        # 项目id
        self.space_identifier = space_identifier  # type: str
        # 项目类型
        self.space_type = space_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkitemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        return self


class ListWorkitemsResponseBodyWorkitems(TeaModel):
    def __init__(self, assigned_to=None, category_identifier=None, creator=None, document=None, gmt_create=None,
                 gmt_modified=None, identifier=None, logical_status=None, modifier=None, parent_identifier=None,
                 serial_number=None, space_identifier=None, space_name=None, space_type=None, status=None, status_identifier=None,
                 status_stage_identifier=None, subject=None, update_status_at=None, workitem_type_identifier=None):
        # 负责人aliyunPk
        self.assigned_to = assigned_to  # type: str
        # 工作项的类型id
        self.category_identifier = category_identifier  # type: str
        # 创建人aliyunPK
        self.creator = creator  # type: str
        # 工作项内容
        self.document = document  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 工作项唯一标识
        self.identifier = identifier  # type: str
        # 逻辑状态
        self.logical_status = logical_status  # type: str
        # 修改人aliyunPK
        self.modifier = modifier  # type: str
        # 父工作项id
        self.parent_identifier = parent_identifier  # type: str
        # 编号
        self.serial_number = serial_number  # type: str
        # 所属项目id
        self.space_identifier = space_identifier  # type: str
        # 所属项目名称
        self.space_name = space_name  # type: str
        # 项目类型
        self.space_type = space_type  # type: str
        # 状态名称
        self.status = status  # type: str
        # 状态唯一标识
        self.status_identifier = status_identifier  # type: str
        # 状态阶段id
        self.status_stage_identifier = status_stage_identifier  # type: str
        # 工作项标题
        self.subject = subject  # type: str
        # 状态更新时间
        self.update_status_at = update_status_at  # type: long
        # 工作项类型id
        self.workitem_type_identifier = workitem_type_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkitemsResponseBodyWorkitems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assigned_to is not None:
            result['assignedTo'] = self.assigned_to
        if self.category_identifier is not None:
            result['categoryIdentifier'] = self.category_identifier
        if self.creator is not None:
            result['creator'] = self.creator
        if self.document is not None:
            result['document'] = self.document
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.logical_status is not None:
            result['logicalStatus'] = self.logical_status
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.parent_identifier is not None:
            result['parentIdentifier'] = self.parent_identifier
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.status is not None:
            result['status'] = self.status
        if self.status_identifier is not None:
            result['statusIdentifier'] = self.status_identifier
        if self.status_stage_identifier is not None:
            result['statusStageIdentifier'] = self.status_stage_identifier
        if self.subject is not None:
            result['subject'] = self.subject
        if self.update_status_at is not None:
            result['updateStatusAt'] = self.update_status_at
        if self.workitem_type_identifier is not None:
            result['workitemTypeIdentifier'] = self.workitem_type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignedTo') is not None:
            self.assigned_to = m.get('assignedTo')
        if m.get('categoryIdentifier') is not None:
            self.category_identifier = m.get('categoryIdentifier')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('logicalStatus') is not None:
            self.logical_status = m.get('logicalStatus')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('parentIdentifier') is not None:
            self.parent_identifier = m.get('parentIdentifier')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusIdentifier') is not None:
            self.status_identifier = m.get('statusIdentifier')
        if m.get('statusStageIdentifier') is not None:
            self.status_stage_identifier = m.get('statusStageIdentifier')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('updateStatusAt') is not None:
            self.update_status_at = m.get('updateStatusAt')
        if m.get('workitemTypeIdentifier') is not None:
            self.workitem_type_identifier = m.get('workitemTypeIdentifier')
        return self


class ListWorkitemsResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, max_results=None, next_token=None, request_id=None,
                 success=None, total_count=None, workitems=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 每页数量
        self.max_results = max_results  # type: long
        # 分页Token，没有下一页则为空
        self.next_token = next_token  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool
        # 总数
        self.total_count = total_count  # type: long
        # 工作项信息
        self.workitems = workitems  # type: list[ListWorkitemsResponseBodyWorkitems]

    def validate(self):
        if self.workitems:
            for k in self.workitems:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWorkitemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['workitems'] = []
        if self.workitems is not None:
            for k in self.workitems:
                result['workitems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.workitems = []
        if m.get('workitems') is not None:
            for k in m.get('workitems'):
                temp_model = ListWorkitemsResponseBodyWorkitems()
                self.workitems.append(temp_model.from_map(k))
        return self


class ListWorkitemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListWorkitemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkitemsResponse, self).to_map()
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
            temp_model = ListWorkitemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspacesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, status_list=None, workspace_template_list=None):
        # 本次读取的最大数据记录数量，默认10，最大100
        self.max_results = max_results  # type: int
        # 用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 枚举值：CREATING-创建中, SUCCESS-运行中, FROZEN-冻结中, RECOVERING-恢复中
        self.status_list = status_list  # type: list[str]
        # 空间模板列表
        self.workspace_template_list = workspace_template_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkspacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.status_list is not None:
            result['statusList'] = self.status_list
        if self.workspace_template_list is not None:
            result['workspaceTemplateList'] = self.workspace_template_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        if m.get('workspaceTemplateList') is not None:
            self.workspace_template_list = m.get('workspaceTemplateList')
        return self


class ListWorkspacesShrinkRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, status_list_shrink=None,
                 workspace_template_list_shrink=None):
        # 本次读取的最大数据记录数量，默认10，最大100
        self.max_results = max_results  # type: int
        # 用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 枚举值：CREATING-创建中, SUCCESS-运行中, FROZEN-冻结中, RECOVERING-恢复中
        self.status_list_shrink = status_list_shrink  # type: str
        # 空间模板列表
        self.workspace_template_list_shrink = workspace_template_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkspacesShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.status_list_shrink is not None:
            result['statusList'] = self.status_list_shrink
        if self.workspace_template_list_shrink is not None:
            result['workspaceTemplateList'] = self.workspace_template_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('statusList') is not None:
            self.status_list_shrink = m.get('statusList')
        if m.get('workspaceTemplateList') is not None:
            self.workspace_template_list_shrink = m.get('workspaceTemplateList')
        return self


class ListWorkspacesResponseBodyWorkspaces(TeaModel):
    def __init__(self, code_url=None, code_version=None, create_time=None, id=None, name=None, spec=None, status=None,
                 template=None, user_id=None):
        # 代码来源URL
        self.code_url = code_url  # type: str
        # 代码版本，支持 commitSHA、分支、标签
        self.code_version = code_version  # type: str
        # 创建时间戳
        self.create_time = create_time  # type: str
        # 工作空间唯一标识，字符串形式，可在云效DevStudio访问空间链接中获取
        self.id = id  # type: str
        # 工作空间名称
        self.name = name  # type: str
        # 机器规格
        self.spec = spec  # type: str
        # 空间状态，枚举：CREATING-创建中, SUCCESS-运行中, FROZEN-冻结中, RECOVERING-恢复中
        self.status = status  # type: str
        # 工作空间模板
        self.template = template  # type: str
        # 用户阿里云PK
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkspacesResponseBodyWorkspaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_url is not None:
            result['codeUrl'] = self.code_url
        if self.code_version is not None:
            result['codeVersion'] = self.code_version
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        if self.template is not None:
            result['template'] = self.template
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('codeUrl') is not None:
            self.code_url = m.get('codeUrl')
        if m.get('codeVersion') is not None:
            self.code_version = m.get('codeVersion')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, max_results=None, next_token=None, request_id=None,
                 success=None, total_count=None, workspaces=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results  # type: int
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count  # type: int
        # 工作空间列表
        self.workspaces = workspaces  # type: list[ListWorkspacesResponseBodyWorkspaces]

    def validate(self):
        if self.workspaces:
            for k in self.workspaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListWorkspacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['workspaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.workspaces = []
        if m.get('workspaces') is not None:
            for k in m.get('workspaces'):
                temp_model = ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k))
        return self


class ListWorkspacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListWorkspacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListWorkspacesResponse, self).to_map()
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
            temp_model = ListWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogPipelineJobRunResponseBodyLog(TeaModel):
    def __init__(self, content=None, more=None):
        self.content = content  # type: str
        self.more = more  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogPipelineJobRunResponseBodyLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.more is not None:
            result['more'] = self.more
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('more') is not None:
            self.more = m.get('more')
        return self


class LogPipelineJobRunResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, log=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.log = log  # type: LogPipelineJobRunResponseBodyLog
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.log:
            self.log.validate()

    def to_map(self):
        _map = super(LogPipelineJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.log is not None:
            result['log'] = self.log.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('log') is not None:
            temp_model = LogPipelineJobRunResponseBodyLog()
            self.log = temp_model.from_map(m['log'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class LogPipelineJobRunResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: LogPipelineJobRunResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LogPipelineJobRunResponse, self).to_map()
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
            temp_model = LogPipelineJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogVMDeployMachineResponseBodyDeployMachineLog(TeaModel):
    def __init__(self, aliyun_region=None, deploy_begin_time=None, deploy_end_time=None, deploy_log=None,
                 deploy_log_path=None):
        # 部署地域
        self.aliyun_region = aliyun_region  # type: str
        # 部署开始时间
        self.deploy_begin_time = deploy_begin_time  # type: long
        # 部署结束时间
        self.deploy_end_time = deploy_end_time  # type: long
        # 部署日志
        self.deploy_log = deploy_log  # type: str
        # 部署日志路径
        self.deploy_log_path = deploy_log_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogVMDeployMachineResponseBodyDeployMachineLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_region is not None:
            result['aliyunRegion'] = self.aliyun_region
        if self.deploy_begin_time is not None:
            result['deployBeginTime'] = self.deploy_begin_time
        if self.deploy_end_time is not None:
            result['deployEndTime'] = self.deploy_end_time
        if self.deploy_log is not None:
            result['deployLog'] = self.deploy_log
        if self.deploy_log_path is not None:
            result['deployLogPath'] = self.deploy_log_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunRegion') is not None:
            self.aliyun_region = m.get('aliyunRegion')
        if m.get('deployBeginTime') is not None:
            self.deploy_begin_time = m.get('deployBeginTime')
        if m.get('deployEndTime') is not None:
            self.deploy_end_time = m.get('deployEndTime')
        if m.get('deployLog') is not None:
            self.deploy_log = m.get('deployLog')
        if m.get('deployLogPath') is not None:
            self.deploy_log_path = m.get('deployLogPath')
        return self


class LogVMDeployMachineResponseBody(TeaModel):
    def __init__(self, deploy_machine_log=None, error_code=None, error_message=None, request_id=None, success=None):
        # 部署单
        self.deploy_machine_log = deploy_machine_log  # type: LogVMDeployMachineResponseBodyDeployMachineLog
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.deploy_machine_log:
            self.deploy_machine_log.validate()

    def to_map(self):
        _map = super(LogVMDeployMachineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_machine_log is not None:
            result['deployMachineLog'] = self.deploy_machine_log.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deployMachineLog') is not None:
            temp_model = LogVMDeployMachineResponseBodyDeployMachineLog()
            self.deploy_machine_log = temp_model.from_map(m['deployMachineLog'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class LogVMDeployMachineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: LogVMDeployMachineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LogVMDeployMachineResponse, self).to_map()
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
            temp_model = LogVMDeployMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PassPipelineValidateResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PassPipelineValidateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class PassPipelineValidateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PassPipelineValidateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PassPipelineValidateResponse, self).to_map()
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
            temp_model = PassPipelineValidateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefusePipelineValidateResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefusePipelineValidateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RefusePipelineValidateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefusePipelineValidateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefusePipelineValidateResponse, self).to_map()
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
            temp_model = RefusePipelineValidateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseWorkspaceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ReleaseWorkspaceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReleaseWorkspaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseWorkspaceResponse, self).to_map()
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
            temp_model = ReleaseWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSshKeyResponseBodySshKey(TeaModel):
    def __init__(self, id=None, public_key=None):
        # 企业公钥id
        self.id = id  # type: long
        # 企业公钥
        self.public_key = public_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetSshKeyResponseBodySshKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.public_key is not None:
            result['publicKey'] = self.public_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('publicKey') is not None:
            self.public_key = m.get('publicKey')
        return self


class ResetSshKeyResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, ssh_key=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 企业公钥
        self.ssh_key = ssh_key  # type: ResetSshKeyResponseBodySshKey
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        if self.ssh_key:
            self.ssh_key.validate()

    def to_map(self):
        _map = super(ResetSshKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.ssh_key is not None:
            result['sshKey'] = self.ssh_key.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sshKey') is not None:
            temp_model = ResetSshKeyResponseBodySshKey()
            self.ssh_key = temp_model.from_map(m['sshKey'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ResetSshKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResetSshKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetSshKeyResponse, self).to_map()
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
            temp_model = ResetSshKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeVMDeployOrderResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResumeVMDeployOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ResumeVMDeployOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResumeVMDeployOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResumeVMDeployOrderResponse, self).to_map()
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
            temp_model = ResumeVMDeployOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryPipelineJobRunResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryPipelineJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RetryPipelineJobRunResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RetryPipelineJobRunResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RetryPipelineJobRunResponse, self).to_map()
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
            temp_model = RetryPipelineJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryVMDeployMachineResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryVMDeployMachineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RetryVMDeployMachineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RetryVMDeployMachineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RetryVMDeployMachineResponse, self).to_map()
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
            temp_model = RetryVMDeployMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SkipPipelineJobRunResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SkipPipelineJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SkipPipelineJobRunResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SkipPipelineJobRunResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SkipPipelineJobRunResponse, self).to_map()
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
            temp_model = SkipPipelineJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SkipVMDeployMachineResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SkipVMDeployMachineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SkipVMDeployMachineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SkipVMDeployMachineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SkipVMDeployMachineResponse, self).to_map()
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
            temp_model = SkipVMDeployMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartPipelineRunRequest(TeaModel):
    def __init__(self, params=None):
        # 流水线运行参数,json字符串 branchModeBranchs  分支模式运行的分支 envs  环境变量 runningBranchs 运行分支 runningTags  运行代码tag comment  运行备注
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartPipelineRunRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')
        return self


class StartPipelineRunResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, pipeline_run_id=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 流水线运行实例id
        self.pipeline_run_id = pipeline_run_id  # type: long
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartPipelineRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.pipeline_run_id is not None:
            result['pipelineRunId'] = self.pipeline_run_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('pipelineRunId') is not None:
            self.pipeline_run_id = m.get('pipelineRunId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StartPipelineRunResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartPipelineRunResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartPipelineRunResponse, self).to_map()
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
            temp_model = StartPipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopPipelineJobRunResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopPipelineJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StopPipelineJobRunResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopPipelineJobRunResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopPipelineJobRunResponse, self).to_map()
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
            temp_model = StopPipelineJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopPipelineRunResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopPipelineRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StopPipelineRunResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopPipelineRunResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopPipelineRunResponse, self).to_map()
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
            temp_model = StopPipelineRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopVMDeployOrderResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopVMDeployOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StopVMDeployOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopVMDeployOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopVMDeployOrderResponse, self).to_map()
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
            temp_model = StopVMDeployOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerRepositoryMirrorSyncRequest(TeaModel):
    def __init__(self, access_token=None, account=None, organization_id=None, token=None):
        # 个人访问令牌。 使用阿里云AK+SK或使用STS临时授权方式不需要传该字段
        self.access_token = access_token  # type: str
        # 远程同步库克隆账号
        self.account = account  # type: str
        # 企业标识，也称企业id，字符串形式，可在云效访问链接中获取，如 https://devops.aliyun.com/organization/\
        self.organization_id = organization_id  # type: str
        # 远程同步库克隆令牌
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerRepositoryMirrorSyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['accessToken'] = self.access_token
        if self.account is not None:
            result['account'] = self.account
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessToken') is not None:
            self.access_token = m.get('accessToken')
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class TriggerRepositoryMirrorSyncResponseBodyResult(TeaModel):
    def __init__(self, result=None):
        # 仓库同步触发结果
        self.result = result  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerRepositoryMirrorSyncResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class TriggerRepositoryMirrorSyncResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, result=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 响应结果
        self.result = result  # type: TriggerRepositoryMirrorSyncResponseBodyResult
        # 请求结果
        self.success = success  # type: bool

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(TriggerRepositoryMirrorSyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = TriggerRepositoryMirrorSyncResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class TriggerRepositoryMirrorSyncResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TriggerRepositoryMirrorSyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerRepositoryMirrorSyncResponse, self).to_map()
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
            temp_model = TriggerRepositoryMirrorSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowTagRequest(TeaModel):
    def __init__(self, color=None, flow_tag_group_id=None, name=None):
        self.color = color  # type: str
        self.flow_tag_group_id = flow_tag_group_id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color is not None:
            result['color'] = self.color
        if self.flow_tag_group_id is not None:
            result['flowTagGroupId'] = self.flow_tag_group_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('color') is not None:
            self.color = m.get('color')
        if m.get('flowTagGroupId') is not None:
            self.flow_tag_group_id = m.get('flowTagGroupId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateFlowTagResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateFlowTagResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFlowTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFlowTagResponse, self).to_map()
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
            temp_model = UpdateFlowTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFlowTagGroupRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowTagGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateFlowTagGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFlowTagGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateFlowTagGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateFlowTagGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFlowTagGroupResponse, self).to_map()
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
            temp_model = UpdateFlowTagGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHostGroupRequest(TeaModel):
    def __init__(self, aliyun_region=None, ecs_label_key=None, ecs_label_value=None, ecs_type=None, env_id=None,
                 machine_infos=None, name=None, service_connection_id=None, tag_ids=None, type=None):
        self.aliyun_region = aliyun_region  # type: str
        self.ecs_label_key = ecs_label_key  # type: str
        self.ecs_label_value = ecs_label_value  # type: str
        self.ecs_type = ecs_type  # type: str
        self.env_id = env_id  # type: str
        self.machine_infos = machine_infos  # type: str
        self.name = name  # type: str
        self.service_connection_id = service_connection_id  # type: long
        self.tag_ids = tag_ids  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_region is not None:
            result['aliyunRegion'] = self.aliyun_region
        if self.ecs_label_key is not None:
            result['ecsLabelKey'] = self.ecs_label_key
        if self.ecs_label_value is not None:
            result['ecsLabelValue'] = self.ecs_label_value
        if self.ecs_type is not None:
            result['ecsType'] = self.ecs_type
        if self.env_id is not None:
            result['envId'] = self.env_id
        if self.machine_infos is not None:
            result['machineInfos'] = self.machine_infos
        if self.name is not None:
            result['name'] = self.name
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        if self.tag_ids is not None:
            result['tagIds'] = self.tag_ids
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunRegion') is not None:
            self.aliyun_region = m.get('aliyunRegion')
        if m.get('ecsLabelKey') is not None:
            self.ecs_label_key = m.get('ecsLabelKey')
        if m.get('ecsLabelValue') is not None:
            self.ecs_label_value = m.get('ecsLabelValue')
        if m.get('ecsType') is not None:
            self.ecs_type = m.get('ecsType')
        if m.get('envId') is not None:
            self.env_id = m.get('envId')
        if m.get('machineInfos') is not None:
            self.machine_infos = m.get('machineInfos')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        if m.get('tagIds') is not None:
            self.tag_ids = m.get('tagIds')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateHostGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateHostGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHostGroupResponse, self).to_map()
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
            temp_model = UpdateHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePipelineBaseInfoRequest(TeaModel):
    def __init__(self, env_id=None, pipeline_name=None, tag_list=None):
        self.env_id = env_id  # type: long
        self.pipeline_name = pipeline_name  # type: str
        self.tag_list = tag_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelineBaseInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['envId'] = self.env_id
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        if self.tag_list is not None:
            result['tagList'] = self.tag_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('envId') is not None:
            self.env_id = m.get('envId')
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        if m.get('tagList') is not None:
            self.tag_list = m.get('tagList')
        return self


class UpdatePipelineBaseInfoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePipelineBaseInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdatePipelineBaseInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdatePipelineBaseInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePipelineBaseInfoResponse, self).to_map()
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
            temp_model = UpdatePipelineBaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectMemberRequest(TeaModel):
    def __init__(self, role_identifier=None, target_identifier=None, target_type=None, user_identifier=None,
                 user_type=None):
        # 角色id
        self.role_identifier = role_identifier  # type: str
        # 资源id，也就是项目id
        self.target_identifier = target_identifier  # type: str
        # 资源类型
        self.target_type = target_type  # type: str
        # 用户id
        self.user_identifier = user_identifier  # type: str
        # 用户类型
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_identifier is not None:
            result['roleIdentifier'] = self.role_identifier
        if self.target_identifier is not None:
            result['targetIdentifier'] = self.target_identifier
        if self.target_type is not None:
            result['targetType'] = self.target_type
        if self.user_identifier is not None:
            result['userIdentifier'] = self.user_identifier
        if self.user_type is not None:
            result['userType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('roleIdentifier') is not None:
            self.role_identifier = m.get('roleIdentifier')
        if m.get('targetIdentifier') is not None:
            self.target_identifier = m.get('targetIdentifier')
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        if m.get('userIdentifier') is not None:
            self.user_identifier = m.get('userIdentifier')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        return self


class UpdateProjectMemberResponseBodyMember(TeaModel):
    def __init__(self, gmt_create=None, gmt_modified=None, id=None, role_identifier=None, target_identifier=None,
                 target_type=None, user_identifier=None, user_type=None):
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # id
        self.id = id  # type: str
        # 角色id
        self.role_identifier = role_identifier  # type: str
        # 资源id，也就是项目id
        self.target_identifier = target_identifier  # type: str
        # 资源类型
        self.target_type = target_type  # type: str
        # 用户id
        self.user_identifier = user_identifier  # type: str
        # 用户类型
        self.user_type = user_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectMemberResponseBodyMember, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.role_identifier is not None:
            result['roleIdentifier'] = self.role_identifier
        if self.target_identifier is not None:
            result['targetIdentifier'] = self.target_identifier
        if self.target_type is not None:
            result['targetType'] = self.target_type
        if self.user_identifier is not None:
            result['userIdentifier'] = self.user_identifier
        if self.user_type is not None:
            result['userType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('roleIdentifier') is not None:
            self.role_identifier = m.get('roleIdentifier')
        if m.get('targetIdentifier') is not None:
            self.target_identifier = m.get('targetIdentifier')
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        if m.get('userIdentifier') is not None:
            self.user_identifier = m.get('userIdentifier')
        if m.get('userType') is not None:
            self.user_type = m.get('userType')
        return self


class UpdateProjectMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, member=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str
        # 成员信息
        self.member = member  # type: UpdateProjectMemberResponseBodyMember
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super(UpdateProjectMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.member is not None:
            result['member'] = self.member.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('member') is not None:
            temp_model = UpdateProjectMemberResponseBodyMember()
            self.member = temp_model.from_map(m['member'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProjectMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProjectMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProjectMemberResponse, self).to_map()
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
            temp_model = UpdateProjectMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceMemberRequest(TeaModel):
    def __init__(self, role_name=None):
        # 角色部署组 deployGroup   user  成员，使用权限   admin 管理员，使用编辑权限   owner 拥有者，所有权限 流水线 pipeline   owner 拥有者，所有权限   admin 查看、运行、编辑权限   member  运行权限   viewer 查看权限
        self.role_name = role_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['roleName'] = self.role_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')
        return self


class UpdateResourceMemberResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateResourceMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateResourceMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceMemberResponse, self).to_map()
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
            temp_model = UpdateResourceMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVariableGroupRequest(TeaModel):
    def __init__(self, description=None, name=None, variables=None):
        # 变量组描述
        self.description = description  # type: str
        # 变量组名称
        self.name = name  # type: str
        # 变量信息json字符串 isEncrypted 是否加密 name 变量名称 value 变量值
        self.variables = variables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVariableGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.variables is not None:
            result['variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('variables') is not None:
            self.variables = m.get('variables')
        return self


class UpdateVariableGroupResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVariableGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateVariableGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateVariableGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVariableGroupResponse, self).to_map()
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
            temp_model = UpdateVariableGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkItemRequest(TeaModel):
    def __init__(self, field_type=None, identifier=None, property_key=None, property_value=None):
        # 更新字段的类型，标题：subject/自定义字段：customField/状态：status/描述：document/基本字段：basic(包括负责人、迭代、参与人等)
        self.field_type = field_type  # type: str
        # 工作项唯一标识id
        self.identifier = identifier  # type: str
        # 更新的字段名
        self.property_key = property_key  # type: str
        # 更新后的值
        self.property_value = property_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_type is not None:
            result['fieldType'] = self.field_type
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.property_key is not None:
            result['propertyKey'] = self.property_key
        if self.property_value is not None:
            result['propertyValue'] = self.property_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('propertyKey') is not None:
            self.property_key = m.get('propertyKey')
        if m.get('propertyValue') is not None:
            self.property_value = m.get('propertyValue')
        return self


class UpdateWorkItemResponseBodyWorkitem(TeaModel):
    def __init__(self, assigned_to=None, category_identifier=None, creator=None, document=None, gmt_create=None,
                 gmt_modified=None, identifier=None, logical_status=None, modifier=None, parent_identifier=None,
                 serial_number=None, space_identifier=None, space_name=None, space_type=None, status=None, status_identifier=None,
                 status_stage_identifier=None, subject=None, update_status_at=None, workitem_type_identifier=None):
        # 负责人
        self.assigned_to = assigned_to  # type: str
        # 工作项的类型id
        self.category_identifier = category_identifier  # type: str
        # 创建人
        self.creator = creator  # type: str
        # 工作项内容
        self.document = document  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 工作项唯一标识
        self.identifier = identifier  # type: str
        # 逻辑状态
        self.logical_status = logical_status  # type: str
        # 修改人
        self.modifier = modifier  # type: str
        # 父工作项id
        self.parent_identifier = parent_identifier  # type: str
        # 编号
        self.serial_number = serial_number  # type: str
        # 所属项目id
        self.space_identifier = space_identifier  # type: str
        # 所属项目名称
        self.space_name = space_name  # type: str
        # 项目类型
        self.space_type = space_type  # type: str
        # 状态名称
        self.status = status  # type: str
        # 状态id
        self.status_identifier = status_identifier  # type: str
        # 状态阶段id
        self.status_stage_identifier = status_stage_identifier  # type: str
        # 工作项标题
        self.subject = subject  # type: str
        # 状态更新时间
        self.update_status_at = update_status_at  # type: long
        # 工作项类型id
        self.workitem_type_identifier = workitem_type_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateWorkItemResponseBodyWorkitem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assigned_to is not None:
            result['assignedTo'] = self.assigned_to
        if self.category_identifier is not None:
            result['categoryIdentifier'] = self.category_identifier
        if self.creator is not None:
            result['creator'] = self.creator
        if self.document is not None:
            result['document'] = self.document
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.logical_status is not None:
            result['logicalStatus'] = self.logical_status
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.parent_identifier is not None:
            result['parentIdentifier'] = self.parent_identifier
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.space_identifier is not None:
            result['spaceIdentifier'] = self.space_identifier
        if self.space_name is not None:
            result['spaceName'] = self.space_name
        if self.space_type is not None:
            result['spaceType'] = self.space_type
        if self.status is not None:
            result['status'] = self.status
        if self.status_identifier is not None:
            result['statusIdentifier'] = self.status_identifier
        if self.status_stage_identifier is not None:
            result['statusStageIdentifier'] = self.status_stage_identifier
        if self.subject is not None:
            result['subject'] = self.subject
        if self.update_status_at is not None:
            result['updateStatusAt'] = self.update_status_at
        if self.workitem_type_identifier is not None:
            result['workitemTypeIdentifier'] = self.workitem_type_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignedTo') is not None:
            self.assigned_to = m.get('assignedTo')
        if m.get('categoryIdentifier') is not None:
            self.category_identifier = m.get('categoryIdentifier')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('document') is not None:
            self.document = m.get('document')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('logicalStatus') is not None:
            self.logical_status = m.get('logicalStatus')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('parentIdentifier') is not None:
            self.parent_identifier = m.get('parentIdentifier')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('spaceIdentifier') is not None:
            self.space_identifier = m.get('spaceIdentifier')
        if m.get('spaceName') is not None:
            self.space_name = m.get('spaceName')
        if m.get('spaceType') is not None:
            self.space_type = m.get('spaceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusIdentifier') is not None:
            self.status_identifier = m.get('statusIdentifier')
        if m.get('statusStageIdentifier') is not None:
            self.status_stage_identifier = m.get('statusStageIdentifier')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('updateStatusAt') is not None:
            self.update_status_at = m.get('updateStatusAt')
        if m.get('workitemTypeIdentifier') is not None:
            self.workitem_type_identifier = m.get('workitemTypeIdentifier')
        return self


class UpdateWorkItemResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None, workitem=None):
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # true或者false
        self.success = success  # type: bool
        # 工作项信息
        self.workitem = workitem  # type: UpdateWorkItemResponseBodyWorkitem

    def validate(self):
        if self.workitem:
            self.workitem.validate()

    def to_map(self):
        _map = super(UpdateWorkItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.workitem is not None:
            result['workitem'] = self.workitem.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('workitem') is not None:
            temp_model = UpdateWorkItemResponseBodyWorkitem()
            self.workitem = temp_model.from_map(m['workitem'])
        return self


class UpdateWorkItemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateWorkItemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateWorkItemResponse, self).to_map()
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
            temp_model = UpdateWorkItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


