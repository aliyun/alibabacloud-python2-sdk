# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddLogMaskConfigRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mask_name=None, mask_regex=None, mask_txt=None,
                 mask_description=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mask_name = mask_name  # type: str
        self.mask_regex = mask_regex  # type: str
        self.mask_txt = mask_txt  # type: str
        self.mask_description = mask_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddLogMaskConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_name is not None:
            result['MaskName'] = self.mask_name
        if self.mask_regex is not None:
            result['MaskRegex'] = self.mask_regex
        if self.mask_txt is not None:
            result['MaskTxt'] = self.mask_txt
        if self.mask_description is not None:
            result['MaskDescription'] = self.mask_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskName') is not None:
            self.mask_name = m.get('MaskName')
        if m.get('MaskRegex') is not None:
            self.mask_regex = m.get('MaskRegex')
        if m.get('MaskTxt') is not None:
            self.mask_txt = m.get('MaskTxt')
        if m.get('MaskDescription') is not None:
            self.mask_description = m.get('MaskDescription')
        return self


class AddLogMaskConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddLogMaskConfigResponseBody, self).to_map()
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


class AddLogMaskConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddLogMaskConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddLogMaskConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddLogMaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateDbToRuleRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, rule_ids=None, rule_db_relations=None, oper_type=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.rule_ids = rule_ids  # type: str
        self.rule_db_relations = rule_db_relations  # type: str
        self.oper_type = oper_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateDbToRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        if self.rule_db_relations is not None:
            result['RuleDbRelations'] = self.rule_db_relations
        if self.oper_type is not None:
            result['OperType'] = self.oper_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        if m.get('RuleDbRelations') is not None:
            self.rule_db_relations = m.get('RuleDbRelations')
        if m.get('OperType') is not None:
            self.oper_type = m.get('OperType')
        return self


class AssociateDbToRuleResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateDbToRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateDbToRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssociateDbToRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateDbToRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociateDbToRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateRuleToDbRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, json_param=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.json_param = json_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateRuleToDbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class AssociateRuleToDbResponseBodyServerData(TeaModel):
    def __init__(self, json_result=None):
        self.json_result = json_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateRuleToDbResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class AssociateRuleToDbResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: AssociateRuleToDbResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(AssociateRuleToDbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = AssociateRuleToDbResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class AssociateRuleToDbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AssociateRuleToDbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateRuleToDbResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociateRuleToDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeAgentStatusRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, agent_id=None, agent_status=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.agent_id = agent_id  # type: str
        self.agent_status = agent_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeAgentStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        return self


class ChangeAgentStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeAgentStatusResponseBody, self).to_map()
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


class ChangeAgentStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangeAgentStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeAgentStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangeAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeLogMaskConfigStateRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mask_id=None, mask_state=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mask_id = mask_id  # type: int
        self.mask_state = mask_state  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeLogMaskConfigStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id is not None:
            result['MaskId'] = self.mask_id
        if self.mask_state is not None:
            result['MaskState'] = self.mask_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskId') is not None:
            self.mask_id = m.get('MaskId')
        if m.get('MaskState') is not None:
            self.mask_state = m.get('MaskState')
        return self


class ChangeLogMaskConfigStateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeLogMaskConfigStateResponseBody, self).to_map()
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


class ChangeLogMaskConfigStateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangeLogMaskConfigStateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeLogMaskConfigStateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangeLogMaskConfigStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeRulePriorityRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, rule_infos=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: str
        self.rule_infos = rule_infos  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeRulePriorityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_infos is not None:
            result['RuleInfos'] = self.rule_infos
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleInfos') is not None:
            self.rule_infos = m.get('RuleInfos')
        return self


class ChangeRulePriorityResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeRulePriorityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeRulePriorityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangeRulePriorityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeRulePriorityResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangeRulePriorityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeRuleStatusRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, json_param=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.json_param = json_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeRuleStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class ChangeRuleStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeRuleStatusResponseBody, self).to_map()
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


class ChangeRuleStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangeRuleStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeRuleStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangeRuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMailRegisteredRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mail=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mail = mail  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckMailRegisteredRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mail is not None:
            result['Mail'] = self.mail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        return self


class CheckMailRegisteredResponseBody(TeaModel):
    def __init__(self, registered=None, request_id=None):
        self.registered = registered  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckMailRegisteredResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registered is not None:
            result['Registered'] = self.registered
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Registered') is not None:
            self.registered = m.get('Registered')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckMailRegisteredResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckMailRegisteredResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckMailRegisteredResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckMailRegisteredResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearAgentRecordsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, agent_ids=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.agent_ids = agent_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearAgentRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        return self


class ClearAgentRecordsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearAgentRecordsResponseBody, self).to_map()
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


class ClearAgentRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ClearAgentRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClearAgentRecordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ClearAgentRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceNetworkRequest(TeaModel):
    def __init__(self, instance_id=None, public_access_control=None, region_id=None, private_white_list=None,
                 public_white_list=None, security_group_ids=None):
        self.instance_id = instance_id  # type: str
        self.public_access_control = public_access_control  # type: int
        self.region_id = region_id  # type: str
        self.private_white_list = private_white_list  # type: list[str]
        self.public_white_list = public_white_list  # type: list[str]
        self.security_group_ids = security_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigInstanceNetworkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_access_control is not None:
            result['PublicAccessControl'] = self.public_access_control
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.private_white_list is not None:
            result['PrivateWhiteList'] = self.private_white_list
        if self.public_white_list is not None:
            result['PublicWhiteList'] = self.public_white_list
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicAccessControl') is not None:
            self.public_access_control = m.get('PublicAccessControl')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PrivateWhiteList') is not None:
            self.private_white_list = m.get('PrivateWhiteList')
        if m.get('PublicWhiteList') is not None:
            self.public_white_list = m.get('PublicWhiteList')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class ConfigInstanceNetworkResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigInstanceNetworkResponseBody, self).to_map()
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


class ConfigInstanceNetworkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConfigInstanceNetworkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigInstanceNetworkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigInstanceNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSourceRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_name=None, db_instance_id=None, asset_type=None,
                 db_type=None, db_version=None, db_certificate=None, db_username=None, db_password=None, db_addresses=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_name = db_name  # type: str
        self.db_instance_id = db_instance_id  # type: str
        self.asset_type = asset_type  # type: int
        self.db_type = db_type  # type: int
        self.db_version = db_version  # type: int
        self.db_certificate = db_certificate  # type: str
        self.db_username = db_username  # type: str
        self.db_password = db_password  # type: str
        self.db_addresses = db_addresses  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.db_certificate is not None:
            result['DbCertificate'] = self.db_certificate
        if self.db_username is not None:
            result['DbUsername'] = self.db_username
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DbCertificate') is not None:
            self.db_certificate = m.get('DbCertificate')
        if m.get('DbUsername') is not None:
            self.db_username = m.get('DbUsername')
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')
        return self


class CreateDataSourceResponseBody(TeaModel):
    def __init__(self, db_id=None, request_id=None):
        self.db_id = db_id  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDataSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDataSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGradeProtectionReportRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGradeProtectionReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class CreateGradeProtectionReportResponseBodyServerData(TeaModel):
    def __init__(self, file_name=None):
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGradeProtectionReportResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreateGradeProtectionReportResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: CreateGradeProtectionReportResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(CreateGradeProtectionReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreateGradeProtectionReportResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreateGradeProtectionReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGradeProtectionReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGradeProtectionReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGradeProtectionReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntegratedReportRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntegratedReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class CreateIntegratedReportResponseBodyServerData(TeaModel):
    def __init__(self, file_name=None):
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntegratedReportResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreateIntegratedReportResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: CreateIntegratedReportResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(CreateIntegratedReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreateIntegratedReportResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreateIntegratedReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIntegratedReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntegratedReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIntegratedReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogAlarmTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, task_name=None, to_mail_list=None, db_id_list=None,
                 risk_level_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_name = task_name  # type: str
        self.to_mail_list = to_mail_list  # type: list[str]
        self.db_id_list = db_id_list  # type: list[str]
        self.risk_level_list = risk_level_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogAlarmTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        if self.db_id_list is not None:
            result['DbIdList'] = self.db_id_list
        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        if m.get('DbIdList') is not None:
            self.db_id_list = m.get('DbIdList')
        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')
        return self


class CreateLogAlarmTaskResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogAlarmTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLogAlarmTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateLogAlarmTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLogAlarmTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLogAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePCIReportRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePCIReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class CreatePCIReportResponseBodyServerData(TeaModel):
    def __init__(self, file_name=None):
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePCIReportResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreatePCIReportResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: CreatePCIReportResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(CreatePCIReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreatePCIReportResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreatePCIReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreatePCIReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePCIReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePCIReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReportPushTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, schedule_type=None, schedule_time=None, job_status=None,
                 report_type=None, db_list=None, email_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.schedule_type = schedule_type  # type: str
        self.schedule_time = schedule_time  # type: str
        self.job_status = job_status  # type: int
        self.report_type = report_type  # type: list[str]
        self.db_list = db_list  # type: list[str]
        self.email_list = email_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReportPushTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.email_list is not None:
            result['EmailList'] = self.email_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('EmailList') is not None:
            self.email_list = m.get('EmailList')
        return self


class CreateReportPushTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReportPushTaskResponseBody, self).to_map()
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


class CreateReportPushTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateReportPushTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateReportPushTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateReportPushTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, rule_info=None, rule_db_relation=None, rule_group=None,
                 effect_current_dbstatus=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.rule_info = rule_info  # type: str
        self.rule_db_relation = rule_db_relation  # type: str
        self.rule_group = rule_group  # type: str
        self.effect_current_dbstatus = effect_current_dbstatus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_info is not None:
            result['RuleInfo'] = self.rule_info
        if self.rule_db_relation is not None:
            result['RuleDbRelation'] = self.rule_db_relation
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.effect_current_dbstatus is not None:
            result['EffectCurrentDBStatus'] = self.effect_current_dbstatus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleInfo') is not None:
            self.rule_info = m.get('RuleInfo')
        if m.get('RuleDbRelation') is not None:
            self.rule_db_relation = m.get('RuleDbRelation')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('EffectCurrentDBStatus') is not None:
            self.effect_current_dbstatus = m.get('EffectCurrentDBStatus')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleGroupRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, group_name=None, group_type=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.group_name = group_name  # type: str
        self.group_type = group_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        return self


class CreateRuleGroupResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRuleGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRuleGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRuleGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRuleGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSOXReportRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSOXReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class CreateSOXReportResponseBodyServerData(TeaModel):
    def __init__(self, file_name=None):
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSOXReportResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreateSOXReportResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: CreateSOXReportResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(CreateSOXReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreateSOXReportResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreateSOXReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSOXReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSOXReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSOXReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSqlRuleRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, json_param=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.json_param = json_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSqlRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class CreateSqlRuleResponseBodyServerData(TeaModel):
    def __init__(self, json_result=None):
        self.json_result = json_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSqlRuleResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class CreateSqlRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: CreateSqlRuleResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(CreateSqlRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreateSqlRuleResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreateSqlRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSqlRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSqlRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSqlRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSystemAlarmTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, task_name=None, to_mail_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_name = task_name  # type: str
        self.to_mail_list = to_mail_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSystemAlarmTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        return self


class CreateSystemAlarmTaskResponseBody(TeaModel):
    def __init__(self, task_id=None, request_id=None):
        self.task_id = task_id  # type: int
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSystemAlarmTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSystemAlarmTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSystemAlarmTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSystemAlarmTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSystemAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, task_ids=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class DeleteAlarmTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAlarmTaskResponseBody, self).to_map()
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


class DeleteAlarmTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteAlarmTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAlarmTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_ids=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_ids = db_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_ids is not None:
            result['DbIds'] = self.db_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbIds') is not None:
            self.db_ids = m.get('DbIds')
        return self


class DeleteDataSourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDataSourceResponseBody, self).to_map()
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


class DeleteDataSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDataSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReportPushTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, job_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.job_id = job_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReportPushTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteReportPushTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReportPushTaskResponseBody, self).to_map()
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


class DeleteReportPushTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteReportPushTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteReportPushTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteReportPushTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, rule_id=None, rule_type=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.rule_id = rule_id  # type: str
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleGroupRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, group_key_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.group_key_id = group_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRuleGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_key_id is not None:
            result['GroupKeyId'] = self.group_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupKeyId') is not None:
            self.group_key_id = m.get('GroupKeyId')
        return self


class DeleteRuleGroupResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRuleGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRuleGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRuleGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRuleGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterTemplatesFromRuleRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, sentence_param=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.sentence_param = sentence_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterTemplatesFromRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sentence_param is not None:
            result['SentenceParam'] = self.sentence_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SentenceParam') is not None:
            self.sentence_param = m.get('SentenceParam')
        return self


class DeregisterTemplatesFromRuleResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeregisterTemplatesFromRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeregisterTemplatesFromRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeregisterTemplatesFromRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeregisterTemplatesFromRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeregisterTemplatesFromRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAttributeResponseBodyInstanceAttribute(TeaModel):
    def __init__(self, vpc_id=None, vswitch_id=None, internet_ip=None, network_type=None, image_version_name=None,
                 series_code=None, description=None, access_type=None, ecs_status=None, operatable=None,
                 plan_upgrade_status=None, expire_time=None, upgradeable=None, instance_id=None, internet_endpoint=None,
                 intranet_ip=None, renewable=None, region_id=None, intranet_endpoint=None, start_time=None, upgrade_status=None,
                 plan_upgradeable=None, instance_status=None, license_code=None, public_access_control=None, public_white_list=None,
                 security_group_ids=None, private_white_list=None):
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.internet_ip = internet_ip  # type: str
        self.network_type = network_type  # type: str
        self.image_version_name = image_version_name  # type: str
        self.series_code = series_code  # type: str
        self.description = description  # type: str
        self.access_type = access_type  # type: int
        self.ecs_status = ecs_status  # type: str
        self.operatable = operatable  # type: bool
        self.plan_upgrade_status = plan_upgrade_status  # type: int
        self.expire_time = expire_time  # type: long
        self.upgradeable = upgradeable  # type: bool
        self.instance_id = instance_id  # type: str
        self.internet_endpoint = internet_endpoint  # type: str
        self.intranet_ip = intranet_ip  # type: str
        self.renewable = renewable  # type: bool
        self.region_id = region_id  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.start_time = start_time  # type: long
        self.upgrade_status = upgrade_status  # type: int
        self.plan_upgradeable = plan_upgradeable  # type: bool
        self.instance_status = instance_status  # type: str
        self.license_code = license_code  # type: str
        self.public_access_control = public_access_control  # type: int
        self.public_white_list = public_white_list  # type: list[str]
        self.security_group_ids = security_group_ids  # type: list[str]
        self.private_white_list = private_white_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBodyInstanceAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.image_version_name is not None:
            result['ImageVersionName'] = self.image_version_name
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.ecs_status is not None:
            result['EcsStatus'] = self.ecs_status
        if self.operatable is not None:
            result['Operatable'] = self.operatable
        if self.plan_upgrade_status is not None:
            result['PlanUpgradeStatus'] = self.plan_upgrade_status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.upgradeable is not None:
            result['Upgradeable'] = self.upgradeable
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.renewable is not None:
            result['Renewable'] = self.renewable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status
        if self.plan_upgradeable is not None:
            result['PlanUpgradeable'] = self.plan_upgradeable
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_access_control is not None:
            result['PublicAccessControl'] = self.public_access_control
        if self.public_white_list is not None:
            result['PublicWhiteList'] = self.public_white_list
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.private_white_list is not None:
            result['PrivateWhiteList'] = self.private_white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ImageVersionName') is not None:
            self.image_version_name = m.get('ImageVersionName')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('EcsStatus') is not None:
            self.ecs_status = m.get('EcsStatus')
        if m.get('Operatable') is not None:
            self.operatable = m.get('Operatable')
        if m.get('PlanUpgradeStatus') is not None:
            self.plan_upgrade_status = m.get('PlanUpgradeStatus')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Upgradeable') is not None:
            self.upgradeable = m.get('Upgradeable')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Renewable') is not None:
            self.renewable = m.get('Renewable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')
        if m.get('PlanUpgradeable') is not None:
            self.plan_upgradeable = m.get('PlanUpgradeable')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicAccessControl') is not None:
            self.public_access_control = m.get('PublicAccessControl')
        if m.get('PublicWhiteList') is not None:
            self.public_white_list = m.get('PublicWhiteList')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('PrivateWhiteList') is not None:
            self.private_white_list = m.get('PrivateWhiteList')
        return self


class DescribeInstanceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_attribute=None):
        self.request_id = request_id  # type: str
        self.instance_attribute = instance_attribute  # type: DescribeInstanceAttributeResponseBodyInstanceAttribute

    def validate(self):
        if self.instance_attribute:
            self.instance_attribute.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_attribute is not None:
            result['InstanceAttribute'] = self.instance_attribute.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceAttribute') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstanceAttribute()
            self.instance_attribute = temp_model.from_map(m['InstanceAttribute'])
        return self


class DescribeInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequestTag, self).to_map()
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


class DescribeInstancesRequest(TeaModel):
    def __init__(self, instance_status=None, region_id=None, page_no=None, current_page=None, page_size=None,
                 resource_group_id=None, instance_id=None, tag=None):
        self.instance_status = instance_status  # type: str
        self.region_id = region_id  # type: str
        self.page_no = page_no  # type: int
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.instance_id = instance_id  # type: list[str]
        self.tag = tag  # type: list[DescribeInstancesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(self, vpc_id=None, vswitch_id=None, internet_ip=None, network_type=None, image_version_name=None,
                 series_code=None, description=None, ecs_status=None, operatable=None, plan_upgrade_status=None,
                 expire_time=None, upgradeable=None, legacy=None, instance_id=None, internet_endpoint=None, intranet_ip=None,
                 renewable=None, region_id=None, intranet_endpoint=None, start_time=None, upgrade_status=None,
                 plan_upgradeable=None, instance_status=None, license_code=None):
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.internet_ip = internet_ip  # type: str
        self.network_type = network_type  # type: str
        self.image_version_name = image_version_name  # type: str
        self.series_code = series_code  # type: str
        self.description = description  # type: str
        self.ecs_status = ecs_status  # type: str
        self.operatable = operatable  # type: bool
        self.plan_upgrade_status = plan_upgrade_status  # type: int
        self.expire_time = expire_time  # type: long
        self.upgradeable = upgradeable  # type: bool
        self.legacy = legacy  # type: bool
        self.instance_id = instance_id  # type: str
        self.internet_endpoint = internet_endpoint  # type: str
        self.intranet_ip = intranet_ip  # type: str
        self.renewable = renewable  # type: bool
        self.region_id = region_id  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.start_time = start_time  # type: long
        self.upgrade_status = upgrade_status  # type: int
        self.plan_upgradeable = plan_upgradeable  # type: bool
        self.instance_status = instance_status  # type: str
        self.license_code = license_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.image_version_name is not None:
            result['ImageVersionName'] = self.image_version_name
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_status is not None:
            result['EcsStatus'] = self.ecs_status
        if self.operatable is not None:
            result['Operatable'] = self.operatable
        if self.plan_upgrade_status is not None:
            result['PlanUpgradeStatus'] = self.plan_upgrade_status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.upgradeable is not None:
            result['Upgradeable'] = self.upgradeable
        if self.legacy is not None:
            result['Legacy'] = self.legacy
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.renewable is not None:
            result['Renewable'] = self.renewable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status
        if self.plan_upgradeable is not None:
            result['PlanUpgradeable'] = self.plan_upgradeable
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ImageVersionName') is not None:
            self.image_version_name = m.get('ImageVersionName')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsStatus') is not None:
            self.ecs_status = m.get('EcsStatus')
        if m.get('Operatable') is not None:
            self.operatable = m.get('Operatable')
        if m.get('PlanUpgradeStatus') is not None:
            self.plan_upgrade_status = m.get('PlanUpgradeStatus')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Upgradeable') is not None:
            self.upgradeable = m.get('Upgradeable')
        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Renewable') is not None:
            self.renewable = m.get('Renewable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')
        if m.get('PlanUpgradeable') is not None:
            self.plan_upgradeable = m.get('PlanUpgradeable')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, instances=None):
        self.total_count = total_count  # type: long
        self.request_id = request_id  # type: str
        self.instances = instances  # type: list[DescribeInstancesResponseBodyInstances]

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoginTicketRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLoginTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeLoginTicketResponseBodyLoginTicketZones(TeaModel):
    def __init__(self, zone_id=None, local_name=None):
        self.zone_id = zone_id  # type: str
        self.local_name = local_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLoginTicketResponseBodyLoginTicketZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        return self


class DescribeLoginTicketResponseBodyLoginTicket(TeaModel):
    def __init__(self, ticket=None, certificate=None, zones=None):
        self.ticket = ticket  # type: str
        self.certificate = certificate  # type: str
        self.zones = zones  # type: list[DescribeLoginTicketResponseBodyLoginTicketZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeLoginTicketResponseBodyLoginTicket, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeLoginTicketResponseBodyLoginTicketZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeLoginTicketResponseBody(TeaModel):
    def __init__(self, request_id=None, login_ticket=None):
        self.request_id = request_id  # type: str
        self.login_ticket = login_ticket  # type: DescribeLoginTicketResponseBodyLoginTicket

    def validate(self):
        if self.login_ticket:
            self.login_ticket.validate()

    def to_map(self):
        _map = super(DescribeLoginTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_ticket is not None:
            result['LoginTicket'] = self.login_ticket.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoginTicket') is not None:
            temp_model = DescribeLoginTicketResponseBodyLoginTicket()
            self.login_ticket = temp_model.from_map(m['LoginTicket'])
        return self


class DescribeLoginTicketResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeLoginTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLoginTicketResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLoginTicketResponseBody()
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


class DescribeSyncInfoRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSyncInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeSyncInfoResponseBodyInstanceInfo(TeaModel):
    def __init__(self, status=None, vswitch_id=None, region_no=None, ecs_instance_id=None, image_version_name=None,
                 plan_code=None, ecs_uuid=None, access_type=None, ecs_status=None, plan_upgrade_status=None, zone_no=None,
                 aliuid=None, product_name=None, ecs_eip=None, expire_time=None, ecs_internet_ip=None, instance_id=None,
                 renewable=None, ecs_intranet_ip=None, start_time=None, region_name=None, upgrade_status=None,
                 plan_upgradeable=None, custom_name=None, ecs_network_type=None, public_access_control=None, vendor_code=None,
                 plan_name=None, product_code=None):
        self.status = status  # type: int
        self.vswitch_id = vswitch_id  # type: str
        self.region_no = region_no  # type: str
        self.ecs_instance_id = ecs_instance_id  # type: str
        self.image_version_name = image_version_name  # type: str
        self.plan_code = plan_code  # type: str
        self.ecs_uuid = ecs_uuid  # type: str
        self.access_type = access_type  # type: int
        self.ecs_status = ecs_status  # type: str
        self.plan_upgrade_status = plan_upgrade_status  # type: int
        self.zone_no = zone_no  # type: str
        self.aliuid = aliuid  # type: long
        self.product_name = product_name  # type: str
        self.ecs_eip = ecs_eip  # type: str
        self.expire_time = expire_time  # type: long
        self.ecs_internet_ip = ecs_internet_ip  # type: str
        self.instance_id = instance_id  # type: str
        self.renewable = renewable  # type: bool
        self.ecs_intranet_ip = ecs_intranet_ip  # type: str
        self.start_time = start_time  # type: long
        self.region_name = region_name  # type: str
        self.upgrade_status = upgrade_status  # type: int
        self.plan_upgradeable = plan_upgradeable  # type: str
        self.custom_name = custom_name  # type: str
        self.ecs_network_type = ecs_network_type  # type: str
        self.public_access_control = public_access_control  # type: int
        self.vendor_code = vendor_code  # type: str
        self.plan_name = plan_name  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSyncInfoResponseBodyInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.image_version_name is not None:
            result['ImageVersionName'] = self.image_version_name
        if self.plan_code is not None:
            result['PlanCode'] = self.plan_code
        if self.ecs_uuid is not None:
            result['EcsUuid'] = self.ecs_uuid
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.ecs_status is not None:
            result['EcsStatus'] = self.ecs_status
        if self.plan_upgrade_status is not None:
            result['PlanUpgradeStatus'] = self.plan_upgrade_status
        if self.zone_no is not None:
            result['ZoneNo'] = self.zone_no
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.ecs_eip is not None:
            result['EcsEip'] = self.ecs_eip
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ecs_internet_ip is not None:
            result['EcsInternetIp'] = self.ecs_internet_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renewable is not None:
            result['Renewable'] = self.renewable
        if self.ecs_intranet_ip is not None:
            result['EcsIntranetIp'] = self.ecs_intranet_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status
        if self.plan_upgradeable is not None:
            result['PlanUpgradeable'] = self.plan_upgradeable
        if self.custom_name is not None:
            result['CustomName'] = self.custom_name
        if self.ecs_network_type is not None:
            result['EcsNetworkType'] = self.ecs_network_type
        if self.public_access_control is not None:
            result['PublicAccessControl'] = self.public_access_control
        if self.vendor_code is not None:
            result['VendorCode'] = self.vendor_code
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('ImageVersionName') is not None:
            self.image_version_name = m.get('ImageVersionName')
        if m.get('PlanCode') is not None:
            self.plan_code = m.get('PlanCode')
        if m.get('EcsUuid') is not None:
            self.ecs_uuid = m.get('EcsUuid')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('EcsStatus') is not None:
            self.ecs_status = m.get('EcsStatus')
        if m.get('PlanUpgradeStatus') is not None:
            self.plan_upgrade_status = m.get('PlanUpgradeStatus')
        if m.get('ZoneNo') is not None:
            self.zone_no = m.get('ZoneNo')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('EcsEip') is not None:
            self.ecs_eip = m.get('EcsEip')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('EcsInternetIp') is not None:
            self.ecs_internet_ip = m.get('EcsInternetIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Renewable') is not None:
            self.renewable = m.get('Renewable')
        if m.get('EcsIntranetIp') is not None:
            self.ecs_intranet_ip = m.get('EcsIntranetIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')
        if m.get('PlanUpgradeable') is not None:
            self.plan_upgradeable = m.get('PlanUpgradeable')
        if m.get('CustomName') is not None:
            self.custom_name = m.get('CustomName')
        if m.get('EcsNetworkType') is not None:
            self.ecs_network_type = m.get('EcsNetworkType')
        if m.get('PublicAccessControl') is not None:
            self.public_access_control = m.get('PublicAccessControl')
        if m.get('VendorCode') is not None:
            self.vendor_code = m.get('VendorCode')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeSyncInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, instance_info=None):
        self.request_id = request_id  # type: str
        self.instance_info = instance_info  # type: DescribeSyncInfoResponseBodyInstanceInfo

    def validate(self):
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        _map = super(DescribeSyncInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceInfo') is not None:
            temp_model = DescribeSyncInfoResponseBodyInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        return self


class DescribeSyncInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSyncInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSyncInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSyncInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableLogMaskConfigsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mask_id_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mask_id_list = mask_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableLogMaskConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id_list is not None:
            result['MaskIdList'] = self.mask_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskIdList') is not None:
            self.mask_id_list = m.get('MaskIdList')
        return self


class DisableLogMaskConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableLogMaskConfigsResponseBody, self).to_map()
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


class DisableLogMaskConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableLogMaskConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableLogMaskConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableLogMaskConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateRulesFromDbRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, json_param=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.json_param = json_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateRulesFromDbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class DissociateRulesFromDbResponseBodyServerData(TeaModel):
    def __init__(self, json_result=None):
        self.json_result = json_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateRulesFromDbResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class DissociateRulesFromDbResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: DissociateRulesFromDbResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(DissociateRulesFromDbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = DissociateRulesFromDbResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class DissociateRulesFromDbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DissociateRulesFromDbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateRulesFromDbResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DissociateRulesFromDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateTemplatesFromRuleRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, json_param=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.json_param = json_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateTemplatesFromRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class DissociateTemplatesFromRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DissociateTemplatesFromRuleResponseBody, self).to_map()
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


class DissociateTemplatesFromRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DissociateTemplatesFromRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DissociateTemplatesFromRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DissociateTemplatesFromRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditLogMaskConfigRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mask_id=None, mask_name=None, mask_regex=None,
                 mask_txt=None, mask_description=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mask_id = mask_id  # type: int
        self.mask_name = mask_name  # type: str
        self.mask_regex = mask_regex  # type: str
        self.mask_txt = mask_txt  # type: str
        self.mask_description = mask_description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditLogMaskConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id is not None:
            result['MaskId'] = self.mask_id
        if self.mask_name is not None:
            result['MaskName'] = self.mask_name
        if self.mask_regex is not None:
            result['MaskRegex'] = self.mask_regex
        if self.mask_txt is not None:
            result['MaskTxt'] = self.mask_txt
        if self.mask_description is not None:
            result['MaskDescription'] = self.mask_description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskId') is not None:
            self.mask_id = m.get('MaskId')
        if m.get('MaskName') is not None:
            self.mask_name = m.get('MaskName')
        if m.get('MaskRegex') is not None:
            self.mask_regex = m.get('MaskRegex')
        if m.get('MaskTxt') is not None:
            self.mask_txt = m.get('MaskTxt')
        if m.get('MaskDescription') is not None:
            self.mask_description = m.get('MaskDescription')
        return self


class EditLogMaskConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditLogMaskConfigResponseBody, self).to_map()
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


class EditLogMaskConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EditLogMaskConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditLogMaskConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EditLogMaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableLogMaskConfigsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mask_id_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mask_id_list = mask_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableLogMaskConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id_list is not None:
            result['MaskIdList'] = self.mask_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskIdList') is not None:
            self.mask_id_list = m.get('MaskIdList')
        return self


class EnableLogMaskConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableLogMaskConfigsResponseBody, self).to_map()
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


class EnableLogMaskConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableLogMaskConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableLogMaskConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableLogMaskConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentFileUrlRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentFileUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAgentFileUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, linux_file_url=None, access_token=None, win_file_url=None):
        self.request_id = request_id  # type: str
        self.linux_file_url = linux_file_url  # type: str
        self.access_token = access_token  # type: str
        self.win_file_url = win_file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentFileUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.linux_file_url is not None:
            result['LinuxFileUrl'] = self.linux_file_url
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.win_file_url is not None:
            result['WinFileUrl'] = self.win_file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LinuxFileUrl') is not None:
            self.linux_file_url = m.get('LinuxFileUrl')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('WinFileUrl') is not None:
            self.win_file_url = m.get('WinFileUrl')
        return self


class GetAgentFileUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAgentFileUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentFileUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAgentFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentListRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, agent_ip=None, agent_status=None, agent_os=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.agent_ip = agent_ip  # type: str
        self.agent_status = agent_status  # type: int
        self.agent_os = agent_os  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_ip is not None:
            result['AgentIp'] = self.agent_ip
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.agent_os is not None:
            result['AgentOs'] = self.agent_os
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentIp') is not None:
            self.agent_ip = m.get('AgentIp')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('AgentOs') is not None:
            self.agent_os = m.get('AgentOs')
        return self


class GetAgentListResponseBodyAgentList(TeaModel):
    def __init__(self, vpc_id=None, private_ip=None, rmagent_mem=None, agent_id=None, rmagent_cpu=None,
                 first_login_time=None, agent_os=None, agent_status=None, agent_port=None, agent_version=None, send_packets=None,
                 send_bytes=None, last_active_time=None, send_packet_count=None, ecs_id=None, public_ip=None,
                 send_byte_count=None):
        self.vpc_id = vpc_id  # type: str
        self.private_ip = private_ip  # type: str
        self.rmagent_mem = rmagent_mem  # type: int
        self.agent_id = agent_id  # type: str
        self.rmagent_cpu = rmagent_cpu  # type: int
        self.first_login_time = first_login_time  # type: str
        self.agent_os = agent_os  # type: str
        self.agent_status = agent_status  # type: int
        self.agent_port = agent_port  # type: str
        self.agent_version = agent_version  # type: str
        self.send_packets = send_packets  # type: long
        self.send_bytes = send_bytes  # type: long
        self.last_active_time = last_active_time  # type: str
        self.send_packet_count = send_packet_count  # type: long
        self.ecs_id = ecs_id  # type: str
        self.public_ip = public_ip  # type: str
        self.send_byte_count = send_byte_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAgentListResponseBodyAgentList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.rmagent_mem is not None:
            result['RmagentMem'] = self.rmagent_mem
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.rmagent_cpu is not None:
            result['RmagentCpu'] = self.rmagent_cpu
        if self.first_login_time is not None:
            result['FirstLoginTime'] = self.first_login_time
        if self.agent_os is not None:
            result['AgentOs'] = self.agent_os
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.agent_port is not None:
            result['AgentPort'] = self.agent_port
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.send_packets is not None:
            result['SendPackets'] = self.send_packets
        if self.send_bytes is not None:
            result['SendBytes'] = self.send_bytes
        if self.last_active_time is not None:
            result['LastActiveTime'] = self.last_active_time
        if self.send_packet_count is not None:
            result['SendPacketCount'] = self.send_packet_count
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.send_byte_count is not None:
            result['SendByteCount'] = self.send_byte_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('RmagentMem') is not None:
            self.rmagent_mem = m.get('RmagentMem')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('RmagentCpu') is not None:
            self.rmagent_cpu = m.get('RmagentCpu')
        if m.get('FirstLoginTime') is not None:
            self.first_login_time = m.get('FirstLoginTime')
        if m.get('AgentOs') is not None:
            self.agent_os = m.get('AgentOs')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('AgentPort') is not None:
            self.agent_port = m.get('AgentPort')
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('SendPackets') is not None:
            self.send_packets = m.get('SendPackets')
        if m.get('SendBytes') is not None:
            self.send_bytes = m.get('SendBytes')
        if m.get('LastActiveTime') is not None:
            self.last_active_time = m.get('LastActiveTime')
        if m.get('SendPacketCount') is not None:
            self.send_packet_count = m.get('SendPacketCount')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('SendByteCount') is not None:
            self.send_byte_count = m.get('SendByteCount')
        return self


