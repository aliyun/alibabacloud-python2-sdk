# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class SendHotlineHeartBeatRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, token=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendHotlineHeartBeatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class SendHotlineHeartBeatResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendHotlineHeartBeatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendHotlineHeartBeatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendHotlineHeartBeatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendHotlineHeartBeatResponse, self).to_map()
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
            temp_model = SendHotlineHeartBeatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartChatWorkRequest(TeaModel):
    def __init__(self, instance_id=None, account_name=None):
        # instanceId
        self.instance_id = instance_id  # type: str
        # accountName
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartChatWorkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class StartChatWorkResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, data=None, code=None, success=None):
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # data
        self.data = data  # type: str
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartChatWorkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartChatWorkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartChatWorkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartChatWorkResponse, self).to_map()
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
            temp_model = StartChatWorkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HangUpDoubleCallRequest(TeaModel):
    def __init__(self, instance_id=None, acid=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 会话ID
        self.acid = acid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HangUpDoubleCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class HangUpDoubleCallResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否调用成功
        self.success = success  # type: bool
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HangUpDoubleCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class HangUpDoubleCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HangUpDoubleCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HangUpDoubleCallResponse, self).to_map()
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
            temp_model = HangUpDoubleCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAgentRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, display_name=None,
                 skill_group_id=None, skill_group_id_list=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.display_name = display_name  # type: str
        self.skill_group_id = skill_group_id  # type: list[int]
        self.skill_group_id_list = skill_group_id_list  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAgentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')
        return self


class UpdateAgentResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAgentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAgentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateAgentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAgentResponse, self).to_map()
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
            temp_model = UpdateAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditQualityRuleTagRequestAnalysisTypes(TeaModel):
    def __init__(self, name=None, id=None):
        self.name = name  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditQualityRuleTagRequestAnalysisTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class EditQualityRuleTagRequest(TeaModel):
    def __init__(self, instance_id=None, analysis_types=None):
        self.instance_id = instance_id  # type: str
        self.analysis_types = analysis_types  # type: list[EditQualityRuleTagRequestAnalysisTypes]

    def validate(self):
        if self.analysis_types:
            for k in self.analysis_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EditQualityRuleTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['AnalysisTypes'] = []
        if self.analysis_types is not None:
            for k in self.analysis_types:
                result['AnalysisTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.analysis_types = []
        if m.get('AnalysisTypes') is not None:
            for k in m.get('AnalysisTypes'):
                temp_model = EditQualityRuleTagRequestAnalysisTypes()
                self.analysis_types.append(temp_model.from_map(k))
        return self


class EditQualityRuleTagResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditQualityRuleTagResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EditQualityRuleTagResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EditQualityRuleTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditQualityRuleTagResponse, self).to_map()
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
            temp_model = EditQualityRuleTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOnlineServiceVolumeRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids=None, dep_ids=None, group_ids=None, time_latitude_type=None, exist_agent_grouping=None,
                 exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids = agent_ids  # type: list[long]
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 技能组id列表
        self.group_ids = group_ids  # type: list[long]
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnlineServiceVolumeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetOnlineServiceVolumeShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids_shrink=None, dep_ids_shrink=None, group_ids_shrink=None, time_latitude_type=None,
                 exist_agent_grouping=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink  # type: str
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink  # type: str
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnlineServiceVolumeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetOnlineServiceVolumeResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnlineServiceVolumeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetOnlineServiceVolumeResponseBody(TeaModel):
    def __init__(self, message=None, code=None, success=None, data=None, request_id=None):
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetOnlineServiceVolumeResponseBodyData
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOnlineServiceVolumeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetOnlineServiceVolumeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOnlineServiceVolumeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOnlineServiceVolumeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOnlineServiceVolumeResponse, self).to_map()
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
            temp_model = GetOnlineServiceVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOutboundTaskRequest(TeaModel):
    def __init__(self, outbound_task_id=None, instance_id=None):
        self.outbound_task_id = outbound_task_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOutboundTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteOutboundTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOutboundTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteOutboundTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteOutboundTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteOutboundTaskResponse, self).to_map()
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
            temp_model = DeleteOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOuterAccountRequest(TeaModel):
    def __init__(self, outer_account_id=None, outer_account_type=None, outer_account_name=None, avatar=None,
                 real_name=None, outer_department_id=None, outer_group_ids=None, ext=None, outer_department_type=None,
                 outer_group_type=None):
        self.outer_account_id = outer_account_id  # type: str
        self.outer_account_type = outer_account_type  # type: str
        self.outer_account_name = outer_account_name  # type: str
        self.avatar = avatar  # type: str
        self.real_name = real_name  # type: str
        self.outer_department_id = outer_department_id  # type: str
        self.outer_group_ids = outer_group_ids  # type: str
        self.ext = ext  # type: str
        self.outer_department_type = outer_department_type  # type: str
        self.outer_group_type = outer_group_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOuterAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id
        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type
        if self.outer_account_name is not None:
            result['OuterAccountName'] = self.outer_account_name
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.outer_department_id is not None:
            result['OuterDepartmentId'] = self.outer_department_id
        if self.outer_group_ids is not None:
            result['OuterGroupIds'] = self.outer_group_ids
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.outer_department_type is not None:
            result['OuterDepartmentType'] = self.outer_department_type
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')
        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')
        if m.get('OuterAccountName') is not None:
            self.outer_account_name = m.get('OuterAccountName')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('OuterDepartmentId') is not None:
            self.outer_department_id = m.get('OuterDepartmentId')
        if m.get('OuterGroupIds') is not None:
            self.outer_group_ids = m.get('OuterGroupIds')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('OuterDepartmentType') is not None:
            self.outer_department_type = m.get('OuterDepartmentType')
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        return self


class AddOuterAccountResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddOuterAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddOuterAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddOuterAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddOuterAccountResponse, self).to_map()
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
            temp_model = AddOuterAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentByIdRequest(TeaModel):
    def __init__(self, instance_id=None, agent_id=None):
        self.instance_id = instance_id  # type: str
        self.agent_id = agent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        return self


class GetAgentByIdResponseBodyData(TeaModel):
    def __init__(self, show_name=None, foreign_key=None, servicer_type=None, real_name=None, create_user_name=None,
                 agent_id=None, foreign_nick=None):
        self.show_name = show_name  # type: str
        self.foreign_key = foreign_key  # type: str
        self.servicer_type = servicer_type  # type: int
        self.real_name = real_name  # type: str
        self.create_user_name = create_user_name  # type: str
        self.agent_id = agent_id  # type: int
        self.foreign_nick = foreign_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentByIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.foreign_key is not None:
            result['ForeignKey'] = self.foreign_key
        if self.servicer_type is not None:
            result['ServicerType'] = self.servicer_type
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.foreign_nick is not None:
            result['ForeignNick'] = self.foreign_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('ForeignKey') is not None:
            self.foreign_key = m.get('ForeignKey')
        if m.get('ServicerType') is not None:
            self.servicer_type = m.get('ServicerType')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('ForeignNick') is not None:
            self.foreign_nick = m.get('ForeignNick')
        return self


class GetAgentByIdResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetAgentByIdResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAgentByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAgentByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAgentByIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAgentByIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentByIdResponse, self).to_map()
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
            temp_model = GetAgentByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityRuleDetailRequest(TeaModel):
    def __init__(self, instance_id=None, quality_rule_id=None):
        self.instance_id = instance_id  # type: str
        self.quality_rule_id = quality_rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityRuleDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.quality_rule_id is not None:
            result['QualityRuleId'] = self.quality_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QualityRuleId') is not None:
            self.quality_rule_id = m.get('QualityRuleId')
        return self


class GetQualityRuleDetailResponseBodyData(TeaModel):
    def __init__(self, rule_tag=None, key_words=None, match_type=None, name=None, rule_create_time=None,
                 rule_id=None):
        self.rule_tag = rule_tag  # type: int
        self.key_words = key_words  # type: list[str]
        self.match_type = match_type  # type: int
        self.name = name  # type: str
        self.rule_create_time = rule_create_time  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityRuleDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_create_time is not None:
            result['RuleCreateTime'] = self.rule_create_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleCreateTime') is not None:
            self.rule_create_time = m.get('RuleCreateTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetQualityRuleDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetQualityRuleDetailResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQualityRuleDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityRuleDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityRuleDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQualityRuleDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQualityRuleDetailResponse, self).to_map()
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
            temp_model = GetQualityRuleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityProjectLogRequest(TeaModel):
    def __init__(self, instance_id=None, project_id=None):
        self.instance_id = instance_id  # type: str
        self.project_id = project_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityProjectLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetQualityProjectLogResponseBodyData(TeaModel):
    def __init__(self, action_type=None, action_data=None, project_id=None, project_create_time=None,
                 action_time=None):
        self.action_type = action_type  # type: str
        self.action_data = action_data  # type: str
        self.project_id = project_id  # type: long
        self.project_create_time = project_create_time  # type: str
        self.action_time = action_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityProjectLogResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.action_data is not None:
            result['ActionData'] = self.action_data
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_create_time is not None:
            result['ProjectCreateTime'] = self.project_create_time
        if self.action_time is not None:
            result['ActionTime'] = self.action_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('ActionData') is not None:
            self.action_data = m.get('ActionData')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectCreateTime') is not None:
            self.project_create_time = m.get('ProjectCreateTime')
        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')
        return self


class GetQualityProjectLogResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetQualityProjectLogResponseBodyData]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQualityProjectLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetQualityProjectLogResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityProjectLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQualityProjectLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQualityProjectLogResponse, self).to_map()
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
            temp_model = GetQualityProjectLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotlineRecordDetailRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, close_time_end=None, current_page=None, page_size=None,
                 close_time_start=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 实例id
        self.instance_id = instance_id  # type: str
        # 热线挂断的时间范围
        self.close_time_end = close_time_end  # type: long
        # 当前页
        self.current_page = current_page  # type: int
        # 每页数据量
        self.page_size = page_size  # type: int
        # 热线挂断的时间范围
        self.close_time_start = close_time_start  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotlineRecordDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.close_time_end is not None:
            result['CloseTimeEnd'] = self.close_time_end
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.close_time_start is not None:
            result['CloseTimeStart'] = self.close_time_start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CloseTimeEnd') is not None:
            self.close_time_end = m.get('CloseTimeEnd')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CloseTimeStart') is not None:
            self.close_time_start = m.get('CloseTimeStart')
        return self


class ListHotlineRecordDetailResponseBodyResultDataData(TeaModel):
    def __init__(self, servicer_name=None, start_time=None, end_time=None, oss_url=None):
        self.servicer_name = servicer_name  # type: str
        # 热线开始时间
        self.start_time = start_time  # type: long
        # 热线结束时间
        self.end_time = end_time  # type: long
        # 热线通话录音地址
        self.oss_url = oss_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotlineRecordDetailResponseBodyResultDataData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        return self


class ListHotlineRecordDetailResponseBodyResultData(TeaModel):
    def __init__(self, current_page=None, total_results=None, total_page=None, one_page_size=None, data=None):
        self.current_page = current_page  # type: long
        self.total_results = total_results  # type: long
        self.total_page = total_page  # type: long
        self.one_page_size = one_page_size  # type: long
        self.data = data  # type: list[ListHotlineRecordDetailResponseBodyResultDataData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotlineRecordDetailResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListHotlineRecordDetailResponseBodyResultDataData()
                self.data.append(temp_model.from_map(k))
        return self


class ListHotlineRecordDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, result_data=None, code=None,
                 success=None):
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # data
        self.result_data = result_data  # type: ListHotlineRecordDetailResponseBodyResultData
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        _map = super(ListHotlineRecordDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ResultData') is not None:
            temp_model = ListHotlineRecordDetailResponseBodyResultData()
            self.result_data = temp_model.from_map(m['ResultData'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotlineRecordDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHotlineRecordDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotlineRecordDetailResponse, self).to_map()
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
            temp_model = ListHotlineRecordDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineMessageLogRequest(TeaModel):
    def __init__(self, instance_id=None, acid=None):
        # 实例id
        self.instance_id = instance_id  # type: str
        # 会话id
        self.acid = acid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineMessageLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class GetHotlineMessageLogResponseBodyData(TeaModel):
    def __init__(self, acid=None, sender_type=None, start_time=None, end_time=None, mid=None, content=None):
        # 会话ID
        self.acid = acid  # type: str
        # 发送方类型（1：会员，2：坐席）
        self.sender_type = sender_type  # type: int
        # 开始时间
        self.start_time = start_time  # type: long
        # 结束时间
        self.end_time = end_time  # type: long
        # 记录id
        self.mid = mid  # type: str
        # 会话内容
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineMessageLogResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.sender_type is not None:
            result['SenderType'] = self.sender_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.mid is not None:
            result['Mid'] = self.mid
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('SenderType') is not None:
            self.sender_type = m.get('SenderType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetHotlineMessageLogResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 调用是否成功
        self.success = success  # type: bool
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str
        self.data = data  # type: list[GetHotlineMessageLogResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHotlineMessageLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetHotlineMessageLogResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetHotlineMessageLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineMessageLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineMessageLogResponse, self).to_map()
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
            temp_model = GetHotlineMessageLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityProjectListRequest(TeaModel):
    def __init__(self, instance_id=None, project_id=None, project_name=None, status=None, page_no=None,
                 page_size=None, check_freq_type=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 质检项ID
        self.project_id = project_id  # type: long
        # 质检项名称
        self.project_name = project_name  # type: str
        # 质检项状态
        self.status = status  # type: int
        # PageNo
        self.page_no = page_no  # type: int
        # PageSize
        self.page_size = page_size  # type: int
        # 质检频率
        self.check_freq_type = check_freq_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityProjectListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.status is not None:
            result['Status'] = self.status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.check_freq_type is not None:
            result['checkFreqType'] = self.check_freq_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('checkFreqType') is not None:
            self.check_freq_type = m.get('checkFreqType')
        return self


class GetQualityProjectListResponseBodyDataQualityProjectList(TeaModel):
    def __init__(self, status=None, quality_type=None, quality_rule_ids=None, create_time=None, project_name=None,
                 check_freq_type=None, dep_list=None, servicer_list=None, version=None, group_list=None, id=None, modify_time=None):
        # 质检任务状态
        self.status = status  # type: int
        # 质检任务类型
        self.quality_type = quality_type  # type: int
        # 质检规则列表
        self.quality_rule_ids = quality_rule_ids  # type: list[long]
        # CreateTime
        self.create_time = create_time  # type: str
        # 质检任务名称
        self.project_name = project_name  # type: str
        # 质检任务频率
        self.check_freq_type = check_freq_type  # type: int
        # 技能组分组列表
        self.dep_list = dep_list  # type: list[long]
        # 坐席列表
        self.servicer_list = servicer_list  # type: list[long]
        # 版本
        self.version = version  # type: int
        # 技能组列表
        self.group_list = group_list  # type: list[long]
        # 质检任务Id
        self.id = id  # type: long
        # 修改时间
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityProjectListResponseBodyDataQualityProjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.quality_type is not None:
            result['QualityType'] = self.quality_type
        if self.quality_rule_ids is not None:
            result['QualityRuleIds'] = self.quality_rule_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.dep_list is not None:
            result['DepList'] = self.dep_list
        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list
        if self.version is not None:
            result['Version'] = self.version
        if self.group_list is not None:
            result['GroupList'] = self.group_list
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('QualityType') is not None:
            self.quality_type = m.get('QualityType')
        if m.get('QualityRuleIds') is not None:
            self.quality_rule_ids = m.get('QualityRuleIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')
        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetQualityProjectListResponseBodyData(TeaModel):
    def __init__(self, quality_project_list=None, page_no=None, page_size=None, total=None):
        # 质检项列表
        self.quality_project_list = quality_project_list  # type: list[GetQualityProjectListResponseBodyDataQualityProjectList]
        # PageNo
        self.page_no = page_no  # type: int
        # PageSize
        self.page_size = page_size  # type: int
        # Total
        self.total = total  # type: long

    def validate(self):
        if self.quality_project_list:
            for k in self.quality_project_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQualityProjectListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityProjectList'] = []
        if self.quality_project_list is not None:
            for k in self.quality_project_list:
                result['QualityProjectList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.quality_project_list = []
        if m.get('QualityProjectList') is not None:
            for k in m.get('QualityProjectList'):
                temp_model = GetQualityProjectListResponseBodyDataQualityProjectList()
                self.quality_project_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQualityProjectListResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        # Message
        self.message = message  # type: str
        # RequestId
        self.request_id = request_id  # type: str
        # Data
        self.data = data  # type: GetQualityProjectListResponseBodyData
        # Code
        self.code = code  # type: str
        # Success
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQualityProjectListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityProjectListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityProjectListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQualityProjectListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQualityProjectListResponse, self).to_map()
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
            temp_model = GetQualityProjectListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOutboundTaskRequest(TeaModel):
    def __init__(self, task_type=None, task_name=None, description=None, start_date=None, end_date=None,
                 start_time=None, end_time=None, retry_time=None, retry_interval=None, skill_group=None, ani=None,
                 group_name=None, model=None, department_id=None, ext_attrs=None, call_infos=None, instance_id=None):
        self.task_type = task_type  # type: int
        self.task_name = task_name  # type: str
        self.description = description  # type: str
        self.start_date = start_date  # type: str
        self.end_date = end_date  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.retry_time = retry_time  # type: int
        self.retry_interval = retry_interval  # type: int
        self.skill_group = skill_group  # type: long
        self.ani = ani  # type: str
        self.group_name = group_name  # type: str
        self.model = model  # type: int
        self.department_id = department_id  # type: long
        self.ext_attrs = ext_attrs  # type: str
        self.call_infos = call_infos  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOutboundTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.description is not None:
            result['Description'] = self.description
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.ani is not None:
            result['Ani'] = self.ani
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.model is not None:
            result['Model'] = self.model
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs
        if self.call_infos is not None:
            result['CallInfos'] = self.call_infos
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('ExtAttrs') is not None:
            self.ext_attrs = m.get('ExtAttrs')
        if m.get('CallInfos') is not None:
            self.call_infos = m.get('CallInfos')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateOutboundTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOutboundTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateOutboundTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateOutboundTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOutboundTaskResponse, self).to_map()
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
            temp_model = CreateOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineRuntimeInfoRequest(TeaModel):
    def __init__(self, instance_id=None, account_name=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 账号名
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineRuntimeInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetHotlineRuntimeInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 接口调用是否成功
        self.success = success  # type: bool
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str
        # 数据结果
        self.data = data  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineRuntimeInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetHotlineRuntimeInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineRuntimeInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineRuntimeInfoResponse, self).to_map()
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
            temp_model = GetHotlineRuntimeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeDoubleCallRequest(TeaModel):
    def __init__(self, instance_id=None, account_name=None, servicer_phone=None, member_phone=None,
                 outbound_call_number=None, biz_data=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 账号名称
        self.account_name = account_name  # type: str
        # 坐席手机号（需要通过坐席手机呼叫才需要填写）
        self.servicer_phone = servicer_phone  # type: str
        # 用户手机号
        self.member_phone = member_phone  # type: str
        # 外呼主叫号码
        self.outbound_call_number = outbound_call_number  # type: str
        # 业务携带数据（JsonString）
        self.biz_data = biz_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeDoubleCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.servicer_phone is not None:
            result['ServicerPhone'] = self.servicer_phone
        if self.member_phone is not None:
            result['MemberPhone'] = self.member_phone
        if self.outbound_call_number is not None:
            result['OutboundCallNumber'] = self.outbound_call_number
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('ServicerPhone') is not None:
            self.servicer_phone = m.get('ServicerPhone')
        if m.get('MemberPhone') is not None:
            self.member_phone = m.get('MemberPhone')
        if m.get('OutboundCallNumber') is not None:
            self.outbound_call_number = m.get('OutboundCallNumber')
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        return self


class MakeDoubleCallResponseBodyData(TeaModel):
    def __init__(self, acid=None):
        # 会话id
        self.acid = acid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeDoubleCallResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class MakeDoubleCallResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 调用是否成功
        self.success = success  # type: bool
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str
        # 返回数据
        self.data = data  # type: MakeDoubleCallResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(MakeDoubleCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = MakeDoubleCallResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class MakeDoubleCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MakeDoubleCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MakeDoubleCallResponse, self).to_map()
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
            temp_model = MakeDoubleCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupAgentStatusDetailsRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids=None, group_ids=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 技能组id列表
        self.group_ids = group_ids  # type: list[long]
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupAgentStatusDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupAgentStatusDetailsShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids_shrink=None, group_ids_shrink=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupAgentStatusDetailsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupAgentStatusDetailsResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: long
        # 每页的数量
        self.page_size = page_size  # type: long
        # 总记录数
        self.total_num = total_num  # type: long
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupAgentStatusDetailsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupAgentStatusDetailsResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 接口调用是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetSkillGroupAgentStatusDetailsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSkillGroupAgentStatusDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupAgentStatusDetailsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupAgentStatusDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSkillGroupAgentStatusDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSkillGroupAgentStatusDetailsResponse, self).to_map()
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
            temp_model = GetSkillGroupAgentStatusDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentServiceStatusRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids=None, dep_ids=None, time_latitude_type=None, exist_department_grouping=None,
                 exist_agent_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids = agent_ids  # type: list[long]
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        return self


class GetAgentServiceStatusShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids_shrink=None, dep_ids_shrink=None, time_latitude_type=None, exist_department_grouping=None,
                 exist_agent_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink  # type: str
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentServiceStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        return self


class GetAgentServiceStatusResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # 总记录数
        self.total_num = total_num  # type: long
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentServiceStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetAgentServiceStatusResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        # 错误描述
        self.message = message  # type: str
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # data
        self.data = data  # type: GetAgentServiceStatusResponseBodyData
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAgentServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAgentServiceStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAgentServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAgentServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentServiceStatusResponse, self).to_map()
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
            temp_model = GetAgentServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNumLocationRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, phone_num=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.phone_num = phone_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNumLocationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        return self


class GetNumLocationResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNumLocationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNumLocationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNumLocationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNumLocationResponse, self).to_map()
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
            temp_model = GetNumLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityRuleListRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None):
        self.instance_id = instance_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityRuleListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetQualityRuleListResponseBodyDataQualityRuleList(TeaModel):
    def __init__(self, rule_tag=None, key_words=None, match_type=None, name=None, rule_create_time=None,
                 rule_id=None):
        self.rule_tag = rule_tag  # type: int
        self.key_words = key_words  # type: list[str]
        self.match_type = match_type  # type: int
        self.name = name  # type: str
        self.rule_create_time = rule_create_time  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityRuleListResponseBodyDataQualityRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_create_time is not None:
            result['RuleCreateTime'] = self.rule_create_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleCreateTime') is not None:
            self.rule_create_time = m.get('RuleCreateTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetQualityRuleListResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total=None, quality_rule_list=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long
        self.quality_rule_list = quality_rule_list  # type: list[GetQualityRuleListResponseBodyDataQualityRuleList]

    def validate(self):
        if self.quality_rule_list:
            for k in self.quality_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQualityRuleListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['QualityRuleList'] = []
        if self.quality_rule_list is not None:
            for k in self.quality_rule_list:
                result['QualityRuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.quality_rule_list = []
        if m.get('QualityRuleList') is not None:
            for k in m.get('QualityRuleList'):
                temp_model = GetQualityRuleListResponseBodyDataQualityRuleList()
                self.quality_rule_list.append(temp_model.from_map(k))
        return self


class GetQualityRuleListResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetQualityRuleListResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQualityRuleListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityRuleListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityRuleListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQualityRuleListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQualityRuleListResponse, self).to_map()
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
            temp_model = GetQualityRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOutboundPhoneNumberRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOutboundPhoneNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class ListOutboundPhoneNumberResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[str]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOutboundPhoneNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOutboundPhoneNumberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOutboundPhoneNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOutboundPhoneNumberResponse, self).to_map()
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
            temp_model = ListOutboundPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentBySkillGroupIdRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, skill_group_id=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.skill_group_id = skill_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAgentBySkillGroupIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        return self


class ListAgentBySkillGroupIdResponseBodyData(TeaModel):
    def __init__(self, status=None, display_name=None, agent_id=None, account_name=None, tenant_id=None):
        self.status = status  # type: int
        self.display_name = display_name  # type: str
        self.agent_id = agent_id  # type: long
        self.account_name = account_name  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAgentBySkillGroupIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListAgentBySkillGroupIdResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[ListAgentBySkillGroupIdResponseBodyData]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAgentBySkillGroupIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAgentBySkillGroupIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAgentBySkillGroupIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAgentBySkillGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAgentBySkillGroupIdResponse, self).to_map()
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
            temp_model = ListAgentBySkillGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HangupThirdCallRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, call_id=None, job_id=None,
                 connection_id=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.call_id = call_id  # type: str
        self.job_id = job_id  # type: str
        self.connection_id = connection_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HangupThirdCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        return self


class HangupThirdCallResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(HangupThirdCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HangupThirdCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HangupThirdCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HangupThirdCallResponse, self).to_map()
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
            temp_model = HangupThirdCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartHotlineServiceRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None):
        # js sdk中自动生成的鉴权token
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartHotlineServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class StartHotlineServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartHotlineServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class StartHotlineServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartHotlineServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartHotlineServiceResponse, self).to_map()
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
            temp_model = StartHotlineServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None):
        # js sdk中自动生成的鉴权token
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetAgentResponseBodyDataGroupList(TeaModel):
    def __init__(self, display_name=None, description=None, channel_type=None, skill_group_id=None, name=None):
        self.display_name = display_name  # type: str
        self.description = description  # type: str
        self.channel_type = channel_type  # type: int
        self.skill_group_id = skill_group_id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentResponseBodyDataGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAgentResponseBodyData(TeaModel):
    def __init__(self, status=None, display_name=None, agent_id=None, group_list=None, account_name=None,
                 tenant_id=None):
        self.status = status  # type: int
        self.display_name = display_name  # type: str
        self.agent_id = agent_id  # type: long
        self.group_list = group_list  # type: list[GetAgentResponseBodyDataGroupList]
        self.account_name = account_name  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        if self.group_list:
            for k in self.group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAgentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        result['GroupList'] = []
        if self.group_list is not None:
            for k in self.group_list:
                result['GroupList'].append(k.to_map() if k else None)
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        self.group_list = []
        if m.get('GroupList') is not None:
            for k in m.get('GroupList'):
                temp_model = GetAgentResponseBodyDataGroupList()
                self.group_list.append(temp_model.from_map(k))
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetAgentResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: GetAgentResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAgentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAgentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetAgentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAgentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentResponse, self).to_map()
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
            temp_model = GetAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentIndexRealTimeRequest(TeaModel):
    def __init__(self, instance_id=None, page_size=None, current_page=None, dep_ids=None, group_ids=None):
        self.instance_id = instance_id  # type: str
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int
        self.dep_ids = dep_ids  # type: list[int]
        self.group_ids = group_ids  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentIndexRealTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        return self


class GetAgentIndexRealTimeResponseBodyDataColumns(TeaModel):
    def __init__(self, key=None, title=None):
        self.key = key  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentIndexRealTimeResponseBodyDataColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetAgentIndexRealTimeResponseBodyData(TeaModel):
    def __init__(self, rows=None, page_size=None, total=None, columns=None, page=None):
        self.rows = rows  # type: list[dict[str, any]]
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.columns = columns  # type: list[GetAgentIndexRealTimeResponseBodyDataColumns]
        self.page = page  # type: int

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAgentIndexRealTimeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = GetAgentIndexRealTimeResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetAgentIndexRealTimeResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetAgentIndexRealTimeResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAgentIndexRealTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAgentIndexRealTimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAgentIndexRealTimeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAgentIndexRealTimeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentIndexRealTimeResponse, self).to_map()
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
            temp_model = GetAgentIndexRealTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineGroupDetailReportRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, start_date=None, end_date=None, instance_id=None,
                 dep_ids=None, group_ids=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.start_date = start_date  # type: long
        self.end_date = end_date  # type: long
        self.instance_id = instance_id  # type: str
        self.dep_ids = dep_ids  # type: list[int]
        self.group_ids = group_ids  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineGroupDetailReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        return self


class GetHotlineGroupDetailReportResponseBodyDataColumns(TeaModel):
    def __init__(self, key=None, title=None):
        self.key = key  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineGroupDetailReportResponseBodyDataColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetHotlineGroupDetailReportResponseBodyData(TeaModel):
    def __init__(self, rows=None, page_size=None, total=None, columns=None, page=None):
        self.rows = rows  # type: list[dict[str, any]]
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.columns = columns  # type: list[GetHotlineGroupDetailReportResponseBodyDataColumns]
        self.page = page  # type: int

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHotlineGroupDetailReportResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = GetHotlineGroupDetailReportResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetHotlineGroupDetailReportResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetHotlineGroupDetailReportResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHotlineGroupDetailReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetHotlineGroupDetailReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotlineGroupDetailReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineGroupDetailReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineGroupDetailReportResponse, self).to_map()
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
            temp_model = GetHotlineGroupDetailReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptPhoneNumRequest(TeaModel):
    def __init__(self, instance_id=None, phone_num=None):
        # 实例Id
        self.instance_id = instance_id  # type: str
        # 号码明文
        self.phone_num = phone_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptPhoneNumRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        return self


class EncryptPhoneNumResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 接口调用是否成功
        self.success = success  # type: bool
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str
        # 加密后密文
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EncryptPhoneNumResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class EncryptPhoneNumResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EncryptPhoneNumResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EncryptPhoneNumResponse, self).to_map()
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
            temp_model = EncryptPhoneNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceListRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, name=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetInstanceListResponseBodyCommodityInstances(TeaModel):
    def __init__(self, instance_id=None, name=None):
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceListResponseBodyCommodityInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetInstanceListResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, message=None, page_size=None, page_number=None,
                 http_status_code=None, commodity_instances=None, code=None, success=None):
        self.total_count = total_count  # type: int
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.http_status_code = http_status_code  # type: int
        self.commodity_instances = commodity_instances  # type: list[GetInstanceListResponseBodyCommodityInstances]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.commodity_instances:
            for k in self.commodity_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['CommodityInstances'] = []
        if self.commodity_instances is not None:
            for k in self.commodity_instances:
                result['CommodityInstances'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.commodity_instances = []
        if m.get('CommodityInstances') is not None:
            for k in m.get('CommodityInstances'):
                temp_model = GetInstanceListResponseBodyCommodityInstances()
                self.commodity_instances.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceListResponse, self).to_map()
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
            temp_model = GetInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityProjectDetailRequest(TeaModel):
    def __init__(self, instance_id=None, project_id=None):
        # 租户实例ID
        self.instance_id = instance_id  # type: str
        # 质检任务ID
        self.project_id = project_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityProjectDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetQualityProjectDetailResponseBodyData(TeaModel):
    def __init__(self, status=None, quality_type=None, quality_rule_ids=None, create_time=None, project_name=None,
                 check_freq_type=None, dep_list=None, servicer_list=None, version=None, group_list=None, id=None, modify_time=None):
        # 质检任务状态
        self.status = status  # type: int
        # 质检类型
        self.quality_type = quality_type  # type: int
        # 质检规则ID
        self.quality_rule_ids = quality_rule_ids  # type: list[long]
        # 创建时间
        self.create_time = create_time  # type: str
        # 质检任务名称
        self.project_name = project_name  # type: str
        # 质检周期
        self.check_freq_type = check_freq_type  # type: int
        # 技能组分组
        self.dep_list = dep_list  # type: list[long]
        # 坐席列表
        self.servicer_list = servicer_list  # type: list[long]
        # Version
        self.version = version  # type: int
        # 技能组列表
        self.group_list = group_list  # type: list[long]
        # 质检任务ID
        self.id = id  # type: long
        # 修改时间
        self.modify_time = modify_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityProjectDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.quality_type is not None:
            result['QualityType'] = self.quality_type
        if self.quality_rule_ids is not None:
            result['QualityRuleIds'] = self.quality_rule_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.dep_list is not None:
            result['DepList'] = self.dep_list
        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list
        if self.version is not None:
            result['Version'] = self.version
        if self.group_list is not None:
            result['GroupList'] = self.group_list
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('QualityType') is not None:
            self.quality_type = m.get('QualityType')
        if m.get('QualityRuleIds') is not None:
            self.quality_rule_ids = m.get('QualityRuleIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')
        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetQualityProjectDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        # Message
        self.message = message  # type: str
        # RequestId
        self.request_id = request_id  # type: str
        # Data
        self.data = data  # type: GetQualityProjectDetailResponseBodyData
        # Code
        self.code = code  # type: str
        # Success
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQualityProjectDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityProjectDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityProjectDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQualityProjectDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQualityProjectDetailResponse, self).to_map()
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
            temp_model = GetQualityProjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCcoSmartCallOperateRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 call_id=None, command=None, param=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.call_id = call_id  # type: str
        self.command = command  # type: str
        self.param = param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCcoSmartCallOperateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.command is not None:
            result['Command'] = self.command
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class SendCcoSmartCallOperateResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCcoSmartCallOperateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SendCcoSmartCallOperateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendCcoSmartCallOperateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCcoSmartCallOperateResponse, self).to_map()
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
            temp_model = SendCcoSmartCallOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AnswerCallRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, call_id=None, job_id=None,
                 connection_id=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.call_id = call_id  # type: str
        self.job_id = job_id  # type: str
        self.connection_id = connection_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AnswerCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        return self


class AnswerCallResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AnswerCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AnswerCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AnswerCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AnswerCallResponse, self).to_map()
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
            temp_model = AnswerCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMicroOutboundRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 account_type=None, account_id=None, command_code=None, calling_number=None, called_number=None, ext_info=None,
                 app_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.account_type = account_type  # type: str
        self.account_id = account_id  # type: str
        self.command_code = command_code  # type: str
        self.calling_number = calling_number  # type: str
        self.called_number = called_number  # type: str
        self.ext_info = ext_info  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMicroOutboundRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.command_code is not None:
            result['CommandCode'] = self.command_code
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CommandCode') is not None:
            self.command_code = m.get('CommandCode')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class StartMicroOutboundResponseBody(TeaModel):
    def __init__(self, invoke_create_time=None, request_id=None, message=None, invoke_cmd_id=None,
                 customer_info=None, code=None):
        self.invoke_create_time = invoke_create_time  # type: str
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.invoke_cmd_id = invoke_cmd_id  # type: str
        self.customer_info = customer_info  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMicroOutboundResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_create_time is not None:
            result['InvokeCreateTime'] = self.invoke_create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.invoke_cmd_id is not None:
            result['InvokeCmdId'] = self.invoke_cmd_id
        if self.customer_info is not None:
            result['CustomerInfo'] = self.customer_info
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvokeCreateTime') is not None:
            self.invoke_create_time = m.get('InvokeCreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InvokeCmdId') is not None:
            self.invoke_cmd_id = m.get('InvokeCmdId')
        if m.get('CustomerInfo') is not None:
            self.customer_info = m.get('CustomerInfo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StartMicroOutboundResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartMicroOutboundResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartMicroOutboundResponse, self).to_map()
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
            temp_model = StartMicroOutboundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendHotlineServiceRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, type=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendHotlineServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SuspendHotlineServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendHotlineServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendHotlineServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SuspendHotlineServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SuspendHotlineServiceResponse, self).to_map()
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
            temp_model = SuspendHotlineServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentStatisticsRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids=None, dep_ids=None, time_latitude_type=None, exist_department_grouping=None,
                 exist_agent_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids = agent_ids  # type: list[long]
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        return self


class GetAgentStatisticsShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids_shrink=None, dep_ids_shrink=None, time_latitude_type=None, exist_department_grouping=None,
                 exist_agent_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink  # type: str
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentStatisticsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        return self


class GetAgentStatisticsResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentStatisticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetAgentStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetAgentStatisticsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAgentStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetAgentStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAgentStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAgentStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentStatisticsResponse, self).to_map()
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
            temp_model = GetAgentStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOuterAccountRequest(TeaModel):
    def __init__(self, outer_account_id=None, outer_account_type=None, outer_account_name=None, avatar=None,
                 real_name=None, outer_department_id=None, outer_group_ids=None, ext=None, outer_group_type=None,
                 outer_department_type=None):
        self.outer_account_id = outer_account_id  # type: str
        self.outer_account_type = outer_account_type  # type: str
        self.outer_account_name = outer_account_name  # type: str
        self.avatar = avatar  # type: str
        self.real_name = real_name  # type: str
        self.outer_department_id = outer_department_id  # type: str
        self.outer_group_ids = outer_group_ids  # type: str
        self.ext = ext  # type: str
        self.outer_group_type = outer_group_type  # type: str
        self.outer_department_type = outer_department_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOuterAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id
        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type
        if self.outer_account_name is not None:
            result['OuterAccountName'] = self.outer_account_name
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.outer_department_id is not None:
            result['OuterDepartmentId'] = self.outer_department_id
        if self.outer_group_ids is not None:
            result['OuterGroupIds'] = self.outer_group_ids
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        if self.outer_department_type is not None:
            result['OuterDepartmentType'] = self.outer_department_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')
        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')
        if m.get('OuterAccountName') is not None:
            self.outer_account_name = m.get('OuterAccountName')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('OuterDepartmentId') is not None:
            self.outer_department_id = m.get('OuterDepartmentId')
        if m.get('OuterGroupIds') is not None:
            self.outer_group_ids = m.get('OuterGroupIds')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        if m.get('OuterDepartmentType') is not None:
            self.outer_department_type = m.get('OuterDepartmentType')
        return self


class UpdateOuterAccountResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateOuterAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateOuterAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateOuterAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateOuterAccountResponse, self).to_map()
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
            temp_model = UpdateOuterAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineWaitingNumberRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineWaitingNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetHotlineWaitingNumberResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: long
        self.code = code  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineWaitingNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotlineWaitingNumberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineWaitingNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineWaitingNumberResponse, self).to_map()
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
            temp_model = GetHotlineWaitingNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HoldCallRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, call_id=None, job_id=None,
                 connection_id=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.call_id = call_id  # type: str
        self.job_id = job_id  # type: str
        self.connection_id = connection_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HoldCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        return self


class HoldCallResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(HoldCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HoldCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HoldCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HoldCallResponse, self).to_map()
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
            temp_model = HoldCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSeatInformationRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids=None, exist_department_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSeatInformationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.dep_ids is not None:
            result['depIds'] = self.dep_ids
        if self.exist_department_grouping is not None:
            result['existDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('depIds') is not None:
            self.dep_ids = m.get('depIds')
        if m.get('existDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('existDepartmentGrouping')
        return self


class GetSeatInformationShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids_shrink=None, exist_department_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSeatInformationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['depIds'] = self.dep_ids_shrink
        if self.exist_department_grouping is not None:
            result['existDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('depIds') is not None:
            self.dep_ids_shrink = m.get('depIds')
        if m.get('existDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('existDepartmentGrouping')
        return self


class GetSeatInformationResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rowr=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rowr = rowr  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSeatInformationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rowr is not None:
            result['Rowr'] = self.rowr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rowr') is not None:
            self.rowr = m.get('Rowr')
        return self


class GetSeatInformationResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetSeatInformationResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSeatInformationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSeatInformationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSeatInformationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSeatInformationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSeatInformationResponse, self).to_map()
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
            temp_model = GetSeatInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRtcTokenRequest(TeaModel):
    def __init__(self, instance_id=None, account_name=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 账号名称
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRtcTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetRtcTokenResponseBodyData(TeaModel):
    def __init__(self, token=None, rtc_id=None, account_name=None):
        # token信息
        self.token = token  # type: str
        # rtcId
        self.rtc_id = rtc_id  # type: str
        # 账号名
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRtcTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.rtc_id is not None:
            result['RtcId'] = self.rtc_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('RtcId') is not None:
            self.rtc_id = m.get('RtcId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetRtcTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # 是否成功
        self.success = success  # type: bool
        # 错误码
        self.code = code  # type: str
        # 错误信息
        self.message = message  # type: str
        # data
        self.data = data  # type: GetRtcTokenResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRtcTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetRtcTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetRtcTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRtcTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRtcTokenResponse, self).to_map()
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
            temp_model = GetRtcTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupAndAgentStatusSummaryRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids=None, group_ids=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 技能组id列表
        self.group_ids = group_ids  # type: list[long]
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupAndAgentStatusSummaryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupAndAgentStatusSummaryShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids_shrink=None, group_ids_shrink=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupAndAgentStatusSummaryShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupAndAgentStatusSummaryResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 每页的数量
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupAndAgentStatusSummaryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupAndAgentStatusSummaryResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 接口调用是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetSkillGroupAndAgentStatusSummaryResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSkillGroupAndAgentStatusSummaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupAndAgentStatusSummaryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupAndAgentStatusSummaryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSkillGroupAndAgentStatusSummaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSkillGroupAndAgentStatusSummaryResponse, self).to_map()
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
            temp_model = GetSkillGroupAndAgentStatusSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecordDataRequest(TeaModel):
    def __init__(self, instance_id=None, acid=None):
        self.instance_id = instance_id  # type: str
        self.acid = acid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRecordDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class GetRecordDataResponseBodyData(TeaModel):
    def __init__(self, oss_link=None, acid=None):
        self.oss_link = oss_link  # type: str
        self.acid = acid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRecordDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_link is not None:
            result['OssLink'] = self.oss_link
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssLink') is not None:
            self.oss_link = m.get('OssLink')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class GetRecordDataResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetRecordDataResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRecordDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetRecordDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetRecordDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRecordDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRecordDataResponse, self).to_map()
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
            temp_model = GetRecordDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupLatitudeStateRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids=None, group_ids=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 技能组id列表
        self.group_ids = group_ids  # type: list[long]
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupLatitudeStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupLatitudeStateShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids_shrink=None, group_ids_shrink=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupLatitudeStateShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupLatitudeStateResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 每页的数量
        self.page_size = page_size  # type: int
        # 总共记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupLatitudeStateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupLatitudeStateResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 接口调用是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetSkillGroupLatitudeStateResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSkillGroupLatitudeStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupLatitudeStateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupLatitudeStateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSkillGroupLatitudeStateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSkillGroupLatitudeStateResponse, self).to_map()
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
            temp_model = GetSkillGroupLatitudeStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQualityRuleRequest(TeaModel):
    def __init__(self, instance_id=None, id=None):
        self.instance_id = instance_id  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQualityRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteQualityRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQualityRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQualityRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteQualityRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQualityRuleResponse, self).to_map()
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
            temp_model = DeleteQualityRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendOutboundTaskRequest(TeaModel):
    def __init__(self, outbound_task_id=None, instance_id=None):
        self.outbound_task_id = outbound_task_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendOutboundTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SuspendOutboundTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SuspendOutboundTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendOutboundTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SuspendOutboundTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SuspendOutboundTaskResponse, self).to_map()
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
            temp_model = SuspendOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineServiceStatisticsRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids=None, dep_ids=None, group_ids=None, time_latitude_type=None, exist_agent_grouping=None,
                 exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids = agent_ids  # type: list[long]
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 技能组id列表
        self.group_ids = group_ids  # type: list[long]
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineServiceStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetHotlineServiceStatisticsShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids_shrink=None, dep_ids_shrink=None, group_ids_shrink=None, time_latitude_type=None,
                 exist_agent_grouping=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink  # type: str
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink  # type: str
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineServiceStatisticsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetHotlineServiceStatisticsResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineServiceStatisticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetHotlineServiceStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetHotlineServiceStatisticsResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHotlineServiceStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetHotlineServiceStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetHotlineServiceStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineServiceStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineServiceStatisticsResponse, self).to_map()
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
            temp_model = GetHotlineServiceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditQualityProjectRequest(TeaModel):
    def __init__(self, instance_id=None, project_id=None, project_name=None, check_freq_type=None,
                 project_version=None, scope_type=None, time_range_start=None, time_range_end=None, analysis_ids=None,
                 dep_list=None, group_list=None, servicer_list=None, channel_touch_type=None):
        self.instance_id = instance_id  # type: str
        self.project_id = project_id  # type: long
        self.project_name = project_name  # type: str
        self.check_freq_type = check_freq_type  # type: int
        self.project_version = project_version  # type: int
        self.scope_type = scope_type  # type: int
        self.time_range_start = time_range_start  # type: str
        self.time_range_end = time_range_end  # type: str
        self.analysis_ids = analysis_ids  # type: list[int]
        self.dep_list = dep_list  # type: list[int]
        self.group_list = group_list  # type: list[int]
        self.servicer_list = servicer_list  # type: list[str]
        self.channel_touch_type = channel_touch_type  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditQualityProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        if self.time_range_start is not None:
            result['TimeRangeStart'] = self.time_range_start
        if self.time_range_end is not None:
            result['TimeRangeEnd'] = self.time_range_end
        if self.analysis_ids is not None:
            result['AnalysisIds'] = self.analysis_ids
        if self.dep_list is not None:
            result['DepList'] = self.dep_list
        if self.group_list is not None:
            result['GroupList'] = self.group_list
        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list
        if self.channel_touch_type is not None:
            result['ChannelTouchType'] = self.channel_touch_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')
        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')
        if m.get('AnalysisIds') is not None:
            self.analysis_ids = m.get('AnalysisIds')
        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')
        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')
        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')
        if m.get('ChannelTouchType') is not None:
            self.channel_touch_type = m.get('ChannelTouchType')
        return self


class EditQualityProjectResponseBodyData(TeaModel):
    def __init__(self, version=None, project_id=None, instance_id=None):
        self.version = version  # type: int
        self.project_id = project_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditQualityProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EditQualityProjectResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[EditQualityProjectResponseBodyData]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EditQualityProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = EditQualityProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EditQualityProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EditQualityProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditQualityProjectResponse, self).to_map()
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
            temp_model = EditQualityProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOuterOrderedNumbersRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOuterOrderedNumbersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        return self


class ListOuterOrderedNumbersResponseBody(TeaModel):
    def __init__(self, numbers=None, message=None, request_id=None, code=None):
        self.numbers = numbers  # type: list[str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOuterOrderedNumbersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListOuterOrderedNumbersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOuterOrderedNumbersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOuterOrderedNumbersResponse, self).to_map()
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
            temp_model = ListOuterOrderedNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentBasisStatusRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids=None, dep_ids=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids = agent_ids  # type: list[long]
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentBasisStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        return self


class GetAgentBasisStatusShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids_shrink=None, dep_ids_shrink=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink  # type: str
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentBasisStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        return self


class GetAgentBasisStatusResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentBasisStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetAgentBasisStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetAgentBasisStatusResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAgentBasisStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetAgentBasisStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAgentBasisStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAgentBasisStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentBasisStatusResponse, self).to_map()
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
            temp_model = GetAgentBasisStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityResultRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, touch_start_time=None, touch_end_time=None,
                 channel_type=None, hit_status=None, group_ids=None, quality_rule_ids=None, project_ids=None):
        self.instance_id = instance_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.touch_start_time = touch_start_time  # type: str
        self.touch_end_time = touch_end_time  # type: str
        self.channel_type = channel_type  # type: str
        self.hit_status = hit_status  # type: int
        self.group_ids = group_ids  # type: list[int]
        self.quality_rule_ids = quality_rule_ids  # type: list[int]
        self.project_ids = project_ids  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.touch_start_time is not None:
            result['TouchStartTime'] = self.touch_start_time
        if self.touch_end_time is not None:
            result['TouchEndTime'] = self.touch_end_time
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.hit_status is not None:
            result['HitStatus'] = self.hit_status
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.quality_rule_ids is not None:
            result['QualityRuleIds'] = self.quality_rule_ids
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TouchStartTime') is not None:
            self.touch_start_time = m.get('TouchStartTime')
        if m.get('TouchEndTime') is not None:
            self.touch_end_time = m.get('TouchEndTime')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('HitStatus') is not None:
            self.hit_status = m.get('HitStatus')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('QualityRuleIds') is not None:
            self.quality_rule_ids = m.get('QualityRuleIds')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class GetQualityResultResponseBodyDataQualityResultResponseList(TeaModel):
    def __init__(self, touch_id=None, servicer_name=None, member_name=None, project_name=None, project_id=None,
                 channel_type=None, channel_type_name=None, touch_start_time=None, servicer_id=None, rule_name=None,
                 rule_id=None, group_name=None, group_id=None, instance_name=None, hit_status=None, hit_detail=None):
        self.touch_id = touch_id  # type: str
        self.servicer_name = servicer_name  # type: str
        self.member_name = member_name  # type: str
        self.project_name = project_name  # type: str
        self.project_id = project_id  # type: str
        self.channel_type = channel_type  # type: str
        self.channel_type_name = channel_type_name  # type: str
        self.touch_start_time = touch_start_time  # type: str
        self.servicer_id = servicer_id  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_id = rule_id  # type: str
        self.group_name = group_name  # type: str
        self.group_id = group_id  # type: str
        self.instance_name = instance_name  # type: str
        self.hit_status = hit_status  # type: bool
        self.hit_detail = hit_detail  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityResultResponseBodyDataQualityResultResponseList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.channel_type_name is not None:
            result['ChannelTypeName'] = self.channel_type_name
        if self.touch_start_time is not None:
            result['TouchStartTime'] = self.touch_start_time
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.hit_status is not None:
            result['HitStatus'] = self.hit_status
        if self.hit_detail is not None:
            result['HitDetail'] = self.hit_detail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ChannelTypeName') is not None:
            self.channel_type_name = m.get('ChannelTypeName')
        if m.get('TouchStartTime') is not None:
            self.touch_start_time = m.get('TouchStartTime')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('HitStatus') is not None:
            self.hit_status = m.get('HitStatus')
        if m.get('HitDetail') is not None:
            self.hit_detail = m.get('HitDetail')
        return self


class GetQualityResultResponseBodyData(TeaModel):
    def __init__(self, page_no=None, quality_result_response_list=None, page_size=None, total_num=None):
        self.page_no = page_no  # type: int
        self.quality_result_response_list = quality_result_response_list  # type: list[GetQualityResultResponseBodyDataQualityResultResponseList]
        self.page_size = page_size  # type: int
        self.total_num = total_num  # type: int

    def validate(self):
        if self.quality_result_response_list:
            for k in self.quality_result_response_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQualityResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        result['QualityResultResponseList'] = []
        if self.quality_result_response_list is not None:
            for k in self.quality_result_response_list:
                result['QualityResultResponseList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.quality_result_response_list = []
        if m.get('QualityResultResponseList') is not None:
            for k in m.get('QualityResultResponseList'):
                temp_model = GetQualityResultResponseBodyDataQualityResultResponseList()
                self.quality_result_response_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetQualityResultResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, channel_type_name=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetQualityResultResponseBodyData
        self.code = code  # type: str
        self.channel_type_name = channel_type_name  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQualityResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.channel_type_name is not None:
            result['ChannelTypeName'] = self.channel_type_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ChannelTypeName') is not None:
            self.channel_type_name = m.get('ChannelTypeName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQualityResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQualityResultResponse, self).to_map()
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
            temp_model = GetQualityResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexCurrentValueRequest(TeaModel):
    def __init__(self, dep_ids=None, group_ids=None, instance_id=None):
        self.dep_ids = dep_ids  # type: str
        self.group_ids = group_ids  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIndexCurrentValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetIndexCurrentValueResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[dict[str, any]]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIndexCurrentValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIndexCurrentValueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetIndexCurrentValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIndexCurrentValueResponse, self).to_map()
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
            temp_model = GetIndexCurrentValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateWebSocketSignRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateWebSocketSignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GenerateWebSocketSignResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateWebSocketSignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GenerateWebSocketSignResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateWebSocketSignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateWebSocketSignResponse, self).to_map()
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
            temp_model = GenerateWebSocketSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAgentRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, display_name=None,
                 skill_group_id=None, skill_group_id_list=None):
        # js sdk中自动生成的鉴权token
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.display_name = display_name  # type: str
        self.skill_group_id = skill_group_id  # type: list[long]
        self.skill_group_id_list = skill_group_id_list  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAgentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')
        return self


class CreateAgentResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: long
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAgentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class CreateAgentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAgentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAgentResponse, self).to_map()
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
            temp_model = CreateAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskDetailRequest(TeaModel):
    def __init__(self, outbound_task_id=None, status_list=None, end_reason_list=None, skill_group=None,
                 servicer_name=None, servicer_id=None, priority_list=None, task_id=None, ani=None, dnis=None, sid=None,
                 department_id_list=None, instance_id=None, page_size=None, current_page=None):
        self.outbound_task_id = outbound_task_id  # type: str
        self.status_list = status_list  # type: str
        self.end_reason_list = end_reason_list  # type: str
        self.skill_group = skill_group  # type: str
        self.servicer_name = servicer_name  # type: str
        self.servicer_id = servicer_id  # type: str
        self.priority_list = priority_list  # type: str
        self.task_id = task_id  # type: long
        self.ani = ani  # type: str
        self.dnis = dnis  # type: str
        self.sid = sid  # type: str
        self.department_id_list = department_id_list  # type: str
        self.instance_id = instance_id  # type: str
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.end_reason_list is not None:
            result['EndReasonList'] = self.end_reason_list
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.ani is not None:
            result['Ani'] = self.ani
        if self.dnis is not None:
            result['Dnis'] = self.dnis
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.department_id_list is not None:
            result['DepartmentIdList'] = self.department_id_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('EndReasonList') is not None:
            self.end_reason_list = m.get('EndReasonList')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('DepartmentIdList') is not None:
            self.department_id_list = m.get('DepartmentIdList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryTaskDetailResponseBodyDataList(TeaModel):
    def __init__(self, status=None, member_name=None, servicer_name=None, outbound_num=None, retry_time=None,
                 priority=None, gmt_modified=None, dnis=None, servicer_id=None, outbound_task_id=None, bu_id=None,
                 end_reason=None, gmt_create=None, department_id=None, ani=None, member_id=None, skill_group=None,
                 ext_attrs=None, id=None):
        self.status = status  # type: int
        self.member_name = member_name  # type: str
        self.servicer_name = servicer_name  # type: str
        self.outbound_num = outbound_num  # type: int
        self.retry_time = retry_time  # type: str
        self.priority = priority  # type: int
        self.gmt_modified = gmt_modified  # type: long
        self.dnis = dnis  # type: str
        self.servicer_id = servicer_id  # type: long
        self.outbound_task_id = outbound_task_id  # type: long
        self.bu_id = bu_id  # type: long
        self.end_reason = end_reason  # type: int
        self.gmt_create = gmt_create  # type: long
        self.department_id = department_id  # type: long
        self.ani = ani  # type: str
        self.member_id = member_id  # type: long
        self.skill_group = skill_group  # type: int
        self.ext_attrs = ext_attrs  # type: str
        self.id = id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskDetailResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.outbound_num is not None:
            result['OutboundNum'] = self.outbound_num
        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.dnis is not None:
            result['Dnis'] = self.dnis
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.end_reason is not None:
            result['EndReason'] = self.end_reason
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.ani is not None:
            result['Ani'] = self.ani
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('OutboundNum') is not None:
            self.outbound_num = m.get('OutboundNum')
        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('ExtAttrs') is not None:
            self.ext_attrs = m.get('ExtAttrs')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryTaskDetailResponseBodyData(TeaModel):
    def __init__(self, total_results=None, current_page=None, list=None, page_size=None):
        self.total_results = total_results  # type: str
        self.current_page = current_page  # type: str
        self.list = list  # type: list[QueryTaskDetailResponseBodyDataList]
        self.page_size = page_size  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTaskDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryTaskDetailResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTaskDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.http_status_code = http_status_code  # type: str
        self.data = data  # type: QueryTaskDetailResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTaskDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = QueryTaskDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTaskDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTaskDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTaskDetailResponse, self).to_map()
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
            temp_model = QueryTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditQualityRuleRequest(TeaModel):
    def __init__(self, instance_id=None, name=None, rule_tag=None, match_type=None, quality_rule_id=None,
                 key_words=None):
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.rule_tag = rule_tag  # type: int
        self.match_type = match_type  # type: int
        self.quality_rule_id = quality_rule_id  # type: long
        self.key_words = key_words  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditQualityRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.quality_rule_id is not None:
            result['QualityRuleId'] = self.quality_rule_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('QualityRuleId') is not None:
            self.quality_rule_id = m.get('QualityRuleId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        return self


class EditQualityRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditQualityRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EditQualityRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EditQualityRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditQualityRuleResponse, self).to_map()
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
            temp_model = EditQualityRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMcuLvsIpRequest(TeaModel):
    def __init__(self, instance_id=None):
        # 实例ID
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMcuLvsIpRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetMcuLvsIpResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool
        # error code
        self.code = code  # type: str
        # error message
        self.message = message  # type: str
        # result data
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMcuLvsIpResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetMcuLvsIpResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetMcuLvsIpResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMcuLvsIpResponse, self).to_map()
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
            temp_model = GetMcuLvsIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDepGroupTreeDataRequest(TeaModel):
    def __init__(self, instance_id=None, agent_id=None):
        # 租户实例ID
        self.instance_id = instance_id  # type: str
        # 坐席ID
        self.agent_id = agent_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDepGroupTreeDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        return self


class GetDepGroupTreeDataResponseBodyDataGroupDTOS(TeaModel):
    def __init__(self, skill_group_id=None, name=None):
        # skillGroupId
        self.skill_group_id = skill_group_id  # type: long
        # name
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDepGroupTreeDataResponseBodyDataGroupDTOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetDepGroupTreeDataResponseBodyData(TeaModel):
    def __init__(self, dep_group_name=None, dep_group_id=None, group_dtos=None):
        # depGroupName
        self.dep_group_name = dep_group_name  # type: str
        # depGroupId
        self.dep_group_id = dep_group_id  # type: str
        # groupDTOS
        self.group_dtos = group_dtos  # type: list[GetDepGroupTreeDataResponseBodyDataGroupDTOS]

    def validate(self):
        if self.group_dtos:
            for k in self.group_dtos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDepGroupTreeDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dep_group_name is not None:
            result['DepGroupName'] = self.dep_group_name
        if self.dep_group_id is not None:
            result['DepGroupId'] = self.dep_group_id
        result['GroupDTOS'] = []
        if self.group_dtos is not None:
            for k in self.group_dtos:
                result['GroupDTOS'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DepGroupName') is not None:
            self.dep_group_name = m.get('DepGroupName')
        if m.get('DepGroupId') is not None:
            self.dep_group_id = m.get('DepGroupId')
        self.group_dtos = []
        if m.get('GroupDTOS') is not None:
            for k in m.get('GroupDTOS'):
                temp_model = GetDepGroupTreeDataResponseBodyDataGroupDTOS()
                self.group_dtos.append(temp_model.from_map(k))
        return self


class GetDepGroupTreeDataResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # Id of the request
        self.request_id = request_id  # type: str
        # Message
        self.message = message  # type: str
        # Code
        self.code = code  # type: str
        # Success
        self.success = success  # type: str
        # Data
        self.data = data  # type: list[GetDepGroupTreeDataResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDepGroupTreeDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetDepGroupTreeDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetDepGroupTreeDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDepGroupTreeDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDepGroupTreeDataResponse, self).to_map()
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
            temp_model = GetDepGroupTreeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAgentRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None):
        # js sdk中自动生成的鉴权token
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAgentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DeleteAgentResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAgentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class DeleteAgentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAgentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAgentResponse, self).to_map()
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
            temp_model = DeleteAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerInfoRequest(TeaModel):
    def __init__(self, instance_id=None, member_id=None):
        # 实例ID
        self.instance_id = instance_id  # type: str
        # 会员ID
        self.member_id = member_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomerInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class GetCustomerInfoResponseBodyData(TeaModel):
    def __init__(self, nick=None, photo=None, user_id=None, real_name=None, outer_id=None, customize_fields=None):
        # 昵称
        self.nick = nick  # type: str
        # 头像
        self.photo = photo  # type: str
        # 会员ID
        self.user_id = user_id  # type: long
        # 真实姓名
        self.real_name = real_name  # type: str
        # 外部ID
        self.outer_id = outer_id  # type: str
        # 自定义字段
        self.customize_fields = customize_fields  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomerInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.photo is not None:
            result['Photo'] = self.photo
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.outer_id is not None:
            result['OuterId'] = self.outer_id
        if self.customize_fields is not None:
            result['CustomizeFields'] = self.customize_fields
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Photo') is not None:
            self.photo = m.get('Photo')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('OuterId') is not None:
            self.outer_id = m.get('OuterId')
        if m.get('CustomizeFields') is not None:
            self.customize_fields = m.get('CustomizeFields')
        return self


class GetCustomerInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID
        self.request_id = request_id  # type: str
        # 错误信息
        self.message = message  # type: str
        # 错误码
        self.code = code  # type: str
        # 是否请求成功
        self.success = success  # type: bool
        # 会员信息
        self.data = data  # type: GetCustomerInfoResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCustomerInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetCustomerInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetCustomerInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCustomerInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCustomerInfoResponse, self).to_map()
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
            temp_model = GetCustomerInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineAgentDetailReportRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, start_date=None, end_date=None, instance_id=None,
                 dep_ids=None, group_ids=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.start_date = start_date  # type: long
        self.end_date = end_date  # type: long
        self.instance_id = instance_id  # type: str
        self.dep_ids = dep_ids  # type: list[int]
        self.group_ids = group_ids  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineAgentDetailReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        return self


class GetHotlineAgentDetailReportResponseBodyDataColumns(TeaModel):
    def __init__(self, key=None, title=None):
        self.key = key  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineAgentDetailReportResponseBodyDataColumns, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetHotlineAgentDetailReportResponseBodyData(TeaModel):
    def __init__(self, rows=None, page_size=None, total=None, columns=None, page=None):
        self.rows = rows  # type: list[dict[str, any]]
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.columns = columns  # type: list[GetHotlineAgentDetailReportResponseBodyDataColumns]
        self.page = page  # type: int

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHotlineAgentDetailReportResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = GetHotlineAgentDetailReportResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetHotlineAgentDetailReportResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetHotlineAgentDetailReportResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHotlineAgentDetailReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetHotlineAgentDetailReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotlineAgentDetailReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineAgentDetailReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineAgentDetailReportResponse, self).to_map()
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
            temp_model = GetHotlineAgentDetailReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCcoSmartCallRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 called_show_number=None, called_number=None, voice_code=None, out_id=None, play_times=None, volume=None, speed=None,
                 asr_model_id=None, asr_base_id=None, asr_als_am_id=None, asr_vocabulary_id=None, record_flag=None,
                 pause_time=None, mute_time=None, action_code_break=None, dynamic_id=None, early_media_asr=None,
                 voice_code_param=None, session_timeout=None, action_code_time_break=None, tts_conf=None, tts_style=None,
                 tts_volume=None, tts_speed=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.called_show_number = called_show_number  # type: str
        self.called_number = called_number  # type: str
        self.voice_code = voice_code  # type: str
        self.out_id = out_id  # type: str
        self.play_times = play_times  # type: int
        self.volume = volume  # type: int
        self.speed = speed  # type: int
        self.asr_model_id = asr_model_id  # type: str
        self.asr_base_id = asr_base_id  # type: str
        self.asr_als_am_id = asr_als_am_id  # type: str
        self.asr_vocabulary_id = asr_vocabulary_id  # type: str
        self.record_flag = record_flag  # type: bool
        self.pause_time = pause_time  # type: int
        self.mute_time = mute_time  # type: int
        self.action_code_break = action_code_break  # type: bool
        self.dynamic_id = dynamic_id  # type: str
        self.early_media_asr = early_media_asr  # type: bool
        self.voice_code_param = voice_code_param  # type: str
        self.session_timeout = session_timeout  # type: int
        self.action_code_time_break = action_code_time_break  # type: int
        self.tts_conf = tts_conf  # type: bool
        self.tts_style = tts_style  # type: str
        self.tts_volume = tts_volume  # type: int
        self.tts_speed = tts_speed  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCcoSmartCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id
        if self.asr_base_id is not None:
            result['AsrBaseId'] = self.asr_base_id
        if self.asr_als_am_id is not None:
            result['AsrAlsAmId'] = self.asr_als_am_id
        if self.asr_vocabulary_id is not None:
            result['AsrVocabularyId'] = self.asr_vocabulary_id
        if self.record_flag is not None:
            result['RecordFlag'] = self.record_flag
        if self.pause_time is not None:
            result['PauseTime'] = self.pause_time
        if self.mute_time is not None:
            result['MuteTime'] = self.mute_time
        if self.action_code_break is not None:
            result['ActionCodeBreak'] = self.action_code_break
        if self.dynamic_id is not None:
            result['DynamicId'] = self.dynamic_id
        if self.early_media_asr is not None:
            result['EarlyMediaAsr'] = self.early_media_asr
        if self.voice_code_param is not None:
            result['VoiceCodeParam'] = self.voice_code_param
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.action_code_time_break is not None:
            result['ActionCodeTimeBreak'] = self.action_code_time_break
        if self.tts_conf is not None:
            result['TtsConf'] = self.tts_conf
        if self.tts_style is not None:
            result['TtsStyle'] = self.tts_style
        if self.tts_volume is not None:
            result['TtsVolume'] = self.tts_volume
        if self.tts_speed is not None:
            result['TtsSpeed'] = self.tts_speed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')
        if m.get('AsrBaseId') is not None:
            self.asr_base_id = m.get('AsrBaseId')
        if m.get('AsrAlsAmId') is not None:
            self.asr_als_am_id = m.get('AsrAlsAmId')
        if m.get('AsrVocabularyId') is not None:
            self.asr_vocabulary_id = m.get('AsrVocabularyId')
        if m.get('RecordFlag') is not None:
            self.record_flag = m.get('RecordFlag')
        if m.get('PauseTime') is not None:
            self.pause_time = m.get('PauseTime')
        if m.get('MuteTime') is not None:
            self.mute_time = m.get('MuteTime')
        if m.get('ActionCodeBreak') is not None:
            self.action_code_break = m.get('ActionCodeBreak')
        if m.get('DynamicId') is not None:
            self.dynamic_id = m.get('DynamicId')
        if m.get('EarlyMediaAsr') is not None:
            self.early_media_asr = m.get('EarlyMediaAsr')
        if m.get('VoiceCodeParam') is not None:
            self.voice_code_param = m.get('VoiceCodeParam')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('ActionCodeTimeBreak') is not None:
            self.action_code_time_break = m.get('ActionCodeTimeBreak')
        if m.get('TtsConf') is not None:
            self.tts_conf = m.get('TtsConf')
        if m.get('TtsStyle') is not None:
            self.tts_style = m.get('TtsStyle')
        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')
        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')
        return self


class SendCcoSmartCallResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCcoSmartCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SendCcoSmartCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendCcoSmartCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCcoSmartCallResponse, self).to_map()
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
            temp_model = SendCcoSmartCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatRecordDetailRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, close_time_end=None, current_page=None, page_size=None,
                 close_time_start=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 实例id
        self.instance_id = instance_id  # type: str
        # 在线挂断的时间范围
        self.close_time_end = close_time_end  # type: long
        # 当前页
        self.current_page = current_page  # type: int
        # 每页数据量
        self.page_size = page_size  # type: int
        # 在线挂断的时间范围
        self.close_time_start = close_time_start  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChatRecordDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.close_time_end is not None:
            result['CloseTimeEnd'] = self.close_time_end
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.close_time_start is not None:
            result['CloseTimeStart'] = self.close_time_start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CloseTimeEnd') is not None:
            self.close_time_end = m.get('CloseTimeEnd')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CloseTimeStart') is not None:
            self.close_time_start = m.get('CloseTimeStart')
        return self


class ListChatRecordDetailResponseBodyResultDataDataMessageList(TeaModel):
    def __init__(self, sender_name=None, content=None, sender_type=None, create_time=None, msg_type=None):
        self.sender_name = sender_name  # type: str
        self.content = content  # type: str
        self.sender_type = sender_type  # type: long
        self.create_time = create_time  # type: long
        self.msg_type = msg_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChatRecordDetailResponseBodyResultDataDataMessageList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sender_name is not None:
            result['SenderName'] = self.sender_name
        if self.content is not None:
            result['Content'] = self.content
        if self.sender_type is not None:
            result['SenderType'] = self.sender_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.msg_type is not None:
            result['MsgType'] = self.msg_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SenderName') is not None:
            self.sender_name = m.get('SenderName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SenderType') is not None:
            self.sender_type = m.get('SenderType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')
        return self


