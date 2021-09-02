# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class RetryPipelineJobRunResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RetryPipelineJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, resource_members=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.success = success  # type: bool
        # 成员
        self.resource_members = resource_members  # type: list[ListResourceMembersResponseBodyResourceMembers]

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        result['resourceMembers'] = []
        if self.resource_members is not None:
            for k in self.resource_members:
                result['resourceMembers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        self.resource_members = []
        if m.get('resourceMembers') is not None:
            for k in m.get('resourceMembers'):
                temp_model = ListResourceMembersResponseBodyResourceMembers()
                self.resource_members.append(temp_model.from_map(k))
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


class GetHostGroupResponseBodyHostGroupHostInfos(TeaModel):
    def __init__(self, update_time=None, creator_account_id=None, instance_name=None, modifier_account_id=None,
                 ip=None, create_time=None, object_type=None, aliyun_region_id=None, machine_sn=None):
        self.update_time = update_time  # type: long
        self.creator_account_id = creator_account_id  # type: str
        self.instance_name = instance_name  # type: str
        self.modifier_account_id = modifier_account_id  # type: str
        self.ip = ip  # type: str
        self.create_time = create_time  # type: long
        self.object_type = object_type  # type: str
        self.aliyun_region_id = aliyun_region_id  # type: str
        self.machine_sn = machine_sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostGroupResponseBodyHostGroupHostInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.ip is not None:
            result['ip'] = self.ip
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.object_type is not None:
            result['objectType'] = self.object_type
        if self.aliyun_region_id is not None:
            result['aliyunRegionId'] = self.aliyun_region_id
        if self.machine_sn is not None:
            result['machineSn'] = self.machine_sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        if m.get('aliyunRegionId') is not None:
            self.aliyun_region_id = m.get('aliyunRegionId')
        if m.get('machineSn') is not None:
            self.machine_sn = m.get('machineSn')
        return self


class GetHostGroupResponseBodyHostGroup(TeaModel):
    def __init__(self, creator_account_id=None, upate_time=None, host_num=None, modifier_account_id=None,
                 description=None, type=None, create_time=None, ecs_type=None, aliyun_region=None, ecs_label_key=None, id=None,
                 name=None, service_connection_id=None, host_infos=None, ecs_label_value=None):
        self.creator_account_id = creator_account_id  # type: str
        self.upate_time = upate_time  # type: long
        self.host_num = host_num  # type: long
        self.modifier_account_id = modifier_account_id  # type: str
        self.description = description  # type: str
        self.type = type  # type: str
        self.create_time = create_time  # type: long
        self.ecs_type = ecs_type  # type: str
        self.aliyun_region = aliyun_region  # type: str
        self.ecs_label_key = ecs_label_key  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.service_connection_id = service_connection_id  # type: long
        self.host_infos = host_infos  # type: list[GetHostGroupResponseBodyHostGroupHostInfos]
        self.ecs_label_value = ecs_label_value  # type: str

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
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.upate_time is not None:
            result['upateTIme'] = self.upate_time
        if self.host_num is not None:
            result['hostNum'] = self.host_num
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.ecs_type is not None:
            result['ecsType'] = self.ecs_type
        if self.aliyun_region is not None:
            result['aliyunRegion'] = self.aliyun_region
        if self.ecs_label_key is not None:
            result['ecsLabelKey'] = self.ecs_label_key
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        result['hostInfos'] = []
        if self.host_infos is not None:
            for k in self.host_infos:
                result['hostInfos'].append(k.to_map() if k else None)
        if self.ecs_label_value is not None:
            result['ecsLabelValue'] = self.ecs_label_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('upateTIme') is not None:
            self.upate_time = m.get('upateTIme')
        if m.get('hostNum') is not None:
            self.host_num = m.get('hostNum')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('ecsType') is not None:
            self.ecs_type = m.get('ecsType')
        if m.get('aliyunRegion') is not None:
            self.aliyun_region = m.get('aliyunRegion')
        if m.get('ecsLabelKey') is not None:
            self.ecs_label_key = m.get('ecsLabelKey')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        self.host_infos = []
        if m.get('hostInfos') is not None:
            for k in m.get('hostInfos'):
                temp_model = GetHostGroupResponseBodyHostGroupHostInfos()
                self.host_infos.append(temp_model.from_map(k))
        if m.get('ecsLabelValue') is not None:
            self.ecs_label_value = m.get('ecsLabelValue')
        return self


class GetHostGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, host_group=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        self.host_group = host_group  # type: GetHostGroupResponseBodyHostGroup

    def validate(self):
        if self.host_group:
            self.host_group.validate()

    def to_map(self):
        _map = super(GetHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        if self.host_group is not None:
            result['hostGroup'] = self.host_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('hostGroup') is not None:
            temp_model = GetHostGroupResponseBodyHostGroup()
            self.host_group = temp_model.from_map(m['hostGroup'])
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
    def __init__(self, value=None, name=None, is_encrypted=None):
        # 变量值
        self.value = value  # type: str
        # 变量名
        self.name = name  # type: str
        # 是否加密
        self.is_encrypted = is_encrypted  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVariableGroupResponseBodyVariableGroupVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        if self.name is not None:
            result['name'] = self.name
        if self.is_encrypted is not None:
            result['isEncrypted'] = self.is_encrypted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('isEncrypted') is not None:
            self.is_encrypted = m.get('isEncrypted')
        return self


class GetVariableGroupResponseBodyVariableGroup(TeaModel):
    def __init__(self, ccreator_account_id=None, description=None, update_time=None, id=None,
                 modifier_account_id=None, name=None, related_pipelines=None, variables=None, create_time=None):
        # 创建人阿里云账号id
        self.ccreator_account_id = ccreator_account_id  # type: str
        # 变量组描述
        self.description = description  # type: str
        # 更新时间
        self.update_time = update_time  # type: long
        # 变量组id
        self.id = id  # type: long
        # 更新人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 变量组名称
        self.name = name  # type: str
        # 关联的流水线
        self.related_pipelines = related_pipelines  # type: list[GetVariableGroupResponseBodyVariableGroupRelatedPipelines]
        # 变量
        self.variables = variables  # type: list[GetVariableGroupResponseBodyVariableGroupVariables]
        # 创建时间
        self.create_time = create_time  # type: long

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
        if self.description is not None:
            result['description'] = self.description
        if self.update_time is not None:
            result['updateTime'] = self.update_time
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
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ccreatorAccountId') is not None:
            self.ccreator_account_id = m.get('ccreatorAccountId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
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
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = GetVariableGroupResponseBodyVariableGroupVariables()
                self.variables.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self


class GetVariableGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, variable_group=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        if self.variable_group is not None:
            result['variableGroup'] = self.variable_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class ListPipelinesRequest(TeaModel):
    def __init__(self, pipeline_name=None, creator_account_ids=None, execute_account_ids=None, status_list=None,
                 create_start_time=None, create_end_time=None, execute_start_time=None, execute_end_time=None, max_results=None,
                 next_token=None):
        # 流水线名称
        self.pipeline_name = pipeline_name  # type: str
        # 创建人阿里云账号Id
        self.creator_account_ids = creator_account_ids  # type: str
        # 执行人阿里云账号id
        self.execute_account_ids = execute_account_ids  # type: str
        # 状态列表，多个逗号分割
        self.status_list = status_list  # type: str
        # 创建开始时间
        self.create_start_time = create_start_time  # type: long
        # 创建结束时间
        self.create_end_time = create_end_time  # type: long
        # 执行开始时间
        self.execute_start_time = execute_start_time  # type: long
        # 执行结束时间
        self.execute_end_time = execute_end_time  # type: long
        # 返回的总数
        self.max_results = max_results  # type: long
        # 分页Token
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        if self.creator_account_ids is not None:
            result['creatorAccountIds'] = self.creator_account_ids
        if self.execute_account_ids is not None:
            result['executeAccountIds'] = self.execute_account_ids
        if self.status_list is not None:
            result['statusList'] = self.status_list
        if self.create_start_time is not None:
            result['createStartTime'] = self.create_start_time
        if self.create_end_time is not None:
            result['createEndTime'] = self.create_end_time
        if self.execute_start_time is not None:
            result['executeStartTime'] = self.execute_start_time
        if self.execute_end_time is not None:
            result['executeEndTime'] = self.execute_end_time
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        if m.get('creatorAccountIds') is not None:
            self.creator_account_ids = m.get('creatorAccountIds')
        if m.get('executeAccountIds') is not None:
            self.execute_account_ids = m.get('executeAccountIds')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        if m.get('createStartTime') is not None:
            self.create_start_time = m.get('createStartTime')
        if m.get('createEndTime') is not None:
            self.create_end_time = m.get('createEndTime')
        if m.get('executeStartTime') is not None:
            self.execute_start_time = m.get('executeStartTime')
        if m.get('executeEndTime') is not None:
            self.execute_end_time = m.get('executeEndTime')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListPipelinesResponseBodyPipelines(TeaModel):
    def __init__(self, pipeline_name=None, pipeline_id=None, create_time=None, creator_account_id=None):
        # 流水线名称
        self.pipeline_name = pipeline_name  # type: str
        # 流水线id
        self.pipeline_id = pipeline_id  # type: long
        # 创建时间
        self.create_time = create_time  # type: long
        # 创建人阿里云账号id
        self.creator_account_id = creator_account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelinesResponseBodyPipelines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        return self


class ListPipelinesResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, total_count=None,
                 next_token=None, pipelines=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 总数
        self.total_count = total_count  # type: long
        # 分页Token
        self.next_token = next_token  # type: str
        # 流水线
        self.pipelines = pipelines  # type: list[ListPipelinesResponseBodyPipelines]

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['pipelines'] = []
        if self.pipelines is not None:
            for k in self.pipelines:
                result['pipelines'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.pipelines = []
        if m.get('pipelines') is not None:
            for k in m.get('pipelines'):
                temp_model = ListPipelinesResponseBodyPipelines()
                self.pipelines.append(temp_model.from_map(k))
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
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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
    def __init__(self, name=None, description=None, variables=None):
        # 变量组名称
        self.name = name  # type: str
        # 变量组描述
        self.description = description  # type: str
        # 变量信息json字符串 isEncrypted 是否加密 name 变量名称 value 变量值
        self.variables = variables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVariableGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.variables is not None:
            result['variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('variables') is not None:
            self.variables = m.get('variables')
        return self


class UpdateVariableGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVariableGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class DeleteResourceMemberResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class ListHostGroupsRequest(TeaModel):
    def __init__(self, ids=None, create_start_time=None, create_end_time=None, name=None, creator_account_ids=None,
                 next_token=None, max_results=None, page_sort=None, page_order=None):
        # 主机组id，多个逗号分割
        self.ids = ids  # type: str
        # 主机组创建时间
        self.create_start_time = create_start_time  # type: long
        # 主机组结束时间
        self.create_end_time = create_end_time  # type: long
        # 主机组名称
        self.name = name  # type: str
        # 创建阿里云账号id，多个逗号分割
        self.creator_account_ids = creator_account_ids  # type: str
        # 分页token
        self.next_token = next_token  # type: str
        # 结果返回个数
        self.max_results = max_results  # type: long
        # 排序条件ID
        self.page_sort = page_sort  # type: str
        # 排序顺序
        self.page_order = page_order  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        if self.create_start_time is not None:
            result['createStartTime'] = self.create_start_time
        if self.create_end_time is not None:
            result['createEndTime'] = self.create_end_time
        if self.name is not None:
            result['name'] = self.name
        if self.creator_account_ids is not None:
            result['creatorAccountIds'] = self.creator_account_ids
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.page_sort is not None:
            result['pageSort'] = self.page_sort
        if self.page_order is not None:
            result['pageOrder'] = self.page_order
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('createStartTime') is not None:
            self.create_start_time = m.get('createStartTime')
        if m.get('createEndTime') is not None:
            self.create_end_time = m.get('createEndTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('creatorAccountIds') is not None:
            self.creator_account_ids = m.get('creatorAccountIds')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('pageSort') is not None:
            self.page_sort = m.get('pageSort')
        if m.get('pageOrder') is not None:
            self.page_order = m.get('pageOrder')
        return self


class ListHostGroupsResponseBodyHostGroups(TeaModel):
    def __init__(self, creator_account_id=None, update_time=None, host_num=None, modifier_account_id=None,
                 description=None, type=None, create_time=None, ecs_type=None, aliyun_region=None, ecs_label_key=None, name=None,
                 id=None, service_connection_id=None, ecs_label_value=None):
        # 创建人阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 更新时间
        self.update_time = update_time  # type: long
        # 主机个数
        self.host_num = host_num  # type: long
        # 修改人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 描述
        self.description = description  # type: str
        # 类型
        self.type = type  # type: str
        # 主机时间
        self.create_time = create_time  # type: long
        # 主机类型
        self.ecs_type = ecs_type  # type: str
        # 阿里云区域
        self.aliyun_region = aliyun_region  # type: str
        # ecs标签Key
        self.ecs_label_key = ecs_label_key  # type: str
        # 部署组名称
        self.name = name  # type: str
        # 323232
        self.id = id  # type: long
        # 服务连接Id
        self.service_connection_id = service_connection_id  # type: long
        # Ecs标签值
        self.ecs_label_value = ecs_label_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsResponseBodyHostGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.host_num is not None:
            result['hostNum'] = self.host_num
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.ecs_type is not None:
            result['ecsType'] = self.ecs_type
        if self.aliyun_region is not None:
            result['aliyunRegion'] = self.aliyun_region
        if self.ecs_label_key is not None:
            result['ecsLabelKey'] = self.ecs_label_key
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        if self.ecs_label_value is not None:
            result['ecsLabelValue'] = self.ecs_label_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('hostNum') is not None:
            self.host_num = m.get('hostNum')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('ecsType') is not None:
            self.ecs_type = m.get('ecsType')
        if m.get('aliyunRegion') is not None:
            self.aliyun_region = m.get('aliyunRegion')
        if m.get('ecsLabelKey') is not None:
            self.ecs_label_key = m.get('ecsLabelKey')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        if m.get('ecsLabelValue') is not None:
            self.ecs_label_value = m.get('ecsLabelValue')
        return self


class ListHostGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, host_groups=None,
                 total_count=None, next_token=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 主机组
        self.host_groups = host_groups  # type: list[ListHostGroupsResponseBodyHostGroups]
        # 总数
        self.total_count = total_count  # type: long
        # 分页token,空表示最后一页
        self.next_token = next_token  # type: str

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        result['hostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['hostGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        self.host_groups = []
        if m.get('hostGroups') is not None:
            for k in m.get('hostGroups'):
                temp_model = ListHostGroupsResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
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


class ResetSshKeyResponseBodySshKey(TeaModel):
    def __init__(self, public_key=None, id=None):
        # 企业公钥
        self.public_key = public_key  # type: str
        # 企业公钥id
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetSshKeyResponseBodySshKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_key is not None:
            result['publicKey'] = self.public_key
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('publicKey') is not None:
            self.public_key = m.get('publicKey')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ResetSshKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, ssh_key=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 企业公钥
        self.ssh_key = ssh_key  # type: ResetSshKeyResponseBodySshKey

    def validate(self):
        if self.ssh_key:
            self.ssh_key.validate()

    def to_map(self):
        _map = super(ResetSshKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        if self.ssh_key is not None:
            result['sshKey'] = self.ssh_key.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('sshKey') is not None:
            temp_model = ResetSshKeyResponseBodySshKey()
            self.ssh_key = temp_model.from_map(m['sshKey'])
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


class CreateWorkspaceRequest(TeaModel):
    def __init__(self, name=None, workspace_template=None, code_url=None, code_version=None, file_path=None,
                 reuse=None, resource_identifier=None, request_from=None):
        # 工作空间名称
        self.name = name  # type: str
        # 技术栈
        self.workspace_template = workspace_template  # type: str
        # 代码来源URL（当前仅支持云效 Codeup 来源）
        self.code_url = code_url  # type: str
        # 代码版本，支持 commitSHA、分支、标签
        self.code_version = code_version  # type: str
        # 打开空间默认打开的文件相对路径
        self.file_path = file_path  # type: str
        # 工作空间复用标识，按照"用户+技术栈+代码地址+版本"进行复用 true - 复用 false - 不复用，每次均为新创建
        self.reuse = reuse  # type: bool
        # 资源标识，提供给非标代码源作为空间复用的唯一标识
        self.resource_identifier = resource_identifier  # type: str
        # 请求来源（用于统计，云产品集成时需要传入）
        self.request_from = request_from  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.workspace_template is not None:
            result['workspaceTemplate'] = self.workspace_template
        if self.code_url is not None:
            result['codeUrl'] = self.code_url
        if self.code_version is not None:
            result['codeVersion'] = self.code_version
        if self.file_path is not None:
            result['filePath'] = self.file_path
        if self.reuse is not None:
            result['reuse'] = self.reuse
        if self.resource_identifier is not None:
            result['resourceIdentifier'] = self.resource_identifier
        if self.request_from is not None:
            result['requestFrom'] = self.request_from
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('workspaceTemplate') is not None:
            self.workspace_template = m.get('workspaceTemplate')
        if m.get('codeUrl') is not None:
            self.code_url = m.get('codeUrl')
        if m.get('codeVersion') is not None:
            self.code_version = m.get('codeVersion')
        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')
        if m.get('reuse') is not None:
            self.reuse = m.get('reuse')
        if m.get('resourceIdentifier') is not None:
            self.resource_identifier = m.get('resourceIdentifier')
        if m.get('requestFrom') is not None:
            self.request_from = m.get('requestFrom')
        return self


class CreateWorkspaceResponseBodyWorkspace(TeaModel):
    def __init__(self, id=None, name=None, status=None, template=None, creator=None, create_time=None):
        # 工作空间唯一标识，字符串形式，可在云效DevStudio访问空间链接中获取
        self.id = id  # type: str
        # 工作空间名称
        self.name = name  # type: str
        # 空间状态，枚举：CREATING-创建中, SUCCESS-运行中, FROZEN-冻结中, RECOVERING-恢复中
        self.status = status  # type: str
        # 工作空间模板
        self.template = template  # type: str
        # 创建者，阿里云PK
        self.creator = creator  # type: str
        # 创建时间戳
        self.create_time = create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateWorkspaceResponseBodyWorkspace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.template is not None:
            result['template'] = self.template
        if self.creator is not None:
            result['creator'] = self.creator
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self


class CreateWorkspaceResponseBody(TeaModel):
    def __init__(self, workspace=None, request_id=None, success=None, error_code=None, error_message=None):
        # 工作空间信息
        self.workspace = workspace  # type: CreateWorkspaceResponseBodyWorkspace
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str

    def validate(self):
        if self.workspace:
            self.workspace.validate()

    def to_map(self):
        _map = super(CreateWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['workspace'] = self.workspace.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workspace') is not None:
            temp_model = CreateWorkspaceResponseBodyWorkspace()
            self.workspace = temp_model.from_map(m['workspace'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
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
    def __init__(self, owner_account_id=None, name=None, id=None, type=None, create_time=None):
        # 拥有者阿里云账号id
        self.owner_account_id = owner_account_id  # type: long
        # 服务连接名称
        self.name = name  # type: str
        # 服务连接Id
        self.id = id  # type: long
        # 服务连接类型
        self.type = type  # type: str
        # 创建时间
        self.create_time = create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceConnectionsResponseBodyServiceConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account_id is not None:
            result['ownerAccountId'] = self.owner_account_id
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.type is not None:
            result['type'] = self.type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ownerAccountId') is not None:
            self.owner_account_id = m.get('ownerAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self


class ListServiceConnectionsResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, service_connections=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 服务连接
        self.service_connections = service_connections  # type: list[ListServiceConnectionsResponseBodyServiceConnections]

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        result['serviceConnections'] = []
        if self.service_connections is not None:
            for k in self.service_connections:
                result['serviceConnections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        self.service_connections = []
        if m.get('serviceConnections') is not None:
            for k in m.get('serviceConnections'):
                temp_model = ListServiceConnectionsResponseBodyServiceConnections()
                self.service_connections.append(temp_model.from_map(k))
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


class CreateHostGroupRequest(TeaModel):
    def __init__(self, type=None, env_id=None, name=None, service_connection_id=None, tag_ids=None, ecs_type=None,
                 ecs_label_key=None, ecs_label_value=None, aliyun_region=None, machine_infos=None):
        self.type = type  # type: str
        self.env_id = env_id  # type: str
        self.name = name  # type: str
        self.service_connection_id = service_connection_id  # type: long
        self.tag_ids = tag_ids  # type: str
        self.ecs_type = ecs_type  # type: str
        self.ecs_label_key = ecs_label_key  # type: str
        self.ecs_label_value = ecs_label_value  # type: str
        self.aliyun_region = aliyun_region  # type: str
        self.machine_infos = machine_infos  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.env_id is not None:
            result['envId'] = self.env_id
        if self.name is not None:
            result['name'] = self.name
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        if self.tag_ids is not None:
            result['tagIds'] = self.tag_ids
        if self.ecs_type is not None:
            result['ecsType'] = self.ecs_type
        if self.ecs_label_key is not None:
            result['ecsLabelKey'] = self.ecs_label_key
        if self.ecs_label_value is not None:
            result['ecsLabelValue'] = self.ecs_label_value
        if self.aliyun_region is not None:
            result['aliyunRegion'] = self.aliyun_region
        if self.machine_infos is not None:
            result['machineInfos'] = self.machine_infos
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('envId') is not None:
            self.env_id = m.get('envId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        if m.get('tagIds') is not None:
            self.tag_ids = m.get('tagIds')
        if m.get('ecsType') is not None:
            self.ecs_type = m.get('ecsType')
        if m.get('ecsLabelKey') is not None:
            self.ecs_label_key = m.get('ecsLabelKey')
        if m.get('ecsLabelValue') is not None:
            self.ecs_label_value = m.get('ecsLabelValue')
        if m.get('aliyunRegion') is not None:
            self.aliyun_region = m.get('aliyunRegion')
        if m.get('machineInfos') is not None:
            self.machine_infos = m.get('machineInfos')
        return self


class CreateHostGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, host_group_id=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool
        self.host_group_id = host_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        if self.host_group_id is not None:
            result['hostGroupId'] = self.host_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('hostGroupId') is not None:
            self.host_group_id = m.get('hostGroupId')
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


class StopPipelineRunResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopPipelineRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class UpdateHostGroupRequest(TeaModel):
    def __init__(self, type=None, env_id=None, name=None, service_connection_id=None, tag_ids=None, ecs_type=None,
                 ecs_label_key=None, ecs_label_value=None, aliyun_region=None, machine_infos=None):
        self.type = type  # type: str
        self.env_id = env_id  # type: str
        self.name = name  # type: str
        self.service_connection_id = service_connection_id  # type: long
        self.tag_ids = tag_ids  # type: str
        self.ecs_type = ecs_type  # type: str
        self.ecs_label_key = ecs_label_key  # type: str
        self.ecs_label_value = ecs_label_value  # type: str
        self.aliyun_region = aliyun_region  # type: str
        self.machine_infos = machine_infos  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.env_id is not None:
            result['envId'] = self.env_id
        if self.name is not None:
            result['name'] = self.name
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        if self.tag_ids is not None:
            result['tagIds'] = self.tag_ids
        if self.ecs_type is not None:
            result['ecsType'] = self.ecs_type
        if self.ecs_label_key is not None:
            result['ecsLabelKey'] = self.ecs_label_key
        if self.ecs_label_value is not None:
            result['ecsLabelValue'] = self.ecs_label_value
        if self.aliyun_region is not None:
            result['aliyunRegion'] = self.aliyun_region
        if self.machine_infos is not None:
            result['machineInfos'] = self.machine_infos
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('envId') is not None:
            self.env_id = m.get('envId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        if m.get('tagIds') is not None:
            self.tag_ids = m.get('tagIds')
        if m.get('ecsType') is not None:
            self.ecs_type = m.get('ecsType')
        if m.get('ecsLabelKey') is not None:
            self.ecs_label_key = m.get('ecsLabelKey')
        if m.get('ecsLabelValue') is not None:
            self.ecs_label_value = m.get('ecsLabelValue')
        if m.get('aliyunRegion') is not None:
            self.aliyun_region = m.get('aliyunRegion')
        if m.get('machineInfos') is not None:
            self.machine_infos = m.get('machineInfos')
        return self


class UpdateHostGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class SkipPipelineJobRunResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        self.request_id = request_id  # type: str
        self.error_message = error_message  # type: str
        self.error_code = error_code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SkipPipelineJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class StopPipelineJobRunResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopPipelineJobRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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
    def __init__(self, request_id=None, error_message=None, pipeline_run_id=None, success=None, error_code=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 流水线运行实例id
        self.pipeline_run_id = pipeline_run_id  # type: long
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartPipelineRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.pipeline_run_id is not None:
            result['pipelineRunId'] = self.pipeline_run_id
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('pipelineRunId') is not None:
            self.pipeline_run_id = m.get('pipelineRunId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class ListWorkspacesRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, status_list=None, workspace_template_list=None):
        # 用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 本次读取的最大数据记录数量，默认10，最大100
        self.max_results = max_results  # type: int
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
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.status_list is not None:
            result['statusList'] = self.status_list
        if self.workspace_template_list is not None:
            result['workspaceTemplateList'] = self.workspace_template_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        if m.get('workspaceTemplateList') is not None:
            self.workspace_template_list = m.get('workspaceTemplateList')
        return self


class ListWorkspacesShrinkRequest(TeaModel):
    def __init__(self, next_token=None, max_results=None, status_list_shrink=None,
                 workspace_template_list_shrink=None):
        # 用来标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token  # type: str
        # 本次读取的最大数据记录数量，默认10，最大100
        self.max_results = max_results  # type: int
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
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.status_list_shrink is not None:
            result['statusList'] = self.status_list_shrink
        if self.workspace_template_list_shrink is not None:
            result['workspaceTemplateList'] = self.workspace_template_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('statusList') is not None:
            self.status_list_shrink = m.get('statusList')
        if m.get('workspaceTemplateList') is not None:
            self.workspace_template_list_shrink = m.get('workspaceTemplateList')
        return self


class ListWorkspacesResponseBodyWorkspaces(TeaModel):
    def __init__(self, code_version=None, code_url=None, name=None, spec=None, status=None, template=None, id=None,
                 user_id=None, create_time=None):
        # 代码版本，支持 commitSHA、分支、标签
        self.code_version = code_version  # type: str
        # 代码来源URL
        self.code_url = code_url  # type: str
        # 工作空间名称
        self.name = name  # type: str
        # 机器规格
        self.spec = spec  # type: str
        # 空间状态，枚举：CREATING-创建中, SUCCESS-运行中, FROZEN-冻结中, RECOVERING-恢复中
        self.status = status  # type: str
        # 工作空间模板
        self.template = template  # type: str
        # 工作空间唯一标识，字符串形式，可在云效DevStudio访问空间链接中获取
        self.id = id  # type: str
        # 用户阿里云PK
        self.user_id = user_id  # type: str
        # 创建时间戳
        self.create_time = create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListWorkspacesResponseBodyWorkspaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_version is not None:
            result['codeVersion'] = self.code_version
        if self.code_url is not None:
            result['codeUrl'] = self.code_url
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        if self.template is not None:
            result['template'] = self.template
        if self.id is not None:
            result['id'] = self.id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('codeVersion') is not None:
            self.code_version = m.get('codeVersion')
        if m.get('codeUrl') is not None:
            self.code_url = m.get('codeUrl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(self, total_count=None, next_token=None, max_results=None, workspaces=None, request_id=None,
                 success=None, error_code=None, error_message=None):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count  # type: int
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results  # type: int
        # 工作空间列表
        self.workspaces = workspaces  # type: list[ListWorkspacesResponseBodyWorkspaces]
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str

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
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        result['workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['workspaces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        self.workspaces = []
        if m.get('workspaces') is not None:
            for k in m.get('workspaces'):
                temp_model = ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
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
    def __init__(self, sign=None, type=None, data=None):
        # 代码源唯一标识
        self.sign = sign  # type: str
        # 代码库类型
        self.type = type  # type: str
        # 代码源信息
        self.data = data  # type: GetPipelineRunResponseBodyPipelineRunSourcesData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPipelineRunResponseBodyPipelineRunSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign is not None:
            result['sign'] = self.sign
        if self.type is not None:
            result['type'] = self.type
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sign') is not None:
            self.sign = m.get('sign')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('data') is not None:
            temp_model = GetPipelineRunResponseBodyPipelineRunSourcesData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobs(TeaModel):
    def __init__(self, end_time=None, id=None, name=None, params=None, status=None, start_time=None):
        # 结束时间
        self.end_time = end_time  # type: long
        # 任务Id
        self.id = id  # type: long
        # 任务名称
        self.name = name  # type: str
        # 触发参数
        self.params = params  # type: str
        # 状态
        self.status = status  # type: str
        # 开始时间
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.params is not None:
            result['params'] = self.params
        if self.status is not None:
            result['status'] = self.status
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class GetPipelineRunResponseBodyPipelineRunStagesStageInfo(TeaModel):
    def __init__(self, end_time=None, start_time=None, name=None, status=None, jobs=None):
        # 结束时间
        self.end_time = end_time  # type: long
        # 开始时间
        self.start_time = start_time  # type: long
        # 阶段名称
        self.name = name  # type: str
        # 状态
        self.status = status  # type: str
        # 任务
        self.jobs = jobs  # type: list[GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobs]

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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['jobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = GetPipelineRunResponseBodyPipelineRunStagesStageInfoJobs()
                self.jobs.append(temp_model.from_map(k))
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
    def __init__(self, creator_account_id=None, create_time=None, update_time=None, modifier_account_id=None,
                 pipeline_id=None, pipeline_run_id=None, status=None, trigger_mode=None, stage_group=None, sources=None,
                 stages=None):
        # 创建者阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 创建时间
        self.create_time = create_time  # type: long
        # 更新时间
        self.update_time = update_time  # type: long
        # 更新人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 流水线Id
        self.pipeline_id = pipeline_id  # type: long
        # 流水线运行实例id
        self.pipeline_run_id = pipeline_run_id  # type: long
        # 状态 FAIL 运行失败 SUCCESS 运行成功 RUNNING 运行中
        self.status = status  # type: str
        # 触发模式 1人工触发 2定时触发 3代码提交触发
        self.trigger_mode = trigger_mode  # type: int
        # 阶段拓扑信息
        self.stage_group = stage_group  # type: list[list[str]]
        # 代码源
        self.sources = sources  # type: list[GetPipelineRunResponseBodyPipelineRunSources]
        # 阶段信息
        self.stages = stages  # type: list[GetPipelineRunResponseBodyPipelineRunStages]

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
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.pipeline_run_id is not None:
            result['pipelineRunId'] = self.pipeline_run_id
        if self.status is not None:
            result['status'] = self.status
        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode
        if self.stage_group is not None:
            result['stageGroup'] = self.stage_group
        result['sources'] = []
        if self.sources is not None:
            for k in self.sources:
                result['sources'].append(k.to_map() if k else None)
        result['stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['stages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('pipelineRunId') is not None:
            self.pipeline_run_id = m.get('pipelineRunId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')
        if m.get('stageGroup') is not None:
            self.stage_group = m.get('stageGroup')
        self.sources = []
        if m.get('sources') is not None:
            for k in m.get('sources'):
                temp_model = GetPipelineRunResponseBodyPipelineRunSources()
                self.sources.append(temp_model.from_map(k))
        self.stages = []
        if m.get('stages') is not None:
            for k in m.get('stages'):
                temp_model = GetPipelineRunResponseBodyPipelineRunStages()
                self.stages.append(temp_model.from_map(k))
        return self


class GetPipelineRunResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, pipeline_run=None, success=None, error_code=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 流水线运行实例
        self.pipeline_run = pipeline_run  # type: GetPipelineRunResponseBodyPipelineRun
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 错误码
        self.error_code = error_code  # type: bool

    def validate(self):
        if self.pipeline_run:
            self.pipeline_run.validate()

    def to_map(self):
        _map = super(GetPipelineRunResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.pipeline_run is not None:
            result['pipelineRun'] = self.pipeline_run.to_map()
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('pipelineRun') is not None:
            temp_model = GetPipelineRunResponseBodyPipelineRun()
            self.pipeline_run = temp_model.from_map(m['pipelineRun'])
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class GetPipelineResponseBodyPipelinePipelineConfigSourcesData(TeaModel):
    def __init__(self, branch=None, service_connection_id=None, label=None, is_trigger=None, repo=None,
                 trigger_filter=None, webhook=None, events=None, is_branch_mode=None, is_submodule=None, is_clone_depth=None,
                 clone_depth=None, credential_id=None, credential_type=None, credential_label=None, namespace=None):
        # 分支
        self.branch = branch  # type: str
        # 服务连接Id
        self.service_connection_id = service_connection_id  # type: long
        # 代码源显示标签
        self.label = label  # type: str
        # 是否提交触发
        self.is_trigger = is_trigger  # type: bool
        # 代码库地址
        self.repo = repo  # type: str
        # 触发过滤条件
        self.trigger_filter = trigger_filter  # type: str
        # webhhook地址
        self.webhook = webhook  # type: str
        # 触发事件
        self.events = events  # type: list[str]
        # 是否分支模式
        self.is_branch_mode = is_branch_mode  # type: bool
        # 是否子模块
        self.is_submodule = is_submodule  # type: bool
        # 是否设置clone深度
        self.is_clone_depth = is_clone_depth  # type: bool
        # 克隆深度
        self.clone_depth = clone_depth  # type: long
        # Credential Id
        self.credential_id = credential_id  # type: long
        # Credential Type
        self.credential_type = credential_type  # type: str
        # Credential Label
        self.credential_label = credential_label  # type: str
        # github命名空间
        self.namespace = namespace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPipelineResponseBodyPipelinePipelineConfigSourcesData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.branch is not None:
            result['branch'] = self.branch
        if self.service_connection_id is not None:
            result['serviceConnectionId'] = self.service_connection_id
        if self.label is not None:
            result['label'] = self.label
        if self.is_trigger is not None:
            result['isTrigger'] = self.is_trigger
        if self.repo is not None:
            result['repo'] = self.repo
        if self.trigger_filter is not None:
            result['triggerFilter'] = self.trigger_filter
        if self.webhook is not None:
            result['webhook'] = self.webhook
        if self.events is not None:
            result['events'] = self.events
        if self.is_branch_mode is not None:
            result['isBranchMode'] = self.is_branch_mode
        if self.is_submodule is not None:
            result['isSubmodule'] = self.is_submodule
        if self.is_clone_depth is not None:
            result['isCloneDepth'] = self.is_clone_depth
        if self.clone_depth is not None:
            result['cloneDepth'] = self.clone_depth
        if self.credential_id is not None:
            result['credentialId'] = self.credential_id
        if self.credential_type is not None:
            result['credentialType'] = self.credential_type
        if self.credential_label is not None:
            result['credentialLabel'] = self.credential_label
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('branch') is not None:
            self.branch = m.get('branch')
        if m.get('serviceConnectionId') is not None:
            self.service_connection_id = m.get('serviceConnectionId')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('isTrigger') is not None:
            self.is_trigger = m.get('isTrigger')
        if m.get('repo') is not None:
            self.repo = m.get('repo')
        if m.get('triggerFilter') is not None:
            self.trigger_filter = m.get('triggerFilter')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        if m.get('events') is not None:
            self.events = m.get('events')
        if m.get('isBranchMode') is not None:
            self.is_branch_mode = m.get('isBranchMode')
        if m.get('isSubmodule') is not None:
            self.is_submodule = m.get('isSubmodule')
        if m.get('isCloneDepth') is not None:
            self.is_clone_depth = m.get('isCloneDepth')
        if m.get('cloneDepth') is not None:
            self.clone_depth = m.get('cloneDepth')
        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')
        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')
        if m.get('credentialLabel') is not None:
            self.credential_label = m.get('credentialLabel')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class GetPipelineResponseBodyPipelinePipelineConfigSources(TeaModel):
    def __init__(self, sign=None, type=None, data=None):
        # 代码源唯一标识
        self.sign = sign  # type: str
        # 代码源类型aliyunGit 阿里云代码库 customGitlab  自建git giteeGit 码云 codeup Codeup git 通用git gitlab gitlab bitbucket bitbucket githubOAuth github
        self.type = type  # type: str
        # 代码数据
        self.data = data  # type: GetPipelineResponseBodyPipelinePipelineConfigSourcesData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPipelineResponseBodyPipelinePipelineConfigSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign is not None:
            result['sign'] = self.sign
        if self.type is not None:
            result['type'] = self.type
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sign') is not None:
            self.sign = m.get('sign')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('data') is not None:
            temp_model = GetPipelineResponseBodyPipelinePipelineConfigSourcesData()
            self.data = temp_model.from_map(m['data'])
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


class GetPipelineResponseBodyPipeline(TeaModel):
    def __init__(self, creator_account_id=None, env_id=None, env_name=None, create_time=None, update_time=None,
                 group_id=None, modifier_account_id=None, name=None, tag_list=None, pipeline_config=None):
        # 创建者阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 环境id 0 日常环境  1预发环境 2正式环境
        self.env_id = env_id  # type: int
        # 环境名称
        self.env_name = env_name  # type: str
        # 创建时间
        self.create_time = create_time  # type: long
        # 更新时间
        self.update_time = update_time  # type: long
        # 流水线分组id
        self.group_id = group_id  # type: long
        # 更新人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 流水线名称
        self.name = name  # type: str
        # 标签
        self.tag_list = tag_list  # type: list[GetPipelineResponseBodyPipelineTagList]
        # 流水线配置
        self.pipeline_config = pipeline_config  # type: GetPipelineResponseBodyPipelinePipelineConfig

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()
        if self.pipeline_config:
            self.pipeline_config.validate()

    def to_map(self):
        _map = super(GetPipelineResponseBodyPipeline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.env_id is not None:
            result['envId'] = self.env_id
        if self.env_name is not None:
            result['envName'] = self.env_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.name is not None:
            result['name'] = self.name
        result['tagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['tagList'].append(k.to_map() if k else None)
        if self.pipeline_config is not None:
            result['pipelineConfig'] = self.pipeline_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('envId') is not None:
            self.env_id = m.get('envId')
        if m.get('envName') is not None:
            self.env_name = m.get('envName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.tag_list = []
        if m.get('tagList') is not None:
            for k in m.get('tagList'):
                temp_model = GetPipelineResponseBodyPipelineTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('pipelineConfig') is not None:
            temp_model = GetPipelineResponseBodyPipelinePipelineConfig()
            self.pipeline_config = temp_model.from_map(m['pipelineConfig'])
        return self


class GetPipelineResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, pipeline=None, success=None, error_code=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 流水线
        self.pipeline = pipeline  # type: GetPipelineResponseBodyPipeline
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str

    def validate(self):
        if self.pipeline:
            self.pipeline.validate()

    def to_map(self):
        _map = super(GetPipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.pipeline is not None:
            result['pipeline'] = self.pipeline.to_map()
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('pipeline') is not None:
            temp_model = GetPipelineResponseBodyPipeline()
            self.pipeline = temp_model.from_map(m['pipeline'])
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class CreateVariableGroupRequest(TeaModel):
    def __init__(self, name=None, description=None, variables=None):
        # 变量组名称
        self.name = name  # type: str
        # 变量组描述
        self.description = description  # type: str
        # 变量信息json字符串 isEncrypted 是否加密 name 变量名称 value 变量值
        self.variables = variables  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVariableGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.variables is not None:
            result['variables'] = self.variables
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('variables') is not None:
            self.variables = m.get('variables')
        return self


class CreateVariableGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, variable_group_id=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        if self.variable_group_id is not None:
            result['variableGroupId'] = self.variable_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class DeleteVariableGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVariableGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class GetWorkspaceResponseBodyWorkspace(TeaModel):
    def __init__(self, code_version=None, code_url=None, name=None, spec=None, status=None, template=None, id=None,
                 user_id=None, create_time=None):
        # 代码版本，支持 commitSHA、分支、标签
        self.code_version = code_version  # type: str
        # 代码来源URL
        self.code_url = code_url  # type: str
        # 工作空间名称
        self.name = name  # type: str
        # 机器规格
        self.spec = spec  # type: str
        # 空间状态，枚举：CREATING-创建中, SUCCESS-运行中, FROZEN-冻结中, RECOVERING-恢复中
        self.status = status  # type: str
        # 工作空间模板
        self.template = template  # type: str
        # 工作空间唯一标识，字符串形式，可在云效DevStudio访问空间链接中获取
        self.id = id  # type: str
        # 用户阿里云PK
        self.user_id = user_id  # type: str
        # 创建时间戳
        self.create_time = create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetWorkspaceResponseBodyWorkspace, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_version is not None:
            result['codeVersion'] = self.code_version
        if self.code_url is not None:
            result['codeUrl'] = self.code_url
        if self.name is not None:
            result['name'] = self.name
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        if self.template is not None:
            result['template'] = self.template
        if self.id is not None:
            result['id'] = self.id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('codeVersion') is not None:
            self.code_version = m.get('codeVersion')
        if m.get('codeUrl') is not None:
            self.code_url = m.get('codeUrl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self


class GetWorkspaceResponseBody(TeaModel):
    def __init__(self, workspace=None, success=None, error_code=None, error_message=None, request_id=None):
        # 工作空间信息
        self.workspace = workspace  # type: GetWorkspaceResponseBodyWorkspace
        # 请求是否成功
        self.success = success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.workspace:
            self.workspace.validate()

    def to_map(self):
        _map = super(GetWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace is not None:
            result['workspace'] = self.workspace.to_map()
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('workspace') is not None:
            temp_model = GetWorkspaceResponseBodyWorkspace()
            self.workspace = temp_model.from_map(m['workspace'])
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
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


class CreateSshKeyResponseBodySshKey(TeaModel):
    def __init__(self, public_key=None, id=None):
        # 企业公钥
        self.public_key = public_key  # type: str
        # 企业公钥id
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSshKeyResponseBodySshKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_key is not None:
            result['publicKey'] = self.public_key
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('publicKey') is not None:
            self.public_key = m.get('publicKey')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateSshKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, ssh_key=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 企业公钥
        self.ssh_key = ssh_key  # type: CreateSshKeyResponseBodySshKey

    def validate(self):
        if self.ssh_key:
            self.ssh_key.validate()

    def to_map(self):
        _map = super(CreateSshKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        if self.ssh_key is not None:
            result['sshKey'] = self.ssh_key.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('sshKey') is not None:
            temp_model = CreateSshKeyResponseBodySshKey()
            self.ssh_key = temp_model.from_map(m['sshKey'])
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


class DeleteHostGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class ReleaseWorkspaceResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
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


class ListVariableGroupsRequest(TeaModel):
    def __init__(self, page_sort=None, page_order=None, next_token=None, max_results=None):
        # 排序条件
        self.page_sort = page_sort  # type: str
        # 排序顺序
        self.page_order = page_order  # type: str
        # 分页token，上一次请求的出参nextToken
        self.next_token = next_token  # type: str
        # 最大返回数，默认30
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVariableGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_sort is not None:
            result['pageSort'] = self.page_sort
        if self.page_order is not None:
            result['pageOrder'] = self.page_order
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pageSort') is not None:
            self.page_sort = m.get('pageSort')
        if m.get('pageOrder') is not None:
            self.page_order = m.get('pageOrder')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
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
    def __init__(self, value=None, name=None, is_encrypted=None):
        # 变量值
        self.value = value  # type: str
        # 变量名
        self.name = name  # type: str
        # 是否加密
        self.is_encrypted = is_encrypted  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVariableGroupsResponseBodyVariableGroupsVariables, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        if self.name is not None:
            result['name'] = self.name
        if self.is_encrypted is not None:
            result['isEncrypted'] = self.is_encrypted
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('isEncrypted') is not None:
            self.is_encrypted = m.get('isEncrypted')
        return self


class ListVariableGroupsResponseBodyVariableGroups(TeaModel):
    def __init__(self, creator_account_id=None, update_time=None, modifier_account_id=None, description=None,
                 name=None, id=None, related_pipelines=None, variables=None, create_time=None):
        # 创建人阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 更新时间
        self.update_time = update_time  # type: long
        # 更新人阿里云账号id
        self.modifier_account_id = modifier_account_id  # type: str
        # 变量组描述
        self.description = description  # type: str
        # 变量组名称
        self.name = name  # type: str
        # 变量组id
        self.id = id  # type: long
        # 关联的流水线
        self.related_pipelines = related_pipelines  # type: list[ListVariableGroupsResponseBodyVariableGroupsRelatedPipelines]
        # 变量
        self.variables = variables  # type: list[ListVariableGroupsResponseBodyVariableGroupsVariables]
        # 创建时间
        self.create_time = create_time  # type: long

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
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.modifier_account_id is not None:
            result['modifierAccountId'] = self.modifier_account_id
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        result['relatedPipelines'] = []
        if self.related_pipelines is not None:
            for k in self.related_pipelines:
                result['relatedPipelines'].append(k.to_map() if k else None)
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('modifierAccountId') is not None:
            self.modifier_account_id = m.get('modifierAccountId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.related_pipelines = []
        if m.get('relatedPipelines') is not None:
            for k in m.get('relatedPipelines'):
                temp_model = ListVariableGroupsResponseBodyVariableGroupsRelatedPipelines()
                self.related_pipelines.append(temp_model.from_map(k))
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = ListVariableGroupsResponseBodyVariableGroupsVariables()
                self.variables.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self


class ListVariableGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, variable_groups=None,
                 total_count=None, next_token=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 变量组
        self.variable_groups = variable_groups  # type: list[ListVariableGroupsResponseBodyVariableGroups]
        # 变量组总数
        self.total_count = total_count  # type: long
        # 下一次查询的token，为空表示最后一页
        self.next_token = next_token  # type: str

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        result['variableGroups'] = []
        if self.variable_groups is not None:
            for k in self.variable_groups:
                result['variableGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        self.variable_groups = []
        if m.get('variableGroups') is not None:
            for k in m.get('variableGroups'):
                temp_model = ListVariableGroupsResponseBodyVariableGroups()
                self.variable_groups.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
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


class DeletePipelineResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
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


class FrozenWorkspaceResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, error_code=None, error_message=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 请求是否成功
        self.success = success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FrozenWorkspaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
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


class ListPipelineRunsRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, status=None, max_results=None, next_token=None,
                 trigger_mode=None):
        # 开始时间
        self.start_time = start_time  # type: long
        # 结束时间
        self.end_time = end_time  # type: long
        # 状态 状态 FAIL 运行失败 SUCCESS 运行成功 RUNNING 运行中
        self.status = status  # type: str
        # 最大返回数量
        self.max_results = max_results  # type: long
        # 分页Token
        self.next_token = next_token  # type: str
        # 触发模式 1人工触发 2定时触发 3代码提交触发
        self.trigger_mode = trigger_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineRunsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.status is not None:
            result['status'] = self.status
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')
        return self


class ListPipelineRunsResponseBodyPipelineRuns(TeaModel):
    def __init__(self, pipeline_id=None, start_time=None, creator_account_id=None, end_time=None,
                 pipeline_run_id=None, trigger_mode=None, status=None):
        # 流水线id
        self.pipeline_id = pipeline_id  # type: long
        # 开始时间
        self.start_time = start_time  # type: long
        # 运行人阿里云账号id
        self.creator_account_id = creator_account_id  # type: str
        # 结束时间
        self.end_time = end_time  # type: long
        # 流水线实例id
        self.pipeline_run_id = pipeline_run_id  # type: long
        # 触发模式
        self.trigger_mode = trigger_mode  # type: long
        # 运行状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPipelineRunsResponseBodyPipelineRuns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.creator_account_id is not None:
            result['creatorAccountId'] = self.creator_account_id
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.pipeline_run_id is not None:
            result['pipelineRunId'] = self.pipeline_run_id
        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('creatorAccountId') is not None:
            self.creator_account_id = m.get('creatorAccountId')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pipelineRunId') is not None:
            self.pipeline_run_id = m.get('pipelineRunId')
        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListPipelineRunsResponseBody(TeaModel):
    def __init__(self, request_id=None, error_message=None, error_code=None, success=None, total_count=None,
                 next_token=None, pipeline_runs=None):
        # 请求id，每次请求都是唯一值，便于后续排查问题
        self.request_id = request_id  # type: str
        # 错误信息
        self.error_message = error_message  # type: str
        # 错误码
        self.error_code = error_code  # type: str
        # true 接口调用成功，false 接口调用失败
        self.success = success  # type: bool
        # 总数
        self.total_count = total_count  # type: long
        # 下一个分页token，为空时，表示没有下一页
        self.next_token = next_token  # type: str
        # 流水线运行实例
        self.pipeline_runs = pipeline_runs  # type: list[ListPipelineRunsResponseBodyPipelineRuns]

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.success is not None:
            result['success'] = self.success
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['pipelineRuns'] = []
        if self.pipeline_runs is not None:
            for k in self.pipeline_runs:
                result['pipelineRuns'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.pipeline_runs = []
        if m.get('pipelineRuns') is not None:
            for k in m.get('pipelineRuns'):
                temp_model = ListPipelineRunsResponseBodyPipelineRuns()
                self.pipeline_runs.append(temp_model.from_map(k))
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