class GetAgentListResponseBody(TeaModel):
    def __init__(self, request_id=None, agent_list=None):
        self.request_id = request_id  # type: str
        self.agent_list = agent_list  # type: list[GetAgentListResponseBodyAgentList]

    def validate(self):
        if self.agent_list:
            for k in self.agent_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAgentListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AgentList'] = []
        if self.agent_list is not None:
            for k in self.agent_list:
                result['AgentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.agent_list = []
        if m.get('AgentList') is not None:
            for k in m.get('AgentList'):
                temp_model = GetAgentListResponseBodyAgentList()
                self.agent_list.append(temp_model.from_map(k))
        return self


class GetAgentListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAgentListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAgentListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAgentListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppointOperationRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppointOperationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAppointOperationResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppointOperationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppointOperationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAppointOperationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppointOperationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAppointOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditCountRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetAuditCountResponseBody(TeaModel):
    def __init__(self, session_count=None, sql_count=None, risk_count=None, request_id=None):
        self.session_count = session_count  # type: long
        self.sql_count = sql_count  # type: long
        self.risk_count = risk_count  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuditCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAuditCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuditCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAuditCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditCountDistributionRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditCountDistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetAuditCountDistributionResponseBodyTimeList(TeaModel):
    def __init__(self, session_count=None, begin_date=None, sql_count=None, end_date=None, risk_count=None):
        self.session_count = session_count  # type: long
        self.begin_date = begin_date  # type: str
        self.sql_count = sql_count  # type: long
        self.end_date = end_date  # type: str
        self.risk_count = risk_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuditCountDistributionResponseBodyTimeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        return self


class GetAuditCountDistributionResponseBody(TeaModel):
    def __init__(self, request_id=None, time_list=None):
        self.request_id = request_id  # type: str
        self.time_list = time_list  # type: list[GetAuditCountDistributionResponseBodyTimeList]

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAuditCountDistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetAuditCountDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetAuditCountDistributionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAuditCountDistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuditCountDistributionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAuditCountDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBaseTemplateListRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBaseTemplateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetBaseTemplateListResponseBodyTemplateList(TeaModel):
    def __init__(self, db_type_name=None, template_content=None, sql_type_name=None, template_id=None,
                 template_state=None):
        self.db_type_name = db_type_name  # type: str
        self.template_content = template_content  # type: str
        self.sql_type_name = sql_type_name  # type: str
        self.template_id = template_id  # type: str
        self.template_state = template_state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBaseTemplateListResponseBodyTemplateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.sql_type_name is not None:
            result['SqlTypeName'] = self.sql_type_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_state is not None:
            result['TemplateState'] = self.template_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('SqlTypeName') is not None:
            self.sql_type_name = m.get('SqlTypeName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateState') is not None:
            self.template_state = m.get('TemplateState')
        return self


class GetBaseTemplateListResponseBody(TeaModel):
    def __init__(self, request_id=None, template_list=None):
        self.request_id = request_id  # type: str
        self.template_list = template_list  # type: list[GetBaseTemplateListResponseBodyTemplateList]

    def validate(self):
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetBaseTemplateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TemplateList'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['TemplateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_list = []
        if m.get('TemplateList') is not None:
            for k in m.get('TemplateList'):
                temp_model = GetBaseTemplateListResponseBodyTemplateList()
                self.template_list.append(temp_model.from_map(k))
        return self


class GetBaseTemplateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBaseTemplateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBaseTemplateListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetBaseTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDasUsageRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDasUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDasUsageResponseBodyAuditAssetDbTypes(TeaModel):
    def __init__(self, db_type=None, db_count=None):
        self.db_type = db_type  # type: str
        self.db_count = db_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDasUsageResponseBodyAuditAssetDbTypes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_count is not None:
            result['DbCount'] = self.db_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbCount') is not None:
            self.db_count = m.get('DbCount')
        return self


class GetDasUsageResponseBodyAuditAsset(TeaModel):
    def __init__(self, db_count=None, db_types=None):
        self.db_count = db_count  # type: int
        self.db_types = db_types  # type: list[GetDasUsageResponseBodyAuditAssetDbTypes]

    def validate(self):
        if self.db_types:
            for k in self.db_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDasUsageResponseBodyAuditAsset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_count is not None:
            result['DbCount'] = self.db_count
        result['DbTypes'] = []
        if self.db_types is not None:
            for k in self.db_types:
                result['DbTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbCount') is not None:
            self.db_count = m.get('DbCount')
        self.db_types = []
        if m.get('DbTypes') is not None:
            for k in m.get('DbTypes'):
                temp_model = GetDasUsageResponseBodyAuditAssetDbTypes()
                self.db_types.append(temp_model.from_map(k))
        return self


class GetDasUsageResponseBodyConsoleAccess(TeaModel):
    def __init__(self, last_access_time=None, day_90access_count=None, day_15access_count=None,
                 day_30access_count=None, day_180access_count=None):
        self.last_access_time = last_access_time  # type: str
        self.day_90access_count = day_90access_count  # type: int
        self.day_15access_count = day_15access_count  # type: int
        self.day_30access_count = day_30access_count  # type: int
        self.day_180access_count = day_180access_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDasUsageResponseBodyConsoleAccess, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.day_90access_count is not None:
            result['Day90AccessCount'] = self.day_90access_count
        if self.day_15access_count is not None:
            result['Day15AccessCount'] = self.day_15access_count
        if self.day_30access_count is not None:
            result['Day30AccessCount'] = self.day_30access_count
        if self.day_180access_count is not None:
            result['Day180AccessCount'] = self.day_180access_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('Day90AccessCount') is not None:
            self.day_90access_count = m.get('Day90AccessCount')
        if m.get('Day15AccessCount') is not None:
            self.day_15access_count = m.get('Day15AccessCount')
        if m.get('Day30AccessCount') is not None:
            self.day_30access_count = m.get('Day30AccessCount')
        if m.get('Day180AccessCount') is not None:
            self.day_180access_count = m.get('Day180AccessCount')
        return self


class GetDasUsageResponseBodyAgent(TeaModel):
    def __init__(self, has_flow=None, inst_state=None, active_count=None):
        self.has_flow = has_flow  # type: bool
        self.inst_state = inst_state  # type: str
        self.active_count = active_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDasUsageResponseBodyAgent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_flow is not None:
            result['HasFlow'] = self.has_flow
        if self.inst_state is not None:
            result['InstState'] = self.inst_state
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasFlow') is not None:
            self.has_flow = m.get('HasFlow')
        if m.get('InstState') is not None:
            self.inst_state = m.get('InstState')
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        return self


class GetDasUsageResponseBodyNoticeState(TeaModel):
    def __init__(self, risk_notice=None, sys_notice=None):
        self.risk_notice = risk_notice  # type: bool
        self.sys_notice = sys_notice  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDasUsageResponseBodyNoticeState, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_notice is not None:
            result['RiskNotice'] = self.risk_notice
        if self.sys_notice is not None:
            result['SysNotice'] = self.sys_notice
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RiskNotice') is not None:
            self.risk_notice = m.get('RiskNotice')
        if m.get('SysNotice') is not None:
            self.sys_notice = m.get('SysNotice')
        return self


class GetDasUsageResponseBodyRiskAsset(TeaModel):
    def __init__(self, risk_dbcount=None, day_30risk_dbcount=None):
        self.risk_dbcount = risk_dbcount  # type: int
        self.day_30risk_dbcount = day_30risk_dbcount  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDasUsageResponseBodyRiskAsset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_dbcount is not None:
            result['RiskDBCount'] = self.risk_dbcount
        if self.day_30risk_dbcount is not None:
            result['Day30RiskDBCount'] = self.day_30risk_dbcount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RiskDBCount') is not None:
            self.risk_dbcount = m.get('RiskDBCount')
        if m.get('Day30RiskDBCount') is not None:
            self.day_30risk_dbcount = m.get('Day30RiskDBCount')
        return self


class GetDasUsageResponseBodyRiskRuleMaxHitRule(TeaModel):
    def __init__(self, count=None, rule_name=None):
        self.count = count  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDasUsageResponseBodyRiskRuleMaxHitRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetDasUsageResponseBodyRiskRuleDay30MaxHitRule(TeaModel):
    def __init__(self, count=None, rule_name=None):
        self.count = count  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDasUsageResponseBodyRiskRuleDay30MaxHitRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetDasUsageResponseBodyRiskRule(TeaModel):
    def __init__(self, day_30risk_count=None, risk_count=None, max_hit_rule=None, day_30max_hit_rule=None):
        self.day_30risk_count = day_30risk_count  # type: long
        self.risk_count = risk_count  # type: long
        self.max_hit_rule = max_hit_rule  # type: GetDasUsageResponseBodyRiskRuleMaxHitRule
        self.day_30max_hit_rule = day_30max_hit_rule  # type: GetDasUsageResponseBodyRiskRuleDay30MaxHitRule

    def validate(self):
        if self.max_hit_rule:
            self.max_hit_rule.validate()
        if self.day_30max_hit_rule:
            self.day_30max_hit_rule.validate()

    def to_map(self):
        _map = super(GetDasUsageResponseBodyRiskRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_30risk_count is not None:
            result['Day30RiskCount'] = self.day_30risk_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.max_hit_rule is not None:
            result['MaxHitRule'] = self.max_hit_rule.to_map()
        if self.day_30max_hit_rule is not None:
            result['Day30MaxHitRule'] = self.day_30max_hit_rule.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day30RiskCount') is not None:
            self.day_30risk_count = m.get('Day30RiskCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('MaxHitRule') is not None:
            temp_model = GetDasUsageResponseBodyRiskRuleMaxHitRule()
            self.max_hit_rule = temp_model.from_map(m['MaxHitRule'])
        if m.get('Day30MaxHitRule') is not None:
            temp_model = GetDasUsageResponseBodyRiskRuleDay30MaxHitRule()
            self.day_30max_hit_rule = temp_model.from_map(m['Day30MaxHitRule'])
        return self


class GetDasUsageResponseBodyWpAsset(TeaModel):
    def __init__(self, avg_time=None, db_name=None):
        self.avg_time = avg_time  # type: long
        self.db_name = db_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDasUsageResponseBodyWpAsset, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_time is not None:
            result['AvgTime'] = self.avg_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvgTime') is not None:
            self.avg_time = m.get('AvgTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        return self


class GetDasUsageResponseBody(TeaModel):
    def __init__(self, over_1s_sql_count=None, request_id=None, session_total_count=None, create_time=None,
                 sql_total_count=None, audit_asset=None, console_access=None, agent=None, notice_state=None, risk_asset=None,
                 risk_rule=None, wp_asset=None):
        self.over_1s_sql_count = over_1s_sql_count  # type: long
        self.request_id = request_id  # type: str
        self.session_total_count = session_total_count  # type: long
        self.create_time = create_time  # type: str
        self.sql_total_count = sql_total_count  # type: long
        self.audit_asset = audit_asset  # type: GetDasUsageResponseBodyAuditAsset
        self.console_access = console_access  # type: GetDasUsageResponseBodyConsoleAccess
        self.agent = agent  # type: GetDasUsageResponseBodyAgent
        self.notice_state = notice_state  # type: GetDasUsageResponseBodyNoticeState
        self.risk_asset = risk_asset  # type: GetDasUsageResponseBodyRiskAsset
        self.risk_rule = risk_rule  # type: GetDasUsageResponseBodyRiskRule
        self.wp_asset = wp_asset  # type: GetDasUsageResponseBodyWpAsset

    def validate(self):
        if self.audit_asset:
            self.audit_asset.validate()
        if self.console_access:
            self.console_access.validate()
        if self.agent:
            self.agent.validate()
        if self.notice_state:
            self.notice_state.validate()
        if self.risk_asset:
            self.risk_asset.validate()
        if self.risk_rule:
            self.risk_rule.validate()
        if self.wp_asset:
            self.wp_asset.validate()

    def to_map(self):
        _map = super(GetDasUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.over_1s_sql_count is not None:
            result['Over1sSqlCount'] = self.over_1s_sql_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_total_count is not None:
            result['SessionTotalCount'] = self.session_total_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sql_total_count is not None:
            result['SqlTotalCount'] = self.sql_total_count
        if self.audit_asset is not None:
            result['AuditAsset'] = self.audit_asset.to_map()
        if self.console_access is not None:
            result['ConsoleAccess'] = self.console_access.to_map()
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()
        if self.notice_state is not None:
            result['NoticeState'] = self.notice_state.to_map()
        if self.risk_asset is not None:
            result['RiskAsset'] = self.risk_asset.to_map()
        if self.risk_rule is not None:
            result['RiskRule'] = self.risk_rule.to_map()
        if self.wp_asset is not None:
            result['WpAsset'] = self.wp_asset.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Over1sSqlCount') is not None:
            self.over_1s_sql_count = m.get('Over1sSqlCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionTotalCount') is not None:
            self.session_total_count = m.get('SessionTotalCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SqlTotalCount') is not None:
            self.sql_total_count = m.get('SqlTotalCount')
        if m.get('AuditAsset') is not None:
            temp_model = GetDasUsageResponseBodyAuditAsset()
            self.audit_asset = temp_model.from_map(m['AuditAsset'])
        if m.get('ConsoleAccess') is not None:
            temp_model = GetDasUsageResponseBodyConsoleAccess()
            self.console_access = temp_model.from_map(m['ConsoleAccess'])
        if m.get('Agent') is not None:
            temp_model = GetDasUsageResponseBodyAgent()
            self.agent = temp_model.from_map(m['Agent'])
        if m.get('NoticeState') is not None:
            temp_model = GetDasUsageResponseBodyNoticeState()
            self.notice_state = temp_model.from_map(m['NoticeState'])
        if m.get('RiskAsset') is not None:
            temp_model = GetDasUsageResponseBodyRiskAsset()
            self.risk_asset = temp_model.from_map(m['RiskAsset'])
        if m.get('RiskRule') is not None:
            temp_model = GetDasUsageResponseBodyRiskRule()
            self.risk_rule = temp_model.from_map(m['RiskRule'])
        if m.get('WpAsset') is not None:
            temp_model = GetDasUsageResponseBodyWpAsset()
            self.wp_asset = temp_model.from_map(m['WpAsset'])
        return self


class GetDasUsageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDasUsageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDasUsageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDasUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDBAuditCountListRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDBAuditCountListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetDBAuditCountListResponseBodyDbList(TeaModel):
    def __init__(self, session_count=None, db_id=None, db_name=None, db_type=None, sql_count=None, db_type_name=None,
                 risk_count=None, db_version_name=None, asset_type=None, db_version=None, db_addresses=None):
        self.session_count = session_count  # type: long
        self.db_id = db_id  # type: int
        self.db_name = db_name  # type: str
        self.db_type = db_type  # type: int
        self.sql_count = sql_count  # type: long
        self.db_type_name = db_type_name  # type: str
        self.risk_count = risk_count  # type: long
        self.db_version_name = db_version_name  # type: str
        self.asset_type = asset_type  # type: int
        self.db_version = db_version  # type: int
        self.db_addresses = db_addresses  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDBAuditCountListResponseBodyDbList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.db_version_name is not None:
            result['DbVersionName'] = self.db_version_name
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('DbVersionName') is not None:
            self.db_version_name = m.get('DbVersionName')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')
        return self


class GetDBAuditCountListResponseBody(TeaModel):
    def __init__(self, request_id=None, db_list=None):
        self.request_id = request_id  # type: str
        self.db_list = db_list  # type: list[GetDBAuditCountListResponseBodyDbList]

    def validate(self):
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDBAuditCountListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.db_list = []
        if m.get('DbList') is not None:
            for k in m.get('DbList'):
                temp_model = GetDBAuditCountListResponseBodyDbList()
                self.db_list.append(temp_model.from_map(k))
        return self


class GetDBAuditCountListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDBAuditCountListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDBAuditCountListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDBAuditCountListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupDetailRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, group_key_id=None, group_type=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.group_key_id = group_key_id  # type: str
        self.group_type = group_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_key_id is not None:
            result['GroupKeyId'] = self.group_key_id
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupKeyId') is not None:
            self.group_key_id = m.get('GroupKeyId')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        return self


class GetGroupDetailResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGroupDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLicenseRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLicenseRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLicenseResponseBody(TeaModel):
    def __init__(self, start_time=None, request_id=None, asset_limit=None, asset_limit_used=None):
        self.start_time = start_time  # type: str
        self.request_id = request_id  # type: str
        self.asset_limit = asset_limit  # type: int
        self.asset_limit_used = asset_limit_used  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLicenseResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.asset_limit is not None:
            result['AssetLimit'] = self.asset_limit
        if self.asset_limit_used is not None:
            result['AssetLimitUsed'] = self.asset_limit_used
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AssetLimit') is not None:
            self.asset_limit = m.get('AssetLimit')
        if m.get('AssetLimitUsed') is not None:
            self.asset_limit_used = m.get('AssetLimitUsed')
        return self


class GetLicenseResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLicenseResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLicenseResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogDetailRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, begin_date=None, end_date=None, sql_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.sql_id = sql_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        return self


class GetLogDetailResponseBody(TeaModel):
    def __init__(self, client_port=None, app_client_ip=None, exec_cost_us=None, session_logout_time=None,
                 client_os_user=None, rule_id=None, request_id=None, sql_id=None, session_id=None, sql_type=None, app_username=None,
                 risk_level=None, db_id=None, rule_type=None, rule_key_id=None, sql_result=None, affect_rows=None,
                 sql_type_name=None, schema=None, session_login_time=None, db_user=None, server_mac=None, db_server=None,
                 rule_name=None, response_code=None, sql_content=None, inst_name=None, template_content=None,
                 client_program=None, capture_time=None, client_ip=None, client_mac=None, template_id=None, response_text=None,
                 fetch_cost_us=None, template_rules=None):
        self.client_port = client_port  # type: int
        self.app_client_ip = app_client_ip  # type: str
        self.exec_cost_us = exec_cost_us  # type: int
        self.session_logout_time = session_logout_time  # type: str
        self.client_os_user = client_os_user  # type: str
        self.rule_id = rule_id  # type: int
        self.request_id = request_id  # type: str
        self.sql_id = sql_id  # type: str
        self.session_id = session_id  # type: str
        self.sql_type = sql_type  # type: str
        self.app_username = app_username  # type: str
        self.risk_level = risk_level  # type: int
        self.db_id = db_id  # type: int
        self.rule_type = rule_type  # type: int
        self.rule_key_id = rule_key_id  # type: int
        self.sql_result = sql_result  # type: str
        self.affect_rows = affect_rows  # type: int
        self.sql_type_name = sql_type_name  # type: str
        self.schema = schema  # type: str
        self.session_login_time = session_login_time  # type: str
        self.db_user = db_user  # type: str
        self.server_mac = server_mac  # type: str
        self.db_server = db_server  # type: str
        self.rule_name = rule_name  # type: str
        self.response_code = response_code  # type: str
        self.sql_content = sql_content  # type: str
        self.inst_name = inst_name  # type: str
        self.template_content = template_content  # type: str
        self.client_program = client_program  # type: str
        self.capture_time = capture_time  # type: str
        self.client_ip = client_ip  # type: str
        self.client_mac = client_mac  # type: str
        self.template_id = template_id  # type: str
        self.response_text = response_text  # type: str
        self.fetch_cost_us = fetch_cost_us  # type: int
        self.template_rules = template_rules  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.app_client_ip is not None:
            result['AppClientIp'] = self.app_client_ip
        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us
        if self.session_logout_time is not None:
            result['SessionLogoutTime'] = self.session_logout_time
        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.app_username is not None:
            result['AppUsername'] = self.app_username
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_key_id is not None:
            result['RuleKeyId'] = self.rule_key_id
        if self.sql_result is not None:
            result['SqlResult'] = self.sql_result
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.sql_type_name is not None:
            result['SqlTypeName'] = self.sql_type_name
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.session_login_time is not None:
            result['SessionLoginTime'] = self.session_login_time
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac
        if self.db_server is not None:
            result['DbServer'] = self.db_server
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.sql_content is not None:
            result['SqlContent'] = self.sql_content
        if self.inst_name is not None:
            result['InstName'] = self.inst_name
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.response_text is not None:
            result['ResponseText'] = self.response_text
        if self.fetch_cost_us is not None:
            result['FetchCostUS'] = self.fetch_cost_us
        if self.template_rules is not None:
            result['TemplateRules'] = self.template_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('AppClientIp') is not None:
            self.app_client_ip = m.get('AppClientIp')
        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')
        if m.get('SessionLogoutTime') is not None:
            self.session_logout_time = m.get('SessionLogoutTime')
        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('AppUsername') is not None:
            self.app_username = m.get('AppUsername')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleKeyId') is not None:
            self.rule_key_id = m.get('RuleKeyId')
        if m.get('SqlResult') is not None:
            self.sql_result = m.get('SqlResult')
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('SqlTypeName') is not None:
            self.sql_type_name = m.get('SqlTypeName')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('SessionLoginTime') is not None:
            self.session_login_time = m.get('SessionLoginTime')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')
        if m.get('DbServer') is not None:
            self.db_server = m.get('DbServer')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('SqlContent') is not None:
            self.sql_content = m.get('SqlContent')
        if m.get('InstName') is not None:
            self.inst_name = m.get('InstName')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ResponseText') is not None:
            self.response_text = m.get('ResponseText')
        if m.get('FetchCostUS') is not None:
            self.fetch_cost_us = m.get('FetchCostUS')
        if m.get('TemplateRules') is not None:
            self.template_rules = m.get('TemplateRules')
        return self


class GetLogDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLogDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLogDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogListRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None,
                 page_number=None, page_size=None, sql_id=None, sql_key=None, session_id=None, template_id=None, is_success=None,
                 min_affect_rows=None, max_affect_rows=None, min_exec_cost_us=None, max_exec_cost_us=None, rule_name=None,
                 client_ip_list=None, db_user_list=None, db_host_list=None, risk_level_list=None, rule_type_list=None,
                 sql_type_list=None, client_program_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sql_id = sql_id  # type: str
        self.sql_key = sql_key  # type: str
        self.session_id = session_id  # type: str
        self.template_id = template_id  # type: str
        self.is_success = is_success  # type: str
        self.min_affect_rows = min_affect_rows  # type: int
        self.max_affect_rows = max_affect_rows  # type: int
        self.min_exec_cost_us = min_exec_cost_us  # type: int
        self.max_exec_cost_us = max_exec_cost_us  # type: int
        self.rule_name = rule_name  # type: str
        self.client_ip_list = client_ip_list  # type: list[str]
        self.db_user_list = db_user_list  # type: list[str]
        self.db_host_list = db_host_list  # type: list[str]
        self.risk_level_list = risk_level_list  # type: list[str]
        self.rule_type_list = rule_type_list  # type: list[str]
        self.sql_type_list = sql_type_list  # type: list[str]
        self.client_program_list = client_program_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_key is not None:
            result['SqlKey'] = self.sql_key
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.min_affect_rows is not None:
            result['MinAffectRows'] = self.min_affect_rows
        if self.max_affect_rows is not None:
            result['MaxAffectRows'] = self.max_affect_rows
        if self.min_exec_cost_us is not None:
            result['MinExecCostUS'] = self.min_exec_cost_us
        if self.max_exec_cost_us is not None:
            result['MaxExecCostUS'] = self.max_exec_cost_us
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list
        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list
        if self.db_host_list is not None:
            result['DbHostList'] = self.db_host_list
        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list
        if self.rule_type_list is not None:
            result['RuleTypeList'] = self.rule_type_list
        if self.sql_type_list is not None:
            result['SqlTypeList'] = self.sql_type_list
        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlKey') is not None:
            self.sql_key = m.get('SqlKey')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('MinAffectRows') is not None:
            self.min_affect_rows = m.get('MinAffectRows')
        if m.get('MaxAffectRows') is not None:
            self.max_affect_rows = m.get('MaxAffectRows')
        if m.get('MinExecCostUS') is not None:
            self.min_exec_cost_us = m.get('MinExecCostUS')
        if m.get('MaxExecCostUS') is not None:
            self.max_exec_cost_us = m.get('MaxExecCostUS')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')
        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')
        if m.get('DbHostList') is not None:
            self.db_host_list = m.get('DbHostList')
        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')
        if m.get('RuleTypeList') is not None:
            self.rule_type_list = m.get('RuleTypeList')
        if m.get('SqlTypeList') is not None:
            self.sql_type_list = m.get('SqlTypeList')
        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')
        return self


class GetLogListResponseBodyResults(TeaModel):
    def __init__(self, client_port=None, exec_cost_us=None, app_client_ip=None, session_logout_time=None,
                 client_os_user=None, rule_id=None, sql_id=None, session_id=None, sql_type=None, risk_level=None, app_username=None,
                 db_id=None, rule_type=None, rule_key_id=None, affect_rows=None, schema=None, session_login_time=None,
                 db_user=None, server_mac=None, db_server=None, rule_name=None, sql_content=None, response_code=None,
                 inst_name=None, client_program=None, capture_time=None, client_ip=None, client_mac=None, template_id=None,
                 fetch_cost_us=None, response_text=None):
        self.client_port = client_port  # type: int
        self.exec_cost_us = exec_cost_us  # type: int
        self.app_client_ip = app_client_ip  # type: str
        self.session_logout_time = session_logout_time  # type: str
        self.client_os_user = client_os_user  # type: str
        self.rule_id = rule_id  # type: int
        self.sql_id = sql_id  # type: str
        self.session_id = session_id  # type: str
        self.sql_type = sql_type  # type: str
        self.risk_level = risk_level  # type: int
        self.app_username = app_username  # type: str
        self.db_id = db_id  # type: int
        self.rule_type = rule_type  # type: int
        self.rule_key_id = rule_key_id  # type: int
        self.affect_rows = affect_rows  # type: int
        self.schema = schema  # type: str
        self.session_login_time = session_login_time  # type: str
        self.db_user = db_user  # type: str
        self.server_mac = server_mac  # type: str
        self.db_server = db_server  # type: str
        self.rule_name = rule_name  # type: str
        self.sql_content = sql_content  # type: str
        self.response_code = response_code  # type: str
        self.inst_name = inst_name  # type: str
        self.client_program = client_program  # type: str
        self.capture_time = capture_time  # type: str
        self.client_ip = client_ip  # type: str
        self.client_mac = client_mac  # type: str
        self.template_id = template_id  # type: str
        self.fetch_cost_us = fetch_cost_us  # type: int
        self.response_text = response_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogListResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us
        if self.app_client_ip is not None:
            result['AppClientIp'] = self.app_client_ip
        if self.session_logout_time is not None:
            result['SessionLogoutTime'] = self.session_logout_time
        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.app_username is not None:
            result['AppUsername'] = self.app_username
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_key_id is not None:
            result['RuleKeyId'] = self.rule_key_id
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.session_login_time is not None:
            result['SessionLoginTime'] = self.session_login_time
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac
        if self.db_server is not None:
            result['DbServer'] = self.db_server
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sql_content is not None:
            result['SqlContent'] = self.sql_content
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.inst_name is not None:
            result['InstName'] = self.inst_name
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.fetch_cost_us is not None:
            result['FetchCostUS'] = self.fetch_cost_us
        if self.response_text is not None:
            result['ResponseText'] = self.response_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')
        if m.get('AppClientIp') is not None:
            self.app_client_ip = m.get('AppClientIp')
        if m.get('SessionLogoutTime') is not None:
            self.session_logout_time = m.get('SessionLogoutTime')
        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('AppUsername') is not None:
            self.app_username = m.get('AppUsername')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleKeyId') is not None:
            self.rule_key_id = m.get('RuleKeyId')
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('SessionLoginTime') is not None:
            self.session_login_time = m.get('SessionLoginTime')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')
        if m.get('DbServer') is not None:
            self.db_server = m.get('DbServer')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SqlContent') is not None:
            self.sql_content = m.get('SqlContent')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('InstName') is not None:
            self.inst_name = m.get('InstName')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FetchCostUS') is not None:
            self.fetch_cost_us = m.get('FetchCostUS')
        if m.get('ResponseText') is not None:
            self.response_text = m.get('ResponseText')
        return self


class GetLogListResponseBody(TeaModel):
    def __init__(self, end_date=None, request_id=None, begin_date=None, incomplete=None, page_number=None,
                 page_size=None, total_count=None, results=None):
        self.end_date = end_date  # type: str
        self.request_id = request_id  # type: str
        self.begin_date = begin_date  # type: str
        self.incomplete = incomplete  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.results = results  # type: list[GetLogListResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLogListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.incomplete is not None:
            result['Incomplete'] = self.incomplete
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('Incomplete') is not None:
            self.incomplete = m.get('Incomplete')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetLogListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class GetLogListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLogListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLogListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogMaskConfigsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mask_name=None, mask_type=None, mask_state=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mask_name = mask_name  # type: str
        self.mask_type = mask_type  # type: int
        self.mask_state = mask_state  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogMaskConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_name is not None:
            result['MaskName'] = self.mask_name
        if self.mask_type is not None:
            result['MaskType'] = self.mask_type
        if self.mask_state is not None:
            result['MaskState'] = self.mask_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskName') is not None:
            self.mask_name = m.get('MaskName')
        if m.get('MaskType') is not None:
            self.mask_type = m.get('MaskType')
        if m.get('MaskState') is not None:
            self.mask_state = m.get('MaskState')
        return self


class GetLogMaskConfigsResponseBodyConfigs(TeaModel):
    def __init__(self, mask_description=None, mask_state=None, mask_name=None, mask_regex=None, mask_txt=None,
                 mask_id=None, mask_type=None):
        self.mask_description = mask_description  # type: str
        self.mask_state = mask_state  # type: int
        self.mask_name = mask_name  # type: str
        self.mask_regex = mask_regex  # type: str
        self.mask_txt = mask_txt  # type: str
        self.mask_id = mask_id  # type: int
        self.mask_type = mask_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogMaskConfigsResponseBodyConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mask_description is not None:
            result['MaskDescription'] = self.mask_description
        if self.mask_state is not None:
            result['MaskState'] = self.mask_state
        if self.mask_name is not None:
            result['MaskName'] = self.mask_name
        if self.mask_regex is not None:
            result['MaskRegex'] = self.mask_regex
        if self.mask_txt is not None:
            result['MaskTxt'] = self.mask_txt
        if self.mask_id is not None:
            result['MaskId'] = self.mask_id
        if self.mask_type is not None:
            result['MaskType'] = self.mask_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaskDescription') is not None:
            self.mask_description = m.get('MaskDescription')
        if m.get('MaskState') is not None:
            self.mask_state = m.get('MaskState')
        if m.get('MaskName') is not None:
            self.mask_name = m.get('MaskName')
        if m.get('MaskRegex') is not None:
            self.mask_regex = m.get('MaskRegex')
        if m.get('MaskTxt') is not None:
            self.mask_txt = m.get('MaskTxt')
        if m.get('MaskId') is not None:
            self.mask_id = m.get('MaskId')
        if m.get('MaskType') is not None:
            self.mask_type = m.get('MaskType')
        return self


class GetLogMaskConfigsResponseBody(TeaModel):
    def __init__(self, request_id=None, configs=None):
        self.request_id = request_id  # type: str
        self.configs = configs  # type: list[GetLogMaskConfigsResponseBodyConfigs]

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLogMaskConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = GetLogMaskConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        return self


class GetLogMaskConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLogMaskConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogMaskConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLogMaskConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogQueryConditionRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None, is_risk=None,
                 is_success=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.is_risk = is_risk  # type: str
        self.is_success = is_success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogQueryConditionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.is_risk is not None:
            result['IsRisk'] = self.is_risk
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('IsRisk') is not None:
            self.is_risk = m.get('IsRisk')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetLogQueryConditionResponseBodySqlTypeList(TeaModel):
    def __init__(self, sql_keyword=None, sql_type=None):
        self.sql_keyword = sql_keyword  # type: str
        self.sql_type = sql_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogQueryConditionResponseBodySqlTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sql_keyword is not None:
            result['SqlKeyword'] = self.sql_keyword
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SqlKeyword') is not None:
            self.sql_keyword = m.get('SqlKeyword')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class GetLogQueryConditionResponseBody(TeaModel):
    def __init__(self, request_id=None, db_user_list=None, client_ip_list=None, client_program_list=None,
                 db_server_list=None, sql_type_list=None):
        self.request_id = request_id  # type: str
        self.db_user_list = db_user_list  # type: list[str]
        self.client_ip_list = client_ip_list  # type: list[str]
        self.client_program_list = client_program_list  # type: list[str]
        self.db_server_list = db_server_list  # type: list[str]
        self.sql_type_list = sql_type_list  # type: list[GetLogQueryConditionResponseBodySqlTypeList]

    def validate(self):
        if self.sql_type_list:
            for k in self.sql_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLogQueryConditionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list
        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list
        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list
        if self.db_server_list is not None:
            result['DbServerList'] = self.db_server_list
        result['SqlTypeList'] = []
        if self.sql_type_list is not None:
            for k in self.sql_type_list:
                result['SqlTypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')
        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')
        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')
        if m.get('DbServerList') is not None:
            self.db_server_list = m.get('DbServerList')
        self.sql_type_list = []
        if m.get('SqlTypeList') is not None:
            for k in m.get('SqlTypeList'):
                temp_model = GetLogQueryConditionResponseBodySqlTypeList()
                self.sql_type_list.append(temp_model.from_map(k))
        return self


class GetLogQueryConditionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLogQueryConditionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogQueryConditionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLogQueryConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogStatisticsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None, by_db_id=None,
                 by_client_ip=None, by_db_user=None, by_db_server=None, by_client_program=None, by_sql_type=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.by_db_id = by_db_id  # type: int
        self.by_client_ip = by_client_ip  # type: int
        self.by_db_user = by_db_user  # type: int
        self.by_db_server = by_db_server  # type: int
        self.by_client_program = by_client_program  # type: int
        self.by_sql_type = by_sql_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.by_db_id is not None:
            result['ByDbId'] = self.by_db_id
        if self.by_client_ip is not None:
            result['ByClientIp'] = self.by_client_ip
        if self.by_db_user is not None:
            result['ByDbUser'] = self.by_db_user
        if self.by_db_server is not None:
            result['ByDbServer'] = self.by_db_server
        if self.by_client_program is not None:
            result['ByClientProgram'] = self.by_client_program
        if self.by_sql_type is not None:
            result['BySqlType'] = self.by_sql_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ByDbId') is not None:
            self.by_db_id = m.get('ByDbId')
        if m.get('ByClientIp') is not None:
            self.by_client_ip = m.get('ByClientIp')
        if m.get('ByDbUser') is not None:
            self.by_db_user = m.get('ByDbUser')
        if m.get('ByDbServer') is not None:
            self.by_db_server = m.get('ByDbServer')
        if m.get('ByClientProgram') is not None:
            self.by_client_program = m.get('ByClientProgram')
        if m.get('BySqlType') is not None:
            self.by_sql_type = m.get('BySqlType')
        return self


class GetLogStatisticsResponseBodyCountList(TeaModel):
    def __init__(self, sql_keyword=None, db_id=None, db_name=None, client_program=None, db_user=None, client_ip=None,
                 sql_count=None, risk_count=None, db_server=None, sql_type=None):
        self.sql_keyword = sql_keyword  # type: str
        self.db_id = db_id  # type: int
        self.db_name = db_name  # type: str
        self.client_program = client_program  # type: str
        self.db_user = db_user  # type: str
        self.client_ip = client_ip  # type: str
        self.sql_count = sql_count  # type: long
        self.risk_count = risk_count  # type: long
        self.db_server = db_server  # type: str
        self.sql_type = sql_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogStatisticsResponseBodyCountList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sql_keyword is not None:
            result['SqlKeyword'] = self.sql_keyword
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.db_server is not None:
            result['DbServer'] = self.db_server
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SqlKeyword') is not None:
            self.sql_keyword = m.get('SqlKeyword')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('DbServer') is not None:
            self.db_server = m.get('DbServer')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class GetLogStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, count_list=None):
        self.request_id = request_id  # type: str
        self.count_list = count_list  # type: list[GetLogStatisticsResponseBodyCountList]

    def validate(self):
        if self.count_list:
            for k in self.count_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLogStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CountList'] = []
        if self.count_list is not None:
            for k in self.count_list:
                result['CountList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.count_list = []
        if m.get('CountList') is not None:
            for k in m.get('CountList'):
                temp_model = GetLogStatisticsResponseBodyCountList()
                self.count_list.append(temp_model.from_map(k))
        return self


class GetLogStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLogStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLogStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogTopDistributionRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogTopDistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetLogTopDistributionResponseBodyTimeList(TeaModel):
    def __init__(self, begin_date=None, sql_count=None, end_date=None, top_time=None):
        self.begin_date = begin_date  # type: str
        self.sql_count = sql_count  # type: long
        self.end_date = end_date  # type: str
        self.top_time = top_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogTopDistributionResponseBodyTimeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.top_time is not None:
            result['TopTime'] = self.top_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('TopTime') is not None:
            self.top_time = m.get('TopTime')
        return self


class GetLogTopDistributionResponseBody(TeaModel):
    def __init__(self, request_id=None, time_list=None):
        self.request_id = request_id  # type: str
        self.time_list = time_list  # type: list[GetLogTopDistributionResponseBodyTimeList]

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLogTopDistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetLogTopDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetLogTopDistributionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLogTopDistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogTopDistributionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLogTopDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogTopStatisticsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, top_time=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.top_time = top_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogTopStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.top_time is not None:
            result['TopTime'] = self.top_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('TopTime') is not None:
            self.top_time = m.get('TopTime')
        return self


class GetLogTopStatisticsResponseBodyCountList(TeaModel):
    def __init__(self, client_ip=None, db_user=None, sql_count=None, client_program=None):
        self.client_ip = client_ip  # type: str
        self.db_user = db_user  # type: str
        self.sql_count = sql_count  # type: long
        self.client_program = client_program  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogTopStatisticsResponseBodyCountList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        return self


class GetLogTopStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, count_list=None):
        self.request_id = request_id  # type: str
        self.count_list = count_list  # type: list[GetLogTopStatisticsResponseBodyCountList]

    def validate(self):
        if self.count_list:
            for k in self.count_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLogTopStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CountList'] = []
        if self.count_list is not None:
            for k in self.count_list:
                result['CountList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.count_list = []
        if m.get('CountList') is not None:
            for k in m.get('CountList'):
                temp_model = GetLogTopStatisticsResponseBodyCountList()
                self.count_list.append(temp_model.from_map(k))
        return self


class GetLogTopStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLogTopStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogTopStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLogTopStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogTypeDistributionRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogTypeDistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetLogTypeDistributionResponseBodyTimeList(TeaModel):
    def __init__(self, end_date=None, exec_cost_us=None, insert_sql_count=None, select_sql_count=None,
                 delete_sql_count=None, begin_date=None, other_sql_count=None, sql_count=None, update_sql_count=None):
        self.end_date = end_date  # type: str
        self.exec_cost_us = exec_cost_us  # type: str
        self.insert_sql_count = insert_sql_count  # type: int
        self.select_sql_count = select_sql_count  # type: int
        self.delete_sql_count = delete_sql_count  # type: int
        self.begin_date = begin_date  # type: str
        self.other_sql_count = other_sql_count  # type: int
        self.sql_count = sql_count  # type: int
        self.update_sql_count = update_sql_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLogTypeDistributionResponseBodyTimeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us
        if self.insert_sql_count is not None:
            result['InsertSqlCount'] = self.insert_sql_count
        if self.select_sql_count is not None:
            result['SelectSqlCount'] = self.select_sql_count
        if self.delete_sql_count is not None:
            result['DeleteSqlCount'] = self.delete_sql_count
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.other_sql_count is not None:
            result['OtherSqlCount'] = self.other_sql_count
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.update_sql_count is not None:
            result['UpdateSqlCount'] = self.update_sql_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')
        if m.get('InsertSqlCount') is not None:
            self.insert_sql_count = m.get('InsertSqlCount')
        if m.get('SelectSqlCount') is not None:
            self.select_sql_count = m.get('SelectSqlCount')
        if m.get('DeleteSqlCount') is not None:
            self.delete_sql_count = m.get('DeleteSqlCount')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('OtherSqlCount') is not None:
            self.other_sql_count = m.get('OtherSqlCount')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('UpdateSqlCount') is not None:
            self.update_sql_count = m.get('UpdateSqlCount')
        return self


class GetLogTypeDistributionResponseBody(TeaModel):
    def __init__(self, request_id=None, time_list=None):
        self.request_id = request_id  # type: str
        self.time_list = time_list  # type: list[GetLogTypeDistributionResponseBodyTimeList]

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLogTypeDistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetLogTypeDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetLogTypeDistributionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLogTypeDistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLogTypeDistributionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetLogTypeDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNewSqlTemplateListRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None,
                 page_number=None, page_size=None, template_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNewSqlTemplateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetNewSqlTemplateListResponseBodyResults(TeaModel):
    def __init__(self, template_content=None, template_id=None, first_capture_time=None):
        self.template_content = template_content  # type: str
        self.template_id = template_id  # type: str
        self.first_capture_time = first_capture_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNewSqlTemplateListResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.first_capture_time is not None:
            result['FirstCaptureTime'] = self.first_capture_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FirstCaptureTime') is not None:
            self.first_capture_time = m.get('FirstCaptureTime')
        return self


class GetNewSqlTemplateListResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, results=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long
        self.results = results  # type: list[GetNewSqlTemplateListResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetNewSqlTemplateListResponseBody, self).to_map()
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
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
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
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetNewSqlTemplateListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class GetNewSqlTemplateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNewSqlTemplateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNewSqlTemplateListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetNewSqlTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReportFileUrlRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, file_name=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReportFileUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GetReportFileUrlResponseBodyServerData(TeaModel):
    def __init__(self, file_url=None):
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReportFileUrlResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class GetReportFileUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: GetReportFileUrlResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(GetReportFileUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = GetReportFileUrlResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class GetReportFileUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetReportFileUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetReportFileUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetReportFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRiskLevelDistributionRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRiskLevelDistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetRiskLevelDistributionResponseBodyTimeList(TeaModel):
    def __init__(self, middle_risk_count=None, high_risk_count=None, end_date=None, begin_date=None,
                 risk_count=None, low_risk_count=None):
        self.middle_risk_count = middle_risk_count  # type: long
        self.high_risk_count = high_risk_count  # type: long
        self.end_date = end_date  # type: str
        self.begin_date = begin_date  # type: str
        self.risk_count = risk_count  # type: long
        self.low_risk_count = low_risk_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRiskLevelDistributionResponseBodyTimeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.middle_risk_count is not None:
            result['MiddleRiskCount'] = self.middle_risk_count
        if self.high_risk_count is not None:
            result['HighRiskCount'] = self.high_risk_count
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.low_risk_count is not None:
            result['LowRiskCount'] = self.low_risk_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MiddleRiskCount') is not None:
            self.middle_risk_count = m.get('MiddleRiskCount')
        if m.get('HighRiskCount') is not None:
            self.high_risk_count = m.get('HighRiskCount')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('LowRiskCount') is not None:
            self.low_risk_count = m.get('LowRiskCount')
        return self


class GetRiskLevelDistributionResponseBody(TeaModel):
    def __init__(self, request_id=None, time_list=None):
        self.request_id = request_id  # type: str
        self.time_list = time_list  # type: list[GetRiskLevelDistributionResponseBodyTimeList]

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRiskLevelDistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetRiskLevelDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetRiskLevelDistributionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRiskLevelDistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRiskLevelDistributionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRiskLevelDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRiskStatisticsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None, by_db_id=None,
                 by_risk_level=None, by_rule_type=None, by_rule_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.by_db_id = by_db_id  # type: int
        self.by_risk_level = by_risk_level  # type: int
        self.by_rule_type = by_rule_type  # type: int
        self.by_rule_id = by_rule_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRiskStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.by_db_id is not None:
            result['ByDbId'] = self.by_db_id
        if self.by_risk_level is not None:
            result['ByRiskLevel'] = self.by_risk_level
        if self.by_rule_type is not None:
            result['ByRuleType'] = self.by_rule_type
        if self.by_rule_id is not None:
            result['ByRuleId'] = self.by_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ByDbId') is not None:
            self.by_db_id = m.get('ByDbId')
        if m.get('ByRiskLevel') is not None:
            self.by_risk_level = m.get('ByRiskLevel')
        if m.get('ByRuleType') is not None:
            self.by_rule_type = m.get('ByRuleType')
        if m.get('ByRuleId') is not None:
            self.by_rule_id = m.get('ByRuleId')
        return self


class GetRiskStatisticsResponseBodyTimeList(TeaModel):
    def __init__(self, risk_level=None, db_id=None, db_name=None, rule_type=None, last_capture_time=None,
                 risk_count=None, rule_name=None, rule_id=None):
        self.risk_level = risk_level  # type: int
        self.db_id = db_id  # type: int
        self.db_name = db_name  # type: str
        self.rule_type = rule_type  # type: int
        self.last_capture_time = last_capture_time  # type: str
        self.risk_count = risk_count  # type: long
        self.rule_name = rule_name  # type: str
        self.rule_id = rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRiskStatisticsResponseBodyTimeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.last_capture_time is not None:
            result['LastCaptureTime'] = self.last_capture_time
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('LastCaptureTime') is not None:
            self.last_capture_time = m.get('LastCaptureTime')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetRiskStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, time_list=None):
        self.request_id = request_id  # type: str
        self.time_list = time_list  # type: list[GetRiskStatisticsResponseBodyTimeList]

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRiskStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetRiskStatisticsResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetRiskStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRiskStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRiskStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRiskStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleDetailRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, rule_id=None, rule_key_id=None, db_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.rule_id = rule_id  # type: int
        self.rule_key_id = rule_key_id  # type: int
        self.db_id = db_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_key_id is not None:
            result['RuleKeyId'] = self.rule_key_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleKeyId') is not None:
            self.rule_key_id = m.get('RuleKeyId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        return self


class GetRuleDetailResponseBodyServerData(TeaModel):
    def __init__(self, json_result=None):
        self.json_result = json_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleDetailResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class GetRuleDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: GetRuleDetailResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = GetRuleDetailResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class GetRuleDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRuleDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRuleDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRuleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleGroupNameRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, group_name=None, group_type=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.group_name = group_name  # type: str
        self.group_type = group_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleGroupNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        return self


class GetRuleGroupNameResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRuleGroupNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRuleGroupNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRuleGroupNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRuleGroupNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRuleGroupNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionDetailRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, session_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GetSessionDetailResponseBody(TeaModel):
    def __init__(self, login_time=None, db_id=None, login_code=None, client_port=None, login_message=None,
                 db_user=None, logout_time=None, server_port=None, client_os_user=None, server_mac=None, request_id=None,
                 client_program=None, client_ip=None, server_ip=None, session_id=None, client_mac=None):
        self.login_time = login_time  # type: str
        self.db_id = db_id  # type: int
        self.login_code = login_code  # type: int
        self.client_port = client_port  # type: int
        self.login_message = login_message  # type: str
        self.db_user = db_user  # type: str
        self.logout_time = logout_time  # type: str
        self.server_port = server_port  # type: int
        self.client_os_user = client_os_user  # type: str
        self.server_mac = server_mac  # type: str
        self.request_id = request_id  # type: str
        self.client_program = client_program  # type: str
        self.client_ip = client_ip  # type: str
        self.server_ip = server_ip  # type: str
        self.session_id = session_id  # type: str
        self.client_mac = client_mac  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_time is not None:
            result['LoginTime'] = self.login_time
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.login_code is not None:
            result['LoginCode'] = self.login_code
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.login_message is not None:
            result['LoginMessage'] = self.login_message
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.logout_time is not None:
            result['LogoutTime'] = self.logout_time
        if self.server_port is not None:
            result['ServerPort'] = self.server_port
        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user
        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginTime') is not None:
            self.login_time = m.get('LoginTime')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('LoginCode') is not None:
            self.login_code = m.get('LoginCode')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('LoginMessage') is not None:
            self.login_message = m.get('LoginMessage')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('LogoutTime') is not None:
            self.logout_time = m.get('LogoutTime')
        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')
        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')
        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')
        return self


class GetSessionDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSessionDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSessionDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSessionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionDistributionRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionDistributionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetSessionDistributionResponseBodyTimeList(TeaModel):
    def __init__(self, begin_date=None, login_session_count=None, active_session_count=None, end_date=None,
                 error_session_count=None):
        self.begin_date = begin_date  # type: str
        self.login_session_count = login_session_count  # type: int
        self.active_session_count = active_session_count  # type: int
        self.end_date = end_date  # type: str
        self.error_session_count = error_session_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionDistributionResponseBodyTimeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.login_session_count is not None:
            result['LoginSessionCount'] = self.login_session_count
        if self.active_session_count is not None:
            result['ActiveSessionCount'] = self.active_session_count
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.error_session_count is not None:
            result['ErrorSessionCount'] = self.error_session_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('LoginSessionCount') is not None:
            self.login_session_count = m.get('LoginSessionCount')
        if m.get('ActiveSessionCount') is not None:
            self.active_session_count = m.get('ActiveSessionCount')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ErrorSessionCount') is not None:
            self.error_session_count = m.get('ErrorSessionCount')
        return self


class GetSessionDistributionResponseBody(TeaModel):
    def __init__(self, request_id=None, time_list=None):
        self.request_id = request_id  # type: str
        self.time_list = time_list  # type: list[GetSessionDistributionResponseBodyTimeList]

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSessionDistributionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetSessionDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetSessionDistributionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSessionDistributionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSessionDistributionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSessionDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionListRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None,
                 page_number=None, page_size=None, session_id=None, action_list=None, client_ip_list=None, db_user_list=None,
                 db_host_list=None, client_program_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.session_id = session_id  # type: str
        self.action_list = action_list  # type: list[str]
        self.client_ip_list = client_ip_list  # type: list[str]
        self.db_user_list = db_user_list  # type: list[str]
        self.db_host_list = db_host_list  # type: list[str]
        self.client_program_list = client_program_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.action_list is not None:
            result['ActionList'] = self.action_list
        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list
        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list
        if self.db_host_list is not None:
            result['DbHostList'] = self.db_host_list
        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('ActionList') is not None:
            self.action_list = m.get('ActionList')
        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')
        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')
        if m.get('DbHostList') is not None:
            self.db_host_list = m.get('DbHostList')
        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')
        return self


class GetSessionListResponseBodyResults(TeaModel):
    def __init__(self, db_id=None, login_code=None, action=None, client_port=None, login_message=None, db_user=None,
                 server_port=None, client_os_user=None, server_mac=None, client_program=None, capture_time=None, client_ip=None,
                 server_ip=None, session_id=None, client_mac=None):
        self.db_id = db_id  # type: int
        self.login_code = login_code  # type: int
        self.action = action  # type: str
        self.client_port = client_port  # type: int
        self.login_message = login_message  # type: str
        self.db_user = db_user  # type: str
        self.server_port = server_port  # type: int
        self.client_os_user = client_os_user  # type: str
        self.server_mac = server_mac  # type: str
        self.client_program = client_program  # type: str
        self.capture_time = capture_time  # type: str
        self.client_ip = client_ip  # type: str
        self.server_ip = server_ip  # type: str
        self.session_id = session_id  # type: str
        self.client_mac = client_mac  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionListResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.login_code is not None:
            result['LoginCode'] = self.login_code
        if self.action is not None:
            result['Action'] = self.action
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.login_message is not None:
            result['LoginMessage'] = self.login_message
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.server_port is not None:
            result['ServerPort'] = self.server_port
        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user
        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('LoginCode') is not None:
            self.login_code = m.get('LoginCode')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('LoginMessage') is not None:
            self.login_message = m.get('LoginMessage')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')
        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')
        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')
        return self


class GetSessionListResponseBody(TeaModel):
    def __init__(self, end_date=None, request_id=None, begin_date=None, incomplete=None, page_number=None,
                 page_size=None, total_count=None, results=None):
        self.end_date = end_date  # type: str
        self.request_id = request_id  # type: str
        self.begin_date = begin_date  # type: str
        self.incomplete = incomplete  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long
        self.results = results  # type: list[GetSessionListResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSessionListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.incomplete is not None:
            result['Incomplete'] = self.incomplete
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('Incomplete') is not None:
            self.incomplete = m.get('Incomplete')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetSessionListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class GetSessionListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSessionListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSessionListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSessionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionQueryConditionRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionQueryConditionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetSessionQueryConditionResponseBody(TeaModel):
    def __init__(self, request_id=None, db_user_list=None, client_ip_list=None, client_program_list=None,
                 db_server_list=None):
        self.request_id = request_id  # type: str
        self.db_user_list = db_user_list  # type: list[str]
        self.client_ip_list = client_ip_list  # type: list[str]
        self.client_program_list = client_program_list  # type: list[str]
        self.db_server_list = db_server_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSessionQueryConditionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list
        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list
        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list
        if self.db_server_list is not None:
            result['DbServerList'] = self.db_server_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')
        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')
        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')
        if m.get('DbServerList') is not None:
            self.db_server_list = m.get('DbServerList')
        return self


class GetSessionQueryConditionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSessionQueryConditionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSessionQueryConditionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSessionQueryConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlTemplateListRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None,
                 page_number=None, page_size=None, sql_id=None, template_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sql_id = sql_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSqlTemplateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetSqlTemplateListResponseBodyResultsRuleList(TeaModel):
    def __init__(self, risk_level=None, rule_state=None, db_id=None, rule_name=None, rule_id=None):
        self.risk_level = risk_level  # type: int
        self.rule_state = rule_state  # type: int
        self.db_id = db_id  # type: int
        self.rule_name = rule_name  # type: str
        self.rule_id = rule_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSqlTemplateListResponseBodyResultsRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rule_state is not None:
            result['RuleState'] = self.rule_state
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RuleState') is not None:
            self.rule_state = m.get('RuleState')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetSqlTemplateListResponseBodyResults(TeaModel):
    def __init__(self, template_content=None, last_capture_time=None, capture_count=None, template_id=None,
                 sql_type=None, rule_list=None):
        self.template_content = template_content  # type: str
        self.last_capture_time = last_capture_time  # type: str
        self.capture_count = capture_count  # type: long
        self.template_id = template_id  # type: str
        self.sql_type = sql_type  # type: int
        self.rule_list = rule_list  # type: list[GetSqlTemplateListResponseBodyResultsRuleList]

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSqlTemplateListResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.last_capture_time is not None:
            result['LastCaptureTime'] = self.last_capture_time
        if self.capture_count is not None:
            result['CaptureCount'] = self.capture_count
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('LastCaptureTime') is not None:
            self.last_capture_time = m.get('LastCaptureTime')
        if m.get('CaptureCount') is not None:
            self.capture_count = m.get('CaptureCount')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = GetSqlTemplateListResponseBodyResultsRuleList()
                self.rule_list.append(temp_model.from_map(k))
        return self


class GetSqlTemplateListResponseBody(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, results=None):
        self.request_id = request_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long
        self.results = results  # type: list[GetSqlTemplateListResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSqlTemplateListResponseBody, self).to_map()
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
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
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
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetSqlTemplateListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class GetSqlTemplateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSqlTemplateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSqlTemplateListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSqlTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopSqlTemplateListRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None, order_type=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.order_type = order_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTopSqlTemplateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class GetTopSqlTemplateListResponseBodyTemplateList(TeaModel):
    def __init__(self, template_content=None, exec_cost_us=None, affect_rows=None, exec_cost_usmean=None,
                 last_capture_time=None, template_id=None, capture_count=None):
        self.template_content = template_content  # type: str
        self.exec_cost_us = exec_cost_us  # type: str
        self.affect_rows = affect_rows  # type: str
        self.exec_cost_usmean = exec_cost_usmean  # type: str
        self.last_capture_time = last_capture_time  # type: str
        self.template_id = template_id  # type: str
        self.capture_count = capture_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTopSqlTemplateListResponseBodyTemplateList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.exec_cost_usmean is not None:
            result['ExecCostUSMean'] = self.exec_cost_usmean
        if self.last_capture_time is not None:
            result['LastCaptureTime'] = self.last_capture_time
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.capture_count is not None:
            result['CaptureCount'] = self.capture_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('ExecCostUSMean') is not None:
            self.exec_cost_usmean = m.get('ExecCostUSMean')
        if m.get('LastCaptureTime') is not None:
            self.last_capture_time = m.get('LastCaptureTime')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CaptureCount') is not None:
            self.capture_count = m.get('CaptureCount')
        return self


class GetTopSqlTemplateListResponseBody(TeaModel):
    def __init__(self, request_id=None, template_list=None):
        self.request_id = request_id  # type: str
        self.template_list = template_list  # type: list[GetTopSqlTemplateListResponseBodyTemplateList]

    def validate(self):
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTopSqlTemplateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TemplateList'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['TemplateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_list = []
        if m.get('TemplateList') is not None:
            for k in m.get('TemplateList'):
                temp_model = GetTopSqlTemplateListResponseBodyTemplateList()
                self.template_list.append(temp_model.from_map(k))
        return self


class GetTopSqlTemplateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTopSqlTemplateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTopSqlTemplateListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTopSqlTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GradeProtectionReportRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GradeProtectionReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GradeProtectionReportResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GradeProtectionReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GradeProtectionReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GradeProtectionReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GradeProtectionReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GradeProtectionReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportDataSourceRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, data_json=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.data_json = data_json  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_json is not None:
            result['DataJson'] = self.data_json
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataJson') is not None:
            self.data_json = m.get('DataJson')
        return self


class ImportDataSourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportDataSourceResponseBody, self).to_map()
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


class ImportDataSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ImportDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportDataSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IntegratedReportRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IntegratedReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class IntegratedReportResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IntegratedReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IntegratedReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: IntegratedReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IntegratedReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = IntegratedReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAssociatedRulesRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, rule_name=None, rule_type=None, rule_defn=None, db_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_type = rule_type  # type: str
        self.rule_defn = rule_defn  # type: str
        self.db_id = db_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAssociatedRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_defn is not None:
            result['RuleDefn'] = self.rule_defn
        if self.db_id is not None:
            result['DbId'] = self.db_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleDefn') is not None:
            self.rule_defn = m.get('RuleDefn')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        return self


class ListAssociatedRulesResponseBodyServerData(TeaModel):
    def __init__(self, json_result=None):
        self.json_result = json_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAssociatedRulesResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class ListAssociatedRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: ListAssociatedRulesResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(ListAssociatedRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = ListAssociatedRulesResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class ListAssociatedRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAssociatedRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAssociatedRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAssociatedRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceAttributeRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_ids=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_ids = db_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_ids is not None:
            result['DbIds'] = self.db_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbIds') is not None:
            self.db_ids = m.get('DbIds')
        return self


class ListDataSourceAttributeResponseBodyDbList(TeaModel):
    def __init__(self, result_audit_mode=None, db_id=None, result_audit_max_size=None, audit_mode=None,
                 result_audit_max_line=None):
        self.result_audit_mode = result_audit_mode  # type: str
        self.db_id = db_id  # type: int
        self.result_audit_max_size = result_audit_max_size  # type: int
        self.audit_mode = audit_mode  # type: str
        self.result_audit_max_line = result_audit_max_line  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourceAttributeResponseBodyDbList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_audit_mode is not None:
            result['ResultAuditMode'] = self.result_audit_mode
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.result_audit_max_size is not None:
            result['ResultAuditMaxSize'] = self.result_audit_max_size
        if self.audit_mode is not None:
            result['AuditMode'] = self.audit_mode
        if self.result_audit_max_line is not None:
            result['ResultAuditMaxLine'] = self.result_audit_max_line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResultAuditMode') is not None:
            self.result_audit_mode = m.get('ResultAuditMode')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('ResultAuditMaxSize') is not None:
            self.result_audit_max_size = m.get('ResultAuditMaxSize')
        if m.get('AuditMode') is not None:
            self.audit_mode = m.get('AuditMode')
        if m.get('ResultAuditMaxLine') is not None:
            self.result_audit_max_line = m.get('ResultAuditMaxLine')
        return self


class ListDataSourceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None, db_list=None):
        self.request_id = request_id  # type: str
        self.db_list = db_list  # type: list[ListDataSourceAttributeResponseBodyDbList]

    def validate(self):
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.db_list = []
        if m.get('DbList') is not None:
            for k in m.get('DbList'):
                temp_model = ListDataSourceAttributeResponseBodyDbList()
                self.db_list.append(temp_model.from_map(k))
        return self


class ListDataSourceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataSourceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourceAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataSourceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourcesRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        return self


class ListDataSourcesResponseBodyDbList(TeaModel):
    def __init__(self, db_id=None, create_time=None, db_username=None, db_certificate=None, db_instance_id=None,
                 asset_type=None, db_version=None, db_name=None, db_type=None, audit_switch=None, db_type_name=None,
                 db_version_name=None, db_addresses=None):
        self.db_id = db_id  # type: int
        self.create_time = create_time  # type: str
        self.db_username = db_username  # type: str
        self.db_certificate = db_certificate  # type: str
        self.db_instance_id = db_instance_id  # type: str
        self.asset_type = asset_type  # type: int
        self.db_version = db_version  # type: int
        self.db_name = db_name  # type: str
        self.db_type = db_type  # type: int
        self.audit_switch = audit_switch  # type: int
        self.db_type_name = db_type_name  # type: str
        self.db_version_name = db_version_name  # type: str
        self.db_addresses = db_addresses  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataSourcesResponseBodyDbList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.db_username is not None:
            result['DbUsername'] = self.db_username
        if self.db_certificate is not None:
            result['DbCertificate'] = self.db_certificate
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.audit_switch is not None:
            result['AuditSwitch'] = self.audit_switch
        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name
        if self.db_version_name is not None:
            result['DbVersionName'] = self.db_version_name
        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DbUsername') is not None:
            self.db_username = m.get('DbUsername')
        if m.get('DbCertificate') is not None:
            self.db_certificate = m.get('DbCertificate')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('AuditSwitch') is not None:
            self.audit_switch = m.get('AuditSwitch')
        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')
        if m.get('DbVersionName') is not None:
            self.db_version_name = m.get('DbVersionName')
        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, db_list=None):
        self.request_id = request_id  # type: str
        self.db_list = db_list  # type: list[ListDataSourcesResponseBodyDbList]

    def validate(self):
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.db_list = []
        if m.get('DbList') is not None:
            for k in m.get('DbList'):
                temp_model = ListDataSourcesResponseBodyDbList()
                self.db_list.append(temp_model.from_map(k))
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataSourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogAlarmTasksRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogAlarmTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListLogAlarmTasksResponseBodyTaskList(TeaModel):
    def __init__(self, task_status=None, task_id=None, create_time=None, task_name=None, to_mail_list=None,
                 risk_level_list=None, db_id_list=None):
        self.task_status = task_status  # type: int
        self.task_id = task_id  # type: int
        self.create_time = create_time  # type: str
        self.task_name = task_name  # type: str
        self.to_mail_list = to_mail_list  # type: list[str]
        self.risk_level_list = risk_level_list  # type: list[str]
        self.db_id_list = db_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogAlarmTasksResponseBodyTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list
        if self.db_id_list is not None:
            result['DbIdList'] = self.db_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')
        if m.get('DbIdList') is not None:
            self.db_id_list = m.get('DbIdList')
        return self


class ListLogAlarmTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, task_list=None):
        self.request_id = request_id  # type: str
        self.task_list = task_list  # type: list[ListLogAlarmTasksResponseBodyTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLogAlarmTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListLogAlarmTasksResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListLogAlarmTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListLogAlarmTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLogAlarmTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListLogAlarmTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReportPushTasksRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListReportPushTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListReportPushTasksResponseBodyTaskList(TeaModel):
    def __init__(self, schedule_time=None, job_status=None, job_id=None, schedule_type=None, db_list=None,
                 report_type=None, email_list=None):
        self.schedule_time = schedule_time  # type: str
        self.job_status = job_status  # type: int
        self.job_id = job_id  # type: int
        self.schedule_type = schedule_type  # type: str
        self.db_list = db_list  # type: list[str]
        self.report_type = report_type  # type: list[str]
        self.email_list = email_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListReportPushTasksResponseBodyTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.email_list is not None:
            result['EmailList'] = self.email_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('EmailList') is not None:
            self.email_list = m.get('EmailList')
        return self


class ListReportPushTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, task_list=None):
        self.request_id = request_id  # type: str
        self.task_list = task_list  # type: list[ListReportPushTasksResponseBodyTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListReportPushTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListReportPushTasksResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListReportPushTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListReportPushTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListReportPushTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListReportPushTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRuleGroupsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, rule_name=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRuleGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListRuleGroupsResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRuleGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRuleGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRuleGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRuleGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRuleGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, foreground_type=None, rule_name=None,
                 rule_type=None, rule_group_id=None, risk_level=None, rule_quote=None, rule_state=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: str
        self.foreground_type = foreground_type  # type: str
        self.rule_name = rule_name  # type: str
        self.rule_type = rule_type  # type: str
        self.rule_group_id = rule_group_id  # type: str
        self.risk_level = risk_level  # type: str
        self.rule_quote = rule_quote  # type: int
        self.rule_state = rule_state  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.foreground_type is not None:
            result['ForegroundType'] = self.foreground_type
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_group_id is not None:
            result['RuleGroupId'] = self.rule_group_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rule_quote is not None:
            result['RuleQuote'] = self.rule_quote
        if self.rule_state is not None:
            result['RuleState'] = self.rule_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('ForegroundType') is not None:
            self.foreground_type = m.get('ForegroundType')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RuleQuote') is not None:
            self.rule_quote = m.get('RuleQuote')
        if m.get('RuleState') is not None:
            self.rule_state = m.get('RuleState')
        return self


class ListRulesResponseBodyServerData(TeaModel):
    def __init__(self, json_result=None):
        self.json_result = json_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRulesResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: ListRulesResponseBodyServerData

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super(ListRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = ListRulesResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class ListRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSqlTypeKeysForRuleRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSqlTypeKeysForRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListSqlTypeKeysForRuleResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSqlTypeKeysForRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSqlTypeKeysForRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSqlTypeKeysForRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSqlTypeKeysForRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSqlTypeKeysForRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSqlTypesForRuleRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, type_id=None, sqltype_1=None, key_world=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.type_id = type_id  # type: str
        self.sqltype_1 = sqltype_1  # type: str
        self.key_world = key_world  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSqlTypesForRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        if self.sqltype_1 is not None:
            result['Sqltype1'] = self.sqltype_1
        if self.key_world is not None:
            result['KeyWorld'] = self.key_world
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
        if m.get('Sqltype1') is not None:
            self.sqltype_1 = m.get('Sqltype1')
        if m.get('KeyWorld') is not None:
            self.key_world = m.get('KeyWorld')
        return self


class ListSqlTypesForRuleResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSqlTypesForRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSqlTypesForRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSqlTypesForRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSqlTypesForRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSqlTypesForRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSupportDbTypesRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSupportDbTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListSupportDbTypesResponseBodyTypeListDbVersions(TeaModel):
    def __init__(self, db_version_name=None, db_version=None):
        self.db_version_name = db_version_name  # type: str
        self.db_version = db_version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSupportDbTypesResponseBodyTypeListDbVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_version_name is not None:
            result['DbVersionName'] = self.db_version_name
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbVersionName') is not None:
            self.db_version_name = m.get('DbVersionName')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        return self


class ListSupportDbTypesResponseBodyTypeList(TeaModel):
    def __init__(self, db_type=None, db_type_name=None, db_versions=None):
        self.db_type = db_type  # type: int
        self.db_type_name = db_type_name  # type: str
        self.db_versions = db_versions  # type: list[ListSupportDbTypesResponseBodyTypeListDbVersions]

    def validate(self):
        if self.db_versions:
            for k in self.db_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSupportDbTypesResponseBodyTypeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name
        result['DbVersions'] = []
        if self.db_versions is not None:
            for k in self.db_versions:
                result['DbVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')
        self.db_versions = []
        if m.get('DbVersions') is not None:
            for k in m.get('DbVersions'):
                temp_model = ListSupportDbTypesResponseBodyTypeListDbVersions()
                self.db_versions.append(temp_model.from_map(k))
        return self


class ListSupportDbTypesResponseBody(TeaModel):
    def __init__(self, request_id=None, type_list=None):
        self.request_id = request_id  # type: str
        self.type_list = type_list  # type: list[ListSupportDbTypesResponseBodyTypeList]

    def validate(self):
        if self.type_list:
            for k in self.type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSupportDbTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TypeList'] = []
        if self.type_list is not None:
            for k in self.type_list:
                result['TypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.type_list = []
        if m.get('TypeList') is not None:
            for k in m.get('TypeList'):
                temp_model = ListSupportDbTypesResponseBodyTypeList()
                self.type_list.append(temp_model.from_map(k))
        return self


class ListSupportDbTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSupportDbTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSupportDbTypesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSupportDbTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemAlarmsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, alarm_type=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.alarm_type = alarm_type  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSystemAlarmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class ListSystemAlarmsResponseBodyAlarms(TeaModel):
    def __init__(self, read_mark=None, alarm_detail=None, alarm_type=None, alarm_id=None, create_time=None):
        self.read_mark = read_mark  # type: int
        self.alarm_detail = alarm_detail  # type: str
        self.alarm_type = alarm_type  # type: str
        self.alarm_id = alarm_id  # type: int
        self.create_time = create_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSystemAlarmsResponseBodyAlarms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.read_mark is not None:
            result['ReadMark'] = self.read_mark
        if self.alarm_detail is not None:
            result['AlarmDetail'] = self.alarm_detail
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReadMark') is not None:
            self.read_mark = m.get('ReadMark')
        if m.get('AlarmDetail') is not None:
            self.alarm_detail = m.get('AlarmDetail')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ListSystemAlarmsResponseBody(TeaModel):
    def __init__(self, request_id=None, alarms=None):
        self.request_id = request_id  # type: str
        self.alarms = alarms  # type: list[ListSystemAlarmsResponseBodyAlarms]

    def validate(self):
        if self.alarms:
            for k in self.alarms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSystemAlarmsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Alarms'] = []
        if self.alarms is not None:
            for k in self.alarms:
                result['Alarms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.alarms = []
        if m.get('Alarms') is not None:
            for k in m.get('Alarms'):
                temp_model = ListSystemAlarmsResponseBodyAlarms()
                self.alarms.append(temp_model.from_map(k))
        return self


class ListSystemAlarmsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSystemAlarmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSystemAlarmsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSystemAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemAlarmTasksRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSystemAlarmTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListSystemAlarmTasksResponseBodyTaskList(TeaModel):
    def __init__(self, task_status=None, task_id=None, create_time=None, task_name=None, to_mail_list=None):
        self.task_status = task_status  # type: int
        self.task_id = task_id  # type: int
        self.create_time = create_time  # type: str
        self.task_name = task_name  # type: str
        self.to_mail_list = to_mail_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSystemAlarmTasksResponseBodyTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        return self


class ListSystemAlarmTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, task_list=None):
        self.request_id = request_id  # type: str
        self.task_list = task_list  # type: list[ListSystemAlarmTasksResponseBodyTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSystemAlarmTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListSystemAlarmTasksResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListSystemAlarmTasksResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSystemAlarmTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSystemAlarmTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSystemAlarmTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, page_size=None, current_page=None):
        self.region_id = region_id  # type: str
        self.resource_type = resource_type  # type: str
        self.page_size = page_size  # type: int
        self.current_page = current_page  # type: int

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(self, tag_count=None, tag_key=None):
        self.tag_count = tag_count  # type: int
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysResponseBodyTagKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total_count=None, tag_keys=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.tag_keys = tag_keys  # type: list[ListTagKeysResponseBodyTagKeys]

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
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


class ListTemplatesForSqlRuleRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, sql_type_1=None, chose_condition=None, db_id=None,
                 rule_id=None, page_number=None, page_size=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.sql_type_1 = sql_type_1  # type: str
        self.chose_condition = chose_condition  # type: str
        self.db_id = db_id  # type: int
        self.rule_id = rule_id  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesForSqlRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_type_1 is not None:
            result['SqlType1'] = self.sql_type_1
        if self.chose_condition is not None:
            result['ChoseCondition'] = self.chose_condition
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlType1') is not None:
            self.sql_type_1 = m.get('SqlType1')
        if m.get('ChoseCondition') is not None:
            self.chose_condition = m.get('ChoseCondition')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTemplatesForSqlRuleResponseBodyServerData(TeaModel):
    def __init__(self, count_timely=None, black_or_white=None, sql_text=None, sqltype_1=None, sql_id=None):
        self.count_timely = count_timely  # type: str
        self.black_or_white = black_or_white  # type: int
        self.sql_text = sql_text  # type: str
        self.sqltype_1 = sqltype_1  # type: str
        self.sql_id = sql_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTemplatesForSqlRuleResponseBodyServerData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_timely is not None:
            result['CountTimely'] = self.count_timely
        if self.black_or_white is not None:
            result['BlackOrWhite'] = self.black_or_white
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        if self.sqltype_1 is not None:
            result['Sqltype1'] = self.sqltype_1
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountTimely') is not None:
            self.count_timely = m.get('CountTimely')
        if m.get('BlackOrWhite') is not None:
            self.black_or_white = m.get('BlackOrWhite')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        if m.get('Sqltype1') is not None:
            self.sqltype_1 = m.get('Sqltype1')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        return self


class ListTemplatesForSqlRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, server_data=None):
        self.request_id = request_id  # type: str
        self.server_data = server_data  # type: list[ListTemplatesForSqlRuleResponseBodyServerData]

    def validate(self):
        if self.server_data:
            for k in self.server_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTemplatesForSqlRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServerData'] = []
        if self.server_data is not None:
            for k in self.server_data:
                result['ServerData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.server_data = []
        if m.get('ServerData') is not None:
            for k in m.get('ServerData'):
                temp_model = ListTemplatesForSqlRuleResponseBodyServerData()
                self.server_data.append(temp_model.from_map(k))
        return self


class ListTemplatesForSqlRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTemplatesForSqlRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTemplatesForSqlRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTemplatesForSqlRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsedSqlTypesRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, rule_id=None, rule_type=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.rule_id = rule_id  # type: str
        self.rule_type = rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsedSqlTypesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class ListUsedSqlTypesResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsedSqlTypesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUsedSqlTypesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUsedSqlTypesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsedSqlTypesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUsedSqlTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBaseTemplateStateRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, template_state=None, template_ids=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.template_state = template_state  # type: int
        self.template_ids = template_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBaseTemplateStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_state is not None:
            result['TemplateState'] = self.template_state
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateState') is not None:
            self.template_state = m.get('TemplateState')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class ModifyBaseTemplateStateResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBaseTemplateStateResponseBody, self).to_map()
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


class ModifyBaseTemplateStateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyBaseTemplateStateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBaseTemplateStateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBaseTemplateStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCustomNameRequest(TeaModel):
    def __init__(self, source_ip=None, commodity_code=None, instance_id=None, custom_name=None):
        self.source_ip = source_ip  # type: str
        self.commodity_code = commodity_code  # type: str
        self.instance_id = instance_id  # type: str
        self.custom_name = custom_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCustomNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.custom_name is not None:
            result['CustomName'] = self.custom_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CustomName') is not None:
            self.custom_name = m.get('CustomName')
        return self


class ModifyCustomNameResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyCustomNameResponseBody, self).to_map()
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


class ModifyCustomNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyCustomNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyCustomNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCustomNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, db_name=None, db_version=None,
                 db_certificate=None, db_username=None, db_password=None, db_instance_id=None, db_addresses=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.db_name = db_name  # type: str
        self.db_version = db_version  # type: int
        self.db_certificate = db_certificate  # type: str
        self.db_username = db_username  # type: str
        self.db_password = db_password  # type: str
        self.db_instance_id = db_instance_id  # type: str
        self.db_addresses = db_addresses  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.db_certificate is not None:
            result['DbCertificate'] = self.db_certificate
        if self.db_username is not None:
            result['DbUsername'] = self.db_username
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DbCertificate') is not None:
            self.db_certificate = m.get('DbCertificate')
        if m.get('DbUsername') is not None:
            self.db_username = m.get('DbUsername')
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')
        return self


class ModifyDataSourceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceResponseBody, self).to_map()
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


class ModifyDataSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDataSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDataSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceAttributeRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, audit_mode=None, result_audit_mode=None,
                 result_audit_max_line=None, result_audit_max_size=None, db_ids=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.audit_mode = audit_mode  # type: str
        self.result_audit_mode = result_audit_mode  # type: str
        self.result_audit_max_line = result_audit_max_line  # type: int
        self.result_audit_max_size = result_audit_max_size  # type: int
        self.db_ids = db_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.audit_mode is not None:
            result['AuditMode'] = self.audit_mode
        if self.result_audit_mode is not None:
            result['ResultAuditMode'] = self.result_audit_mode
        if self.result_audit_max_line is not None:
            result['ResultAuditMaxLine'] = self.result_audit_max_line
        if self.result_audit_max_size is not None:
            result['ResultAuditMaxSize'] = self.result_audit_max_size
        if self.db_ids is not None:
            result['DbIds'] = self.db_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AuditMode') is not None:
            self.audit_mode = m.get('AuditMode')
        if m.get('ResultAuditMode') is not None:
            self.result_audit_mode = m.get('ResultAuditMode')
        if m.get('ResultAuditMaxLine') is not None:
            self.result_audit_max_line = m.get('ResultAuditMaxLine')
        if m.get('ResultAuditMaxSize') is not None:
            self.result_audit_max_size = m.get('ResultAuditMaxSize')
        if m.get('DbIds') is not None:
            self.db_ids = m.get('DbIds')
        return self


class ModifyDataSourceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDataSourceAttributeResponseBody, self).to_map()
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


class ModifyDataSourceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyDataSourceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDataSourceAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDataSourceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, description=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.description = description  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAttributeResponseBody, self).to_map()
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


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogAlarmTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, task_name=None, task_id=None, to_mail_list=None,
                 db_id_list=None, risk_level_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_name = task_name  # type: str
        self.task_id = task_id  # type: int
        self.to_mail_list = to_mail_list  # type: list[str]
        self.db_id_list = db_id_list  # type: list[str]
        self.risk_level_list = risk_level_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogAlarmTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        if self.db_id_list is not None:
            result['DbIdList'] = self.db_id_list
        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        if m.get('DbIdList') is not None:
            self.db_id_list = m.get('DbIdList')
        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')
        return self


class ModifyLogAlarmTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyLogAlarmTaskResponseBody, self).to_map()
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


class ModifyLogAlarmTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyLogAlarmTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyLogAlarmTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyLogAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPlanRequest(TeaModel):
    def __init__(self, commodity_code=None, instance_id=None, region_id=None):
        self.commodity_code = commodity_code  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyPlanResponseBody, self).to_map()
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


class ModifyPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReportPushTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, job_id=None, schedule_type=None, schedule_time=None,
                 job_status=None, report_type=None, db_list=None, email_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.job_id = job_id  # type: int
        self.schedule_type = schedule_type  # type: str
        self.schedule_time = schedule_time  # type: str
        self.job_status = job_status  # type: int
        self.report_type = report_type  # type: list[str]
        self.db_list = db_list  # type: list[str]
        self.email_list = email_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyReportPushTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.email_list is not None:
            result['EmailList'] = self.email_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('EmailList') is not None:
            self.email_list = m.get('EmailList')
        return self


class ModifyReportPushTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyReportPushTaskResponseBody, self).to_map()
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


class ModifyReportPushTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyReportPushTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyReportPushTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyReportPushTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleGroupRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, group_id=None, group_name=None, group_type=None,
                 group_key_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.group_type = group_type  # type: str
        self.group_key_id = group_key_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRuleGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_key_id is not None:
            result['GroupKeyId'] = self.group_key_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupKeyId') is not None:
            self.group_key_id = m.get('GroupKeyId')
        return self


class ModifyRuleGroupResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyRuleGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyRuleGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyRuleGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyRuleGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySystemAlarmTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, task_name=None, task_id=None, to_mail_list=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_name = task_name  # type: str
        self.task_id = task_id  # type: int
        self.to_mail_list = to_mail_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySystemAlarmTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        return self


class ModifySystemAlarmTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifySystemAlarmTaskResponseBody, self).to_map()
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


class ModifySystemAlarmTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifySystemAlarmTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifySystemAlarmTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySystemAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, resource_id=None, resource_group_id=None, resource_type=None, region_id=None):
        self.resource_id = resource_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_type = resource_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
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


class PciReportRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PciReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class PciReportResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PciReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PciReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PciReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PciReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PciReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutLoginCountRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutLoginCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class PutLoginCountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutLoginCountResponseBody, self).to_map()
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


class PutLoginCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PutLoginCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutLoginCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PutLoginCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadMarkSystemAlarmsRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, alarm_ids=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.alarm_ids = alarm_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReadMarkSystemAlarmsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.alarm_ids is not None:
            result['AlarmIds'] = self.alarm_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AlarmIds') is not None:
            self.alarm_ids = m.get('AlarmIds')
        return self


class ReadMarkSystemAlarmsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReadMarkSystemAlarmsResponseBody, self).to_map()
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


class ReadMarkSystemAlarmsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReadMarkSystemAlarmsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReadMarkSystemAlarmsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReadMarkSystemAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, service_code=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.service_code = service_code  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RefundInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefundInstanceResponseBody, self).to_map()
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


class RefundInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefundInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefundInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefundInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterNoticeMailRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mail=None, vcode=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mail = mail  # type: str
        self.vcode = vcode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterNoticeMailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mail is not None:
            result['Mail'] = self.mail
        if self.vcode is not None:
            result['Vcode'] = self.vcode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        if m.get('Vcode') is not None:
            self.vcode = m.get('Vcode')
        return self


class RegisterNoticeMailResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterNoticeMailResponseBody, self).to_map()
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


class RegisterNoticeMailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RegisterNoticeMailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterNoticeMailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RegisterNoticeMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveLogMaskConfigRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mask_id=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mask_id = mask_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveLogMaskConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id is not None:
            result['MaskId'] = self.mask_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskId') is not None:
            self.mask_id = m.get('MaskId')
        return self


class RemoveLogMaskConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveLogMaskConfigResponseBody, self).to_map()
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


class RemoveLogMaskConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveLogMaskConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveLogMaskConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveLogMaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerifyCodeMailRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, mail=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mail = mail  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerifyCodeMailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mail is not None:
            result['Mail'] = self.mail
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        return self


class SendVerifyCodeMailResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerifyCodeMailResponseBody, self).to_map()
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


class SendVerifyCodeMailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendVerifyCodeMailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendVerifyCodeMailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SendVerifyCodeMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SoxReportRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, db_id=None, begin_date=None, end_date=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.db_id = db_id  # type: int
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SoxReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class SoxReportResponseBody(TeaModel):
    def __init__(self, server_data=None, request_id=None):
        self.server_data = server_data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SoxReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SoxReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SoxReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SoxReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SoxReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAlarmTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, task_ids=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartAlarmTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class StartAlarmTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartAlarmTaskResponseBody, self).to_map()
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


class StartAlarmTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartAlarmTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartAlarmTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, vswitch_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceResponseBody, self).to_map()
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


class StartInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAlarmTaskRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, task_ids=None):
        self.region_id = region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.task_ids = task_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAlarmTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class StopAlarmTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAlarmTaskResponseBody, self).to_map()
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


class StopAlarmTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopAlarmTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopAlarmTaskResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopAlarmTaskResponseBody()
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


class UpgradeInstanceVersionRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeInstanceVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpgradeInstanceVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeInstanceVersionResponseBody, self).to_map()
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


class UpgradeInstanceVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeInstanceVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeInstanceVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeInstanceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