class ListChatRecordDetailResponseBodyResultDataData(TeaModel):
    def __init__(self, servicer_name=None, start_time=None, end_time=None, message_list=None):
        self.servicer_name = servicer_name  # type: str
        # 在线开始时间
        self.start_time = start_time  # type: long
        # 在线结束时间
        self.end_time = end_time  # type: long
        # 在线会话详细信息
        self.message_list = message_list  # type: list[ListChatRecordDetailResponseBodyResultDataDataMessageList]

    def validate(self):
        if self.message_list:
            for k in self.message_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChatRecordDetailResponseBodyResultDataData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['MessageList'] = []
        if self.message_list is not None:
            for k in self.message_list:
                result['MessageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.message_list = []
        if m.get('MessageList') is not None:
            for k in m.get('MessageList'):
                temp_model = ListChatRecordDetailResponseBodyResultDataDataMessageList()
                self.message_list.append(temp_model.from_map(k))
        return self


class ListChatRecordDetailResponseBodyResultData(TeaModel):
    def __init__(self, current_page=None, total_results=None, total_page=None, one_page_size=None, data=None):
        self.current_page = current_page  # type: long
        self.total_results = total_results  # type: long
        self.total_page = total_page  # type: long
        self.one_page_size = one_page_size  # type: long
        self.data = data  # type: list[ListChatRecordDetailResponseBodyResultDataData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChatRecordDetailResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListChatRecordDetailResponseBodyResultDataData()
                self.data.append(temp_model.from_map(k))
        return self


class ListChatRecordDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, result_data=None, code=None,
                 success=None):
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # data
        self.result_data = result_data  # type: ListChatRecordDetailResponseBodyResultData
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        _map = super(ListChatRecordDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ResultData') is not None:
            temp_model = ListChatRecordDetailResponseBodyResultData()
            self.result_data = temp_model.from_map(m['ResultData'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListChatRecordDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListChatRecordDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChatRecordDetailResponse, self).to_map()
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
            temp_model = ListChatRecordDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSkillGroupRequest(TeaModel):
    def __init__(self, outer_group_id=None, outer_group_name=None, outer_group_type=None, outer_department_id=None,
                 outer_department_type=None):
        self.outer_group_id = outer_group_id  # type: str
        self.outer_group_name = outer_group_name  # type: str
        self.outer_group_type = outer_group_type  # type: str
        self.outer_department_id = outer_department_id  # type: str
        self.outer_department_type = outer_department_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSkillGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_group_id is not None:
            result['OuterGroupId'] = self.outer_group_id
        if self.outer_group_name is not None:
            result['OuterGroupName'] = self.outer_group_name
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        if self.outer_department_id is not None:
            result['OuterDepartmentId'] = self.outer_department_id
        if self.outer_department_type is not None:
            result['OuterDepartmentType'] = self.outer_department_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OuterGroupId') is not None:
            self.outer_group_id = m.get('OuterGroupId')
        if m.get('OuterGroupName') is not None:
            self.outer_group_name = m.get('OuterGroupName')
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        if m.get('OuterDepartmentId') is not None:
            self.outer_department_id = m.get('OuterDepartmentId')
        if m.get('OuterDepartmentType') is not None:
            self.outer_department_type = m.get('OuterDepartmentType')
        return self


class AddSkillGroupResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddSkillGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddSkillGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddSkillGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddSkillGroupResponse, self).to_map()
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
            temp_model = AddSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HangupCallRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, call_id=None, job_id=None,
                 connection_id=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.call_id = call_id  # type: str
        self.job_id = job_id  # type: str
        self.connection_id = connection_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HangupCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        return self


class HangupCallResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(HangupCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HangupCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HangupCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HangupCallResponse, self).to_map()
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
            temp_model = HangupCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSkillGroupRequest(TeaModel):
    def __init__(self, outer_group_type=None, outer_group_id=None):
        self.outer_group_type = outer_group_type  # type: str
        self.outer_group_id = outer_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSkillGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        if self.outer_group_id is not None:
            result['OuterGroupId'] = self.outer_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        if m.get('OuterGroupId') is not None:
            self.outer_group_id = m.get('OuterGroupId')
        return self


class DeleteSkillGroupResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: bool
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSkillGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSkillGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSkillGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSkillGroupResponse, self).to_map()
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
            temp_model = DeleteSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQualityProjectRequest(TeaModel):
    def __init__(self, project_name=None, check_freq_type=None, scope_type=None, time_range_start=None,
                 time_range_end=None, instance_id=None, channel_touch_type=None, dep_list=None, group_list=None,
                 servicer_list=None, analysis_ids=None):
        self.project_name = project_name  # type: str
        self.check_freq_type = check_freq_type  # type: int
        self.scope_type = scope_type  # type: int
        self.time_range_start = time_range_start  # type: str
        self.time_range_end = time_range_end  # type: str
        self.instance_id = instance_id  # type: str
        self.channel_touch_type = channel_touch_type  # type: list[int]
        self.dep_list = dep_list  # type: list[int]
        self.group_list = group_list  # type: list[int]
        self.servicer_list = servicer_list  # type: list[str]
        self.analysis_ids = analysis_ids  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQualityProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        if self.time_range_start is not None:
            result['TimeRangeStart'] = self.time_range_start
        if self.time_range_end is not None:
            result['TimeRangeEnd'] = self.time_range_end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.channel_touch_type is not None:
            result['ChannelTouchType'] = self.channel_touch_type
        if self.dep_list is not None:
            result['DepList'] = self.dep_list
        if self.group_list is not None:
            result['GroupList'] = self.group_list
        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list
        if self.analysis_ids is not None:
            result['AnalysisIds'] = self.analysis_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')
        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ChannelTouchType') is not None:
            self.channel_touch_type = m.get('ChannelTouchType')
        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')
        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')
        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')
        if m.get('AnalysisIds') is not None:
            self.analysis_ids = m.get('AnalysisIds')
        return self


class CreateQualityProjectResponseBodyData(TeaModel):
    def __init__(self, version=None, project_id=None, instance_id=None):
        self.version = version  # type: int
        self.project_id = project_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQualityProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateQualityProjectResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: CreateQualityProjectResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateQualityProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateQualityProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQualityProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateQualityProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateQualityProjectResponse, self).to_map()
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
            temp_model = CreateQualityProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySkillGroupsRequest(TeaModel):
    def __init__(self, instance_id=None, page_no=None, page_size=None, client_token=None):
        self.instance_id = instance_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySkillGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class QuerySkillGroupsResponseBodyData(TeaModel):
    def __init__(self, display_name=None, description=None, channel_type=None, skill_group_name=None,
                 skill_group_id=None):
        self.display_name = display_name  # type: str
        self.description = description  # type: str
        self.channel_type = channel_type  # type: int
        self.skill_group_name = skill_group_name  # type: str
        self.skill_group_id = skill_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySkillGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        return self


class QuerySkillGroupsResponseBody(TeaModel):
    def __init__(self, one_page_size=None, total_page=None, request_id=None, current_page=None, total_results=None,
                 data=None):
        self.one_page_size = one_page_size  # type: int
        self.total_page = total_page  # type: int
        self.request_id = request_id  # type: str
        self.current_page = current_page  # type: int
        self.total_results = total_results  # type: int
        self.data = data  # type: list[QuerySkillGroupsResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySkillGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySkillGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QuerySkillGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySkillGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySkillGroupsResponse, self).to_map()
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
            temp_model = QuerySkillGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQualityRuleRequest(TeaModel):
    def __init__(self, instance_id=None, name=None, rule_tag=None, match_type=None, key_words=None):
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.rule_tag = rule_tag  # type: int
        self.match_type = match_type  # type: int
        self.key_words = key_words  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQualityRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        return self


class CreateQualityRuleResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateQualityRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQualityRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateQualityRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateQualityRuleResponse, self).to_map()
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
            temp_model = CreateQualityRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 租户实例id
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListRolesResponseBodyData(TeaModel):
    def __init__(self, role_id=None, create_time=None, bu_id=None, title=None, code=None, description=None,
                 role_group_id=None, role_group_name=None):
        # 角色id
        self.role_id = role_id  # type: long
        # 创建时间
        self.create_time = create_time  # type: str
        # 租户id
        self.bu_id = bu_id  # type: long
        # 角色名称
        self.title = title  # type: str
        # 角色code
        self.code = code  # type: str
        # 角色描述
        self.description = description  # type: str
        # 所属角色组id
        self.role_group_id = role_group_id  # type: long
        # 所属角色组名称
        self.role_group_name = role_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRolesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.title is not None:
            result['Title'] = self.title
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.role_group_id is not None:
            result['RoleGroupId'] = self.role_group_id
        if self.role_group_name is not None:
            result['RoleGroupName'] = self.role_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RoleGroupId') is not None:
            self.role_group_id = m.get('RoleGroupId')
        if m.get('RoleGroupName') is not None:
            self.role_group_name = m.get('RoleGroupName')
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, data=None, success=None):
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # data
        self.data = data  # type: list[ListRolesResponseBodyData]
        # success
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRolesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRolesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRolesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRolesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRolesResponse, self).to_map()
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
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineCallActionRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, act=None, from_source=None, biz=None,
                 acc=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.act = act  # type: int
        self.from_source = from_source  # type: str
        self.biz = biz  # type: str
        self.acc = acc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineCallActionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.act is not None:
            result['Act'] = self.act
        if self.from_source is not None:
            result['FromSource'] = self.from_source
        if self.biz is not None:
            result['Biz'] = self.biz
        if self.acc is not None:
            result['Acc'] = self.acc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('FromSource') is not None:
            self.from_source = m.get('FromSource')
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        return self


class GetHotlineCallActionResponseBodyData(TeaModel):
    def __init__(self, touch_id=None, dep_id=None, member_name=None, servicer_name=None, channel_type=None,
                 action_id=None, callout_name=None, sub_touch_id=None, servicer_id=None, bu_id=None, callout_id=None,
                 case_id=None, channel_id=None, is_transfer=None, member_id=None, task_id=None, member_list=None):
        self.touch_id = touch_id  # type: long
        self.dep_id = dep_id  # type: long
        self.member_name = member_name  # type: str
        self.servicer_name = servicer_name  # type: str
        self.channel_type = channel_type  # type: long
        self.action_id = action_id  # type: long
        self.callout_name = callout_name  # type: str
        self.sub_touch_id = sub_touch_id  # type: long
        self.servicer_id = servicer_id  # type: long
        self.bu_id = bu_id  # type: long
        self.callout_id = callout_id  # type: long
        self.case_id = case_id  # type: long
        self.channel_id = channel_id  # type: str
        self.is_transfer = is_transfer  # type: str
        self.member_id = member_id  # type: long
        self.task_id = task_id  # type: long
        self.member_list = member_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineCallActionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.dep_id is not None:
            result['DepId'] = self.dep_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.action_id is not None:
            result['ActionId'] = self.action_id
        if self.callout_name is not None:
            result['CalloutName'] = self.callout_name
        if self.sub_touch_id is not None:
            result['SubTouchId'] = self.sub_touch_id
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.callout_id is not None:
            result['CalloutId'] = self.callout_id
        if self.case_id is not None:
            result['CaseId'] = self.case_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.is_transfer is not None:
            result['IsTransfer'] = self.is_transfer
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.member_list is not None:
            result['MemberList'] = self.member_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('DepId') is not None:
            self.dep_id = m.get('DepId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')
        if m.get('CalloutName') is not None:
            self.callout_name = m.get('CalloutName')
        if m.get('SubTouchId') is not None:
            self.sub_touch_id = m.get('SubTouchId')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('CalloutId') is not None:
            self.callout_id = m.get('CalloutId')
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('IsTransfer') is not None:
            self.is_transfer = m.get('IsTransfer')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('MemberList') is not None:
            self.member_list = m.get('MemberList')
        return self


class GetHotlineCallActionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetHotlineCallActionResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHotlineCallActionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetHotlineCallActionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotlineCallActionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineCallActionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineCallActionResponse, self).to_map()
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
            temp_model = GetHotlineCallActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSkillGroupRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, channel_type=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.channel_type = channel_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSkillGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        return self


class ListSkillGroupResponseBodyData(TeaModel):
    def __init__(self, display_name=None, description=None, channel_type=None, skill_group_id=None, name=None):
        self.display_name = display_name  # type: str
        self.description = description  # type: str
        self.channel_type = channel_type  # type: int
        self.skill_group_id = skill_group_id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSkillGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListSkillGroupResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[ListSkillGroupResponseBodyData]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSkillGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSkillGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSkillGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSkillGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSkillGroupResponse, self).to_map()
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
            temp_model = ListSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOnlineSeatInformationRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids=None, dep_ids=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids = agent_ids  # type: list[long]
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnlineSeatInformationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        return self


class GetOnlineSeatInformationShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids_shrink=None, dep_ids_shrink=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink  # type: str
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnlineSeatInformationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        return self


class GetOnlineSeatInformationResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOnlineSeatInformationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetOnlineSeatInformationResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetOnlineSeatInformationResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOnlineSeatInformationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetOnlineSeatInformationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetOnlineSeatInformationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOnlineSeatInformationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOnlineSeatInformationResponse, self).to_map()
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
            temp_model = GetOnlineSeatInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQualityProjectRequest(TeaModel):
    def __init__(self, instance_id=None, project_id=None):
        self.instance_id = instance_id  # type: str
        self.project_id = project_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQualityProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteQualityProjectResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQualityProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQualityProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteQualityProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQualityProjectResponse, self).to_map()
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
            temp_model = DeleteQualityProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTouchListRequest(TeaModel):
    def __init__(self, instance_id=None, first_time_start=None, first_time_end=None, close_time_start=None,
                 close_time_end=None, touch_id=None, channel_id=None, channel_type=None, touch_type=None, member_id=None,
                 member_name=None, servicer_id=None, servicer_name=None, queue_id=None, evaluation_status=None,
                 evaluation_level=None, evaluation_score=None, page_size=None, current_page=None):
        self.instance_id = instance_id  # type: str
        self.first_time_start = first_time_start  # type: long
        self.first_time_end = first_time_end  # type: long
        self.close_time_start = close_time_start  # type: long
        self.close_time_end = close_time_end  # type: long
        self.touch_id = touch_id  # type: list[long]
        self.channel_id = channel_id  # type: list[str]
        self.channel_type = channel_type  # type: list[int]
        self.touch_type = touch_type  # type: list[int]
        self.member_id = member_id  # type: list[long]
        self.member_name = member_name  # type: list[str]
        self.servicer_id = servicer_id  # type: list[long]
        self.servicer_name = servicer_name  # type: list[str]
        self.queue_id = queue_id  # type: list[long]
        self.evaluation_status = evaluation_status  # type: list[int]
        self.evaluation_level = evaluation_level  # type: list[int]
        self.evaluation_score = evaluation_score  # type: list[int]
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTouchListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.first_time_start is not None:
            result['FirstTimeStart'] = self.first_time_start
        if self.first_time_end is not None:
            result['FirstTimeEnd'] = self.first_time_end
        if self.close_time_start is not None:
            result['CloseTimeStart'] = self.close_time_start
        if self.close_time_end is not None:
            result['CloseTimeEnd'] = self.close_time_end
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.touch_type is not None:
            result['TouchType'] = self.touch_type
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.queue_id is not None:
            result['QueueId'] = self.queue_id
        if self.evaluation_status is not None:
            result['EvaluationStatus'] = self.evaluation_status
        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level
        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('FirstTimeStart') is not None:
            self.first_time_start = m.get('FirstTimeStart')
        if m.get('FirstTimeEnd') is not None:
            self.first_time_end = m.get('FirstTimeEnd')
        if m.get('CloseTimeStart') is not None:
            self.close_time_start = m.get('CloseTimeStart')
        if m.get('CloseTimeEnd') is not None:
            self.close_time_end = m.get('CloseTimeEnd')
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('TouchType') is not None:
            self.touch_type = m.get('TouchType')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')
        if m.get('EvaluationStatus') is not None:
            self.evaluation_status = m.get('EvaluationStatus')
        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')
        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryTouchListResponseBodyResultDataDataExtAttrs(TeaModel):
    def __init__(self, evaluation_score=None, evaluation_level=None, evaluation_solution=None,
                 online_session_source=None, online_join_resp_interval=None, evaluation_status=None, out_call_route_number=None,
                 dnis=None, ani=None):
        self.evaluation_score = evaluation_score  # type: int
        self.evaluation_level = evaluation_level  # type: int
        self.evaluation_solution = evaluation_solution  # type: int
        self.online_session_source = online_session_source  # type: int
        self.online_join_resp_interval = online_join_resp_interval  # type: int
        self.evaluation_status = evaluation_status  # type: int
        # 外呼为主叫号码
        self.out_call_route_number = out_call_route_number  # type: str
        # 外呼为被叫号码,入呼为被叫号码
        self.dnis = dnis  # type: str
        # 入呼为主叫号码
        self.ani = ani  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTouchListResponseBodyResultDataDataExtAttrs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score
        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level
        if self.evaluation_solution is not None:
            result['EvaluationSolution'] = self.evaluation_solution
        if self.online_session_source is not None:
            result['OnlineSessionSource'] = self.online_session_source
        if self.online_join_resp_interval is not None:
            result['OnlineJoinRespInterval'] = self.online_join_resp_interval
        if self.evaluation_status is not None:
            result['EvaluationStatus'] = self.evaluation_status
        if self.out_call_route_number is not None:
            result['OutCallRouteNumber'] = self.out_call_route_number
        if self.dnis is not None:
            result['Dnis'] = self.dnis
        if self.ani is not None:
            result['Ani'] = self.ani
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')
        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')
        if m.get('EvaluationSolution') is not None:
            self.evaluation_solution = m.get('EvaluationSolution')
        if m.get('OnlineSessionSource') is not None:
            self.online_session_source = m.get('OnlineSessionSource')
        if m.get('OnlineJoinRespInterval') is not None:
            self.online_join_resp_interval = m.get('OnlineJoinRespInterval')
        if m.get('EvaluationStatus') is not None:
            self.evaluation_status = m.get('EvaluationStatus')
        if m.get('OutCallRouteNumber') is not None:
            self.out_call_route_number = m.get('OutCallRouteNumber')
        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        return self


class QueryTouchListResponseBodyResultDataData(TeaModel):
    def __init__(self, status=None, to_id=None, parent_touch_id=None, servicer_name=None, channel_type=None,
                 close_time=None, gmt_modified=None, servicer_id=None, switch_user=None, bu_id=None, from_id=None,
                 user_touch_id=None, touch_time=None, touch_content=None, feedback=None, touch_id=None, queue_id=None, dep_id=None,
                 touch_end_reason=None, member_name=None, common_queue_name=None, first_time=None, touch_type=None, channel_id=None,
                 gmt_create=None, member_id=None, ext_attrs=None):
        self.status = status  # type: int
        self.to_id = to_id  # type: long
        self.parent_touch_id = parent_touch_id  # type: long
        self.servicer_name = servicer_name  # type: str
        self.channel_type = channel_type  # type: int
        self.close_time = close_time  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.servicer_id = servicer_id  # type: long
        self.switch_user = switch_user  # type: str
        self.bu_id = bu_id  # type: long
        self.from_id = from_id  # type: long
        self.user_touch_id = user_touch_id  # type: long
        self.touch_time = touch_time  # type: str
        self.touch_content = touch_content  # type: str
        self.feedback = feedback  # type: str
        self.touch_id = touch_id  # type: str
        self.queue_id = queue_id  # type: long
        self.dep_id = dep_id  # type: long
        self.touch_end_reason = touch_end_reason  # type: int
        self.member_name = member_name  # type: str
        self.common_queue_name = common_queue_name  # type: str
        self.first_time = first_time  # type: long
        self.touch_type = touch_type  # type: int
        self.channel_id = channel_id  # type: str
        self.gmt_create = gmt_create  # type: long
        self.member_id = member_id  # type: long
        self.ext_attrs = ext_attrs  # type: QueryTouchListResponseBodyResultDataDataExtAttrs

    def validate(self):
        if self.ext_attrs:
            self.ext_attrs.validate()

    def to_map(self):
        _map = super(QueryTouchListResponseBodyResultDataData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.to_id is not None:
            result['ToId'] = self.to_id
        if self.parent_touch_id is not None:
            result['ParentTouchId'] = self.parent_touch_id
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.close_time is not None:
            result['CloseTime'] = self.close_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.switch_user is not None:
            result['SwitchUser'] = self.switch_user
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.from_id is not None:
            result['FromId'] = self.from_id
        if self.user_touch_id is not None:
            result['UserTouchId'] = self.user_touch_id
        if self.touch_time is not None:
            result['TouchTime'] = self.touch_time
        if self.touch_content is not None:
            result['TouchContent'] = self.touch_content
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.queue_id is not None:
            result['QueueId'] = self.queue_id
        if self.dep_id is not None:
            result['DepId'] = self.dep_id
        if self.touch_end_reason is not None:
            result['TouchEndReason'] = self.touch_end_reason
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.common_queue_name is not None:
            result['CommonQueueName'] = self.common_queue_name
        if self.first_time is not None:
            result['FirstTime'] = self.first_time
        if self.touch_type is not None:
            result['TouchType'] = self.touch_type
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToId') is not None:
            self.to_id = m.get('ToId')
        if m.get('ParentTouchId') is not None:
            self.parent_touch_id = m.get('ParentTouchId')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CloseTime') is not None:
            self.close_time = m.get('CloseTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('SwitchUser') is not None:
            self.switch_user = m.get('SwitchUser')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('FromId') is not None:
            self.from_id = m.get('FromId')
        if m.get('UserTouchId') is not None:
            self.user_touch_id = m.get('UserTouchId')
        if m.get('TouchTime') is not None:
            self.touch_time = m.get('TouchTime')
        if m.get('TouchContent') is not None:
            self.touch_content = m.get('TouchContent')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')
        if m.get('DepId') is not None:
            self.dep_id = m.get('DepId')
        if m.get('TouchEndReason') is not None:
            self.touch_end_reason = m.get('TouchEndReason')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('CommonQueueName') is not None:
            self.common_queue_name = m.get('CommonQueueName')
        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')
        if m.get('TouchType') is not None:
            self.touch_type = m.get('TouchType')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('ExtAttrs') is not None:
            temp_model = QueryTouchListResponseBodyResultDataDataExtAttrs()
            self.ext_attrs = temp_model.from_map(m['ExtAttrs'])
        return self


class QueryTouchListResponseBodyResultData(TeaModel):
    def __init__(self, total_results=None, next_page=None, current_page=None, data=None, total_page=None,
                 previous_page=None, one_page_size=None, empty=None):
        self.total_results = total_results  # type: int
        self.next_page = next_page  # type: int
        self.current_page = current_page  # type: int
        self.data = data  # type: list[QueryTouchListResponseBodyResultDataData]
        self.total_page = total_page  # type: int
        self.previous_page = previous_page  # type: int
        self.one_page_size = one_page_size  # type: int
        self.empty = empty  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTouchListResponseBodyResultData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.previous_page is not None:
            result['PreviousPage'] = self.previous_page
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        if self.empty is not None:
            result['Empty'] = self.empty
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTouchListResponseBodyResultDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PreviousPage') is not None:
            self.previous_page = m.get('PreviousPage')
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        if m.get('Empty') is not None:
            self.empty = m.get('Empty')
        return self


class QueryTouchListResponseBody(TeaModel):
    def __init__(self, result_data=None, message=None, request_id=None, code=None, success=None):
        self.result_data = result_data  # type: QueryTouchListResponseBodyResultData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        _map = super(QueryTouchListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultData') is not None:
            temp_model = QueryTouchListResponseBodyResultData()
            self.result_data = temp_model.from_map(m['ResultData'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTouchListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTouchListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTouchListResponse, self).to_map()
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
            temp_model = QueryTouchListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHotlineInQueueRequest(TeaModel):
    def __init__(self, outer_group_id=None, outer_group_type=None):
        self.outer_group_id = outer_group_id  # type: str
        self.outer_group_type = outer_group_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHotlineInQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_group_id is not None:
            result['OuterGroupId'] = self.outer_group_id
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OuterGroupId') is not None:
            self.outer_group_id = m.get('OuterGroupId')
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        return self


class QueryHotlineInQueueResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHotlineInQueueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryHotlineInQueueResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryHotlineInQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryHotlineInQueueResponse, self).to_map()
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
            temp_model = QueryHotlineInQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishHotlineServiceRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishHotlineServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class FinishHotlineServiceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishHotlineServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class FinishHotlineServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FinishHotlineServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FinishHotlineServiceResponse, self).to_map()
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
            temp_model = FinishHotlineServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOutboundStrategiesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 bu_id=None, keyword=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.bu_id = bu_id  # type: long
        self.keyword = keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOutboundStrategiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class ListOutboundStrategiesResponseBodyOutboundStrategies(TeaModel):
    def __init__(self, status=None, success_rate=None, process=None, gmt_modified_str=None, outbound_num=None,
                 modifier_id=None, outbound_strategy_name=None, outbound_strategy_id=None, scene_name=None, creator_id=None,
                 robot_name=None, modifier_name=None, resource_allocation=None, ext_attr=None, num_type=None, bu_id=None,
                 robot_id=None, creator_name=None, department_id=None, robot_type=None, rule_code=None, gmt_create_str=None):
        self.status = status  # type: int
        self.success_rate = success_rate  # type: int
        self.process = process  # type: int
        self.gmt_modified_str = gmt_modified_str  # type: str
        self.outbound_num = outbound_num  # type: str
        self.modifier_id = modifier_id  # type: long
        self.outbound_strategy_name = outbound_strategy_name  # type: str
        self.outbound_strategy_id = outbound_strategy_id  # type: long
        self.scene_name = scene_name  # type: str
        self.creator_id = creator_id  # type: long
        self.robot_name = robot_name  # type: str
        self.modifier_name = modifier_name  # type: str
        self.resource_allocation = resource_allocation  # type: int
        self.ext_attr = ext_attr  # type: str
        self.num_type = num_type  # type: int
        self.bu_id = bu_id  # type: long
        self.robot_id = robot_id  # type: str
        self.creator_name = creator_name  # type: str
        self.department_id = department_id  # type: long
        self.robot_type = robot_type  # type: int
        self.rule_code = rule_code  # type: long
        self.gmt_create_str = gmt_create_str  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOutboundStrategiesResponseBodyOutboundStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.success_rate is not None:
            result['SuccessRate'] = self.success_rate
        if self.process is not None:
            result['Process'] = self.process
        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str
        if self.outbound_num is not None:
            result['OutboundNum'] = self.outbound_num
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.outbound_strategy_name is not None:
            result['OutboundStrategyName'] = self.outbound_strategy_name
        if self.outbound_strategy_id is not None:
            result['OutboundStrategyId'] = self.outbound_strategy_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.modifier_name is not None:
            result['ModifierName'] = self.modifier_name
        if self.resource_allocation is not None:
            result['ResourceAllocation'] = self.resource_allocation
        if self.ext_attr is not None:
            result['ExtAttr'] = self.ext_attr
        if self.num_type is not None:
            result['NumType'] = self.num_type
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        if self.rule_code is not None:
            result['RuleCode'] = self.rule_code
        if self.gmt_create_str is not None:
            result['GmtCreateStr'] = self.gmt_create_str
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessRate') is not None:
            self.success_rate = m.get('SuccessRate')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')
        if m.get('OutboundNum') is not None:
            self.outbound_num = m.get('OutboundNum')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('OutboundStrategyName') is not None:
            self.outbound_strategy_name = m.get('OutboundStrategyName')
        if m.get('OutboundStrategyId') is not None:
            self.outbound_strategy_id = m.get('OutboundStrategyId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('ModifierName') is not None:
            self.modifier_name = m.get('ModifierName')
        if m.get('ResourceAllocation') is not None:
            self.resource_allocation = m.get('ResourceAllocation')
        if m.get('ExtAttr') is not None:
            self.ext_attr = m.get('ExtAttr')
        if m.get('NumType') is not None:
            self.num_type = m.get('NumType')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        if m.get('RuleCode') is not None:
            self.rule_code = m.get('RuleCode')
        if m.get('GmtCreateStr') is not None:
            self.gmt_create_str = m.get('GmtCreateStr')
        return self


class ListOutboundStrategiesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, outbound_strategies=None, code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.outbound_strategies = outbound_strategies  # type: list[ListOutboundStrategiesResponseBodyOutboundStrategies]
        self.code = code  # type: str

    def validate(self):
        if self.outbound_strategies:
            for k in self.outbound_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOutboundStrategiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OutboundStrategies'] = []
        if self.outbound_strategies is not None:
            for k in self.outbound_strategies:
                result['OutboundStrategies'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.outbound_strategies = []
        if m.get('OutboundStrategies') is not None:
            for k in m.get('OutboundStrategies'):
                temp_model = ListOutboundStrategiesResponseBodyOutboundStrategies()
                self.outbound_strategies.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListOutboundStrategiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOutboundStrategiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOutboundStrategiesResponse, self).to_map()
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
            temp_model = ListOutboundStrategiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotlineRecordRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, call_id=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.call_id = call_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotlineRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class ListHotlineRecordResponseBodyData(TeaModel):
    def __init__(self, end_time=None, start_time=None, connection_id=None, call_id=None, url=None):
        self.end_time = end_time  # type: long
        self.start_time = start_time  # type: long
        self.connection_id = connection_id  # type: str
        self.call_id = call_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotlineRecordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListHotlineRecordResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[ListHotlineRecordResponseBodyData]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotlineRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListHotlineRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotlineRecordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHotlineRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotlineRecordResponse, self).to_map()
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
            temp_model = ListHotlineRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeQualityProjectStatusRequest(TeaModel):
    def __init__(self, instance_id=None, status=None, project_id=None):
        self.instance_id = instance_id  # type: str
        self.status = status  # type: int
        self.project_id = project_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeQualityProjectStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ChangeQualityProjectStatusResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeQualityProjectStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeQualityProjectStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangeQualityProjectStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeQualityProjectStatusResponse, self).to_map()
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
            temp_model = ChangeQualityProjectStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferCallToSkillGroupRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, skill_group_id=None, call_id=None,
                 job_id=None, connection_id=None, hold_connection_id=None, type=None, is_single_transfer=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.skill_group_id = skill_group_id  # type: long
        self.call_id = call_id  # type: str
        self.job_id = job_id  # type: str
        self.connection_id = connection_id  # type: str
        self.hold_connection_id = hold_connection_id  # type: str
        self.type = type  # type: int
        self.is_single_transfer = is_single_transfer  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferCallToSkillGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.hold_connection_id is not None:
            result['HoldConnectionId'] = self.hold_connection_id
        if self.type is not None:
            result['Type'] = self.type
        if self.is_single_transfer is not None:
            result['IsSingleTransfer'] = self.is_single_transfer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('HoldConnectionId') is not None:
            self.hold_connection_id = m.get('HoldConnectionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('IsSingleTransfer') is not None:
            self.is_single_transfer = m.get('IsSingleTransfer')
        return self


class TransferCallToSkillGroupResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferCallToSkillGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferCallToSkillGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TransferCallToSkillGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferCallToSkillGroupResponse, self).to_map()
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
            temp_model = TransferCallToSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupServiceCapabilityRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids=None, group_ids=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 技能组id列表
        self.group_ids = group_ids  # type: list[long]
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupServiceCapabilityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupServiceCapabilityShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids_shrink=None, group_ids_shrink=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupServiceCapabilityShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupServiceCapabilityResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: long
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupServiceCapabilityResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupServiceCapabilityResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetSkillGroupServiceCapabilityResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSkillGroupServiceCapabilityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupServiceCapabilityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupServiceCapabilityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSkillGroupServiceCapabilityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSkillGroupServiceCapabilityResponse, self).to_map()
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
            temp_model = GetSkillGroupServiceCapabilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSkillGroupRequest(TeaModel):
    def __init__(self, instance_id=None, skill_group_id=None, client_token=None):
        self.instance_id = instance_id  # type: str
        self.skill_group_id = skill_group_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSkillGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RemoveSkillGroupResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveSkillGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveSkillGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveSkillGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveSkillGroupResponse, self).to_map()
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
            temp_model = RemoveSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCallV2Request(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, caller=None, caller_type=None,
                 callee=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.caller = caller  # type: str
        self.caller_type = caller_type  # type: int
        self.callee = callee  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartCallV2Request, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.callee is not None:
            result['Callee'] = self.callee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        return self


class StartCallV2ResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartCallV2ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartCallV2Response(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartCallV2ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartCallV2Response, self).to_map()
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
            temp_model = StartCallV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeChatAgentStatusRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, method=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 示例id
        self.instance_id = instance_id  # type: str
        # 账户名称
        self.account_name = account_name  # type: str
        # 修改到的状态类型
        self.method = method  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeChatAgentStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class ChangeChatAgentStatusResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, data=None, code=None, success=None):
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: int
        # data
        self.data = data  # type: str
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeChatAgentStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeChatAgentStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangeChatAgentStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeChatAgentStatusResponse, self).to_map()
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
            temp_model = ChangeChatAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordDataRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 account_type=None, account_id=None, acid=None, sec_level=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.account_type = account_type  # type: str
        self.account_id = account_id  # type: str
        self.acid = acid  # type: str
        self.sec_level = sec_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.sec_level is not None:
            result['SecLevel'] = self.sec_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('SecLevel') is not None:
            self.sec_level = m.get('SecLevel')
        return self


class DescribeRecordDataResponseBody(TeaModel):
    def __init__(self, acid=None, request_id=None, message=None, oss_link=None, agent_id=None, code=None):
        self.acid = acid  # type: str
        self.request_id = request_id  # type: str
        self.message = message  # type: str
        self.oss_link = oss_link  # type: str
        self.agent_id = agent_id  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.oss_link is not None:
            result['OssLink'] = self.oss_link
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OssLink') is not None:
            self.oss_link = m.get('OssLink')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeRecordDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRecordDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRecordDataResponse, self).to_map()
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
            temp_model = DescribeRecordDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOuterAccountRequest(TeaModel):
    def __init__(self, outer_account_id=None, outer_account_type=None):
        self.outer_account_id = outer_account_id  # type: str
        self.outer_account_type = outer_account_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOuterAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id
        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')
        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')
        return self


class DeleteOuterAccountResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: bool
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteOuterAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteOuterAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteOuterAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteOuterAccountResponse, self).to_map()
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
            temp_model = DeleteOuterAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDepartmentalLatitudeAgentStatusRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids=None, exist_department_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: long
        # 当前页（默认为1）
        self.current_page = current_page  # type: long
        # 技能组分组id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 是否根据技能组分组id分组显示
        self.exist_department_grouping = exist_department_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDepartmentalLatitudeAgentStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        return self


class GetDepartmentalLatitudeAgentStatusShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids_shrink=None, exist_department_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: long
        # 当前页（默认为1）
        self.current_page = current_page  # type: long
        # 技能组分组id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 是否根据技能组分组id分组显示
        self.exist_department_grouping = exist_department_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDepartmentalLatitudeAgentStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        return self


class GetDepartmentalLatitudeAgentStatusResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 每页的数量
        self.page_size = page_size  # type: int
        # 总共记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDepartmentalLatitudeAgentStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetDepartmentalLatitudeAgentStatusResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        # 错误描述
        self.message = message  # type: str
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 数据
        self.data = data  # type: GetDepartmentalLatitudeAgentStatusResponseBodyData
        # 错误编码
        self.code = code  # type: str
        # 接口调用是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDepartmentalLatitudeAgentStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetDepartmentalLatitudeAgentStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDepartmentalLatitudeAgentStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDepartmentalLatitudeAgentStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDepartmentalLatitudeAgentStatusResponse, self).to_map()
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
            temp_model = GetDepartmentalLatitudeAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineAgentDetailRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineAgentDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetHotlineAgentDetailResponseBodyData(TeaModel):
    def __init__(self, agent_status_code=None, token=None, agent_id=None, assigned=None, rest_type=None,
                 agent_status=None, tenant_id=None):
        self.agent_status_code = agent_status_code  # type: str
        self.token = token  # type: str
        self.agent_id = agent_id  # type: long
        self.assigned = assigned  # type: bool
        self.rest_type = rest_type  # type: int
        self.agent_status = agent_status  # type: int
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineAgentDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status_code is not None:
            result['AgentStatusCode'] = self.agent_status_code
        if self.token is not None:
            result['Token'] = self.token
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.assigned is not None:
            result['Assigned'] = self.assigned
        if self.rest_type is not None:
            result['RestType'] = self.rest_type
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentStatusCode') is not None:
            self.agent_status_code = m.get('AgentStatusCode')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('Assigned') is not None:
            self.assigned = m.get('Assigned')
        if m.get('RestType') is not None:
            self.rest_type = m.get('RestType')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetHotlineAgentDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetHotlineAgentDetailResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHotlineAgentDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetHotlineAgentDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetHotlineAgentDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineAgentDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineAgentDetailResponse, self).to_map()
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
            temp_model = GetHotlineAgentDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeCallRequest(TeaModel):
    def __init__(self, outer_account_id=None, outer_account_type=None, command_code=None, calling_number=None,
                 called_number=None, ext_info=None):
        self.outer_account_id = outer_account_id  # type: str
        self.outer_account_type = outer_account_type  # type: str
        self.command_code = command_code  # type: str
        self.calling_number = calling_number  # type: str
        self.called_number = called_number  # type: str
        self.ext_info = ext_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id
        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type
        if self.command_code is not None:
            result['CommandCode'] = self.command_code
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')
        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')
        if m.get('CommandCode') is not None:
            self.command_code = m.get('CommandCode')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class MakeCallResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(MakeCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MakeCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MakeCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MakeCallResponse, self).to_map()
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
            temp_model = MakeCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchCallRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, call_id=None, job_id=None,
                 connection_id=None, hold_connection_id=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.call_id = call_id  # type: str
        self.job_id = job_id  # type: str
        self.connection_id = connection_id  # type: str
        self.hold_connection_id = hold_connection_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FetchCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.hold_connection_id is not None:
            result['HoldConnectionId'] = self.hold_connection_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('HoldConnectionId') is not None:
            self.hold_connection_id = m.get('HoldConnectionId')
        return self


class FetchCallResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(FetchCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FetchCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FetchCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FetchCallResponse, self).to_map()
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
            temp_model = FetchCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineAgentStatusRequest(TeaModel):
    def __init__(self, instance_id=None, account_name=None):
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineAgentStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetHotlineAgentStatusResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineAgentStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetHotlineAgentStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineAgentStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineAgentStatusResponse, self).to_map()
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
            temp_model = GetHotlineAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCallRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, caller=None, callee=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.caller = caller  # type: str
        self.callee = callee  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.callee is not None:
            result['Callee'] = self.callee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        return self


class StartCallResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartCallResponse, self).to_map()
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
            temp_model = StartCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityRuleTagListRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityRuleTagListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetQualityRuleTagListResponseBodyData(TeaModel):
    def __init__(self, rule_tag_id=None, rule_tag_name=None):
        self.rule_tag_id = rule_tag_id  # type: long
        self.rule_tag_name = rule_tag_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQualityRuleTagListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_tag_id is not None:
            result['RuleTagId'] = self.rule_tag_id
        if self.rule_tag_name is not None:
            result['RuleTagName'] = self.rule_tag_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleTagId') is not None:
            self.rule_tag_id = m.get('RuleTagId')
        if m.get('RuleTagName') is not None:
            self.rule_tag_name = m.get('RuleTagName')
        return self


class GetQualityRuleTagListResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetQualityRuleTagListResponseBodyData]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetQualityRuleTagListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetQualityRuleTagListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityRuleTagListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQualityRuleTagListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQualityRuleTagListResponse, self).to_map()
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
            temp_model = GetQualityRuleTagListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOutbounNumListRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOutbounNumListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetOutbounNumListResponseBodyDataNumGroup(TeaModel):
    def __init__(self, type=None, value=None, description=None):
        self.type = type  # type: int
        self.value = value  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOutbounNumListResponseBodyDataNumGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetOutbounNumListResponseBodyDataNum(TeaModel):
    def __init__(self, type=None, value=None, description=None):
        self.type = type  # type: int
        self.value = value  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOutbounNumListResponseBodyDataNum, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetOutbounNumListResponseBodyData(TeaModel):
    def __init__(self, num_group=None, num=None):
        self.num_group = num_group  # type: list[GetOutbounNumListResponseBodyDataNumGroup]
        self.num = num  # type: list[GetOutbounNumListResponseBodyDataNum]

    def validate(self):
        if self.num_group:
            for k in self.num_group:
                if k:
                    k.validate()
        if self.num:
            for k in self.num:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOutbounNumListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NumGroup'] = []
        if self.num_group is not None:
            for k in self.num_group:
                result['NumGroup'].append(k.to_map() if k else None)
        result['Num'] = []
        if self.num is not None:
            for k in self.num:
                result['Num'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.num_group = []
        if m.get('NumGroup') is not None:
            for k in m.get('NumGroup'):
                temp_model = GetOutbounNumListResponseBodyDataNumGroup()
                self.num_group.append(temp_model.from_map(k))
        self.num = []
        if m.get('Num') is not None:
            for k in m.get('Num'):
                temp_model = GetOutbounNumListResponseBodyDataNum()
                self.num.append(temp_model.from_map(k))
        return self


class GetOutbounNumListResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None, http_status_code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetOutbounNumListResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool
        self.http_status_code = http_status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOutbounNumListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetOutbounNumListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetOutbounNumListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOutbounNumListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOutbounNumListResponse, self).to_map()
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
            temp_model = GetOutbounNumListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateThirdSsoAgentRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, client_id=None, account_id=None, account_name=None,
                 display_name=None, skill_group_ids=None, role_ids=None):
        # clientToken
        self.client_token = client_token  # type: str
        # param1
        self.instance_id = instance_id  # type: str
        # param2
        self.client_id = client_id  # type: str
        # param3
        self.account_id = account_id  # type: str
        # param4
        self.account_name = account_name  # type: str
        # param5
        self.display_name = display_name  # type: str
        # param6
        self.skill_group_ids = skill_group_ids  # type: list[long]
        # param7
        self.role_ids = role_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateThirdSsoAgentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.skill_group_ids is not None:
            result['SkillGroupIds'] = self.skill_group_ids
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('SkillGroupIds') is not None:
            self.skill_group_ids = m.get('SkillGroupIds')
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')
        return self


class CreateThirdSsoAgentResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, data=None, code=None, success=None):
        # message
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # httpStatusCode
        self.http_status_code = http_status_code  # type: long
        # 新创建的坐席id
        self.data = data  # type: long
        # code
        self.code = code  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateThirdSsoAgentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateThirdSsoAgentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateThirdSsoAgentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateThirdSsoAgentResponse, self).to_map()
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
            temp_model = CreateThirdSsoAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupStatusTotalRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids=None, dep_ids=None, group_ids=None, time_latitude_type=None, exist_agent_grouping=None,
                 exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids = agent_ids  # type: list[long]
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 技能组id列表
        self.group_ids = group_ids  # type: list[long]
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupStatusTotalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupStatusTotalShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids_shrink=None, dep_ids_shrink=None, group_ids_shrink=None, time_latitude_type=None,
                 exist_agent_grouping=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink  # type: str
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink  # type: str
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupStatusTotalShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupStatusTotalResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # 总记录数
        self.total_num = total_num  # type: long
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupStatusTotalResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupStatusTotalResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 接口调用是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetSkillGroupStatusTotalResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSkillGroupStatusTotalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupStatusTotalResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupStatusTotalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSkillGroupStatusTotalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSkillGroupStatusTotalResponse, self).to_map()
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
            temp_model = GetSkillGroupStatusTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateQualityProjectsRequest(TeaModel):
    def __init__(self, project_name=None, check_freq_type=None, time_range_start=None, time_range_end=None,
                 analysis_ids=None, instance_list=None, channel_touch_type=None):
        self.project_name = project_name  # type: str
        self.check_freq_type = check_freq_type  # type: int
        self.time_range_start = time_range_start  # type: str
        self.time_range_end = time_range_end  # type: str
        self.analysis_ids = analysis_ids  # type: list[int]
        self.instance_list = instance_list  # type: list[str]
        self.channel_touch_type = channel_touch_type  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchCreateQualityProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.time_range_start is not None:
            result['TimeRangeStart'] = self.time_range_start
        if self.time_range_end is not None:
            result['TimeRangeEnd'] = self.time_range_end
        if self.analysis_ids is not None:
            result['AnalysisIds'] = self.analysis_ids
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        if self.channel_touch_type is not None:
            result['ChannelTouchType'] = self.channel_touch_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')
        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')
        if m.get('AnalysisIds') is not None:
            self.analysis_ids = m.get('AnalysisIds')
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        if m.get('ChannelTouchType') is not None:
            self.channel_touch_type = m.get('ChannelTouchType')
        return self


class BatchCreateQualityProjectsResponseBodyData(TeaModel):
    def __init__(self, version=None, project_id=None, instance_id=None):
        self.version = version  # type: int
        self.project_id = project_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchCreateQualityProjectsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class BatchCreateQualityProjectsResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: list[BatchCreateQualityProjectsResponseBodyData]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchCreateQualityProjectsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = BatchCreateQualityProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchCreateQualityProjectsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchCreateQualityProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchCreateQualityProjectsResponse, self).to_map()
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
            temp_model = BatchCreateQualityProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTaskDetailRequest(TeaModel):
    def __init__(self, outbound_task_id=None, call_infos=None, instance_id=None):
        self.outbound_task_id = outbound_task_id  # type: long
        self.call_infos = call_infos  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTaskDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.call_infos is not None:
            result['CallInfos'] = self.call_infos
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('CallInfos') is not None:
            self.call_infos = m.get('CallInfos')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class InsertTaskDetailResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertTaskDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertTaskDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InsertTaskDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertTaskDetailResponse, self).to_map()
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
            temp_model = InsertTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSkillGroupRequest(TeaModel):
    def __init__(self, instance_id=None, skill_group_id=None, skill_group_name=None, description=None,
                 display_name=None, client_token=None):
        self.instance_id = instance_id  # type: str
        self.skill_group_id = skill_group_id  # type: long
        self.skill_group_name = skill_group_name  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSkillGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateSkillGroupResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSkillGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSkillGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSkillGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSkillGroupResponse, self).to_map()
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
            temp_model = UpdateSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HotlineSessionQueryRequest(TeaModel):
    def __init__(self, instance_id=None, acid=None, call_type=None, called_number=None, calling_number=None,
                 group_id=None, group_name=None, member_id=None, member_name=None, query_end_time=None,
                 query_start_time=None, request_id=None, servicer_name=None, servicer_id=None, params=None, page_size=None,
                 page_no=None, call_result=None, id=None, acid_list=None, call_type_list=None, group_id_list=None,
                 calling_number_list=None, called_number_list=None, member_id_list=None, servicer_id_list=None, call_result_list=None):
        self.instance_id = instance_id  # type: str
        self.acid = acid  # type: str
        self.call_type = call_type  # type: int
        self.called_number = called_number  # type: str
        self.calling_number = calling_number  # type: str
        self.group_id = group_id  # type: long
        self.group_name = group_name  # type: str
        self.member_id = member_id  # type: str
        self.member_name = member_name  # type: str
        self.query_end_time = query_end_time  # type: long
        self.query_start_time = query_start_time  # type: long
        self.request_id = request_id  # type: str
        self.servicer_name = servicer_name  # type: str
        self.servicer_id = servicer_id  # type: str
        self.params = params  # type: str
        self.page_size = page_size  # type: int
        self.page_no = page_no  # type: int
        self.call_result = call_result  # type: str
        self.id = id  # type: str
        self.acid_list = acid_list  # type: list[str]
        self.call_type_list = call_type_list  # type: list[int]
        self.group_id_list = group_id_list  # type: list[int]
        self.calling_number_list = calling_number_list  # type: list[str]
        self.called_number_list = called_number_list  # type: list[str]
        self.member_id_list = member_id_list  # type: list[str]
        self.servicer_id_list = servicer_id_list  # type: list[str]
        self.call_result_list = call_result_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(HotlineSessionQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.query_end_time is not None:
            result['QueryEndTime'] = self.query_end_time
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.params is not None:
            result['Params'] = self.params
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.id is not None:
            result['Id'] = self.id
        if self.acid_list is not None:
            result['AcidList'] = self.acid_list
        if self.call_type_list is not None:
            result['CallTypeList'] = self.call_type_list
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list
        if self.calling_number_list is not None:
            result['CallingNumberList'] = self.calling_number_list
        if self.called_number_list is not None:
            result['CalledNumberList'] = self.called_number_list
        if self.member_id_list is not None:
            result['MemberIdList'] = self.member_id_list
        if self.servicer_id_list is not None:
            result['ServicerIdList'] = self.servicer_id_list
        if self.call_result_list is not None:
            result['CallResultList'] = self.call_result_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('QueryEndTime') is not None:
            self.query_end_time = m.get('QueryEndTime')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AcidList') is not None:
            self.acid_list = m.get('AcidList')
        if m.get('CallTypeList') is not None:
            self.call_type_list = m.get('CallTypeList')
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')
        if m.get('CallingNumberList') is not None:
            self.calling_number_list = m.get('CallingNumberList')
        if m.get('CalledNumberList') is not None:
            self.called_number_list = m.get('CalledNumberList')
        if m.get('MemberIdList') is not None:
            self.member_id_list = m.get('MemberIdList')
        if m.get('ServicerIdList') is not None:
            self.servicer_id_list = m.get('ServicerIdList')
        if m.get('CallResultList') is not None:
            self.call_result_list = m.get('CallResultList')
        return self


class HotlineSessionQueryResponseBodyDataCallDetailRecord(TeaModel):
    def __init__(self, call_result=None, trunk_call=None, servicer_name=None, out_queue_time=None,
                 call_continue_time=None, create_time=None, pick_up_time=None, ring_continue_time=None, called_number=None,
                 servicer_id=None, hang_up_time=None, evaluation_level=None, passive_transfer_id=None, active_transfer_id=None,
                 hang_up_role=None, passive_transfer_id_type=None, member_name=None, evaluation_score=None, acid=None,
                 ring_start_time=None, call_type=None, group_name=None, group_id=None, ring_end_time=None, calling_number=None,
                 in_queue_time=None, member_id=None, id=None, queue_up_continue_time=None):
        self.call_result = call_result  # type: str
        self.trunk_call = trunk_call  # type: str
        self.servicer_name = servicer_name  # type: str
        self.out_queue_time = out_queue_time  # type: str
        self.call_continue_time = call_continue_time  # type: int
        self.create_time = create_time  # type: str
        self.pick_up_time = pick_up_time  # type: str
        self.ring_continue_time = ring_continue_time  # type: int
        self.called_number = called_number  # type: str
        self.servicer_id = servicer_id  # type: str
        self.hang_up_time = hang_up_time  # type: str
        self.evaluation_level = evaluation_level  # type: int
        self.passive_transfer_id = passive_transfer_id  # type: str
        self.active_transfer_id = active_transfer_id  # type: str
        self.hang_up_role = hang_up_role  # type: str
        self.passive_transfer_id_type = passive_transfer_id_type  # type: str
        self.member_name = member_name  # type: str
        self.evaluation_score = evaluation_score  # type: int
        self.acid = acid  # type: str
        self.ring_start_time = ring_start_time  # type: str
        self.call_type = call_type  # type: int
        self.group_name = group_name  # type: str
        self.group_id = group_id  # type: long
        self.ring_end_time = ring_end_time  # type: str
        self.calling_number = calling_number  # type: str
        self.in_queue_time = in_queue_time  # type: str
        self.member_id = member_id  # type: str
        self.id = id  # type: str
        self.queue_up_continue_time = queue_up_continue_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(HotlineSessionQueryResponseBodyDataCallDetailRecord, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.trunk_call is not None:
            result['TrunkCall'] = self.trunk_call
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.out_queue_time is not None:
            result['OutQueueTime'] = self.out_queue_time
        if self.call_continue_time is not None:
            result['CallContinueTime'] = self.call_continue_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pick_up_time is not None:
            result['PickUpTime'] = self.pick_up_time
        if self.ring_continue_time is not None:
            result['RingContinueTime'] = self.ring_continue_time
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.hang_up_time is not None:
            result['HangUpTime'] = self.hang_up_time
        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level
        if self.passive_transfer_id is not None:
            result['PassiveTransferId'] = self.passive_transfer_id
        if self.active_transfer_id is not None:
            result['ActiveTransferId'] = self.active_transfer_id
        if self.hang_up_role is not None:
            result['HangUpRole'] = self.hang_up_role
        if self.passive_transfer_id_type is not None:
            result['PassiveTransferIdType'] = self.passive_transfer_id_type
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.ring_start_time is not None:
            result['RingStartTime'] = self.ring_start_time
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.ring_end_time is not None:
            result['RingEndTime'] = self.ring_end_time
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.in_queue_time is not None:
            result['InQueueTime'] = self.in_queue_time
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.id is not None:
            result['Id'] = self.id
        if self.queue_up_continue_time is not None:
            result['QueueUpContinueTime'] = self.queue_up_continue_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('TrunkCall') is not None:
            self.trunk_call = m.get('TrunkCall')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('OutQueueTime') is not None:
            self.out_queue_time = m.get('OutQueueTime')
        if m.get('CallContinueTime') is not None:
            self.call_continue_time = m.get('CallContinueTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PickUpTime') is not None:
            self.pick_up_time = m.get('PickUpTime')
        if m.get('RingContinueTime') is not None:
            self.ring_continue_time = m.get('RingContinueTime')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('HangUpTime') is not None:
            self.hang_up_time = m.get('HangUpTime')
        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')
        if m.get('PassiveTransferId') is not None:
            self.passive_transfer_id = m.get('PassiveTransferId')
        if m.get('ActiveTransferId') is not None:
            self.active_transfer_id = m.get('ActiveTransferId')
        if m.get('HangUpRole') is not None:
            self.hang_up_role = m.get('HangUpRole')
        if m.get('PassiveTransferIdType') is not None:
            self.passive_transfer_id_type = m.get('PassiveTransferIdType')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('RingStartTime') is not None:
            self.ring_start_time = m.get('RingStartTime')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RingEndTime') is not None:
            self.ring_end_time = m.get('RingEndTime')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('InQueueTime') is not None:
            self.in_queue_time = m.get('InQueueTime')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('QueueUpContinueTime') is not None:
            self.queue_up_continue_time = m.get('QueueUpContinueTime')
        return self


class HotlineSessionQueryResponseBodyData(TeaModel):
    def __init__(self, call_detail_record=None, page_size=None, page_number=None, total_count=None):
        self.call_detail_record = call_detail_record  # type: list[HotlineSessionQueryResponseBodyDataCallDetailRecord]
        self.page_size = page_size  # type: int
        self.page_number = page_number  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.call_detail_record:
            for k in self.call_detail_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(HotlineSessionQueryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallDetailRecord'] = []
        if self.call_detail_record is not None:
            for k in self.call_detail_record:
                result['CallDetailRecord'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.call_detail_record = []
        if m.get('CallDetailRecord') is not None:
            for k in m.get('CallDetailRecord'):
                temp_model = HotlineSessionQueryResponseBodyDataCallDetailRecord()
                self.call_detail_record.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class HotlineSessionQueryResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: HotlineSessionQueryResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(HotlineSessionQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = HotlineSessionQueryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HotlineSessionQueryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HotlineSessionQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HotlineSessionQueryResponse, self).to_map()
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
            temp_model = HotlineSessionQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueueInformationRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids=None, group_ids=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 技能组id列表
        self.group_ids = group_ids  # type: list[long]
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueueInformationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetQueueInformationShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 dep_ids_shrink=None, group_ids_shrink=None, exist_department_grouping=None, exist_skill_group_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink  # type: str
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueueInformationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetQueueInformationResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: int
        # 页大小
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetQueueInformationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetQueueInformationResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetQueueInformationResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetQueueInformationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetQueueInformationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetQueueInformationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetQueueInformationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetQueueInformationResponse, self).to_map()
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
            temp_model = GetQueueInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupServiceStatusRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids=None, dep_ids=None, group_ids=None, time_latitude_type=None, exist_agent_grouping=None,
                 exist_department_grouping=None, exist_skill_group_grouping=None, exist_robot_instance_grouping=None,
                 exist_channel_instance_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 技能组id列表
        self.agent_ids = agent_ids  # type: list[long]
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 技能组id列表
        self.group_ids = group_ids  # type: list[long]
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据技能组分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool
        # 是否根据机器实例分组
        self.exist_robot_instance_grouping = exist_robot_instance_grouping  # type: bool
        # 是否根据渠道实例分组
        self.exist_channel_instance_grouping = exist_channel_instance_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupServiceStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        if self.exist_robot_instance_grouping is not None:
            result['ExistRobotInstanceGrouping'] = self.exist_robot_instance_grouping
        if self.exist_channel_instance_grouping is not None:
            result['ExistChannelInstanceGrouping'] = self.exist_channel_instance_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        if m.get('ExistRobotInstanceGrouping') is not None:
            self.exist_robot_instance_grouping = m.get('ExistRobotInstanceGrouping')
        if m.get('ExistChannelInstanceGrouping') is not None:
            self.exist_channel_instance_grouping = m.get('ExistChannelInstanceGrouping')
        return self


class GetSkillGroupServiceStatusShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids_shrink=None, dep_ids_shrink=None, group_ids_shrink=None, time_latitude_type=None,
                 exist_agent_grouping=None, exist_department_grouping=None, exist_skill_group_grouping=None,
                 exist_robot_instance_grouping=None, exist_channel_instance_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 技能组id列表
        self.agent_ids_shrink = agent_ids_shrink  # type: str
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink  # type: str
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据技能组分组
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping  # type: bool
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping  # type: bool
        # 是否根据机器实例分组
        self.exist_robot_instance_grouping = exist_robot_instance_grouping  # type: bool
        # 是否根据渠道实例分组
        self.exist_channel_instance_grouping = exist_channel_instance_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupServiceStatusShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        if self.exist_robot_instance_grouping is not None:
            result['ExistRobotInstanceGrouping'] = self.exist_robot_instance_grouping
        if self.exist_channel_instance_grouping is not None:
            result['ExistChannelInstanceGrouping'] = self.exist_channel_instance_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        if m.get('ExistRobotInstanceGrouping') is not None:
            self.exist_robot_instance_grouping = m.get('ExistRobotInstanceGrouping')
        if m.get('ExistChannelInstanceGrouping') is not None:
            self.exist_channel_instance_grouping = m.get('ExistChannelInstanceGrouping')
        return self


class GetSkillGroupServiceStatusResponseBodyData(TeaModel):
    def __init__(self, page_size=None, total_num=None, rows=None, page_num=None):
        # 页大小
        self.page_size = page_size  # type: int
        # 总记录数
        self.total_num = total_num  # type: int
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str
        # 当前页数
        self.page_num = page_num  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSkillGroupServiceStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class GetSkillGroupServiceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetSkillGroupServiceStatusResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSkillGroupServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupServiceStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSkillGroupServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSkillGroupServiceStatusResponse, self).to_map()
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
            temp_model = GetSkillGroupServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentDetailReportRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids=None, dep_ids=None, time_latitude_type=None, exist_agent_grouping=None,
                 exist_department_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids = agent_ids  # type: list[long]
        # 部门id列表
        self.dep_ids = dep_ids  # type: list[long]
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据坐席分组显示
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组显示
        self.exist_department_grouping = exist_department_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentDetailReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        return self


class GetAgentDetailReportShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, start_date=None, end_date=None, page_size=None, current_page=None,
                 agent_ids_shrink=None, dep_ids_shrink=None, time_latitude_type=None, exist_agent_grouping=None,
                 exist_department_grouping=None):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id  # type: str
        # 开始日期时间戳（毫秒）
        self.start_date = start_date  # type: long
        # 结束日期时间戳（毫秒）
        self.end_date = end_date  # type: long
        # 每页大小（默认为10)
        self.page_size = page_size  # type: int
        # 当前页（默认为1）
        self.current_page = current_page  # type: int
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink  # type: str
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink  # type: str
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type  # type: str
        # 是否根据坐席分组显示
        self.exist_agent_grouping = exist_agent_grouping  # type: bool
        # 是否根据部门分组显示
        self.exist_department_grouping = exist_department_grouping  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentDetailReportShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        return self


class GetAgentDetailReportResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_num=None, rows=None):
        # 当前页数
        self.page_num = page_num  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # 总记录数
        self.total_num = total_num  # type: long
        # 信息为list<map>类型的json字符串
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentDetailReportResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetAgentDetailReportResponseBody(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id  # type: str
        # 错误描述
        self.message = message  # type: str
        # 错误编码
        self.code = code  # type: str
        # 调用接口是否成功
        self.success = success  # type: str
        # data
        self.data = data  # type: GetAgentDetailReportResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAgentDetailReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetAgentDetailReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAgentDetailReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAgentDetailReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentDetailReportResponse, self).to_map()
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
            temp_model = GetAgentDetailReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTicketsRequest(TeaModel):
    def __init__(self, instance_id=None, case_id=None, case_type=None, case_status=None, sr_type=None,
                 task_status=None, channel_id=None, channel_type=None, touch_id=None, deal_id=None, extra=None, page_size=None,
                 current_page=None):
        self.instance_id = instance_id  # type: str
        self.case_id = case_id  # type: long
        self.case_type = case_type  # type: int
        self.case_status = case_status  # type: int
        self.sr_type = sr_type  # type: long
        self.task_status = task_status  # type: int
        self.channel_id = channel_id  # type: str
        self.channel_type = channel_type  # type: int
        self.touch_id = touch_id  # type: long
        self.deal_id = deal_id  # type: long
        self.extra = extra  # type: dict[str, any]
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTicketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.case_id is not None:
            result['CaseId'] = self.case_id
        if self.case_type is not None:
            result['CaseType'] = self.case_type
        if self.case_status is not None:
            result['CaseStatus'] = self.case_status
        if self.sr_type is not None:
            result['SrType'] = self.sr_type
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.deal_id is not None:
            result['DealId'] = self.deal_id
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')
        if m.get('CaseType') is not None:
            self.case_type = m.get('CaseType')
        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')
        if m.get('SrType') is not None:
            self.sr_type = m.get('SrType')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('DealId') is not None:
            self.deal_id = m.get('DealId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryTicketsShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, case_id=None, case_type=None, case_status=None, sr_type=None,
                 task_status=None, channel_id=None, channel_type=None, touch_id=None, deal_id=None, extra_shrink=None,
                 page_size=None, current_page=None):
        self.instance_id = instance_id  # type: str
        self.case_id = case_id  # type: long
        self.case_type = case_type  # type: int
        self.case_status = case_status  # type: int
        self.sr_type = sr_type  # type: long
        self.task_status = task_status  # type: int
        self.channel_id = channel_id  # type: str
        self.channel_type = channel_type  # type: int
        self.touch_id = touch_id  # type: long
        self.deal_id = deal_id  # type: long
        self.extra_shrink = extra_shrink  # type: str
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTicketsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.case_id is not None:
            result['CaseId'] = self.case_id
        if self.case_type is not None:
            result['CaseType'] = self.case_type
        if self.case_status is not None:
            result['CaseStatus'] = self.case_status
        if self.sr_type is not None:
            result['SrType'] = self.sr_type
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.deal_id is not None:
            result['DealId'] = self.deal_id
        if self.extra_shrink is not None:
            result['Extra'] = self.extra_shrink
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')
        if m.get('CaseType') is not None:
            self.case_type = m.get('CaseType')
        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')
        if m.get('SrType') is not None:
            self.sr_type = m.get('SrType')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('DealId') is not None:
            self.deal_id = m.get('DealId')
        if m.get('Extra') is not None:
            self.extra_shrink = m.get('Extra')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryTicketsResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTicketsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTicketsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTicketsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTicketsResponse, self).to_map()
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
            temp_model = QueryTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOutboundTaskRequest(TeaModel):
    def __init__(self, task_id=None, task_type=None, task_name=None, start_date=None, end_date=None, start_time=None,
                 end_time=None, skill_group=None, ani=None, status=None, group_name=None, department_id=None,
                 instance_id=None, page_size=None, current_page=None):
        self.task_id = task_id  # type: long
        self.task_type = task_type  # type: int
        self.task_name = task_name  # type: str
        self.start_date = start_date  # type: str
        self.end_date = end_date  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.skill_group = skill_group  # type: long
        self.ani = ani  # type: str
        self.status = status  # type: str
        self.group_name = group_name  # type: str
        self.department_id = department_id  # type: str
        self.instance_id = instance_id  # type: str
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOutboundTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.ani is not None:
            result['Ani'] = self.ani
        if self.status is not None:
            result['Status'] = self.status
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryOutboundTaskResponseBodyDataList(TeaModel):
    def __init__(self, status=None, type=None, end_date=None, retry_time=None, retry_interval=None, start_date=None,
                 gmt_modified=None, creator=None, end_time=None, start_time=None, model=None, bu_id=None, modifier=None,
                 group_name=None, description=None, department_id=None, gmt_create=None, skill_group=None, name=None,
                 ext_attrs=None, caller_num=None, id=None):
        self.status = status  # type: int
        self.type = type  # type: int
        self.end_date = end_date  # type: str
        self.retry_time = retry_time  # type: int
        self.retry_interval = retry_interval  # type: int
        self.start_date = start_date  # type: str
        self.gmt_modified = gmt_modified  # type: long
        self.creator = creator  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.model = model  # type: int
        self.bu_id = bu_id  # type: long
        self.modifier = modifier  # type: str
        self.group_name = group_name  # type: str
        self.description = description  # type: str
        self.department_id = department_id  # type: long
        self.gmt_create = gmt_create  # type: long
        self.skill_group = skill_group  # type: long
        self.name = name  # type: str
        self.ext_attrs = ext_attrs  # type: str
        self.caller_num = caller_num  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOutboundTaskResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.model is not None:
            result['Model'] = self.model
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.name is not None:
            result['Name'] = self.name
        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs
        if self.caller_num is not None:
            result['CallerNum'] = self.caller_num
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExtAttrs') is not None:
            self.ext_attrs = m.get('ExtAttrs')
        if m.get('CallerNum') is not None:
            self.caller_num = m.get('CallerNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryOutboundTaskResponseBodyData(TeaModel):
    def __init__(self, total_results=None, current_page=None, list=None, page_size=None):
        self.total_results = total_results  # type: str
        self.current_page = current_page  # type: str
        self.list = list  # type: list[QueryOutboundTaskResponseBodyDataList]
        self.page_size = page_size  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryOutboundTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryOutboundTaskResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryOutboundTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, http_status_code=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.http_status_code = http_status_code  # type: str
        self.data = data  # type: QueryOutboundTaskResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryOutboundTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = QueryOutboundTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOutboundTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryOutboundTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOutboundTaskResponse, self).to_map()
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
            temp_model = QueryOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinThirdCallRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, account_name=None, call_id=None, job_id=None,
                 connection_id=None, hold_connection_id=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.account_name = account_name  # type: str
        self.call_id = call_id  # type: str
        self.job_id = job_id  # type: str
        self.connection_id = connection_id  # type: str
        self.hold_connection_id = hold_connection_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JoinThirdCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.hold_connection_id is not None:
            result['HoldConnectionId'] = self.hold_connection_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('HoldConnectionId') is not None:
            self.hold_connection_id = m.get('HoldConnectionId')
        return self


class JoinThirdCallResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(JoinThirdCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class JoinThirdCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: JoinThirdCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(JoinThirdCallResponse, self).to_map()
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
            temp_model = JoinThirdCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSkillGroupRequest(TeaModel):
    def __init__(self, instance_id=None, skill_group_name=None, description=None, display_name=None,
                 channel_type=None, client_token=None):
        self.instance_id = instance_id  # type: str
        self.skill_group_name = skill_group_name  # type: str
        self.description = description  # type: str
        self.display_name = display_name  # type: str
        self.channel_type = channel_type  # type: int
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSkillGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSkillGroupResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: long
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSkillGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSkillGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSkillGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSkillGroupResponse, self).to_map()
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
            temp_model = CreateSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartOutboundTaskRequest(TeaModel):
    def __init__(self, outbound_task_id=None, instance_id=None):
        self.outbound_task_id = outbound_task_id  # type: long
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartOutboundTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RestartOutboundTaskResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartOutboundTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartOutboundTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestartOutboundTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartOutboundTaskResponse, self).to_map()
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
            temp_model = RestartOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


