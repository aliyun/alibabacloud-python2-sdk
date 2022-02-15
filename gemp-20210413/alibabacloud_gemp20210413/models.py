# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddProblemServiceGroupRequest(TeaModel):
    def __init__(self, problem_id=None, service_group_ids=None):
        # 故障ID
        self.problem_id = problem_id  # type: long
        # 应急协同组
        self.service_group_ids = service_group_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProblemServiceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.service_group_ids is not None:
            result['serviceGroupIds'] = self.service_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('serviceGroupIds') is not None:
            self.service_group_ids = m.get('serviceGroupIds')
        return self


class AddProblemServiceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddProblemServiceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddProblemServiceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddProblemServiceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddProblemServiceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddProblemServiceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelProblemRequest(TeaModel):
    def __init__(self, cancel_reason=None, cancel_reason_description=None, client_token=None, problem_id=None,
                 problem_notify_type=None):
        # 取消原因
        self.cancel_reason = cancel_reason  # type: long
        # 取消原因描述
        self.cancel_reason_description = cancel_reason_description  # type: str
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 故障id
        self.problem_id = problem_id  # type: long
        # PROBLEM_NOTIFY	通告类型 PROBLEM_NOTIFY：故障通告 PROBLEM_UPDATE：故障更新 PROBLEM_UPGRADE：故障升级 PROBLEM_DEGRADE：故障降级 PROBLEM_RECOVER：故障恢复 PROBLEM_REISSUE： 故障补发 PROBLEM_CANCEL：故障取消
        self.problem_notify_type = problem_notify_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelProblemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancel_reason is not None:
            result['cancelReason'] = self.cancel_reason
        if self.cancel_reason_description is not None:
            result['cancelReasonDescription'] = self.cancel_reason_description
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_notify_type is not None:
            result['problemNotifyType'] = self.problem_notify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cancelReason') is not None:
            self.cancel_reason = m.get('cancelReason')
        if m.get('cancelReasonDescription') is not None:
            self.cancel_reason_description = m.get('cancelReasonDescription')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemNotifyType') is not None:
            self.problem_notify_type = m.get('problemNotifyType')
        return self


class CancelProblemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelProblemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelProblemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelProblemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelProblemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelProblemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckWebhookRequest(TeaModel):
    def __init__(self, client_token=None, webhook=None, webhook_type=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # webook地址
        self.webhook = webhook  # type: str
        # webhook地址类型 企业微信WEIXIN_GROUP 钉钉群 DING_GROUP 飞书 FEISHU_GROUP
        self.webhook_type = webhook_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.webhook is not None:
            result['webhook'] = self.webhook
        if self.webhook_type is not None:
            result['webhookType'] = self.webhook_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        if m.get('webhookType') is not None:
            self.webhook_type = m.get('webhookType')
        return self


class CheckWebhookResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CheckWebhookResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CheckWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckWebhookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmIntegrationConfigRequest(TeaModel):
    def __init__(self, client_token=None, integration_config_id=None):
        # 幂等id
        self.client_token = client_token  # type: str
        self.integration_config_id = integration_config_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmIntegrationConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        return self


class ConfirmIntegrationConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmIntegrationConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ConfirmIntegrationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConfirmIntegrationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmIntegrationConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfirmIntegrationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEscalationPlanRequestEscalationPlanRulesEscalationPlanConditions(TeaModel):
    def __init__(self, effection=None, level=None):
        # 影响等级
        self.effection = effection  # type: str
        # 事件等级
        self.level = level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEscalationPlanRequestEscalationPlanRulesEscalationPlanConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effection is not None:
            result['effection'] = self.effection
        if self.level is not None:
            result['level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('level') is not None:
            self.level = m.get('level')
        return self


class CreateEscalationPlanRequestEscalationPlanRulesEscalationPlanStrategies(TeaModel):
    def __init__(self, enable_webhook=None, notice_channels=None, notice_objects=None, notice_time=None,
                 service_group_ids=None):
        # 是否支持群通知
        self.enable_webhook = enable_webhook  # type: bool
        # 升级通知策略
        self.notice_channels = notice_channels  # type: list[str]
        # 升级通知对象id列表
        self.notice_objects = notice_objects  # type: list[long]
        # 通知时间
        self.notice_time = notice_time  # type: str
        # 服务组id
        self.service_group_ids = service_group_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEscalationPlanRequestEscalationPlanRulesEscalationPlanStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_webhook is not None:
            result['enableWebhook'] = self.enable_webhook
        if self.notice_channels is not None:
            result['noticeChannels'] = self.notice_channels
        if self.notice_objects is not None:
            result['noticeObjects'] = self.notice_objects
        if self.notice_time is not None:
            result['noticeTime'] = self.notice_time
        if self.service_group_ids is not None:
            result['serviceGroupIds'] = self.service_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableWebhook') is not None:
            self.enable_webhook = m.get('enableWebhook')
        if m.get('noticeChannels') is not None:
            self.notice_channels = m.get('noticeChannels')
        if m.get('noticeObjects') is not None:
            self.notice_objects = m.get('noticeObjects')
        if m.get('noticeTime') is not None:
            self.notice_time = m.get('noticeTime')
        if m.get('serviceGroupIds') is not None:
            self.service_group_ids = m.get('serviceGroupIds')
        return self


class CreateEscalationPlanRequestEscalationPlanRules(TeaModel):
    def __init__(self, escalation_plan_conditions=None, escalation_plan_strategies=None,
                 escalation_plan_type=None):
        # 升级条件
        self.escalation_plan_conditions = escalation_plan_conditions  # type: list[CreateEscalationPlanRequestEscalationPlanRulesEscalationPlanConditions]
        # 升级策略
        self.escalation_plan_strategies = escalation_plan_strategies  # type: list[CreateEscalationPlanRequestEscalationPlanRulesEscalationPlanStrategies]
        # 升级类型
        self.escalation_plan_type = escalation_plan_type  # type: str

    def validate(self):
        if self.escalation_plan_conditions:
            for k in self.escalation_plan_conditions:
                if k:
                    k.validate()
        if self.escalation_plan_strategies:
            for k in self.escalation_plan_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEscalationPlanRequestEscalationPlanRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['escalationPlanConditions'] = []
        if self.escalation_plan_conditions is not None:
            for k in self.escalation_plan_conditions:
                result['escalationPlanConditions'].append(k.to_map() if k else None)
        result['escalationPlanStrategies'] = []
        if self.escalation_plan_strategies is not None:
            for k in self.escalation_plan_strategies:
                result['escalationPlanStrategies'].append(k.to_map() if k else None)
        if self.escalation_plan_type is not None:
            result['escalationPlanType'] = self.escalation_plan_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.escalation_plan_conditions = []
        if m.get('escalationPlanConditions') is not None:
            for k in m.get('escalationPlanConditions'):
                temp_model = CreateEscalationPlanRequestEscalationPlanRulesEscalationPlanConditions()
                self.escalation_plan_conditions.append(temp_model.from_map(k))
        self.escalation_plan_strategies = []
        if m.get('escalationPlanStrategies') is not None:
            for k in m.get('escalationPlanStrategies'):
                temp_model = CreateEscalationPlanRequestEscalationPlanRulesEscalationPlanStrategies()
                self.escalation_plan_strategies.append(temp_model.from_map(k))
        if m.get('escalationPlanType') is not None:
            self.escalation_plan_type = m.get('escalationPlanType')
        return self


class CreateEscalationPlanRequestEscalationPlanScopeObjects(TeaModel):
    def __init__(self, scope=None, scope_object_id=None):
        # 范围对象类型
        self.scope = scope  # type: str
        # 范围对象id
        self.scope_object_id = scope_object_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEscalationPlanRequestEscalationPlanScopeObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        if self.scope_object_id is not None:
            result['scopeObjectId'] = self.scope_object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scopeObjectId') is not None:
            self.scope_object_id = m.get('scopeObjectId')
        return self


class CreateEscalationPlanRequest(TeaModel):
    def __init__(self, client_token=None, escalation_plan_description=None, escalation_plan_name=None,
                 escalation_plan_rules=None, escalation_plan_scope_objects=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 升级计划描述
        self.escalation_plan_description = escalation_plan_description  # type: str
        # 升级计划名称
        self.escalation_plan_name = escalation_plan_name  # type: str
        # 升级计划规则列表
        self.escalation_plan_rules = escalation_plan_rules  # type: list[CreateEscalationPlanRequestEscalationPlanRules]
        # 升级计划范围对象列表
        self.escalation_plan_scope_objects = escalation_plan_scope_objects  # type: list[CreateEscalationPlanRequestEscalationPlanScopeObjects]

    def validate(self):
        if self.escalation_plan_rules:
            for k in self.escalation_plan_rules:
                if k:
                    k.validate()
        if self.escalation_plan_scope_objects:
            for k in self.escalation_plan_scope_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEscalationPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.escalation_plan_description is not None:
            result['escalationPlanDescription'] = self.escalation_plan_description
        if self.escalation_plan_name is not None:
            result['escalationPlanName'] = self.escalation_plan_name
        result['escalationPlanRules'] = []
        if self.escalation_plan_rules is not None:
            for k in self.escalation_plan_rules:
                result['escalationPlanRules'].append(k.to_map() if k else None)
        result['escalationPlanScopeObjects'] = []
        if self.escalation_plan_scope_objects is not None:
            for k in self.escalation_plan_scope_objects:
                result['escalationPlanScopeObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('escalationPlanDescription') is not None:
            self.escalation_plan_description = m.get('escalationPlanDescription')
        if m.get('escalationPlanName') is not None:
            self.escalation_plan_name = m.get('escalationPlanName')
        self.escalation_plan_rules = []
        if m.get('escalationPlanRules') is not None:
            for k in m.get('escalationPlanRules'):
                temp_model = CreateEscalationPlanRequestEscalationPlanRules()
                self.escalation_plan_rules.append(temp_model.from_map(k))
        self.escalation_plan_scope_objects = []
        if m.get('escalationPlanScopeObjects') is not None:
            for k in m.get('escalationPlanScopeObjects'):
                temp_model = CreateEscalationPlanRequestEscalationPlanScopeObjects()
                self.escalation_plan_scope_objects.append(temp_model.from_map(k))
        return self


class CreateEscalationPlanResponseBodyData(TeaModel):
    def __init__(self, escalation_plan_id=None):
        # 升级计划id
        self.escalation_plan_id = escalation_plan_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEscalationPlanResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        return self


class CreateEscalationPlanResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: CreateEscalationPlanResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateEscalationPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateEscalationPlanResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateEscalationPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateEscalationPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEscalationPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateEscalationPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIncidentRequest(TeaModel):
    def __init__(self, assign_user_id=None, channels=None, client_token=None, effect=None,
                 incident_description=None, incident_level=None, incident_title=None, related_service_id=None, service_group_id=None):
        # 分派的用户ID
        self.assign_user_id = assign_user_id  # type: long
        # 通知渠道     SMS 短信   EMAIL 邮件   PHONE  电话  WEIXIN_GROUP企微群 DING_GROUP 钉钉群
        self.channels = channels  # type: list[str]
        # 幂等UUID
        self.client_token = client_token  # type: str
        # 影响等级 高：HIGH 低 LOW
        self.effect = effect  # type: str
        # 事件描述
        self.incident_description = incident_description  # type: str
        # P1	事件级别 P1 P2 P3 P4
        self.incident_level = incident_level  # type: str
        # 事件标题
        self.incident_title = incident_title  # type: str
        # 关联服务ID
        self.related_service_id = related_service_id  # type: long
        # 服务组Id
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIncidentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_user_id is not None:
            result['assignUserId'] = self.assign_user_id
        if self.channels is not None:
            result['channels'] = self.channels
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.effect is not None:
            result['effect'] = self.effect
        if self.incident_description is not None:
            result['incidentDescription'] = self.incident_description
        if self.incident_level is not None:
            result['incidentLevel'] = self.incident_level
        if self.incident_title is not None:
            result['incidentTitle'] = self.incident_title
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignUserId') is not None:
            self.assign_user_id = m.get('assignUserId')
        if m.get('channels') is not None:
            self.channels = m.get('channels')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('incidentDescription') is not None:
            self.incident_description = m.get('incidentDescription')
        if m.get('incidentLevel') is not None:
            self.incident_level = m.get('incidentLevel')
        if m.get('incidentTitle') is not None:
            self.incident_title = m.get('incidentTitle')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class CreateIncidentResponseBodyData(TeaModel):
    def __init__(self, incident_id=None):
        # 事件主健Id
        self.incident_id = incident_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIncidentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        return self


class CreateIncidentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Id of the request
        self.data = data  # type: CreateIncidentResponseBodyData
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateIncidentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateIncidentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateIncidentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIncidentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIncidentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIncidentSubtotalRequest(TeaModel):
    def __init__(self, client_token=None, description=None, incident_id=None):
        # 幂等校验Id
        self.client_token = client_token  # type: str
        # 描述
        self.description = description  # type: str
        # 事件id
        self.incident_id = incident_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIncidentSubtotalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        return self


class CreateIncidentSubtotalResponseBodyData(TeaModel):
    def __init__(self, subtotal_id=None):
        # 小计Id
        self.subtotal_id = subtotal_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIncidentSubtotalResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subtotal_id is not None:
            result['subtotalId'] = self.subtotal_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('subtotalId') is not None:
            self.subtotal_id = m.get('subtotalId')
        return self


class CreateIncidentSubtotalResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateIncidentSubtotalResponseBodyData
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateIncidentSubtotalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateIncidentSubtotalResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateIncidentSubtotalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIncidentSubtotalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIncidentSubtotalResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIncidentSubtotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntegrationConfigRequest(TeaModel):
    def __init__(self, client_token=None, monitor_source_id=None):
        self.client_token = client_token  # type: str
        self.monitor_source_id = monitor_source_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntegrationConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        return self


class CreateIntegrationConfigResponseBodyData(TeaModel):
    def __init__(self, integration_config_id=None):
        # 集成配置id
        self.integration_config_id = integration_config_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIntegrationConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        return self


class CreateIntegrationConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateIntegrationConfigResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateIntegrationConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateIntegrationConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateIntegrationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateIntegrationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIntegrationConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIntegrationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProblemRequest(TeaModel):
    def __init__(self, affect_service_ids=None, client_token=None, discover_time=None, incident_id=None,
                 main_handler_id=None, preliminary_reason=None, problem_level=None, problem_name=None, problem_notify_type=None,
                 problem_status=None, progress_summary=None, progress_summary_rich_text_id=None, recovery_time=None,
                 related_service_id=None, service_group_ids=None):
        # 影响服务列表
        self.affect_service_ids = affect_service_ids  # type: list[long]
        # 幂等校验Id
        self.client_token = client_token  # type: str
        # 发现时间 (XXXX-XX-XX 00:00:00)
        self.discover_time = discover_time  # type: str
        # 事件id
        self.incident_id = incident_id  # type: long
        # 主要处理人
        self.main_handler_id = main_handler_id  # type: long
        # 初步原因
        self.preliminary_reason = preliminary_reason  # type: str
        # 故障等级 1=P1 2=P2 3=P3 4=P4
        self.problem_level = problem_level  # type: str
        # 故障名称
        self.problem_name = problem_name  # type: str
        # 通告类型
        self.problem_notify_type = problem_notify_type  # type: str
        # 故障状态  HANDLING 处理中 RECOVERED 已恢复  REPLAYING 复盘中  REPLAYED 已复盘 CANCEL 已取消
        self.problem_status = problem_status  # type: str
        # 进展摘要
        self.progress_summary = progress_summary  # type: str
        # 进展摘要富文本id
        self.progress_summary_rich_text_id = progress_summary_rich_text_id  # type: long
        # 恢复时间
        self.recovery_time = recovery_time  # type: str
        # 所属服务
        self.related_service_id = related_service_id  # type: long
        # 应急协同组
        self.service_group_ids = service_group_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_service_ids is not None:
            result['affectServiceIds'] = self.affect_service_ids
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.discover_time is not None:
            result['discoverTime'] = self.discover_time
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.main_handler_id is not None:
            result['mainHandlerId'] = self.main_handler_id
        if self.preliminary_reason is not None:
            result['preliminaryReason'] = self.preliminary_reason
        if self.problem_level is not None:
            result['problemLevel'] = self.problem_level
        if self.problem_name is not None:
            result['problemName'] = self.problem_name
        if self.problem_notify_type is not None:
            result['problemNotifyType'] = self.problem_notify_type
        if self.problem_status is not None:
            result['problemStatus'] = self.problem_status
        if self.progress_summary is not None:
            result['progressSummary'] = self.progress_summary
        if self.progress_summary_rich_text_id is not None:
            result['progressSummaryRichTextId'] = self.progress_summary_rich_text_id
        if self.recovery_time is not None:
            result['recoveryTime'] = self.recovery_time
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.service_group_ids is not None:
            result['serviceGroupIds'] = self.service_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('affectServiceIds') is not None:
            self.affect_service_ids = m.get('affectServiceIds')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('discoverTime') is not None:
            self.discover_time = m.get('discoverTime')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('mainHandlerId') is not None:
            self.main_handler_id = m.get('mainHandlerId')
        if m.get('preliminaryReason') is not None:
            self.preliminary_reason = m.get('preliminaryReason')
        if m.get('problemLevel') is not None:
            self.problem_level = m.get('problemLevel')
        if m.get('problemName') is not None:
            self.problem_name = m.get('problemName')
        if m.get('problemNotifyType') is not None:
            self.problem_notify_type = m.get('problemNotifyType')
        if m.get('problemStatus') is not None:
            self.problem_status = m.get('problemStatus')
        if m.get('progressSummary') is not None:
            self.progress_summary = m.get('progressSummary')
        if m.get('progressSummaryRichTextId') is not None:
            self.progress_summary_rich_text_id = m.get('progressSummaryRichTextId')
        if m.get('recoveryTime') is not None:
            self.recovery_time = m.get('recoveryTime')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('serviceGroupIds') is not None:
            self.service_group_ids = m.get('serviceGroupIds')
        return self


class CreateProblemResponseBodyData(TeaModel):
    def __init__(self, problem_id=None):
        # 故障Id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class CreateProblemResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateProblemResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProblemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateProblemResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProblemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProblemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProblemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProblemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProblemEffectionServiceRequest(TeaModel):
    def __init__(self, client_token=None, description=None, level=None, picture_url=None, problem_id=None,
                 service_id=None, status=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 影响描述
        self.description = description  # type: str
        # 影响等级
        self.level = level  # type: str
        # 图片地址
        self.picture_url = picture_url  # type: list[str]
        # 故障id
        self.problem_id = problem_id  # type: long
        # 影响服务id
        self.service_id = service_id  # type: long
        # 影响状态 0 未恢复 1已恢复
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemEffectionServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.level is not None:
            result['level'] = self.level
        if self.picture_url is not None:
            result['pictureUrl'] = self.picture_url
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('pictureUrl') is not None:
            self.picture_url = m.get('pictureUrl')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateProblemEffectionServiceResponseBodyData(TeaModel):
    def __init__(self, effection_service_id=None):
        # 影响服务id
        self.effection_service_id = effection_service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemEffectionServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effection_service_id is not None:
            result['effectionServiceId'] = self.effection_service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effectionServiceId') is not None:
            self.effection_service_id = m.get('effectionServiceId')
        return self


class CreateProblemEffectionServiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateProblemEffectionServiceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProblemEffectionServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateProblemEffectionServiceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProblemEffectionServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProblemEffectionServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProblemEffectionServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProblemEffectionServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProblemMeasureRequest(TeaModel):
    def __init__(self, check_standard=None, check_user_id=None, client_token=None, content=None, director_id=None,
                 plan_finish_time=None, problem_id=None, stalker_id=None, status=None, type=None):
        # 验收标准
        self.check_standard = check_standard  # type: str
        # 验收人id
        self.check_user_id = check_user_id  # type: long
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 措施内容
        self.content = content  # type: str
        # 负责人id
        self.director_id = director_id  # type: long
        # 计划完成时间
        self.plan_finish_time = plan_finish_time  # type: str
        # 故障Id
        self.problem_id = problem_id  # type: long
        # 跟踪人id
        self.stalker_id = stalker_id  # type: long
        # 状态 IMPROVED 改进 2 未改进UNIMPROVED
        self.status = status  # type: str
        # 措施类型
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemMeasureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_standard is not None:
            result['checkStandard'] = self.check_standard
        if self.check_user_id is not None:
            result['checkUserId'] = self.check_user_id
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.content is not None:
            result['content'] = self.content
        if self.director_id is not None:
            result['directorId'] = self.director_id
        if self.plan_finish_time is not None:
            result['planFinishTime'] = self.plan_finish_time
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.stalker_id is not None:
            result['stalkerId'] = self.stalker_id
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('checkStandard') is not None:
            self.check_standard = m.get('checkStandard')
        if m.get('checkUserId') is not None:
            self.check_user_id = m.get('checkUserId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('directorId') is not None:
            self.director_id = m.get('directorId')
        if m.get('planFinishTime') is not None:
            self.plan_finish_time = m.get('planFinishTime')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('stalkerId') is not None:
            self.stalker_id = m.get('stalkerId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateProblemMeasureResponseBodyData(TeaModel):
    def __init__(self, measure_id=None):
        # 故障措施Id
        self.measure_id = measure_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemMeasureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.measure_id is not None:
            result['measureId'] = self.measure_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('measureId') is not None:
            self.measure_id = m.get('measureId')
        return self


class CreateProblemMeasureResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateProblemMeasureResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProblemMeasureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateProblemMeasureResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProblemMeasureResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProblemMeasureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProblemMeasureResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProblemMeasureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProblemSubtotalRequest(TeaModel):
    def __init__(self, client_token=None, description=None, problem_id=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 小计文本
        self.description = description  # type: str
        # 故障Id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemSubtotalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class CreateProblemSubtotalResponseBodyData(TeaModel):
    def __init__(self, subtotal_id=None):
        # 小计id
        self.subtotal_id = subtotal_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemSubtotalResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subtotal_id is not None:
            result['subtotalId'] = self.subtotal_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('subtotalId') is not None:
            self.subtotal_id = m.get('subtotalId')
        return self


class CreateProblemSubtotalResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateProblemSubtotalResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProblemSubtotalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateProblemSubtotalResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProblemSubtotalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProblemSubtotalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProblemSubtotalResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProblemSubtotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProblemTimelineRequest(TeaModel):
    def __init__(self, client_token=None, content=None, key_node=None, problem_id=None, time=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 节点内容
        self.content = content  # type: str
        # 关键节点 码表:PROBLEM_KEY_NODE (逗号分隔)
        self.key_node = key_node  # type: str
        # 故障id
        self.problem_id = problem_id  # type: long
        # 发生时间
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemTimelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.content is not None:
            result['content'] = self.content
        if self.key_node is not None:
            result['keyNode'] = self.key_node
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('keyNode') is not None:
            self.key_node = m.get('keyNode')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class CreateProblemTimelineResponseBodyData(TeaModel):
    def __init__(self, problem_timeline_id=None):
        # 故障事件线id
        self.problem_timeline_id = problem_timeline_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemTimelineResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.problem_timeline_id is not None:
            result['problemTimelineId'] = self.problem_timeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('problemTimelineId') is not None:
            self.problem_timeline_id = m.get('problemTimelineId')
        return self


class CreateProblemTimelineResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # Object
        self.data = data  # type: CreateProblemTimelineResponseBodyData
        # id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProblemTimelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateProblemTimelineResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProblemTimelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProblemTimelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProblemTimelineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProblemTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProblemTimelinesRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None, timeline_nodes=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 故障id
        self.problem_id = problem_id  # type: long
        # 时间线节点
        self.timeline_nodes = timeline_nodes  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemTimelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.timeline_nodes is not None:
            result['timelineNodes'] = self.timeline_nodes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('timelineNodes') is not None:
            self.timeline_nodes = m.get('timelineNodes')
        return self


class CreateProblemTimelinesResponseBodyData(TeaModel):
    def __init__(self, problem_timeline_ids=None):
        self.problem_timeline_ids = problem_timeline_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProblemTimelinesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.problem_timeline_ids is not None:
            result['problemTimelineIds'] = self.problem_timeline_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('problemTimelineIds') is not None:
            self.problem_timeline_ids = m.get('problemTimelineIds')
        return self


class CreateProblemTimelinesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateProblemTimelinesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProblemTimelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateProblemTimelinesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProblemTimelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateProblemTimelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProblemTimelinesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateProblemTimelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRichTextRequest(TeaModel):
    def __init__(self, instance_id=None, instance_type=None, rich_text=None):
        # 资源id
        self.instance_id = instance_id  # type: long
        # 资源类型
        self.instance_type = instance_type  # type: str
        # 文本内容
        self.rich_text = rich_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRichTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.rich_text is not None:
            result['richText'] = self.rich_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('richText') is not None:
            self.rich_text = m.get('richText')
        return self


class CreateRichTextResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, instance_type=None, rich_text=None):
        # 资源id
        self.instance_id = instance_id  # type: long
        # 资源类型
        self.instance_type = instance_type  # type: long
        # 富文本内容
        self.rich_text = rich_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRichTextResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.rich_text is not None:
            result['richText'] = self.rich_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('richText') is not None:
            self.rich_text = m.get('richText')
        return self


class CreateRichTextResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: CreateRichTextResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateRichTextResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateRichTextResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRichTextResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRichTextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRichTextResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRichTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRouteRuleRequestRouteChildRulesConditions(TeaModel):
    def __init__(self, key=None, operation_symbol=None, value=None):
        # 字段名称
        self.key = key  # type: str
        # 操作符号：notContain 不包含；contain 包含；equals 等于；notEquals 不等于；
        self.operation_symbol = operation_symbol  # type: str
        # 字段值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRouteRuleRequestRouteChildRulesConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operation_symbol is not None:
            result['operationSymbol'] = self.operation_symbol
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operationSymbol') is not None:
            self.operation_symbol = m.get('operationSymbol')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateRouteRuleRequestRouteChildRules(TeaModel):
    def __init__(self, child_condition_relation=None, conditions=None, monitor_source_id=None):
        # 0-与，1-或
        self.child_condition_relation = child_condition_relation  # type: long
        # 条件
        self.conditions = conditions  # type: list[CreateRouteRuleRequestRouteChildRulesConditions]
        # 监控源ID
        self.monitor_source_id = monitor_source_id  # type: long

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateRouteRuleRequestRouteChildRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_condition_relation is not None:
            result['childConditionRelation'] = self.child_condition_relation
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('childConditionRelation') is not None:
            self.child_condition_relation = m.get('childConditionRelation')
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = CreateRouteRuleRequestRouteChildRulesConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        return self


class CreateRouteRuleRequest(TeaModel):
    def __init__(self, assign_object_id=None, assign_object_type=None, child_rule_relation=None, client_token=None,
                 effection=None, enable_status=None, incident_level=None, match_count=None, notify_channels=None,
                 related_service_id=None, route_child_rules=None, route_type=None, rule_name=None, time_window=None,
                 time_window_unit=None):
        # 事件分派对象ID（服务组ID 或用户ID）
        self.assign_object_id = assign_object_id  # type: long
        # 事件分派对象类型 SERVICEGROUP服务组 USER 单个用户
        self.assign_object_type = assign_object_type  # type: str
        # 子规则关系AND,OR
        self.child_rule_relation = child_rule_relation  # type: str
        # 幂等号
        self.client_token = client_token  # type: str
        # 影响程度 LOW-一般 HIGH-严重
        self.effection = effection  # type: str
        # 启用状态
        self.enable_status = enable_status  # type: str
        # 事件级别 P1 P2 P3 P4
        self.incident_level = incident_level  # type: str
        # 命中次数
        self.match_count = match_count  # type: int
        # 通知渠道。 SMS 短信  EMAIL 邮件  PHONE电话  WEIXIN_GROUP 企微群 DING_GROUP钉钉群
        self.notify_channels = notify_channels  # type: list[str]
        # 关联服务ID
        self.related_service_id = related_service_id  # type: long
        # 子规则
        self.route_child_rules = route_child_rules  # type: list[CreateRouteRuleRequestRouteChildRules]
        # 路由类型：INCIDENT 触发事件 ALERT仅触发报警
        self.route_type = route_type  # type: str
        # 规则名称
        self.rule_name = rule_name  # type: bytes
        # 时间窗口
        self.time_window = time_window  # type: long
        # 时间窗口单位 MINUTE  分钟  SECOND 秒
        self.time_window_unit = time_window_unit  # type: str

    def validate(self):
        if self.route_child_rules:
            for k in self.route_child_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateRouteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_object_id is not None:
            result['assignObjectId'] = self.assign_object_id
        if self.assign_object_type is not None:
            result['assignObjectType'] = self.assign_object_type
        if self.child_rule_relation is not None:
            result['childRuleRelation'] = self.child_rule_relation
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.effection is not None:
            result['effection'] = self.effection
        if self.enable_status is not None:
            result['enableStatus'] = self.enable_status
        if self.incident_level is not None:
            result['incidentLevel'] = self.incident_level
        if self.match_count is not None:
            result['matchCount'] = self.match_count
        if self.notify_channels is not None:
            result['notifyChannels'] = self.notify_channels
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        result['routeChildRules'] = []
        if self.route_child_rules is not None:
            for k in self.route_child_rules:
                result['routeChildRules'].append(k.to_map() if k else None)
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.time_window is not None:
            result['timeWindow'] = self.time_window
        if self.time_window_unit is not None:
            result['timeWindowUnit'] = self.time_window_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignObjectId') is not None:
            self.assign_object_id = m.get('assignObjectId')
        if m.get('assignObjectType') is not None:
            self.assign_object_type = m.get('assignObjectType')
        if m.get('childRuleRelation') is not None:
            self.child_rule_relation = m.get('childRuleRelation')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('enableStatus') is not None:
            self.enable_status = m.get('enableStatus')
        if m.get('incidentLevel') is not None:
            self.incident_level = m.get('incidentLevel')
        if m.get('matchCount') is not None:
            self.match_count = m.get('matchCount')
        if m.get('notifyChannels') is not None:
            self.notify_channels = m.get('notifyChannels')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        self.route_child_rules = []
        if m.get('routeChildRules') is not None:
            for k in m.get('routeChildRules'):
                temp_model = CreateRouteRuleRequestRouteChildRules()
                self.route_child_rules.append(temp_model.from_map(k))
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('timeWindow') is not None:
            self.time_window = m.get('timeWindow')
        if m.get('timeWindowUnit') is not None:
            self.time_window_unit = m.get('timeWindowUnit')
        return self


class CreateRouteRuleResponseBodyData(TeaModel):
    def __init__(self, route_rule_id=None):
        # 规则ID
        self.route_rule_id = route_rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRouteRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        return self


class CreateRouteRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 结果
        self.data = data  # type: CreateRouteRuleResponseBodyData
        # 请求
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateRouteRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateRouteRuleResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRouteRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRouteRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRouteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(self, client_token=None, service_description=None, service_name=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务描述
        self.service_description = service_description  # type: str
        # 服务名称
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_description is not None:
            result['serviceDescription'] = self.service_description
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceDescription') is not None:
            self.service_description = m.get('serviceDescription')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class CreateServiceResponseBodyData(TeaModel):
    def __init__(self, service_id=None):
        # 服务ID
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 服务ID
        self.data = data  # type: CreateServiceResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateServiceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceGroupRequestMonitorSourceTemplates(TeaModel):
    def __init__(self, monitor_source_id=None, monitor_source_name=None, template_content=None, template_id=None):
        # 监控源ID
        self.monitor_source_id = monitor_source_id  # type: long
        # 监控源名字
        self.monitor_source_name = monitor_source_name  # type: str
        # 模板内容
        self.template_content = template_content  # type: str
        # 消息模版ID
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceGroupRequestMonitorSourceTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        if self.template_content is not None:
            result['templateContent'] = self.template_content
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        if m.get('templateContent') is not None:
            self.template_content = m.get('templateContent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class CreateServiceGroupRequest(TeaModel):
    def __init__(self, client_token=None, enable_webhook=None, monitor_source_templates=None,
                 service_group_description=None, service_group_name=None, user_ids=None, webhook_link=None, webhook_type=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # ENABLE 启用 DISABLE 禁用
        self.enable_webhook = enable_webhook  # type: str
        # 监控源消息模版
        self.monitor_source_templates = monitor_source_templates  # type: list[CreateServiceGroupRequestMonitorSourceTemplates]
        # 服务描述
        self.service_group_description = service_group_description  # type: str
        # 服务小组名称
        self.service_group_name = service_group_name  # type: str
        # 小组人员用户ID
        self.user_ids = user_ids  # type: list[long]
        # webhookLink
        self.webhook_link = webhook_link  # type: str
        # WEIXIN_GROUP微信 DING_GROUP钉钉 FEISHU_GROUP飞书
        self.webhook_type = webhook_type  # type: str

    def validate(self):
        if self.monitor_source_templates:
            for k in self.monitor_source_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.enable_webhook is not None:
            result['enableWebhook'] = self.enable_webhook
        result['monitorSourceTemplates'] = []
        if self.monitor_source_templates is not None:
            for k in self.monitor_source_templates:
                result['monitorSourceTemplates'].append(k.to_map() if k else None)
        if self.service_group_description is not None:
            result['serviceGroupDescription'] = self.service_group_description
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        if self.user_ids is not None:
            result['userIds'] = self.user_ids
        if self.webhook_link is not None:
            result['webhookLink'] = self.webhook_link
        if self.webhook_type is not None:
            result['webhookType'] = self.webhook_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('enableWebhook') is not None:
            self.enable_webhook = m.get('enableWebhook')
        self.monitor_source_templates = []
        if m.get('monitorSourceTemplates') is not None:
            for k in m.get('monitorSourceTemplates'):
                temp_model = CreateServiceGroupRequestMonitorSourceTemplates()
                self.monitor_source_templates.append(temp_model.from_map(k))
        if m.get('serviceGroupDescription') is not None:
            self.service_group_description = m.get('serviceGroupDescription')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        if m.get('webhookLink') is not None:
            self.webhook_link = m.get('webhookLink')
        if m.get('webhookType') is not None:
            self.webhook_type = m.get('webhookType')
        return self


class CreateServiceGroupResponseBodyData(TeaModel):
    def __init__(self, service_group_id=None):
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class CreateServiceGroupResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 服务组ID
        self.data = data  # type: CreateServiceGroupResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateServiceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateServiceGroupResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateServiceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceGroupSchedulingRequestFastSchedulingSchedulingUsers(TeaModel):
    def __init__(self, scheduling_order=None, scheduling_user_id=None):
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: long
        # 轮班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceGroupSchedulingRequestFastSchedulingSchedulingUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        return self


class CreateServiceGroupSchedulingRequestFastScheduling(TeaModel):
    def __init__(self, duty_plan=None, scheduling_users=None, single_duration=None, single_duration_unit=None):
        # 值班方案 dutyPlan FAST_CHOICE 快速选择   CUSTOM  自定义
        self.duty_plan = duty_plan  # type: str
        # 快速轮班用户
        self.scheduling_users = scheduling_users  # type: list[CreateServiceGroupSchedulingRequestFastSchedulingSchedulingUsers]
        # 每人排班时长
        self.single_duration = single_duration  # type: int
        # 每人排班时常单位 HOUR 小时 DAY  天
        self.single_duration_unit = single_duration_unit  # type: str

    def validate(self):
        if self.scheduling_users:
            for k in self.scheduling_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceGroupSchedulingRequestFastScheduling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duty_plan is not None:
            result['dutyPlan'] = self.duty_plan
        result['schedulingUsers'] = []
        if self.scheduling_users is not None:
            for k in self.scheduling_users:
                result['schedulingUsers'].append(k.to_map() if k else None)
        if self.single_duration is not None:
            result['singleDuration'] = self.single_duration
        if self.single_duration_unit is not None:
            result['singleDurationUnit'] = self.single_duration_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dutyPlan') is not None:
            self.duty_plan = m.get('dutyPlan')
        self.scheduling_users = []
        if m.get('schedulingUsers') is not None:
            for k in m.get('schedulingUsers'):
                temp_model = CreateServiceGroupSchedulingRequestFastSchedulingSchedulingUsers()
                self.scheduling_users.append(temp_model.from_map(k))
        if m.get('singleDuration') is not None:
            self.single_duration = m.get('singleDuration')
        if m.get('singleDurationUnit') is not None:
            self.single_duration_unit = m.get('singleDurationUnit')
        return self


class CreateServiceGroupSchedulingRequestFineSchedulingSchedulingFineShifts(TeaModel):
    def __init__(self, cycle_order=None, scheduling_end_time=None, scheduling_order=None,
                 scheduling_start_time=None, scheduling_user_id=None, shift_name=None, skip_one_day=None):
        # 循环次序
        self.cycle_order = cycle_order  # type: int
        # 排班结束时间
        self.scheduling_end_time = scheduling_end_time  # type: str
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: int
        # 排班开始时间
        self.scheduling_start_time = scheduling_start_time  # type: str
        # 排班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long
        # 班次名称
        self.shift_name = shift_name  # type: str
        # 是否跨天
        self.skip_one_day = skip_one_day  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceGroupSchedulingRequestFineSchedulingSchedulingFineShifts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cycle_order is not None:
            result['cycleOrder'] = self.cycle_order
        if self.scheduling_end_time is not None:
            result['schedulingEndTime'] = self.scheduling_end_time
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_start_time is not None:
            result['schedulingStartTime'] = self.scheduling_start_time
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        if self.shift_name is not None:
            result['shiftName'] = self.shift_name
        if self.skip_one_day is not None:
            result['skipOneDay'] = self.skip_one_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cycleOrder') is not None:
            self.cycle_order = m.get('cycleOrder')
        if m.get('schedulingEndTime') is not None:
            self.scheduling_end_time = m.get('schedulingEndTime')
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingStartTime') is not None:
            self.scheduling_start_time = m.get('schedulingStartTime')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        if m.get('shiftName') is not None:
            self.shift_name = m.get('shiftName')
        if m.get('skipOneDay') is not None:
            self.skip_one_day = m.get('skipOneDay')
        return self


class CreateServiceGroupSchedulingRequestFineSchedulingSchedulingTemplateFineShifts(TeaModel):
    def __init__(self, scheduling_end_time=None, scheduling_order=None, scheduling_start_time=None,
                 scheduling_user_id=None, scheduling_user_name=None, skip_one_day=None):
        # 排班结束时间
        self.scheduling_end_time = scheduling_end_time  # type: str
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: long
        # 排班开始时间
        self.scheduling_start_time = scheduling_start_time  # type: str
        # 用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long
        # 用户名字
        self.scheduling_user_name = scheduling_user_name  # type: str
        # 是否跨天
        self.skip_one_day = skip_one_day  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceGroupSchedulingRequestFineSchedulingSchedulingTemplateFineShifts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_end_time is not None:
            result['schedulingEndTime'] = self.scheduling_end_time
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_start_time is not None:
            result['schedulingStartTime'] = self.scheduling_start_time
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        if self.scheduling_user_name is not None:
            result['schedulingUserName'] = self.scheduling_user_name
        if self.skip_one_day is not None:
            result['skipOneDay'] = self.skip_one_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingEndTime') is not None:
            self.scheduling_end_time = m.get('schedulingEndTime')
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingStartTime') is not None:
            self.scheduling_start_time = m.get('schedulingStartTime')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        if m.get('schedulingUserName') is not None:
            self.scheduling_user_name = m.get('schedulingUserName')
        if m.get('skipOneDay') is not None:
            self.skip_one_day = m.get('skipOneDay')
        return self


class CreateServiceGroupSchedulingRequestFineScheduling(TeaModel):
    def __init__(self, period=None, period_unit=None, scheduling_fine_shifts=None,
                 scheduling_template_fine_shifts=None, shift_type=None):
        # 循环周期
        self.period = period  # type: int
        # 循环周期单位 HOUR 小时 DAY  天
        self.period_unit = period_unit  # type: str
        # 精细排班信息表
        self.scheduling_fine_shifts = scheduling_fine_shifts  # type: list[CreateServiceGroupSchedulingRequestFineSchedulingSchedulingFineShifts]
        # 精细排班模版
        self.scheduling_template_fine_shifts = scheduling_template_fine_shifts  # type: list[CreateServiceGroupSchedulingRequestFineSchedulingSchedulingTemplateFineShifts]
        # 班次类型 MORNING_NIGHT 早晚班 MORNING_NOON_NIGHT 早中晚班 CUSTOM 自定义
        self.shift_type = shift_type  # type: str

    def validate(self):
        if self.scheduling_fine_shifts:
            for k in self.scheduling_fine_shifts:
                if k:
                    k.validate()
        if self.scheduling_template_fine_shifts:
            for k in self.scheduling_template_fine_shifts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServiceGroupSchedulingRequestFineScheduling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['periodUnit'] = self.period_unit
        result['schedulingFineShifts'] = []
        if self.scheduling_fine_shifts is not None:
            for k in self.scheduling_fine_shifts:
                result['schedulingFineShifts'].append(k.to_map() if k else None)
        result['schedulingTemplateFineShifts'] = []
        if self.scheduling_template_fine_shifts is not None:
            for k in self.scheduling_template_fine_shifts:
                result['schedulingTemplateFineShifts'].append(k.to_map() if k else None)
        if self.shift_type is not None:
            result['shiftType'] = self.shift_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodUnit') is not None:
            self.period_unit = m.get('periodUnit')
        self.scheduling_fine_shifts = []
        if m.get('schedulingFineShifts') is not None:
            for k in m.get('schedulingFineShifts'):
                temp_model = CreateServiceGroupSchedulingRequestFineSchedulingSchedulingFineShifts()
                self.scheduling_fine_shifts.append(temp_model.from_map(k))
        self.scheduling_template_fine_shifts = []
        if m.get('schedulingTemplateFineShifts') is not None:
            for k in m.get('schedulingTemplateFineShifts'):
                temp_model = CreateServiceGroupSchedulingRequestFineSchedulingSchedulingTemplateFineShifts()
                self.scheduling_template_fine_shifts.append(temp_model.from_map(k))
        if m.get('shiftType') is not None:
            self.shift_type = m.get('shiftType')
        return self


class CreateServiceGroupSchedulingRequest(TeaModel):
    def __init__(self, client_token=None, fast_scheduling=None, fine_scheduling=None, scheduling_way=None,
                 service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 快速排班
        self.fast_scheduling = fast_scheduling  # type: CreateServiceGroupSchedulingRequestFastScheduling
        # 精细排班
        self.fine_scheduling = fine_scheduling  # type: CreateServiceGroupSchedulingRequestFineScheduling
        # 排班方式 FAST 快速排班 FINE  精细排班
        self.scheduling_way = scheduling_way  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        if self.fast_scheduling:
            self.fast_scheduling.validate()
        if self.fine_scheduling:
            self.fine_scheduling.validate()

    def to_map(self):
        _map = super(CreateServiceGroupSchedulingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.fast_scheduling is not None:
            result['fastScheduling'] = self.fast_scheduling.to_map()
        if self.fine_scheduling is not None:
            result['fineScheduling'] = self.fine_scheduling.to_map()
        if self.scheduling_way is not None:
            result['schedulingWay'] = self.scheduling_way
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('fastScheduling') is not None:
            temp_model = CreateServiceGroupSchedulingRequestFastScheduling()
            self.fast_scheduling = temp_model.from_map(m['fastScheduling'])
        if m.get('fineScheduling') is not None:
            temp_model = CreateServiceGroupSchedulingRequestFineScheduling()
            self.fine_scheduling = temp_model.from_map(m['fineScheduling'])
        if m.get('schedulingWay') is not None:
            self.scheduling_way = m.get('schedulingWay')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class CreateServiceGroupSchedulingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceGroupSchedulingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateServiceGroupSchedulingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceGroupSchedulingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceGroupSchedulingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceGroupSchedulingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubscriptionRequestNotifyObjectList(TeaModel):
    def __init__(self, notify_object_id=None):
        # 通知对象id
        self.notify_object_id = notify_object_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubscriptionRequestNotifyObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_object_id is not None:
            result['notifyObjectId'] = self.notify_object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('notifyObjectId') is not None:
            self.notify_object_id = m.get('notifyObjectId')
        return self


class CreateSubscriptionRequestNotifyStrategyListPeriodChannel(TeaModel):
    def __init__(self, non_workday=None, workday=None):
        # 非工作时段
        self.non_workday = non_workday  # type: str
        # 工作时段
        self.workday = workday  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubscriptionRequestNotifyStrategyListPeriodChannel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_workday is not None:
            result['nonWorkday'] = self.non_workday
        if self.workday is not None:
            result['workday'] = self.workday
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nonWorkday') is not None:
            self.non_workday = m.get('nonWorkday')
        if m.get('workday') is not None:
            self.workday = m.get('workday')
        return self


class CreateSubscriptionRequestNotifyStrategyListStrategiesConditions(TeaModel):
    def __init__(self, action=None, effection=None, level=None, problem_notify_type=None):
        # 时间动作
        self.action = action  # type: str
        # 影响范围
        self.effection = effection  # type: str
        # 等级
        self.level = level  # type: str
        # 故障通知类型
        self.problem_notify_type = problem_notify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubscriptionRequestNotifyStrategyListStrategiesConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.effection is not None:
            result['effection'] = self.effection
        if self.level is not None:
            result['level'] = self.level
        if self.problem_notify_type is not None:
            result['problemNotifyType'] = self.problem_notify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('problemNotifyType') is not None:
            self.problem_notify_type = m.get('problemNotifyType')
        return self


class CreateSubscriptionRequestNotifyStrategyListStrategies(TeaModel):
    def __init__(self, conditions=None):
        # 通知策略条件
        self.conditions = conditions  # type: list[CreateSubscriptionRequestNotifyStrategyListStrategiesConditions]

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSubscriptionRequestNotifyStrategyListStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = CreateSubscriptionRequestNotifyStrategyListStrategiesConditions()
                self.conditions.append(temp_model.from_map(k))
        return self


class CreateSubscriptionRequestNotifyStrategyList(TeaModel):
    def __init__(self, channels=None, instance_type=None, period_channel=None, strategies=None):
        # 渠道，多个逗号分隔
        self.channels = channels  # type: str
        # 订阅实例类型，事件、报警、故障
        self.instance_type = instance_type  # type: long
        # 分时段渠道
        self.period_channel = period_channel  # type: CreateSubscriptionRequestNotifyStrategyListPeriodChannel
        # 条件。json格式，包含多个条件，比如级别、影响程度 kv格式
        self.strategies = strategies  # type: list[CreateSubscriptionRequestNotifyStrategyListStrategies]

    def validate(self):
        if self.period_channel:
            self.period_channel.validate()
        if self.strategies:
            for k in self.strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSubscriptionRequestNotifyStrategyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['channels'] = self.channels
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.period_channel is not None:
            result['periodChannel'] = self.period_channel.to_map()
        result['strategies'] = []
        if self.strategies is not None:
            for k in self.strategies:
                result['strategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('channels') is not None:
            self.channels = m.get('channels')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('periodChannel') is not None:
            temp_model = CreateSubscriptionRequestNotifyStrategyListPeriodChannel()
            self.period_channel = temp_model.from_map(m['periodChannel'])
        self.strategies = []
        if m.get('strategies') is not None:
            for k in m.get('strategies'):
                temp_model = CreateSubscriptionRequestNotifyStrategyListStrategies()
                self.strategies.append(temp_model.from_map(k))
        return self


class CreateSubscriptionRequestScopeObjectList(TeaModel):
    def __init__(self, scope_object_id=None):
        # 订阅范围对象id
        self.scope_object_id = scope_object_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubscriptionRequestScopeObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope_object_id is not None:
            result['scopeObjectId'] = self.scope_object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scopeObjectId') is not None:
            self.scope_object_id = m.get('scopeObjectId')
        return self


class CreateSubscriptionRequest(TeaModel):
    def __init__(self, client_token=None, end_time=None, expired_type=None, notify_object_list=None,
                 notify_object_type=None, notify_strategy_list=None, period=None, scope=None, scope_object_list=None, start_time=None,
                 subscription_title=None):
        # 幂等参数
        self.client_token = client_token  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 订阅时效
        self.expired_type = expired_type  # type: long
        # 通知对象列表
        self.notify_object_list = notify_object_list  # type: list[CreateSubscriptionRequestNotifyObjectList]
        # 通知对象类型
        self.notify_object_type = notify_object_type  # type: long
        # 通知策略列表
        self.notify_strategy_list = notify_strategy_list  # type: list[CreateSubscriptionRequestNotifyStrategyList]
        # 时间段
        self.period = period  # type: str
        # 订阅范围类型
        self.scope = scope  # type: long
        # 订阅范围列表
        self.scope_object_list = scope_object_list  # type: list[CreateSubscriptionRequestScopeObjectList]
        # 开始时间
        self.start_time = start_time  # type: str
        # 通知订阅名称
        self.subscription_title = subscription_title  # type: str

    def validate(self):
        if self.notify_object_list:
            for k in self.notify_object_list:
                if k:
                    k.validate()
        if self.notify_strategy_list:
            for k in self.notify_strategy_list:
                if k:
                    k.validate()
        if self.scope_object_list:
            for k in self.scope_object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSubscriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.expired_type is not None:
            result['expiredType'] = self.expired_type
        result['notifyObjectList'] = []
        if self.notify_object_list is not None:
            for k in self.notify_object_list:
                result['notifyObjectList'].append(k.to_map() if k else None)
        if self.notify_object_type is not None:
            result['notifyObjectType'] = self.notify_object_type
        result['notifyStrategyList'] = []
        if self.notify_strategy_list is not None:
            for k in self.notify_strategy_list:
                result['notifyStrategyList'].append(k.to_map() if k else None)
        if self.period is not None:
            result['period'] = self.period
        if self.scope is not None:
            result['scope'] = self.scope
        result['scopeObjectList'] = []
        if self.scope_object_list is not None:
            for k in self.scope_object_list:
                result['scopeObjectList'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.subscription_title is not None:
            result['subscriptionTitle'] = self.subscription_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('expiredType') is not None:
            self.expired_type = m.get('expiredType')
        self.notify_object_list = []
        if m.get('notifyObjectList') is not None:
            for k in m.get('notifyObjectList'):
                temp_model = CreateSubscriptionRequestNotifyObjectList()
                self.notify_object_list.append(temp_model.from_map(k))
        if m.get('notifyObjectType') is not None:
            self.notify_object_type = m.get('notifyObjectType')
        self.notify_strategy_list = []
        if m.get('notifyStrategyList') is not None:
            for k in m.get('notifyStrategyList'):
                temp_model = CreateSubscriptionRequestNotifyStrategyList()
                self.notify_strategy_list.append(temp_model.from_map(k))
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        self.scope_object_list = []
        if m.get('scopeObjectList') is not None:
            for k in m.get('scopeObjectList'):
                temp_model = CreateSubscriptionRequestScopeObjectList()
                self.scope_object_list.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('subscriptionTitle') is not None:
            self.subscription_title = m.get('subscriptionTitle')
        return self


class CreateSubscriptionResponseBodyData(TeaModel):
    def __init__(self, subscription_id=None):
        # 订阅id
        self.subscription_id = subscription_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubscriptionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        return self


class CreateSubscriptionResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateSubscriptionResponseBodyData
        # request id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateSubscriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateSubscriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSubscriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSubscriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantApplicationRequest(TeaModel):
    def __init__(self, channel=None, client_token=None):
        # 应用协同渠道
        self.channel = channel  # type: str
        # 幂等标识
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CreateTenantApplicationResponseBodyData(TeaModel):
    def __init__(self, open_url=None, progress=None):
        # 开通url
        self.open_url = open_url  # type: str
        # 开通进度状态
        self.progress = progress  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTenantApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_url is not None:
            result['openUrl'] = self.open_url
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('openUrl') is not None:
            self.open_url = m.get('openUrl')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class CreateTenantApplicationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: CreateTenantApplicationResponseBodyData
        # id of the req
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateTenantApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateTenantApplicationResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateTenantApplicationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTenantApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTenantApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTenantApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, client_token=None, email=None, phone=None, ram_id=None, username=None):
        self.client_token = client_token  # type: str
        self.email = email  # type: str
        self.phone = phone  # type: str
        self.ram_id = ram_id  # type: long
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.email is not None:
            result['email'] = self.email
        if self.phone is not None:
            result['phone'] = self.phone
        if self.ram_id is not None:
            result['ramId'] = self.ram_id
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('ramId') is not None:
            self.ram_id = m.get('ramId')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class CreateUserResponseBodyData(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: CreateUserResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateUserResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEscalationPlanRequest(TeaModel):
    def __init__(self, client_token=None, escalation_plan_id=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 升级计划ID
        self.escalation_plan_id = escalation_plan_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEscalationPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        return self


class DeleteEscalationPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEscalationPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteEscalationPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEscalationPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEscalationPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEscalationPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIncidentRequest(TeaModel):
    def __init__(self, client_token=None, incident_id=None):
        # 幂等校验
        self.client_token = client_token  # type: str
        # 事件Id
        self.incident_id = incident_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIncidentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        return self


class DeleteIncidentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIncidentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteIncidentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteIncidentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIncidentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntegrationConfigRequest(TeaModel):
    def __init__(self, client_token=None, integration_config_id=None):
        # 幂等id
        self.client_token = client_token  # type: str
        # 集成配置id
        self.integration_config_id = integration_config_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntegrationConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        return self


class DeleteIntegrationConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIntegrationConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteIntegrationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteIntegrationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIntegrationConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteIntegrationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProblemRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None):
        # 幂等校验
        self.client_token = client_token  # type: str
        # 故障Id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProblemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class DeleteProblemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProblemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProblemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProblemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProblemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProblemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProblemEffectionServiceRequest(TeaModel):
    def __init__(self, client_token=None, effection_service_id=None, problem_id=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 影响服务ID
        self.effection_service_id = effection_service_id  # type: long
        # 故障id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProblemEffectionServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.effection_service_id is not None:
            result['effectionServiceId'] = self.effection_service_id
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('effectionServiceId') is not None:
            self.effection_service_id = m.get('effectionServiceId')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class DeleteProblemEffectionServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProblemEffectionServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProblemEffectionServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProblemEffectionServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProblemEffectionServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProblemEffectionServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProblemMeasureRequest(TeaModel):
    def __init__(self, client_token=None, measure_id=None, problem_id=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 故障改成措施id
        self.measure_id = measure_id  # type: long
        # 故障Id
        self.problem_id = problem_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProblemMeasureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.measure_id is not None:
            result['measureId'] = self.measure_id
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('measureId') is not None:
            self.measure_id = m.get('measureId')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class DeleteProblemMeasureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProblemMeasureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProblemMeasureResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProblemMeasureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProblemMeasureResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProblemMeasureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProblemTimelineRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None, problem_timeline_id=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 故障id
        self.problem_id = problem_id  # type: long
        # ID
        self.problem_timeline_id = problem_timeline_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProblemTimelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_timeline_id is not None:
            result['problemTimelineId'] = self.problem_timeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemTimelineId') is not None:
            self.problem_timeline_id = m.get('problemTimelineId')
        return self


class DeleteProblemTimelineResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProblemTimelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProblemTimelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteProblemTimelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProblemTimelineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProblemTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRouteRuleRequest(TeaModel):
    def __init__(self, client_token=None, route_rule_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 规则ID
        self.route_rule_id = route_rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRouteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        return self


class DeleteRouteRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID
        self.request_id = request_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRouteRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteRouteRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRouteRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRouteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceRequest(TeaModel):
    def __init__(self, client_token=None, service_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务ID
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceGroupRequest(TeaModel):
    def __init__(self, client_token=None, service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class DeleteServiceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteServiceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteServiceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceGroupUserRequest(TeaModel):
    def __init__(self, client_token=None, new_user_id=None, old_user_id=None, remove_user=None,
                 service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 新的用户
        self.new_user_id = new_user_id  # type: long
        # 老的用户ID
        self.old_user_id = old_user_id  # type: long
        # 删除服务组成员
        self.remove_user = remove_user  # type: bool
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceGroupUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.new_user_id is not None:
            result['newUserId'] = self.new_user_id
        if self.old_user_id is not None:
            result['oldUserId'] = self.old_user_id
        if self.remove_user is not None:
            result['removeUser'] = self.remove_user
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('newUserId') is not None:
            self.new_user_id = m.get('newUserId')
        if m.get('oldUserId') is not None:
            self.old_user_id = m.get('oldUserId')
        if m.get('removeUser') is not None:
            self.remove_user = m.get('removeUser')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class DeleteServiceGroupUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceGroupUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteServiceGroupUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceGroupUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceGroupUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteServiceGroupUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubscriptionRequest(TeaModel):
    def __init__(self, subscription_id=None):
        self.subscription_id = subscription_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubscriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        return self


class DeleteSubscriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSubscriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteSubscriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteSubscriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSubscriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, client_token=None, user_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 用户ID
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeliverIncidentRequest(TeaModel):
    def __init__(self, assign_user_id=None, client_token=None, incident_id=None):
        # 转交用户ID
        self.assign_user_id = assign_user_id  # type: long
        # 幂等校验id
        self.client_token = client_token  # type: str
        # 事件ID
        self.incident_id = incident_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeliverIncidentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_user_id is not None:
            result['assignUserId'] = self.assign_user_id
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignUserId') is not None:
            self.assign_user_id = m.get('assignUserId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        return self


class DeliverIncidentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeliverIncidentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeliverIncidentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeliverIncidentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeliverIncidentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeliverIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableEscalationPlanRequest(TeaModel):
    def __init__(self, client_token=None, escalation_plan_id=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 升级计划ID
        self.escalation_plan_id = escalation_plan_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableEscalationPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        return self


class DisableEscalationPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableEscalationPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DisableEscalationPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableEscalationPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableEscalationPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableEscalationPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableIntegrationConfigRequest(TeaModel):
    def __init__(self, client_token=None, integration_config_id=None):
        # 幂等id
        self.client_token = client_token  # type: str
        self.integration_config_id = integration_config_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableIntegrationConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        return self


class DisableIntegrationConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableIntegrationConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DisableIntegrationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableIntegrationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableIntegrationConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableIntegrationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableRouteRuleRequest(TeaModel):
    def __init__(self, client_token=None, route_rule_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 请求ID
        self.route_rule_id = route_rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableRouteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        return self


class DisableRouteRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # C4BE3837-1A13-413B-A225-2C88188E8A43
        self.data = data  # type: long
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableRouteRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DisableRouteRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableRouteRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableRouteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableServiceGroupWebhookRequest(TeaModel):
    def __init__(self, client_token=None, service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableServiceGroupWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class DisableServiceGroupWebhookResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableServiceGroupWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DisableServiceGroupWebhookResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableServiceGroupWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableServiceGroupWebhookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableServiceGroupWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSubscriptionRequest(TeaModel):
    def __init__(self, subscription_id=None):
        self.subscription_id = subscription_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableSubscriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        return self


class DisableSubscriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableSubscriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DisableSubscriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableSubscriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableSubscriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableEscalationPlanRequest(TeaModel):
    def __init__(self, client_token=None, escalation_plan_id=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 升级计划ID
        self.escalation_plan_id = escalation_plan_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableEscalationPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        return self


class EnableEscalationPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableEscalationPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EnableEscalationPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableEscalationPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableEscalationPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableEscalationPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableIntegrationConfigRequest(TeaModel):
    def __init__(self, client_token=None, integration_config_id=None):
        # 幂等id
        self.client_token = client_token  # type: str
        self.integration_config_id = integration_config_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableIntegrationConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        return self


class EnableIntegrationConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableIntegrationConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EnableIntegrationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableIntegrationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableIntegrationConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableIntegrationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRouteRuleRequest(TeaModel):
    def __init__(self, client_token=None, route_rule_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 规则ID
        self.route_rule_id = route_rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRouteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        return self


class EnableRouteRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: int
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableRouteRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EnableRouteRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableRouteRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableRouteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableServiceGroupWebhookRequest(TeaModel):
    def __init__(self, client_token=None, service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableServiceGroupWebhookRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class EnableServiceGroupWebhookResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableServiceGroupWebhookResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EnableServiceGroupWebhookResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableServiceGroupWebhookResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableServiceGroupWebhookResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableServiceGroupWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSubscriptionRequest(TeaModel):
    def __init__(self, subscription_id=None):
        self.subscription_id = subscription_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSubscriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        return self


class EnableSubscriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSubscriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EnableSubscriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableSubscriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableSubscriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishIncidentRequest(TeaModel):
    def __init__(self, client_token=None, incident_finish_reason=None, incident_finish_reason_description=None,
                 incident_finish_solution=None, incident_finish_solution_description=None, incident_ids=None):
        # 幂等校验Id
        self.client_token = client_token  # type: str
        # 完结原因
        self.incident_finish_reason = incident_finish_reason  # type: int
        # 原因描述
        self.incident_finish_reason_description = incident_finish_reason_description  # type: str
        # 解决方案
        self.incident_finish_solution = incident_finish_solution  # type: int
        # 解决方案描述
        self.incident_finish_solution_description = incident_finish_solution_description  # type: str
        # 事件ID数组
        self.incident_ids = incident_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishIncidentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.incident_finish_reason is not None:
            result['incidentFinishReason'] = self.incident_finish_reason
        if self.incident_finish_reason_description is not None:
            result['incidentFinishReasonDescription'] = self.incident_finish_reason_description
        if self.incident_finish_solution is not None:
            result['incidentFinishSolution'] = self.incident_finish_solution
        if self.incident_finish_solution_description is not None:
            result['incidentFinishSolutionDescription'] = self.incident_finish_solution_description
        if self.incident_ids is not None:
            result['incidentIds'] = self.incident_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('incidentFinishReason') is not None:
            self.incident_finish_reason = m.get('incidentFinishReason')
        if m.get('incidentFinishReasonDescription') is not None:
            self.incident_finish_reason_description = m.get('incidentFinishReasonDescription')
        if m.get('incidentFinishSolution') is not None:
            self.incident_finish_solution = m.get('incidentFinishSolution')
        if m.get('incidentFinishSolutionDescription') is not None:
            self.incident_finish_solution_description = m.get('incidentFinishSolutionDescription')
        if m.get('incidentIds') is not None:
            self.incident_ids = m.get('incidentIds')
        return self


class FinishIncidentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishIncidentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class FinishIncidentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FinishIncidentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FinishIncidentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FinishIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishProblemRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None):
        # 幂等校验
        self.client_token = client_token  # type: str
        # 故障Id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishProblemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class FinishProblemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FinishProblemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class FinishProblemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: FinishProblemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FinishProblemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FinishProblemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GeneratePictureLinkRequest(TeaModel):
    def __init__(self, keys=None, problem_id=None):
        # keys
        self.keys = keys  # type: list[str]
        # 故障id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GeneratePictureLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['keys'] = self.keys
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keys') is not None:
            self.keys = m.get('keys')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class GeneratePictureLinkResponseBodyDataLinks(TeaModel):
    def __init__(self, key=None, link=None):
        # oss key
        self.key = key  # type: str
        # url
        self.link = link  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GeneratePictureLinkResponseBodyDataLinks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.link is not None:
            result['link'] = self.link
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('link') is not None:
            self.link = m.get('link')
        return self


class GeneratePictureLinkResponseBodyData(TeaModel):
    def __init__(self, links=None):
        # array
        self.links = links  # type: list[GeneratePictureLinkResponseBodyDataLinks]

    def validate(self):
        if self.links:
            for k in self.links:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GeneratePictureLinkResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['links'] = []
        if self.links is not None:
            for k in self.links:
                result['links'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.links = []
        if m.get('links') is not None:
            for k in m.get('links'):
                temp_model = GeneratePictureLinkResponseBodyDataLinks()
                self.links.append(temp_model.from_map(k))
        return self


class GeneratePictureLinkResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GeneratePictureLinkResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GeneratePictureLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GeneratePictureLinkResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GeneratePictureLinkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GeneratePictureLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GeneratePictureLinkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GeneratePictureLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GeneratePictureUploadSignRequestFiles(TeaModel):
    def __init__(self, file_name=None, file_size=None, file_type=None):
        # 文件名称
        self.file_name = file_name  # type: str
        # 文件大小
        self.file_size = file_size  # type: long
        # 文件类型
        self.file_type = file_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GeneratePictureUploadSignRequestFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        return self


class GeneratePictureUploadSignRequest(TeaModel):
    def __init__(self, files=None, instance_id=None, instance_type=None):
        # 文件
        self.files = files  # type: list[GeneratePictureUploadSignRequestFiles]
        # 资源id
        self.instance_id = instance_id  # type: long
        # 资源类型
        self.instance_type = instance_type  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GeneratePictureUploadSignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = GeneratePictureUploadSignRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        return self


class GeneratePictureUploadSignResponseBodyDataFiles(TeaModel):
    def __init__(self, file_name=None, file_size=None, file_type=None, key=None):
        # 文件名称
        self.file_name = file_name  # type: str
        # 文件大小
        self.file_size = file_size  # type: long
        # 文件类型
        self.file_type = file_type  # type: str
        # oss key
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GeneratePictureUploadSignResponseBodyDataFiles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class GeneratePictureUploadSignResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, bucket_name=None, files=None, policy=None, signature=None, url=None):
        # accessKeyId
        self.access_key_id = access_key_id  # type: str
        # oss bucket name
        self.bucket_name = bucket_name  # type: str
        # files
        self.files = files  # type: list[GeneratePictureUploadSignResponseBodyDataFiles]
        # policy
        self.policy = policy  # type: str
        # signature
        self.signature = signature  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GeneratePictureUploadSignResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = GeneratePictureUploadSignResponseBodyDataFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GeneratePictureUploadSignResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: GeneratePictureUploadSignResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GeneratePictureUploadSignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GeneratePictureUploadSignResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GeneratePictureUploadSignResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GeneratePictureUploadSignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GeneratePictureUploadSignResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GeneratePictureUploadSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateProblemPictureLinkRequest(TeaModel):
    def __init__(self, keys=None, problem_id=None):
        # oss key
        self.keys = keys  # type: list[str]
        # 故障id
        self.problem_id = problem_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateProblemPictureLinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['keys'] = self.keys
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keys') is not None:
            self.keys = m.get('keys')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class GenerateProblemPictureLinkResponseBodyDataLinks(TeaModel):
    def __init__(self, key=None, link=None):
        # oss key
        self.key = key  # type: str
        # 图片链接
        self.link = link  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateProblemPictureLinkResponseBodyDataLinks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.link is not None:
            result['link'] = self.link
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('link') is not None:
            self.link = m.get('link')
        return self


class GenerateProblemPictureLinkResponseBodyData(TeaModel):
    def __init__(self, links=None):
        # 图片链接列表
        self.links = links  # type: list[GenerateProblemPictureLinkResponseBodyDataLinks]

    def validate(self):
        if self.links:
            for k in self.links:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateProblemPictureLinkResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['links'] = []
        if self.links is not None:
            for k in self.links:
                result['links'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.links = []
        if m.get('links') is not None:
            for k in m.get('links'):
                temp_model = GenerateProblemPictureLinkResponseBodyDataLinks()
                self.links.append(temp_model.from_map(k))
        return self


class GenerateProblemPictureLinkResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GenerateProblemPictureLinkResponseBodyData
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateProblemPictureLinkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GenerateProblemPictureLinkResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GenerateProblemPictureLinkResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateProblemPictureLinkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateProblemPictureLinkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateProblemPictureLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateProblemPictureUploadSignRequest(TeaModel):
    def __init__(self, file_name=None, file_size=None, file_type=None, problem_id=None):
        # 文件名
        self.file_name = file_name  # type: str
        # 文件大小KB
        self.file_size = file_size  # type: long
        # 文件类型
        self.file_type = file_type  # type: str
        # 故障id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateProblemPictureUploadSignRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_type is not None:
            result['fileType'] = self.file_type
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class GenerateProblemPictureUploadSignResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, bucket_name=None, key=None, policy=None, signature=None, url=None):
        # ossaccessKeyId
        self.access_key_id = access_key_id  # type: str
        # oss bucket name
        self.bucket_name = bucket_name  # type: str
        # oss key
        self.key = key  # type: str
        # policy
        self.policy = policy  # type: str
        # signature
        self.signature = signature  # type: str
        # url
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateProblemPictureUploadSignResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.key is not None:
            result['key'] = self.key
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GenerateProblemPictureUploadSignResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GenerateProblemPictureUploadSignResponseBodyData
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateProblemPictureUploadSignResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GenerateProblemPictureUploadSignResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GenerateProblemPictureUploadSignResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GenerateProblemPictureUploadSignResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateProblemPictureUploadSignResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateProblemPictureUploadSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEscalationPlanRequest(TeaModel):
    def __init__(self, client_token=None, escalation_plan_id=None):
        # 幂等标识
        self.client_token = client_token  # type: str
        # 升级计划id
        self.escalation_plan_id = escalation_plan_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEscalationPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        return self


class GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanConditions(TeaModel):
    def __init__(self, effection=None, level=None):
        # 影响等级
        self.effection = effection  # type: str
        # 事件等级
        self.level = level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effection is not None:
            result['effection'] = self.effection
        if self.level is not None:
            result['level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('level') is not None:
            self.level = m.get('level')
        return self


class GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategiesNoticeObjectList(TeaModel):
    def __init__(self, notice_object_id=None, notice_object_name=None):
        # 通知对象id
        self.notice_object_id = notice_object_id  # type: long
        # 通知对象名称
        self.notice_object_name = notice_object_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategiesNoticeObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notice_object_id is not None:
            result['noticeObjectId'] = self.notice_object_id
        if self.notice_object_name is not None:
            result['noticeObjectName'] = self.notice_object_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('noticeObjectId') is not None:
            self.notice_object_id = m.get('noticeObjectId')
        if m.get('noticeObjectName') is not None:
            self.notice_object_name = m.get('noticeObjectName')
        return self


class GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategiesServiceGroups(TeaModel):
    def __init__(self, id=None, service_group_name=None):
        # 服务组id
        self.id = id  # type: long
        # 服务组名称
        self.service_group_name = service_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategiesServiceGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        return self


class GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategies(TeaModel):
    def __init__(self, enable_webhook=None, escalation_plan_type=None, notice_channels=None,
                 notice_object_list=None, notice_time=None, service_groups=None):
        # 是否支持群通知
        self.enable_webhook = enable_webhook  # type: bool
        # 升级计划类型
        self.escalation_plan_type = escalation_plan_type  # type: str
        # 通知对象渠道
        self.notice_channels = notice_channels  # type: str
        # 通知对象列表
        self.notice_object_list = notice_object_list  # type: list[GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategiesNoticeObjectList]
        # 通知时间
        self.notice_time = notice_time  # type: long
        # 服务组列表
        self.service_groups = service_groups  # type: list[GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategiesServiceGroups]

    def validate(self):
        if self.notice_object_list:
            for k in self.notice_object_list:
                if k:
                    k.validate()
        if self.service_groups:
            for k in self.service_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_webhook is not None:
            result['enableWebhook'] = self.enable_webhook
        if self.escalation_plan_type is not None:
            result['escalationPlanType'] = self.escalation_plan_type
        if self.notice_channels is not None:
            result['noticeChannels'] = self.notice_channels
        result['noticeObjectList'] = []
        if self.notice_object_list is not None:
            for k in self.notice_object_list:
                result['noticeObjectList'].append(k.to_map() if k else None)
        if self.notice_time is not None:
            result['noticeTime'] = self.notice_time
        result['serviceGroups'] = []
        if self.service_groups is not None:
            for k in self.service_groups:
                result['serviceGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableWebhook') is not None:
            self.enable_webhook = m.get('enableWebhook')
        if m.get('escalationPlanType') is not None:
            self.escalation_plan_type = m.get('escalationPlanType')
        if m.get('noticeChannels') is not None:
            self.notice_channels = m.get('noticeChannels')
        self.notice_object_list = []
        if m.get('noticeObjectList') is not None:
            for k in m.get('noticeObjectList'):
                temp_model = GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategiesNoticeObjectList()
                self.notice_object_list.append(temp_model.from_map(k))
        if m.get('noticeTime') is not None:
            self.notice_time = m.get('noticeTime')
        self.service_groups = []
        if m.get('serviceGroups') is not None:
            for k in m.get('serviceGroups'):
                temp_model = GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategiesServiceGroups()
                self.service_groups.append(temp_model.from_map(k))
        return self


class GetEscalationPlanResponseBodyDataEscalationPlanRules(TeaModel):
    def __init__(self, escalation_plan_conditions=None, escalation_plan_rule_id=None,
                 escalation_plan_strategies=None):
        # 升级计划条件
        self.escalation_plan_conditions = escalation_plan_conditions  # type: list[GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanConditions]
        # 升级计划id
        self.escalation_plan_rule_id = escalation_plan_rule_id  # type: long
        # 升级计划策略
        self.escalation_plan_strategies = escalation_plan_strategies  # type: list[GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategies]

    def validate(self):
        if self.escalation_plan_conditions:
            for k in self.escalation_plan_conditions:
                if k:
                    k.validate()
        if self.escalation_plan_strategies:
            for k in self.escalation_plan_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEscalationPlanResponseBodyDataEscalationPlanRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['escalationPlanConditions'] = []
        if self.escalation_plan_conditions is not None:
            for k in self.escalation_plan_conditions:
                result['escalationPlanConditions'].append(k.to_map() if k else None)
        if self.escalation_plan_rule_id is not None:
            result['escalationPlanRuleId'] = self.escalation_plan_rule_id
        result['escalationPlanStrategies'] = []
        if self.escalation_plan_strategies is not None:
            for k in self.escalation_plan_strategies:
                result['escalationPlanStrategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.escalation_plan_conditions = []
        if m.get('escalationPlanConditions') is not None:
            for k in m.get('escalationPlanConditions'):
                temp_model = GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanConditions()
                self.escalation_plan_conditions.append(temp_model.from_map(k))
        if m.get('escalationPlanRuleId') is not None:
            self.escalation_plan_rule_id = m.get('escalationPlanRuleId')
        self.escalation_plan_strategies = []
        if m.get('escalationPlanStrategies') is not None:
            for k in m.get('escalationPlanStrategies'):
                temp_model = GetEscalationPlanResponseBodyDataEscalationPlanRulesEscalationPlanStrategies()
                self.escalation_plan_strategies.append(temp_model.from_map(k))
        return self


class GetEscalationPlanResponseBodyDataEscalationPlanScopeObjects(TeaModel):
    def __init__(self, scope=None, scope_object_id=None, scope_object_name=None):
        # 范围对象类型
        self.scope = scope  # type: str
        # 范围对象id
        self.scope_object_id = scope_object_id  # type: long
        # 范围对象名称
        self.scope_object_name = scope_object_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEscalationPlanResponseBodyDataEscalationPlanScopeObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        if self.scope_object_id is not None:
            result['scopeObjectId'] = self.scope_object_id
        if self.scope_object_name is not None:
            result['scopeObjectName'] = self.scope_object_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scopeObjectId') is not None:
            self.scope_object_id = m.get('scopeObjectId')
        if m.get('scopeObjectName') is not None:
            self.scope_object_name = m.get('scopeObjectName')
        return self


class GetEscalationPlanResponseBodyData(TeaModel):
    def __init__(self, create_time=None, escalation_plan_description=None, escalation_plan_id=None,
                 escalation_plan_name=None, escalation_plan_rules=None, escalation_plan_scope_objects=None):
        # 创建时间
        self.create_time = create_time  # type: str
        # 升级计划描述
        self.escalation_plan_description = escalation_plan_description  # type: str
        # 升级计划id
        self.escalation_plan_id = escalation_plan_id  # type: long
        # 升级计划名称
        self.escalation_plan_name = escalation_plan_name  # type: str
        # 升级计划规则列表
        self.escalation_plan_rules = escalation_plan_rules  # type: list[GetEscalationPlanResponseBodyDataEscalationPlanRules]
        # 升级计划范围对象列表
        self.escalation_plan_scope_objects = escalation_plan_scope_objects  # type: list[GetEscalationPlanResponseBodyDataEscalationPlanScopeObjects]

    def validate(self):
        if self.escalation_plan_rules:
            for k in self.escalation_plan_rules:
                if k:
                    k.validate()
        if self.escalation_plan_scope_objects:
            for k in self.escalation_plan_scope_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEscalationPlanResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.escalation_plan_description is not None:
            result['escalationPlanDescription'] = self.escalation_plan_description
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        if self.escalation_plan_name is not None:
            result['escalationPlanName'] = self.escalation_plan_name
        result['escalationPlanRules'] = []
        if self.escalation_plan_rules is not None:
            for k in self.escalation_plan_rules:
                result['escalationPlanRules'].append(k.to_map() if k else None)
        result['escalationPlanScopeObjects'] = []
        if self.escalation_plan_scope_objects is not None:
            for k in self.escalation_plan_scope_objects:
                result['escalationPlanScopeObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('escalationPlanDescription') is not None:
            self.escalation_plan_description = m.get('escalationPlanDescription')
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        if m.get('escalationPlanName') is not None:
            self.escalation_plan_name = m.get('escalationPlanName')
        self.escalation_plan_rules = []
        if m.get('escalationPlanRules') is not None:
            for k in m.get('escalationPlanRules'):
                temp_model = GetEscalationPlanResponseBodyDataEscalationPlanRules()
                self.escalation_plan_rules.append(temp_model.from_map(k))
        self.escalation_plan_scope_objects = []
        if m.get('escalationPlanScopeObjects') is not None:
            for k in m.get('escalationPlanScopeObjects'):
                temp_model = GetEscalationPlanResponseBodyDataEscalationPlanScopeObjects()
                self.escalation_plan_scope_objects.append(temp_model.from_map(k))
        return self


class GetEscalationPlanResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: GetEscalationPlanResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEscalationPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEscalationPlanResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEscalationPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEscalationPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEscalationPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEscalationPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventRequest(TeaModel):
    def __init__(self, monitor_source_id=None):
        # 监控源ID不能为空
        self.monitor_source_id = monitor_source_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        return self


class GetEventResponseBodyData(TeaModel):
    def __init__(self, event_json=None, event_time=None, monitor_source_id=None, monitor_source_name=None):
        # 告警内容
        self.event_json = event_json  # type: str
        # 告警上报时间
        self.event_time = event_time  # type: str
        # 告警源ID
        self.monitor_source_id = monitor_source_id  # type: long
        # 告警源名称
        self.monitor_source_name = monitor_source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEventResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_json is not None:
            result['eventJson'] = self.event_json
        if self.event_time is not None:
            result['eventTime'] = self.event_time
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eventJson') is not None:
            self.event_json = m.get('eventJson')
        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        return self


class GetEventResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 告警
        self.data = data  # type: GetEventResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEventResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetEventResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEventResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEventResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHomePageGuidanceRequest(TeaModel):
    def __init__(self, client_token=None):
        # 幂等号
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHomePageGuidanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class GetHomePageGuidanceResponseBodyData(TeaModel):
    def __init__(self, notify_subscription_status=None, service_group_status=None, service_status=None,
                 users_status=None):
        # 通知订阅配置状态
        self.notify_subscription_status = notify_subscription_status  # type: bool
        # 服务组配置状态
        self.service_group_status = service_group_status  # type: bool
        # 服务配置状态
        self.service_status = service_status  # type: bool
        # 用户配置状态
        self.users_status = users_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHomePageGuidanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_subscription_status is not None:
            result['notifySubscriptionStatus'] = self.notify_subscription_status
        if self.service_group_status is not None:
            result['serviceGroupStatus'] = self.service_group_status
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.users_status is not None:
            result['usersStatus'] = self.users_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('notifySubscriptionStatus') is not None:
            self.notify_subscription_status = m.get('notifySubscriptionStatus')
        if m.get('serviceGroupStatus') is not None:
            self.service_group_status = m.get('serviceGroupStatus')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('usersStatus') is not None:
            self.users_status = m.get('usersStatus')
        return self


class GetHomePageGuidanceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetHomePageGuidanceResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHomePageGuidanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetHomePageGuidanceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetHomePageGuidanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHomePageGuidanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHomePageGuidanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetHomePageGuidanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIncidentRequest(TeaModel):
    def __init__(self, client_token=None, incident_id=None):
        # 幂等校验
        self.client_token = client_token  # type: str
        # 事件ID
        self.incident_id = incident_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIncidentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        return self


class GetIncidentResponseBodyData(TeaModel):
    def __init__(self, assign_user_id=None, assign_user_name=None, assign_user_phone=None, create_time=None,
                 duration_time=None, effect=None, incident_description=None, incident_id=None, incident_level=None,
                 incident_number=None, incident_status=None, incident_title=None, is_manual=None, is_upgrade=None,
                 notify_channels=None, problem_id=None, problem_number=None, related_service_description=None,
                 related_service_group_id=None, related_service_group_name=None, related_service_id=None, related_service_name=None,
                 route_rule_id=None, route_rule_name=None):
        # 分派的用户ID
        self.assign_user_id = assign_user_id  # type: long
        # 分派的用户姓名 (用户表获取)
        self.assign_user_name = assign_user_name  # type: str
        # 分派的用户手机号
        self.assign_user_phone = assign_user_phone  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 持续时间
        self.duration_time = duration_time  # type: long
        # HIGH	影响等级 高：HIGH 低 LOW
        self.effect = effect  # type: str
        # 事件描述
        self.incident_description = incident_description  # type: str
        # 事件Id
        self.incident_id = incident_id  # type: long
        # 事件级别 P1 P2 P3 P4
        self.incident_level = incident_level  # type: str
        # 事件编号
        self.incident_number = incident_number  # type: str
        # 事件状态 ASSIGNED已分派 RESPONDED已响应  FINISHED已完结
        self.incident_status = incident_status  # type: str
        # 事件标题
        self.incident_title = incident_title  # type: str
        # 事件来源 是：手动 否：自动
        self.is_manual = is_manual  # type: bool
        # 是否升级 是 否
        self.is_upgrade = is_upgrade  # type: bool
        # 通知渠道
        self.notify_channels = notify_channels  # type: list[str]
        # 故障Id
        self.problem_id = problem_id  # type: long
        # 故障编号
        self.problem_number = problem_number  # type: str
        # 关联服务描述
        self.related_service_description = related_service_description  # type: str
        # 关联服服务id
        self.related_service_group_id = related_service_group_id  # type: long
        # 关联服务组名称
        self.related_service_group_name = related_service_group_name  # type: str
        # 关联服务ID
        self.related_service_id = related_service_id  # type: long
        # 关联服务名称
        self.related_service_name = related_service_name  # type: str
        # 流转规则ID
        self.route_rule_id = route_rule_id  # type: long
        # 流转规则名称
        self.route_rule_name = route_rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIncidentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_user_id is not None:
            result['assignUserId'] = self.assign_user_id
        if self.assign_user_name is not None:
            result['assignUserName'] = self.assign_user_name
        if self.assign_user_phone is not None:
            result['assignUserPhone'] = self.assign_user_phone
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.duration_time is not None:
            result['durationTime'] = self.duration_time
        if self.effect is not None:
            result['effect'] = self.effect
        if self.incident_description is not None:
            result['incidentDescription'] = self.incident_description
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_level is not None:
            result['incidentLevel'] = self.incident_level
        if self.incident_number is not None:
            result['incidentNumber'] = self.incident_number
        if self.incident_status is not None:
            result['incidentStatus'] = self.incident_status
        if self.incident_title is not None:
            result['incidentTitle'] = self.incident_title
        if self.is_manual is not None:
            result['isManual'] = self.is_manual
        if self.is_upgrade is not None:
            result['isUpgrade'] = self.is_upgrade
        if self.notify_channels is not None:
            result['notifyChannels'] = self.notify_channels
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_number is not None:
            result['problemNumber'] = self.problem_number
        if self.related_service_description is not None:
            result['relatedServiceDescription'] = self.related_service_description
        if self.related_service_group_id is not None:
            result['relatedServiceGroupId'] = self.related_service_group_id
        if self.related_service_group_name is not None:
            result['relatedServiceGroupName'] = self.related_service_group_name
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.related_service_name is not None:
            result['relatedServiceName'] = self.related_service_name
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        if self.route_rule_name is not None:
            result['routeRuleName'] = self.route_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignUserId') is not None:
            self.assign_user_id = m.get('assignUserId')
        if m.get('assignUserName') is not None:
            self.assign_user_name = m.get('assignUserName')
        if m.get('assignUserPhone') is not None:
            self.assign_user_phone = m.get('assignUserPhone')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('durationTime') is not None:
            self.duration_time = m.get('durationTime')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('incidentDescription') is not None:
            self.incident_description = m.get('incidentDescription')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentLevel') is not None:
            self.incident_level = m.get('incidentLevel')
        if m.get('incidentNumber') is not None:
            self.incident_number = m.get('incidentNumber')
        if m.get('incidentStatus') is not None:
            self.incident_status = m.get('incidentStatus')
        if m.get('incidentTitle') is not None:
            self.incident_title = m.get('incidentTitle')
        if m.get('isManual') is not None:
            self.is_manual = m.get('isManual')
        if m.get('isUpgrade') is not None:
            self.is_upgrade = m.get('isUpgrade')
        if m.get('notifyChannels') is not None:
            self.notify_channels = m.get('notifyChannels')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemNumber') is not None:
            self.problem_number = m.get('problemNumber')
        if m.get('relatedServiceDescription') is not None:
            self.related_service_description = m.get('relatedServiceDescription')
        if m.get('relatedServiceGroupId') is not None:
            self.related_service_group_id = m.get('relatedServiceGroupId')
        if m.get('relatedServiceGroupName') is not None:
            self.related_service_group_name = m.get('relatedServiceGroupName')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('relatedServiceName') is not None:
            self.related_service_name = m.get('relatedServiceName')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('routeRuleName') is not None:
            self.route_rule_name = m.get('routeRuleName')
        return self


class GetIncidentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetIncidentResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetIncidentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetIncidentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetIncidentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetIncidentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIncidentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIncidentStatisticsRequest(TeaModel):
    def __init__(self, client_token=None):
        # 幂等校验Id
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIncidentStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class GetIncidentStatisticsResponseBodyData(TeaModel):
    def __init__(self, all_finish=None, all_response=None, my_finish=None, my_response=None):
        # 所有 完结
        self.all_finish = all_finish  # type: int
        # 所有 待响应
        self.all_response = all_response  # type: int
        # 我的 完结
        self.my_finish = my_finish  # type: int
        # 我的 待响应
        self.my_response = my_response  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIncidentStatisticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_finish is not None:
            result['allFinish'] = self.all_finish
        if self.all_response is not None:
            result['allResponse'] = self.all_response
        if self.my_finish is not None:
            result['myFinish'] = self.my_finish
        if self.my_response is not None:
            result['myResponse'] = self.my_response
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('allFinish') is not None:
            self.all_finish = m.get('allFinish')
        if m.get('allResponse') is not None:
            self.all_response = m.get('allResponse')
        if m.get('myFinish') is not None:
            self.my_finish = m.get('myFinish')
        if m.get('myResponse') is not None:
            self.my_response = m.get('myResponse')
        return self


class GetIncidentStatisticsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetIncidentStatisticsResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetIncidentStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetIncidentStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetIncidentStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetIncidentStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIncidentStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetIncidentStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIncidentSubtotalCountRequest(TeaModel):
    def __init__(self, client_token=None, incident_ids=None):
        # 幂等标识
        self.client_token = client_token  # type: str
        # 事件id列表
        self.incident_ids = incident_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIncidentSubtotalCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.incident_ids is not None:
            result['incidentIds'] = self.incident_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('incidentIds') is not None:
            self.incident_ids = m.get('incidentIds')
        return self


class GetIncidentSubtotalCountResponseBodyData(TeaModel):
    def __init__(self, request_id=None, subtotal_count=None):
        # id of the request
        self.request_id = request_id  # type: str
        # map
        self.subtotal_count = subtotal_count  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIncidentSubtotalCountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.subtotal_count is not None:
            result['subtotalCount'] = self.subtotal_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('subtotalCount') is not None:
            self.subtotal_count = m.get('subtotalCount')
        return self


class GetIncidentSubtotalCountResponseBody(TeaModel):
    def __init__(self, data=None):
        # data
        self.data = data  # type: GetIncidentSubtotalCountResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetIncidentSubtotalCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetIncidentSubtotalCountResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetIncidentSubtotalCountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetIncidentSubtotalCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIncidentSubtotalCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetIncidentSubtotalCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIntegrationConfigRequest(TeaModel):
    def __init__(self, client_token=None, integration_config_id=None):
        # 幂等id
        self.client_token = client_token  # type: str
        # 集成配置id
        self.integration_config_id = integration_config_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIntegrationConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        return self


class GetIntegrationConfigResponseBodyData(TeaModel):
    def __init__(self, access_key=None, integration_config_id=None, is_received_event=None, monitor_source_id=None,
                 monitor_source_name=None, monitor_source_short_name=None, status=None):
        # 集成秘钥
        self.access_key = access_key  # type: str
        # 集成配置id、
        self.integration_config_id = integration_config_id  # type: long
        # 是否接收报警
        self.is_received_event = is_received_event  # type: bool
        # 监控源id
        self.monitor_source_id = monitor_source_id  # type: long
        # 监控源名称
        self.monitor_source_name = monitor_source_name  # type: str
        # 监控源简称
        self.monitor_source_short_name = monitor_source_short_name  # type: str
        # 集成配置状态，DISABLE 禁用，INTEGRATED 已集成，UNINTEGRATED未集成
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIntegrationConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        if self.is_received_event is not None:
            result['isReceivedEvent'] = self.is_received_event
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        if self.monitor_source_short_name is not None:
            result['monitorSourceShortName'] = self.monitor_source_short_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        if m.get('isReceivedEvent') is not None:
            self.is_received_event = m.get('isReceivedEvent')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        if m.get('monitorSourceShortName') is not None:
            self.monitor_source_short_name = m.get('monitorSourceShortName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetIntegrationConfigResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetIntegrationConfigResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetIntegrationConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetIntegrationConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetIntegrationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetIntegrationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIntegrationConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetIntegrationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProblemRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 故障ID
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class GetProblemResponseBodyDataCancelProblemOperateLogs(TeaModel):
    def __init__(self, action_name=None, action_time=None, operator=None, user_id=None):
        # 动作名称
        self.action_name = action_name  # type: str
        # 操作时间
        self.action_time = action_time  # type: str
        # 操作人
        self.operator = operator  # type: str
        # 用户ID
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemResponseBodyDataCancelProblemOperateLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.action_time is not None:
            result['actionTime'] = self.action_time
        if self.operator is not None:
            result['operator'] = self.operator
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('actionTime') is not None:
            self.action_time = m.get('actionTime')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetProblemResponseBodyDataCoordinationGroups(TeaModel):
    def __init__(self, service_group_id=None, service_group_name=None):
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 服务组名字
        self.service_group_name = service_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemResponseBodyDataCoordinationGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        return self


class GetProblemResponseBodyDataEffectionServices(TeaModel):
    def __init__(self, description=None, effection_level=None, effection_service_id=None, effection_status=None,
                 service_name=None):
        # 影响描述
        self.description = description  # type: str
        # 影响等级 P1 . P2 P3 P4
        self.effection_level = effection_level  # type: long
        # 服务ID
        self.effection_service_id = effection_service_id  # type: long
        # 影响服务状态  RECOVERED 已经恢复 ,UN_RECOVERED 未恢复
        self.effection_status = effection_status  # type: int
        # 服务名称
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemResponseBodyDataEffectionServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.effection_level is not None:
            result['effectionLevel'] = self.effection_level
        if self.effection_service_id is not None:
            result['effectionServiceId'] = self.effection_service_id
        if self.effection_status is not None:
            result['effectionStatus'] = self.effection_status
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('effectionLevel') is not None:
            self.effection_level = m.get('effectionLevel')
        if m.get('effectionServiceId') is not None:
            self.effection_service_id = m.get('effectionServiceId')
        if m.get('effectionStatus') is not None:
            self.effection_status = m.get('effectionStatus')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class GetProblemResponseBodyDataHandingProblemOperateLogs(TeaModel):
    def __init__(self, action_name=None, action_time=None, operator=None, user_id=None):
        # 动作名称
        self.action_name = action_name  # type: str
        # 操作时间
        self.action_time = action_time  # type: str
        # 操作人
        self.operator = operator  # type: str
        # 用户id
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemResponseBodyDataHandingProblemOperateLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.action_time is not None:
            result['actionTime'] = self.action_time
        if self.operator is not None:
            result['operator'] = self.operator
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('actionTime') is not None:
            self.action_time = m.get('actionTime')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetProblemResponseBodyDataReplayProblemOperateLogs(TeaModel):
    def __init__(self, action_name=None, action_time=None, operator=None, user_id=None):
        # 动作名称
        self.action_name = action_name  # type: str
        # 操作时间
        self.action_time = action_time  # type: str
        # 操作人
        self.operator = operator  # type: str
        # 用户id
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemResponseBodyDataReplayProblemOperateLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.action_time is not None:
            result['actionTime'] = self.action_time
        if self.operator is not None:
            result['operator'] = self.operator
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('actionTime') is not None:
            self.action_time = m.get('actionTime')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetProblemResponseBodyDataReplayingProblemOperateLogs(TeaModel):
    def __init__(self, action_name=None, action_time=None, operator=None, user_id=None):
        # 动作名称
        self.action_name = action_name  # type: str
        # 操作时间
        self.action_time = action_time  # type: str
        # 操作人
        self.operator = operator  # type: str
        # 用户id
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemResponseBodyDataReplayingProblemOperateLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.action_time is not None:
            result['actionTime'] = self.action_time
        if self.operator is not None:
            result['operator'] = self.operator
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('actionTime') is not None:
            self.action_time = m.get('actionTime')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetProblemResponseBodyDataRestoredProblemOperateLogs(TeaModel):
    def __init__(self, action_name=None, action_time=None, operator=None, user_id=None):
        # 动作名称
        self.action_name = action_name  # type: str
        # 操作时间
        self.action_time = action_time  # type: str
        # 操作人
        self.operator = operator  # type: str
        # 用户id
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemResponseBodyDataRestoredProblemOperateLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.action_time is not None:
            result['actionTime'] = self.action_time
        if self.operator is not None:
            result['operator'] = self.operator
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('actionTime') is not None:
            self.action_time = m.get('actionTime')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetProblemResponseBodyDataTimelines(TeaModel):
    def __init__(self, key_node=None):
        # 关键节点 码表:PROBLEM_KEY_NODE (逗号分隔)
        self.key_node = key_node  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemResponseBodyDataTimelines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_node is not None:
            result['keyNode'] = self.key_node
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('keyNode') is not None:
            self.key_node = m.get('keyNode')
        return self


class GetProblemResponseBodyData(TeaModel):
    def __init__(self, cancel_problem_operate_logs=None, cancel_reason=None, cancel_reason_description=None,
                 coordination_groups=None, create_time=None, discover_time=None, duration_time=None, effection_services=None,
                 feedback=None, handing_problem_operate_logs=None, incident_id=None, incident_number=None,
                 main_handler=None, main_handler_id=None, main_handler_phone=None, preliminary_reason=None, problem_id=None,
                 problem_level=None, problem_name=None, problem_number=None, problem_status=None, progress_summary=None,
                 progress_summary_rich_text_id=None, recovery_time=None, related_service_id=None, replay_problem_operate_logs=None,
                 replaying_problem_operate_logs=None, restored_problem_operate_logs=None, service_name=None, timelines=None):
        # 已取消故障操作日志
        self.cancel_problem_operate_logs = cancel_problem_operate_logs  # type: list[GetProblemResponseBodyDataCancelProblemOperateLogs]
        # 取消原因
        self.cancel_reason = cancel_reason  # type: long
        # 取消原因描述
        self.cancel_reason_description = cancel_reason_description  # type: str
        # 应急协同组
        self.coordination_groups = coordination_groups  # type: list[GetProblemResponseBodyDataCoordinationGroups]
        # 创建时间
        self.create_time = create_time  # type: str
        # 发现时间
        self.discover_time = discover_time  # type: str
        # 持续时间
        self.duration_time = duration_time  # type: long
        # 影响服务
        self.effection_services = effection_services  # type: list[GetProblemResponseBodyDataEffectionServices]
        # 舆情反馈
        self.feedback = feedback  # type: str
        # 处理中故障操作日志
        self.handing_problem_operate_logs = handing_problem_operate_logs  # type: list[GetProblemResponseBodyDataHandingProblemOperateLogs]
        # 事件id
        self.incident_id = incident_id  # type: long
        # 事件编号
        self.incident_number = incident_number  # type: str
        # 主要处理人
        self.main_handler = main_handler  # type: long
        # 主要处理人ID
        self.main_handler_id = main_handler_id  # type: long
        # 主要处理人手机号
        self.main_handler_phone = main_handler_phone  # type: str
        # 初步原因
        self.preliminary_reason = preliminary_reason  # type: str
        # ID
        self.problem_id = problem_id  # type: long
        # 故障等级 P1 P2 P3 P4
        self.problem_level = problem_level  # type: int
        # 故障名称
        self.problem_name = problem_name  # type: str
        # 故障编号
        self.problem_number = problem_number  # type: str
        # 故障状态  HANDLING    处理中 RECOVERED  已恢复  REPLAYING   复盘中  REPLAYED     已复盘 CANCEL        已取消
        self.problem_status = problem_status  # type: int
        # 进展摘要
        self.progress_summary = progress_summary  # type: str
        # 进展摘要富文本id
        self.progress_summary_rich_text_id = progress_summary_rich_text_id  # type: long
        # 恢复时间
        self.recovery_time = recovery_time  # type: str
        # 关联服务ID
        self.related_service_id = related_service_id  # type: long
        # 已复盘故障操作日志
        self.replay_problem_operate_logs = replay_problem_operate_logs  # type: list[GetProblemResponseBodyDataReplayProblemOperateLogs]
        # 复盘中故障操作日志
        self.replaying_problem_operate_logs = replaying_problem_operate_logs  # type: list[GetProblemResponseBodyDataReplayingProblemOperateLogs]
        # 已恢复故障操作日志
        self.restored_problem_operate_logs = restored_problem_operate_logs  # type: list[GetProblemResponseBodyDataRestoredProblemOperateLogs]
        # 关联服务 名称
        self.service_name = service_name  # type: str
        # 故障操作时间线
        self.timelines = timelines  # type: list[GetProblemResponseBodyDataTimelines]

    def validate(self):
        if self.cancel_problem_operate_logs:
            for k in self.cancel_problem_operate_logs:
                if k:
                    k.validate()
        if self.coordination_groups:
            for k in self.coordination_groups:
                if k:
                    k.validate()
        if self.effection_services:
            for k in self.effection_services:
                if k:
                    k.validate()
        if self.handing_problem_operate_logs:
            for k in self.handing_problem_operate_logs:
                if k:
                    k.validate()
        if self.replay_problem_operate_logs:
            for k in self.replay_problem_operate_logs:
                if k:
                    k.validate()
        if self.replaying_problem_operate_logs:
            for k in self.replaying_problem_operate_logs:
                if k:
                    k.validate()
        if self.restored_problem_operate_logs:
            for k in self.restored_problem_operate_logs:
                if k:
                    k.validate()
        if self.timelines:
            for k in self.timelines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProblemResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cancelProblemOperateLogs'] = []
        if self.cancel_problem_operate_logs is not None:
            for k in self.cancel_problem_operate_logs:
                result['cancelProblemOperateLogs'].append(k.to_map() if k else None)
        if self.cancel_reason is not None:
            result['cancelReason'] = self.cancel_reason
        if self.cancel_reason_description is not None:
            result['cancelReasonDescription'] = self.cancel_reason_description
        result['coordinationGroups'] = []
        if self.coordination_groups is not None:
            for k in self.coordination_groups:
                result['coordinationGroups'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.discover_time is not None:
            result['discoverTime'] = self.discover_time
        if self.duration_time is not None:
            result['durationTime'] = self.duration_time
        result['effectionServices'] = []
        if self.effection_services is not None:
            for k in self.effection_services:
                result['effectionServices'].append(k.to_map() if k else None)
        if self.feedback is not None:
            result['feedback'] = self.feedback
        result['handingProblemOperateLogs'] = []
        if self.handing_problem_operate_logs is not None:
            for k in self.handing_problem_operate_logs:
                result['handingProblemOperateLogs'].append(k.to_map() if k else None)
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_number is not None:
            result['incidentNumber'] = self.incident_number
        if self.main_handler is not None:
            result['mainHandler'] = self.main_handler
        if self.main_handler_id is not None:
            result['mainHandlerId'] = self.main_handler_id
        if self.main_handler_phone is not None:
            result['mainHandlerPhone'] = self.main_handler_phone
        if self.preliminary_reason is not None:
            result['preliminaryReason'] = self.preliminary_reason
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_level is not None:
            result['problemLevel'] = self.problem_level
        if self.problem_name is not None:
            result['problemName'] = self.problem_name
        if self.problem_number is not None:
            result['problemNumber'] = self.problem_number
        if self.problem_status is not None:
            result['problemStatus'] = self.problem_status
        if self.progress_summary is not None:
            result['progressSummary'] = self.progress_summary
        if self.progress_summary_rich_text_id is not None:
            result['progressSummaryRichTextId'] = self.progress_summary_rich_text_id
        if self.recovery_time is not None:
            result['recoveryTime'] = self.recovery_time
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        result['replayProblemOperateLogs'] = []
        if self.replay_problem_operate_logs is not None:
            for k in self.replay_problem_operate_logs:
                result['replayProblemOperateLogs'].append(k.to_map() if k else None)
        result['replayingProblemOperateLogs'] = []
        if self.replaying_problem_operate_logs is not None:
            for k in self.replaying_problem_operate_logs:
                result['replayingProblemOperateLogs'].append(k.to_map() if k else None)
        result['restoredProblemOperateLogs'] = []
        if self.restored_problem_operate_logs is not None:
            for k in self.restored_problem_operate_logs:
                result['restoredProblemOperateLogs'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        result['timelines'] = []
        if self.timelines is not None:
            for k in self.timelines:
                result['timelines'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cancel_problem_operate_logs = []
        if m.get('cancelProblemOperateLogs') is not None:
            for k in m.get('cancelProblemOperateLogs'):
                temp_model = GetProblemResponseBodyDataCancelProblemOperateLogs()
                self.cancel_problem_operate_logs.append(temp_model.from_map(k))
        if m.get('cancelReason') is not None:
            self.cancel_reason = m.get('cancelReason')
        if m.get('cancelReasonDescription') is not None:
            self.cancel_reason_description = m.get('cancelReasonDescription')
        self.coordination_groups = []
        if m.get('coordinationGroups') is not None:
            for k in m.get('coordinationGroups'):
                temp_model = GetProblemResponseBodyDataCoordinationGroups()
                self.coordination_groups.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('discoverTime') is not None:
            self.discover_time = m.get('discoverTime')
        if m.get('durationTime') is not None:
            self.duration_time = m.get('durationTime')
        self.effection_services = []
        if m.get('effectionServices') is not None:
            for k in m.get('effectionServices'):
                temp_model = GetProblemResponseBodyDataEffectionServices()
                self.effection_services.append(temp_model.from_map(k))
        if m.get('feedback') is not None:
            self.feedback = m.get('feedback')
        self.handing_problem_operate_logs = []
        if m.get('handingProblemOperateLogs') is not None:
            for k in m.get('handingProblemOperateLogs'):
                temp_model = GetProblemResponseBodyDataHandingProblemOperateLogs()
                self.handing_problem_operate_logs.append(temp_model.from_map(k))
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentNumber') is not None:
            self.incident_number = m.get('incidentNumber')
        if m.get('mainHandler') is not None:
            self.main_handler = m.get('mainHandler')
        if m.get('mainHandlerId') is not None:
            self.main_handler_id = m.get('mainHandlerId')
        if m.get('mainHandlerPhone') is not None:
            self.main_handler_phone = m.get('mainHandlerPhone')
        if m.get('preliminaryReason') is not None:
            self.preliminary_reason = m.get('preliminaryReason')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemLevel') is not None:
            self.problem_level = m.get('problemLevel')
        if m.get('problemName') is not None:
            self.problem_name = m.get('problemName')
        if m.get('problemNumber') is not None:
            self.problem_number = m.get('problemNumber')
        if m.get('problemStatus') is not None:
            self.problem_status = m.get('problemStatus')
        if m.get('progressSummary') is not None:
            self.progress_summary = m.get('progressSummary')
        if m.get('progressSummaryRichTextId') is not None:
            self.progress_summary_rich_text_id = m.get('progressSummaryRichTextId')
        if m.get('recoveryTime') is not None:
            self.recovery_time = m.get('recoveryTime')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        self.replay_problem_operate_logs = []
        if m.get('replayProblemOperateLogs') is not None:
            for k in m.get('replayProblemOperateLogs'):
                temp_model = GetProblemResponseBodyDataReplayProblemOperateLogs()
                self.replay_problem_operate_logs.append(temp_model.from_map(k))
        self.replaying_problem_operate_logs = []
        if m.get('replayingProblemOperateLogs') is not None:
            for k in m.get('replayingProblemOperateLogs'):
                temp_model = GetProblemResponseBodyDataReplayingProblemOperateLogs()
                self.replaying_problem_operate_logs.append(temp_model.from_map(k))
        self.restored_problem_operate_logs = []
        if m.get('restoredProblemOperateLogs') is not None:
            for k in m.get('restoredProblemOperateLogs'):
                temp_model = GetProblemResponseBodyDataRestoredProblemOperateLogs()
                self.restored_problem_operate_logs.append(temp_model.from_map(k))
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        self.timelines = []
        if m.get('timelines') is not None:
            for k in m.get('timelines'):
                temp_model = GetProblemResponseBodyDataTimelines()
                self.timelines.append(temp_model.from_map(k))
        return self


class GetProblemResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 详情
        self.data = data  # type: GetProblemResponseBodyData
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProblemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProblemResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProblemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProblemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProblemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProblemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProblemEffectionServiceRequest(TeaModel):
    def __init__(self, client_token=None, effection_service_id=None, problem_id=None):
        # clientToken
        self.client_token = client_token  # type: str
        # id主键
        self.effection_service_id = effection_service_id  # type: long
        # 故障id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemEffectionServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.effection_service_id is not None:
            result['effectionServiceId'] = self.effection_service_id
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('effectionServiceId') is not None:
            self.effection_service_id = m.get('effectionServiceId')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class GetProblemEffectionServiceResponseBodyData(TeaModel):
    def __init__(self, description=None, effection_service_id=None, level=None, pic_url=None, service_id=None,
                 service_name=None, status=None):
        # 影响描述
        self.description = description  # type: str
        # 影响服务id
        self.effection_service_id = effection_service_id  # type: long
        # 影响等级
        self.level = level  # type: long
        # 图片链接
        self.pic_url = pic_url  # type: list[str]
        # 服务id
        self.service_id = service_id  # type: long
        # 服务名称
        self.service_name = service_name  # type: str
        # 影响状态 0 未恢复 1已恢复
        self.status = status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemEffectionServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.effection_service_id is not None:
            result['effectionServiceId'] = self.effection_service_id
        if self.level is not None:
            result['level'] = self.level
        if self.pic_url is not None:
            result['picUrl'] = self.pic_url
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('effectionServiceId') is not None:
            self.effection_service_id = m.get('effectionServiceId')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetProblemEffectionServiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetProblemEffectionServiceResponseBodyData
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProblemEffectionServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProblemEffectionServiceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProblemEffectionServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProblemEffectionServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProblemEffectionServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProblemEffectionServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProblemImprovementRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 故障ID
        self.problem_id = problem_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemImprovementRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class GetProblemImprovementResponseBodyDataMeasureList(TeaModel):
    def __init__(self, check_standard=None, check_user_id=None, check_user_name=None, content=None,
                 director_id=None, director_name=None, measure_id=None, plan_finish_time=None, stalker_id=None,
                 stalker_name=None, status=None, type=None):
        # 验收标准
        self.check_standard = check_standard  # type: str
        # 验收人id
        self.check_user_id = check_user_id  # type: long
        # 验收人名称
        self.check_user_name = check_user_name  # type: str
        # 措施内容
        self.content = content  # type: str
        # 负责人id
        self.director_id = director_id  # type: long
        # 负责人名称
        self.director_name = director_name  # type: str
        # 改进措施id 用于删除或更新
        self.measure_id = measure_id  # type: long
        # 计划完成时间
        self.plan_finish_time = plan_finish_time  # type: str
        # 跟踪人id
        self.stalker_id = stalker_id  # type: long
        # 跟踪人名称
        self.stalker_name = stalker_name  # type: str
        # UNIMPROVED	状态 IMPROVED 改进 2 未改进UNIMPROVED
        self.status = status  # type: str
        # 措施类型
        self.type = type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemImprovementResponseBodyDataMeasureList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_standard is not None:
            result['checkStandard'] = self.check_standard
        if self.check_user_id is not None:
            result['checkUserId'] = self.check_user_id
        if self.check_user_name is not None:
            result['checkUserName'] = self.check_user_name
        if self.content is not None:
            result['content'] = self.content
        if self.director_id is not None:
            result['directorId'] = self.director_id
        if self.director_name is not None:
            result['directorName'] = self.director_name
        if self.measure_id is not None:
            result['measureId'] = self.measure_id
        if self.plan_finish_time is not None:
            result['planFinishTime'] = self.plan_finish_time
        if self.stalker_id is not None:
            result['stalkerId'] = self.stalker_id
        if self.stalker_name is not None:
            result['stalkerName'] = self.stalker_name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('checkStandard') is not None:
            self.check_standard = m.get('checkStandard')
        if m.get('checkUserId') is not None:
            self.check_user_id = m.get('checkUserId')
        if m.get('checkUserName') is not None:
            self.check_user_name = m.get('checkUserName')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('directorId') is not None:
            self.director_id = m.get('directorId')
        if m.get('directorName') is not None:
            self.director_name = m.get('directorName')
        if m.get('measureId') is not None:
            self.measure_id = m.get('measureId')
        if m.get('planFinishTime') is not None:
            self.plan_finish_time = m.get('planFinishTime')
        if m.get('stalkerId') is not None:
            self.stalker_id = m.get('stalkerId')
        if m.get('stalkerName') is not None:
            self.stalker_name = m.get('stalkerName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetProblemImprovementResponseBodyData(TeaModel):
    def __init__(self, discover_source=None, duty_department_id=None, duty_department_name=None, duty_user_id=None,
                 duty_user_name=None, duty_user_phone=None, injection_mode=None, is_manual=None, measure_list=None,
                 monitor_source_name=None, problem_id=None, problem_reason=None, recent_activity=None, recovery_mode=None,
                 relation_changes=None, remark=None, replay_duty_user_id=None, replay_duty_user_name=None,
                 replay_duty_user_phone=None, user_report=None):
        # 发现来源 码表:PROBLEM_DISCOVER_SOURCE
        self.discover_source = discover_source  # type: str
        # 故障责任部门
        self.duty_department_id = duty_department_id  # type: str
        # 故障责任部门名称
        self.duty_department_name = duty_department_name  # type: str
        # 故障责任人id
        self.duty_user_id = duty_user_id  # type: long
        # 故障责任人名称
        self.duty_user_name = duty_user_name  # type: str
        # 故障责任人手机号
        self.duty_user_phone = duty_user_phone  # type: str
        # 注入方式 码表:PROBLEM_INJECTION_MODE
        self.injection_mode = injection_mode  # type: str
        # 是否手动
        self.is_manual = is_manual  # type: bool
        # 改进措施列表
        self.measure_list = measure_list  # type: list[GetProblemImprovementResponseBodyDataMeasureList]
        # 监控源
        self.monitor_source_name = monitor_source_name  # type: str
        # 故障ID
        self.problem_id = problem_id  # type: str
        # 故障原因
        self.problem_reason = problem_reason  # type: str
        # 最近活动 码表:PROBLEM_RECENT_ACTIVITY
        self.recent_activity = recent_activity  # type: str
        # 恢复方式  码表:PROBLEM_RECOVERY_MODE
        self.recovery_mode = recovery_mode  # type: str
        # 关联变更
        self.relation_changes = relation_changes  # type: str
        # 备注
        self.remark = remark  # type: str
        # 复盘负责人id
        self.replay_duty_user_id = replay_duty_user_id  # type: long
        # 复盘负责人名称
        self.replay_duty_user_name = replay_duty_user_name  # type: str
        # 复盘负责人手机号
        self.replay_duty_user_phone = replay_duty_user_phone  # type: str
        # 用户上报 码表:PROBLEM_USER_REPORT
        self.user_report = user_report  # type: long

    def validate(self):
        if self.measure_list:
            for k in self.measure_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProblemImprovementResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discover_source is not None:
            result['discoverSource'] = self.discover_source
        if self.duty_department_id is not None:
            result['dutyDepartmentId'] = self.duty_department_id
        if self.duty_department_name is not None:
            result['dutyDepartmentName'] = self.duty_department_name
        if self.duty_user_id is not None:
            result['dutyUserId'] = self.duty_user_id
        if self.duty_user_name is not None:
            result['dutyUserName'] = self.duty_user_name
        if self.duty_user_phone is not None:
            result['dutyUserPhone'] = self.duty_user_phone
        if self.injection_mode is not None:
            result['injectionMode'] = self.injection_mode
        if self.is_manual is not None:
            result['isManual'] = self.is_manual
        result['measureList'] = []
        if self.measure_list is not None:
            for k in self.measure_list:
                result['measureList'].append(k.to_map() if k else None)
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_reason is not None:
            result['problemReason'] = self.problem_reason
        if self.recent_activity is not None:
            result['recentActivity'] = self.recent_activity
        if self.recovery_mode is not None:
            result['recoveryMode'] = self.recovery_mode
        if self.relation_changes is not None:
            result['relationChanges'] = self.relation_changes
        if self.remark is not None:
            result['remark'] = self.remark
        if self.replay_duty_user_id is not None:
            result['replayDutyUserId'] = self.replay_duty_user_id
        if self.replay_duty_user_name is not None:
            result['replayDutyUserName'] = self.replay_duty_user_name
        if self.replay_duty_user_phone is not None:
            result['replayDutyUserPhone'] = self.replay_duty_user_phone
        if self.user_report is not None:
            result['userReport'] = self.user_report
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('discoverSource') is not None:
            self.discover_source = m.get('discoverSource')
        if m.get('dutyDepartmentId') is not None:
            self.duty_department_id = m.get('dutyDepartmentId')
        if m.get('dutyDepartmentName') is not None:
            self.duty_department_name = m.get('dutyDepartmentName')
        if m.get('dutyUserId') is not None:
            self.duty_user_id = m.get('dutyUserId')
        if m.get('dutyUserName') is not None:
            self.duty_user_name = m.get('dutyUserName')
        if m.get('dutyUserPhone') is not None:
            self.duty_user_phone = m.get('dutyUserPhone')
        if m.get('injectionMode') is not None:
            self.injection_mode = m.get('injectionMode')
        if m.get('isManual') is not None:
            self.is_manual = m.get('isManual')
        self.measure_list = []
        if m.get('measureList') is not None:
            for k in m.get('measureList'):
                temp_model = GetProblemImprovementResponseBodyDataMeasureList()
                self.measure_list.append(temp_model.from_map(k))
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemReason') is not None:
            self.problem_reason = m.get('problemReason')
        if m.get('recentActivity') is not None:
            self.recent_activity = m.get('recentActivity')
        if m.get('recoveryMode') is not None:
            self.recovery_mode = m.get('recoveryMode')
        if m.get('relationChanges') is not None:
            self.relation_changes = m.get('relationChanges')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('replayDutyUserId') is not None:
            self.replay_duty_user_id = m.get('replayDutyUserId')
        if m.get('replayDutyUserName') is not None:
            self.replay_duty_user_name = m.get('replayDutyUserName')
        if m.get('replayDutyUserPhone') is not None:
            self.replay_duty_user_phone = m.get('replayDutyUserPhone')
        if m.get('userReport') is not None:
            self.user_report = m.get('userReport')
        return self


class GetProblemImprovementResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetProblemImprovementResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProblemImprovementResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProblemImprovementResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProblemImprovementResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProblemImprovementResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProblemImprovementResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProblemImprovementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProblemPreviewRequest(TeaModel):
    def __init__(self, client_token=None, effect_service_ids=None, incident_id=None, problem_id=None,
                 problem_level=None, problem_notify_type=None, related_service_id=None, service_group_ids=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 影响服务
        self.effect_service_ids = effect_service_ids  # type: list[long]
        # 事件Id
        self.incident_id = incident_id  # type: long
        # 故障id
        self.problem_id = problem_id  # type: long
        # 故障等级
        self.problem_level = problem_level  # type: str
        # 通告类型
        self.problem_notify_type = problem_notify_type  # type: str
        # 所属服务
        self.related_service_id = related_service_id  # type: long
        # 应急协同组
        self.service_group_ids = service_group_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemPreviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.effect_service_ids is not None:
            result['effectServiceIds'] = self.effect_service_ids
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_level is not None:
            result['problemLevel'] = self.problem_level
        if self.problem_notify_type is not None:
            result['problemNotifyType'] = self.problem_notify_type
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.service_group_ids is not None:
            result['serviceGroupIds'] = self.service_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('effectServiceIds') is not None:
            self.effect_service_ids = m.get('effectServiceIds')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemLevel') is not None:
            self.problem_level = m.get('problemLevel')
        if m.get('problemNotifyType') is not None:
            self.problem_notify_type = m.get('problemNotifyType')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('serviceGroupIds') is not None:
            self.service_group_ids = m.get('serviceGroupIds')
        return self


class GetProblemPreviewResponseBodyDataMailUsers(TeaModel):
    def __init__(self, username=None):
        # 用户名称
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataMailUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetProblemPreviewResponseBodyDataMail(TeaModel):
    def __init__(self, count=None, users=None):
        # 数量
        self.count = count  # type: long
        self.users = users  # type: list[GetProblemPreviewResponseBodyDataMailUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataMail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = GetProblemPreviewResponseBodyDataMailUsers()
                self.users.append(temp_model.from_map(k))
        return self


class GetProblemPreviewResponseBodyDataProblemCoordinationGroups(TeaModel):
    def __init__(self, service_group_description=None, service_group_id=None, service_group_name=None):
        # 服务组Maison
        self.service_group_description = service_group_description  # type: str
        # 服务Id
        self.service_group_id = service_group_id  # type: long
        # 服务组名称
        self.service_group_name = service_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataProblemCoordinationGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_group_description is not None:
            result['serviceGroupDescription'] = self.service_group_description
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceGroupDescription') is not None:
            self.service_group_description = m.get('serviceGroupDescription')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        return self


class GetProblemPreviewResponseBodyDataProblemEffectionServices(TeaModel):
    def __init__(self, service_id=None, service_name=None):
        # 影响服务Id
        self.service_id = service_id  # type: long
        # 影响服务名称
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataProblemEffectionServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class GetProblemPreviewResponseBodyDataProblem(TeaModel):
    def __init__(self, coordination_groups=None, create_time=None, discover_time=None, effection_services=None,
                 is_manual=None, is_upgrade=None, main_handler_id=None, main_handler_name=None, preliminary_reason=None,
                 problem_id=None, problem_level=None, problem_name=None, problem_status=None, progress_summary=None,
                 progress_summary_rich_text_id=None, recovery_time=None, related_service_id=None, service_name=None):
        # 应急协同组
        self.coordination_groups = coordination_groups  # type: list[GetProblemPreviewResponseBodyDataProblemCoordinationGroups]
        # 创建时间
        self.create_time = create_time  # type: str
        # 发现时间
        self.discover_time = discover_time  # type: str
        # 影响服务
        self.effection_services = effection_services  # type: list[GetProblemPreviewResponseBodyDataProblemEffectionServices]
        # 是否手动
        self.is_manual = is_manual  # type: bool
        # 是否升级
        self.is_upgrade = is_upgrade  # type: bool
        # 主要处理人Id
        self.main_handler_id = main_handler_id  # type: str
        # 主要处理人
        self.main_handler_name = main_handler_name  # type: str
        # 初步原因
        self.preliminary_reason = preliminary_reason  # type: str
        # 故障Id
        self.problem_id = problem_id  # type: long
        # 故障等级 1=P1 2=P2 3=P3 4=P4
        self.problem_level = problem_level  # type: str
        # 故障名称
        self.problem_name = problem_name  # type: str
        # 故障状态 1 处理中 2已恢复 3复盘中 4已复盘 5已取消
        self.problem_status = problem_status  # type: str
        # 进展摘要
        self.progress_summary = progress_summary  # type: str
        # 富文本id
        self.progress_summary_rich_text_id = progress_summary_rich_text_id  # type: long
        # 恢复时间
        self.recovery_time = recovery_time  # type: str
        # 关联服务ID
        self.related_service_id = related_service_id  # type: long
        # 关联服务 名称
        self.service_name = service_name  # type: str

    def validate(self):
        if self.coordination_groups:
            for k in self.coordination_groups:
                if k:
                    k.validate()
        if self.effection_services:
            for k in self.effection_services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataProblem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['coordinationGroups'] = []
        if self.coordination_groups is not None:
            for k in self.coordination_groups:
                result['coordinationGroups'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.discover_time is not None:
            result['discoverTime'] = self.discover_time
        result['effectionServices'] = []
        if self.effection_services is not None:
            for k in self.effection_services:
                result['effectionServices'].append(k.to_map() if k else None)
        if self.is_manual is not None:
            result['isManual'] = self.is_manual
        if self.is_upgrade is not None:
            result['isUpgrade'] = self.is_upgrade
        if self.main_handler_id is not None:
            result['mainHandlerId'] = self.main_handler_id
        if self.main_handler_name is not None:
            result['mainHandlerName'] = self.main_handler_name
        if self.preliminary_reason is not None:
            result['preliminaryReason'] = self.preliminary_reason
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_level is not None:
            result['problemLevel'] = self.problem_level
        if self.problem_name is not None:
            result['problemName'] = self.problem_name
        if self.problem_status is not None:
            result['problemStatus'] = self.problem_status
        if self.progress_summary is not None:
            result['progressSummary'] = self.progress_summary
        if self.progress_summary_rich_text_id is not None:
            result['progressSummaryRichTextId'] = self.progress_summary_rich_text_id
        if self.recovery_time is not None:
            result['recoveryTime'] = self.recovery_time
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.coordination_groups = []
        if m.get('coordinationGroups') is not None:
            for k in m.get('coordinationGroups'):
                temp_model = GetProblemPreviewResponseBodyDataProblemCoordinationGroups()
                self.coordination_groups.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('discoverTime') is not None:
            self.discover_time = m.get('discoverTime')
        self.effection_services = []
        if m.get('effectionServices') is not None:
            for k in m.get('effectionServices'):
                temp_model = GetProblemPreviewResponseBodyDataProblemEffectionServices()
                self.effection_services.append(temp_model.from_map(k))
        if m.get('isManual') is not None:
            self.is_manual = m.get('isManual')
        if m.get('isUpgrade') is not None:
            self.is_upgrade = m.get('isUpgrade')
        if m.get('mainHandlerId') is not None:
            self.main_handler_id = m.get('mainHandlerId')
        if m.get('mainHandlerName') is not None:
            self.main_handler_name = m.get('mainHandlerName')
        if m.get('preliminaryReason') is not None:
            self.preliminary_reason = m.get('preliminaryReason')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemLevel') is not None:
            self.problem_level = m.get('problemLevel')
        if m.get('problemName') is not None:
            self.problem_name = m.get('problemName')
        if m.get('problemStatus') is not None:
            self.problem_status = m.get('problemStatus')
        if m.get('progressSummary') is not None:
            self.progress_summary = m.get('progressSummary')
        if m.get('progressSummaryRichTextId') is not None:
            self.progress_summary_rich_text_id = m.get('progressSummaryRichTextId')
        if m.get('recoveryTime') is not None:
            self.recovery_time = m.get('recoveryTime')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class GetProblemPreviewResponseBodyDataSmsUsers(TeaModel):
    def __init__(self, username=None):
        # 用户名称
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataSmsUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetProblemPreviewResponseBodyDataSms(TeaModel):
    def __init__(self, count=None, users=None):
        # 数量
        self.count = count  # type: long
        self.users = users  # type: list[GetProblemPreviewResponseBodyDataSmsUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataSms, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = GetProblemPreviewResponseBodyDataSmsUsers()
                self.users.append(temp_model.from_map(k))
        return self


class GetProblemPreviewResponseBodyDataVoiceUsers(TeaModel):
    def __init__(self, username=None):
        # 用户
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataVoiceUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetProblemPreviewResponseBodyDataVoice(TeaModel):
    def __init__(self, count=None, users=None):
        # 数量
        self.count = count  # type: long
        self.users = users  # type: list[GetProblemPreviewResponseBodyDataVoiceUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataVoice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = GetProblemPreviewResponseBodyDataVoiceUsers()
                self.users.append(temp_model.from_map(k))
        return self


class GetProblemPreviewResponseBodyDataWebhookServiceGroups(TeaModel):
    def __init__(self, service_name=None):
        # 服务名称
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataWebhookServiceGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class GetProblemPreviewResponseBodyDataWebhook(TeaModel):
    def __init__(self, count=None, service_groups=None):
        # 数量
        self.count = count  # type: long
        self.service_groups = service_groups  # type: list[GetProblemPreviewResponseBodyDataWebhookServiceGroups]

    def validate(self):
        if self.service_groups:
            for k in self.service_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyDataWebhook, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['serviceGroups'] = []
        if self.service_groups is not None:
            for k in self.service_groups:
                result['serviceGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.service_groups = []
        if m.get('serviceGroups') is not None:
            for k in m.get('serviceGroups'):
                temp_model = GetProblemPreviewResponseBodyDataWebhookServiceGroups()
                self.service_groups.append(temp_model.from_map(k))
        return self


class GetProblemPreviewResponseBodyData(TeaModel):
    def __init__(self, de_after_data=None, de_before_data=None, mail=None, problem=None, sms=None,
                 up_after_data=None, up_before_data=None, voice=None, webhook=None):
        # 降级后数据
        self.de_after_data = de_after_data  # type: str
        # 降级前数据
        self.de_before_data = de_before_data  # type: str
        # 邮箱
        self.mail = mail  # type: GetProblemPreviewResponseBodyDataMail
        self.problem = problem  # type: GetProblemPreviewResponseBodyDataProblem
        # 短信
        self.sms = sms  # type: GetProblemPreviewResponseBodyDataSms
        # 升级后数据
        self.up_after_data = up_after_data  # type: str
        # 升级前数据
        self.up_before_data = up_before_data  # type: str
        # 语音
        self.voice = voice  # type: GetProblemPreviewResponseBodyDataVoice
        # webhook
        self.webhook = webhook  # type: GetProblemPreviewResponseBodyDataWebhook

    def validate(self):
        if self.mail:
            self.mail.validate()
        if self.problem:
            self.problem.validate()
        if self.sms:
            self.sms.validate()
        if self.voice:
            self.voice.validate()
        if self.webhook:
            self.webhook.validate()

    def to_map(self):
        _map = super(GetProblemPreviewResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.de_after_data is not None:
            result['deAfterData'] = self.de_after_data
        if self.de_before_data is not None:
            result['deBeforeData'] = self.de_before_data
        if self.mail is not None:
            result['mail'] = self.mail.to_map()
        if self.problem is not None:
            result['problem'] = self.problem.to_map()
        if self.sms is not None:
            result['sms'] = self.sms.to_map()
        if self.up_after_data is not None:
            result['upAfterData'] = self.up_after_data
        if self.up_before_data is not None:
            result['upBeforeData'] = self.up_before_data
        if self.voice is not None:
            result['voice'] = self.voice.to_map()
        if self.webhook is not None:
            result['webhook'] = self.webhook.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deAfterData') is not None:
            self.de_after_data = m.get('deAfterData')
        if m.get('deBeforeData') is not None:
            self.de_before_data = m.get('deBeforeData')
        if m.get('mail') is not None:
            temp_model = GetProblemPreviewResponseBodyDataMail()
            self.mail = temp_model.from_map(m['mail'])
        if m.get('problem') is not None:
            temp_model = GetProblemPreviewResponseBodyDataProblem()
            self.problem = temp_model.from_map(m['problem'])
        if m.get('sms') is not None:
            temp_model = GetProblemPreviewResponseBodyDataSms()
            self.sms = temp_model.from_map(m['sms'])
        if m.get('upAfterData') is not None:
            self.up_after_data = m.get('upAfterData')
        if m.get('upBeforeData') is not None:
            self.up_before_data = m.get('upBeforeData')
        if m.get('voice') is not None:
            temp_model = GetProblemPreviewResponseBodyDataVoice()
            self.voice = temp_model.from_map(m['voice'])
        if m.get('webhook') is not None:
            temp_model = GetProblemPreviewResponseBodyDataWebhook()
            self.webhook = temp_model.from_map(m['webhook'])
        return self


class GetProblemPreviewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetProblemPreviewResponseBodyData
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProblemPreviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProblemPreviewResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProblemPreviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetProblemPreviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProblemPreviewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProblemPreviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceStatisticsRequest(TeaModel):
    def __init__(self, client_token=None):
        # 幂等校验
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class GetResourceStatisticsResponseBodyData(TeaModel):
    def __init__(self, alert_count=None, incident_count=None, integration_count=None, problem_count=None):
        # 报警总数
        self.alert_count = alert_count  # type: int
        # 事件总数
        self.incident_count = incident_count  # type: int
        # 集成总数
        self.integration_count = integration_count  # type: int
        # 故障总数
        self.problem_count = problem_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceStatisticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_count is not None:
            result['alertCount'] = self.alert_count
        if self.incident_count is not None:
            result['incidentCount'] = self.incident_count
        if self.integration_count is not None:
            result['integrationCount'] = self.integration_count
        if self.problem_count is not None:
            result['problemCount'] = self.problem_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alertCount') is not None:
            self.alert_count = m.get('alertCount')
        if m.get('incidentCount') is not None:
            self.incident_count = m.get('incidentCount')
        if m.get('integrationCount') is not None:
            self.integration_count = m.get('integrationCount')
        if m.get('problemCount') is not None:
            self.problem_count = m.get('problemCount')
        return self


class GetResourceStatisticsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: GetResourceStatisticsResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetResourceStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetResourceStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetResourceStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResourceStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetResourceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRichTextRequest(TeaModel):
    def __init__(self, instance_id=None, instance_type=None, rich_text_id=None):
        # 资源类型
        self.instance_id = instance_id  # type: long
        self.instance_type = instance_type  # type: str
        # 资源id
        self.rich_text_id = rich_text_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRichTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.rich_text_id is not None:
            result['richTextId'] = self.rich_text_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('richTextId') is not None:
            self.rich_text_id = m.get('richTextId')
        return self


class GetRichTextResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, instance_type=None, rich_text=None):
        # 资源id
        self.instance_id = instance_id  # type: long
        # 资源类型
        self.instance_type = instance_type  # type: long
        # 富文本内容
        self.rich_text = rich_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRichTextResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.rich_text is not None:
            result['richText'] = self.rich_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('richText') is not None:
            self.rich_text = m.get('richText')
        return self


class GetRichTextResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: GetRichTextResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRichTextResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRichTextResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRichTextResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRichTextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRichTextResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRichTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRouteRuleRequest(TeaModel):
    def __init__(self, client_token=None, route_rule_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 规则ID
        self.route_rule_id = route_rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRouteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        return self


class GetRouteRuleResponseBodyDataEventRouteChildRulesConditions(TeaModel):
    def __init__(self, key=None, operation_symbol=None, value=None):
        # 条件可以
        self.key = key  # type: str
        # 操作符
        self.operation_symbol = operation_symbol  # type: str
        # 匹配值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRouteRuleResponseBodyDataEventRouteChildRulesConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operation_symbol is not None:
            result['operationSymbol'] = self.operation_symbol
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operationSymbol') is not None:
            self.operation_symbol = m.get('operationSymbol')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetRouteRuleResponseBodyDataEventRouteChildRules(TeaModel):
    def __init__(self, child_condition_relation=None, child_route_rule_id=None, conditions=None,
                 is_valid_child_rule=None, monitor_integration_config_id=None, monitor_source_id=None, monitor_source_name=None,
                 parent_rule_id=None):
        # 子条件计算关系，0-与，1-或
        self.child_condition_relation = child_condition_relation  # type: long
        # 子规则ID
        self.child_route_rule_id = child_route_rule_id  # type: long
        # 条件
        self.conditions = conditions  # type: list[GetRouteRuleResponseBodyDataEventRouteChildRulesConditions]
        # 是否有效得规则true有效 false无效
        self.is_valid_child_rule = is_valid_child_rule  # type: bool
        # 集成配置ID
        self.monitor_integration_config_id = monitor_integration_config_id  # type: long
        # 监控源ID
        self.monitor_source_id = monitor_source_id  # type: long
        # 监控源名称
        self.monitor_source_name = monitor_source_name  # type: str
        # 规则ID
        self.parent_rule_id = parent_rule_id  # type: long

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRouteRuleResponseBodyDataEventRouteChildRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_condition_relation is not None:
            result['childConditionRelation'] = self.child_condition_relation
        if self.child_route_rule_id is not None:
            result['childRouteRuleId'] = self.child_route_rule_id
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        if self.is_valid_child_rule is not None:
            result['isValidChildRule'] = self.is_valid_child_rule
        if self.monitor_integration_config_id is not None:
            result['monitorIntegrationConfigId'] = self.monitor_integration_config_id
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        if self.parent_rule_id is not None:
            result['parentRuleId'] = self.parent_rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('childConditionRelation') is not None:
            self.child_condition_relation = m.get('childConditionRelation')
        if m.get('childRouteRuleId') is not None:
            self.child_route_rule_id = m.get('childRouteRuleId')
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = GetRouteRuleResponseBodyDataEventRouteChildRulesConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('isValidChildRule') is not None:
            self.is_valid_child_rule = m.get('isValidChildRule')
        if m.get('monitorIntegrationConfigId') is not None:
            self.monitor_integration_config_id = m.get('monitorIntegrationConfigId')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        if m.get('parentRuleId') is not None:
            self.parent_rule_id = m.get('parentRuleId')
        return self


class GetRouteRuleResponseBodyData(TeaModel):
    def __init__(self, assign_object_id=None, assign_object_name=None, assign_object_type=None,
                 child_rule_relation=None, create_time=None, effection=None, enable_status=None, event_route_child_rules=None,
                 incident_level=None, match_count=None, notify_channel_names=None, notify_channels=None, related_service_id=None,
                 related_service_name=None, route_rule_id=None, route_type=None, rule_name=None, time_window=None, update_time=None):
        # 事件分派对象ID（服务组ID 或用户ID）
        self.assign_object_id = assign_object_id  # type: long
        # 通知对象名称
        self.assign_object_name = assign_object_name  # type: str
        # 事件分派对象类型 SERVICEGROUP 服务组  USER 单个用户
        self.assign_object_type = assign_object_type  # type: str
        # 子规则关系，0与，1或
        self.child_rule_relation = child_rule_relation  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 影响程度  LOW一般  HIGH-严重
        self.effection = effection  # type: str
        # 是否启用  DISABLE禁用 ENABLE 启用
        self.enable_status = enable_status  # type: str
        # 子规则
        self.event_route_child_rules = event_route_child_rules  # type: list[GetRouteRuleResponseBodyDataEventRouteChildRules]
        # 事件级别 P1 P2 P3 P4
        self.incident_level = incident_level  # type: str
        # 命中次数
        self.match_count = match_count  # type: long
        # 通知渠道名称
        self.notify_channel_names = notify_channel_names  # type: list[str]
        # 通知渠道
        self.notify_channels = notify_channels  # type: list[str]
        # 关联服务ID
        self.related_service_id = related_service_id  # type: long
        # 关联服务名称
        self.related_service_name = related_service_name  # type: str
        # 规则ID
        self.route_rule_id = route_rule_id  # type: long
        # 路由类型：INCIDENT 触发事件 ALERT 仅触发报警
        self.route_type = route_type  # type: str
        # 流转规则名字
        self.rule_name = rule_name  # type: str
        # 时间窗口
        self.time_window = time_window  # type: int
        # 修改时间
        self.update_time = update_time  # type: str

    def validate(self):
        if self.event_route_child_rules:
            for k in self.event_route_child_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRouteRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_object_id is not None:
            result['assignObjectId'] = self.assign_object_id
        if self.assign_object_name is not None:
            result['assignObjectName'] = self.assign_object_name
        if self.assign_object_type is not None:
            result['assignObjectType'] = self.assign_object_type
        if self.child_rule_relation is not None:
            result['childRuleRelation'] = self.child_rule_relation
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.effection is not None:
            result['effection'] = self.effection
        if self.enable_status is not None:
            result['enableStatus'] = self.enable_status
        result['eventRouteChildRules'] = []
        if self.event_route_child_rules is not None:
            for k in self.event_route_child_rules:
                result['eventRouteChildRules'].append(k.to_map() if k else None)
        if self.incident_level is not None:
            result['incidentLevel'] = self.incident_level
        if self.match_count is not None:
            result['matchCount'] = self.match_count
        if self.notify_channel_names is not None:
            result['notifyChannelNames'] = self.notify_channel_names
        if self.notify_channels is not None:
            result['notifyChannels'] = self.notify_channels
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.related_service_name is not None:
            result['relatedServiceName'] = self.related_service_name
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.time_window is not None:
            result['timeWindow'] = self.time_window
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignObjectId') is not None:
            self.assign_object_id = m.get('assignObjectId')
        if m.get('assignObjectName') is not None:
            self.assign_object_name = m.get('assignObjectName')
        if m.get('assignObjectType') is not None:
            self.assign_object_type = m.get('assignObjectType')
        if m.get('childRuleRelation') is not None:
            self.child_rule_relation = m.get('childRuleRelation')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('enableStatus') is not None:
            self.enable_status = m.get('enableStatus')
        self.event_route_child_rules = []
        if m.get('eventRouteChildRules') is not None:
            for k in m.get('eventRouteChildRules'):
                temp_model = GetRouteRuleResponseBodyDataEventRouteChildRules()
                self.event_route_child_rules.append(temp_model.from_map(k))
        if m.get('incidentLevel') is not None:
            self.incident_level = m.get('incidentLevel')
        if m.get('matchCount') is not None:
            self.match_count = m.get('matchCount')
        if m.get('notifyChannelNames') is not None:
            self.notify_channel_names = m.get('notifyChannelNames')
        if m.get('notifyChannels') is not None:
            self.notify_channels = m.get('notifyChannels')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('relatedServiceName') is not None:
            self.related_service_name = m.get('relatedServiceName')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('timeWindow') is not None:
            self.time_window = m.get('timeWindow')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetRouteRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 规则详情
        self.data = data  # type: GetRouteRuleResponseBodyData
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRouteRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRouteRuleResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRouteRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRouteRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRouteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRequest(TeaModel):
    def __init__(self, client_token=None, service_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务ID
        self.service_id = service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        return self


class GetServiceResponseBodyData(TeaModel):
    def __init__(self, service_description=None, service_id=None, service_name=None, update_time=None):
        # 服务描述
        self.service_description = service_description  # type: str
        # 服务ID
        self.service_id = service_id  # type: long
        # 服务名字
        self.service_name = service_name  # type: str
        # 修改时间
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_description is not None:
            result['serviceDescription'] = self.service_description
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceDescription') is not None:
            self.service_description = m.get('serviceDescription')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetServiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 服务详情
        self.data = data  # type: GetServiceResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetServiceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceGroupRequest(TeaModel):
    def __init__(self, client_token=None, service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class GetServiceGroupResponseBodyDataUsers(TeaModel):
    def __init__(self, phone=None, service_group_id=None, user_id=None, user_name=None):
        # 手机号
        self.phone = phone  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 用户ID
        self.user_id = user_id  # type: long
        # 用户名字
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupResponseBodyDataUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone is not None:
            result['phone'] = self.phone
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class GetServiceGroupResponseBodyData(TeaModel):
    def __init__(self, create_time=None, enable_webhook=None, service_group_description=None,
                 service_group_id=None, service_group_name=None, update_time=None, users=None, webhook_link=None, webhook_type=None):
        # 创建时间
        self.create_time = create_time  # type: str
        # ENABLE 启用 DISABLE 禁用
        self.enable_webhook = enable_webhook  # type: str
        # 服务组描述
        self.service_group_description = service_group_description  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 服务组名称
        self.service_group_name = service_group_name  # type: str
        # 修改时间
        self.update_time = update_time  # type: str
        # 用户ID
        self.users = users  # type: list[GetServiceGroupResponseBodyDataUsers]
        # webhook 跳转地址
        self.webhook_link = webhook_link  # type: str
        # WEIXIN_GROUP 微信 DING_GROUP 钉钉 FEISHU_GROUP飞书
        self.webhook_type = webhook_type  # type: str

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.enable_webhook is not None:
            result['enableWebhook'] = self.enable_webhook
        if self.service_group_description is not None:
            result['serviceGroupDescription'] = self.service_group_description
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        if self.webhook_link is not None:
            result['webhookLink'] = self.webhook_link
        if self.webhook_type is not None:
            result['webhookType'] = self.webhook_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('enableWebhook') is not None:
            self.enable_webhook = m.get('enableWebhook')
        if m.get('serviceGroupDescription') is not None:
            self.service_group_description = m.get('serviceGroupDescription')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = GetServiceGroupResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        if m.get('webhookLink') is not None:
            self.webhook_link = m.get('webhookLink')
        if m.get('webhookType') is not None:
            self.webhook_type = m.get('webhookType')
        return self


class GetServiceGroupResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetServiceGroupResponseBodyData
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetServiceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetServiceGroupResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetServiceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetServiceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceGroupPersonSchedulingRequest(TeaModel):
    def __init__(self, client_token=None, end_time=None, service_group_id=None, start_time=None, user_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 排班结束时间
        self.end_time = end_time  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 排班开始时间
        self.start_time = start_time  # type: str
        # 用户ID
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupPersonSchedulingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetServiceGroupPersonSchedulingResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 排班日历
        self.data = data  # type: dict[str, any]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupPersonSchedulingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetServiceGroupPersonSchedulingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceGroupPersonSchedulingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceGroupPersonSchedulingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetServiceGroupPersonSchedulingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceGroupSchedulingRequest(TeaModel):
    def __init__(self, client_token=None, service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSchedulingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class GetServiceGroupSchedulingResponseBodyDataFastSchedulingSchedulingUsers(TeaModel):
    def __init__(self, scheduling_order=None, scheduling_user_id=None, scheduling_user_name=None):
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: int
        # 轮班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long
        # 轮班用户名字
        self.scheduling_user_name = scheduling_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSchedulingResponseBodyDataFastSchedulingSchedulingUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        if self.scheduling_user_name is not None:
            result['schedulingUserName'] = self.scheduling_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        if m.get('schedulingUserName') is not None:
            self.scheduling_user_name = m.get('schedulingUserName')
        return self


class GetServiceGroupSchedulingResponseBodyDataFastScheduling(TeaModel):
    def __init__(self, duty_plan=None, id=None, scheduling_users=None, single_duration=None,
                 single_duration_unit=None):
        # 值班方案 dutyPlan FAST_CHOICE 快速选择   CUSTOM  自定义
        self.duty_plan = duty_plan  # type: str
        # 快速排班ID
        self.id = id  # type: long
        # 快速轮班用户
        self.scheduling_users = scheduling_users  # type: list[GetServiceGroupSchedulingResponseBodyDataFastSchedulingSchedulingUsers]
        # 每人排班时长
        self.single_duration = single_duration  # type: int
        # 每人排班时长单位 HOUR 小时 DAY 天
        self.single_duration_unit = single_duration_unit  # type: str

    def validate(self):
        if self.scheduling_users:
            for k in self.scheduling_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceGroupSchedulingResponseBodyDataFastScheduling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duty_plan is not None:
            result['dutyPlan'] = self.duty_plan
        if self.id is not None:
            result['id'] = self.id
        result['schedulingUsers'] = []
        if self.scheduling_users is not None:
            for k in self.scheduling_users:
                result['schedulingUsers'].append(k.to_map() if k else None)
        if self.single_duration is not None:
            result['singleDuration'] = self.single_duration
        if self.single_duration_unit is not None:
            result['singleDurationUnit'] = self.single_duration_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dutyPlan') is not None:
            self.duty_plan = m.get('dutyPlan')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.scheduling_users = []
        if m.get('schedulingUsers') is not None:
            for k in m.get('schedulingUsers'):
                temp_model = GetServiceGroupSchedulingResponseBodyDataFastSchedulingSchedulingUsers()
                self.scheduling_users.append(temp_model.from_map(k))
        if m.get('singleDuration') is not None:
            self.single_duration = m.get('singleDuration')
        if m.get('singleDurationUnit') is not None:
            self.single_duration_unit = m.get('singleDurationUnit')
        return self


class GetServiceGroupSchedulingResponseBodyDataFineSchedulingSchedulingFineShifts(TeaModel):
    def __init__(self, cycle_order=None, scheduling_end_time=None, scheduling_order=None,
                 scheduling_start_time=None, scheduling_user_id=None, scheduling_user_name=None, shift_name=None, skip_one_day=None):
        # 循环次序
        self.cycle_order = cycle_order  # type: long
        # 排班结束时间
        self.scheduling_end_time = scheduling_end_time  # type: str
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: int
        # 排班开始时间
        self.scheduling_start_time = scheduling_start_time  # type: str
        # 排班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long
        # 排班用户名字
        self.scheduling_user_name = scheduling_user_name  # type: str
        # 班次名称
        self.shift_name = shift_name  # type: str
        # 是否跨天
        self.skip_one_day = skip_one_day  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSchedulingResponseBodyDataFineSchedulingSchedulingFineShifts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cycle_order is not None:
            result['cycleOrder'] = self.cycle_order
        if self.scheduling_end_time is not None:
            result['schedulingEndTime'] = self.scheduling_end_time
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_start_time is not None:
            result['schedulingStartTime'] = self.scheduling_start_time
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        if self.scheduling_user_name is not None:
            result['schedulingUserName'] = self.scheduling_user_name
        if self.shift_name is not None:
            result['shiftName'] = self.shift_name
        if self.skip_one_day is not None:
            result['skipOneDay'] = self.skip_one_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cycleOrder') is not None:
            self.cycle_order = m.get('cycleOrder')
        if m.get('schedulingEndTime') is not None:
            self.scheduling_end_time = m.get('schedulingEndTime')
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingStartTime') is not None:
            self.scheduling_start_time = m.get('schedulingStartTime')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        if m.get('schedulingUserName') is not None:
            self.scheduling_user_name = m.get('schedulingUserName')
        if m.get('shiftName') is not None:
            self.shift_name = m.get('shiftName')
        if m.get('skipOneDay') is not None:
            self.skip_one_day = m.get('skipOneDay')
        return self


class GetServiceGroupSchedulingResponseBodyDataFineSchedulingSchedulingTemplateFineShifts(TeaModel):
    def __init__(self, scheduling_end_time=None, scheduling_order=None, scheduling_start_time=None,
                 scheduling_user_id=None, scheduling_user_name=None, shift_name=None, skip_one_day=None):
        # 排班结束时间
        self.scheduling_end_time = scheduling_end_time  # type: str
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: long
        # 排班开始时间
        self.scheduling_start_time = scheduling_start_time  # type: str
        # 用户ID
        self.scheduling_user_id = scheduling_user_id  # type: str
        # 排班用户名字
        self.scheduling_user_name = scheduling_user_name  # type: str
        # 班次名称
        self.shift_name = shift_name  # type: str
        # 是否跨天
        self.skip_one_day = skip_one_day  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSchedulingResponseBodyDataFineSchedulingSchedulingTemplateFineShifts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_end_time is not None:
            result['schedulingEndTime'] = self.scheduling_end_time
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_start_time is not None:
            result['schedulingStartTime'] = self.scheduling_start_time
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        if self.scheduling_user_name is not None:
            result['schedulingUserName'] = self.scheduling_user_name
        if self.shift_name is not None:
            result['shiftName'] = self.shift_name
        if self.skip_one_day is not None:
            result['skipOneDay'] = self.skip_one_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingEndTime') is not None:
            self.scheduling_end_time = m.get('schedulingEndTime')
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingStartTime') is not None:
            self.scheduling_start_time = m.get('schedulingStartTime')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        if m.get('schedulingUserName') is not None:
            self.scheduling_user_name = m.get('schedulingUserName')
        if m.get('shiftName') is not None:
            self.shift_name = m.get('shiftName')
        if m.get('skipOneDay') is not None:
            self.skip_one_day = m.get('skipOneDay')
        return self


class GetServiceGroupSchedulingResponseBodyDataFineScheduling(TeaModel):
    def __init__(self, id=None, period=None, period_unit=None, scheduling_fine_shifts=None,
                 scheduling_template_fine_shifts=None, shift_type=None):
        # 1
        self.id = id  # type: long
        # 1
        self.period = period  # type: int
        # 循环周期单位 HOUR 小时 DAY 天
        self.period_unit = period_unit  # type: str
        # 精细排班班次人员信息
        self.scheduling_fine_shifts = scheduling_fine_shifts  # type: list[GetServiceGroupSchedulingResponseBodyDataFineSchedulingSchedulingFineShifts]
        # 精细排班模版
        self.scheduling_template_fine_shifts = scheduling_template_fine_shifts  # type: list[GetServiceGroupSchedulingResponseBodyDataFineSchedulingSchedulingTemplateFineShifts]
        # 班次类型 MORNING_NIGHT 早晚班 MORNING_NOON_NIGHT 早中晚班 CUSTOM 自定义
        self.shift_type = shift_type  # type: str

    def validate(self):
        if self.scheduling_fine_shifts:
            for k in self.scheduling_fine_shifts:
                if k:
                    k.validate()
        if self.scheduling_template_fine_shifts:
            for k in self.scheduling_template_fine_shifts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceGroupSchedulingResponseBodyDataFineScheduling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['periodUnit'] = self.period_unit
        result['schedulingFineShifts'] = []
        if self.scheduling_fine_shifts is not None:
            for k in self.scheduling_fine_shifts:
                result['schedulingFineShifts'].append(k.to_map() if k else None)
        result['schedulingTemplateFineShifts'] = []
        if self.scheduling_template_fine_shifts is not None:
            for k in self.scheduling_template_fine_shifts:
                result['schedulingTemplateFineShifts'].append(k.to_map() if k else None)
        if self.shift_type is not None:
            result['shiftType'] = self.shift_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodUnit') is not None:
            self.period_unit = m.get('periodUnit')
        self.scheduling_fine_shifts = []
        if m.get('schedulingFineShifts') is not None:
            for k in m.get('schedulingFineShifts'):
                temp_model = GetServiceGroupSchedulingResponseBodyDataFineSchedulingSchedulingFineShifts()
                self.scheduling_fine_shifts.append(temp_model.from_map(k))
        self.scheduling_template_fine_shifts = []
        if m.get('schedulingTemplateFineShifts') is not None:
            for k in m.get('schedulingTemplateFineShifts'):
                temp_model = GetServiceGroupSchedulingResponseBodyDataFineSchedulingSchedulingTemplateFineShifts()
                self.scheduling_template_fine_shifts.append(temp_model.from_map(k))
        if m.get('shiftType') is not None:
            self.shift_type = m.get('shiftType')
        return self


class GetServiceGroupSchedulingResponseBodyDataUsers(TeaModel):
    def __init__(self, user_id=None, user_name=None):
        # 用户ID
        self.user_id = user_id  # type: long
        # 用户名字
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSchedulingResponseBodyDataUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class GetServiceGroupSchedulingResponseBodyData(TeaModel):
    def __init__(self, fast_scheduling=None, fine_scheduling=None, scheduling_way=None, service_group_id=None,
                 users=None):
        # 快速排班
        self.fast_scheduling = fast_scheduling  # type: GetServiceGroupSchedulingResponseBodyDataFastScheduling
        # 精细排班
        self.fine_scheduling = fine_scheduling  # type: GetServiceGroupSchedulingResponseBodyDataFineScheduling
        # 排班方式 FAST 快速排班 FINE 精细排班
        self.scheduling_way = scheduling_way  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 已经排班
        self.users = users  # type: list[GetServiceGroupSchedulingResponseBodyDataUsers]

    def validate(self):
        if self.fast_scheduling:
            self.fast_scheduling.validate()
        if self.fine_scheduling:
            self.fine_scheduling.validate()
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceGroupSchedulingResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fast_scheduling is not None:
            result['fastScheduling'] = self.fast_scheduling.to_map()
        if self.fine_scheduling is not None:
            result['fineScheduling'] = self.fine_scheduling.to_map()
        if self.scheduling_way is not None:
            result['schedulingWay'] = self.scheduling_way
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fastScheduling') is not None:
            temp_model = GetServiceGroupSchedulingResponseBodyDataFastScheduling()
            self.fast_scheduling = temp_model.from_map(m['fastScheduling'])
        if m.get('fineScheduling') is not None:
            temp_model = GetServiceGroupSchedulingResponseBodyDataFineScheduling()
            self.fine_scheduling = temp_model.from_map(m['fineScheduling'])
        if m.get('schedulingWay') is not None:
            self.scheduling_way = m.get('schedulingWay')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = GetServiceGroupSchedulingResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class GetServiceGroupSchedulingResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 排班详情
        self.data = data  # type: GetServiceGroupSchedulingResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetServiceGroupSchedulingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetServiceGroupSchedulingResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetServiceGroupSchedulingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceGroupSchedulingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceGroupSchedulingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetServiceGroupSchedulingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceGroupSchedulingPreviewRequestFastSchedulingSchedulingUsers(TeaModel):
    def __init__(self, scheduling_order=None, scheduling_user_id=None):
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: int
        # 轮班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSchedulingPreviewRequestFastSchedulingSchedulingUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        return self


class GetServiceGroupSchedulingPreviewRequestFastScheduling(TeaModel):
    def __init__(self, duty_plan=None, scheduling_users=None, single_duration=None, single_duration_unit=None):
        # 值班方案 dutyPlan FAST_CHOICE 快速选择 CUSTOM 自定义
        self.duty_plan = duty_plan  # type: str
        # 快速轮班用户
        self.scheduling_users = scheduling_users  # type: list[GetServiceGroupSchedulingPreviewRequestFastSchedulingSchedulingUsers]
        # 每人排班时长
        self.single_duration = single_duration  # type: int
        # 每人排班时长单位 HOUR 小时 DAY 天
        self.single_duration_unit = single_duration_unit  # type: str

    def validate(self):
        if self.scheduling_users:
            for k in self.scheduling_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceGroupSchedulingPreviewRequestFastScheduling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duty_plan is not None:
            result['dutyPlan'] = self.duty_plan
        result['schedulingUsers'] = []
        if self.scheduling_users is not None:
            for k in self.scheduling_users:
                result['schedulingUsers'].append(k.to_map() if k else None)
        if self.single_duration is not None:
            result['singleDuration'] = self.single_duration
        if self.single_duration_unit is not None:
            result['singleDurationUnit'] = self.single_duration_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dutyPlan') is not None:
            self.duty_plan = m.get('dutyPlan')
        self.scheduling_users = []
        if m.get('schedulingUsers') is not None:
            for k in m.get('schedulingUsers'):
                temp_model = GetServiceGroupSchedulingPreviewRequestFastSchedulingSchedulingUsers()
                self.scheduling_users.append(temp_model.from_map(k))
        if m.get('singleDuration') is not None:
            self.single_duration = m.get('singleDuration')
        if m.get('singleDurationUnit') is not None:
            self.single_duration_unit = m.get('singleDurationUnit')
        return self


class GetServiceGroupSchedulingPreviewRequestFineSchedulingSchedulingFineShifts(TeaModel):
    def __init__(self, scheduling_end_time=None, scheduling_order=None, scheduling_start_time=None,
                 shift_name=None):
        # 排班结束时间
        self.scheduling_end_time = scheduling_end_time  # type: str
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: long
        # 排班开始时间
        self.scheduling_start_time = scheduling_start_time  # type: str
        # 班次名称
        self.shift_name = shift_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSchedulingPreviewRequestFineSchedulingSchedulingFineShifts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_end_time is not None:
            result['schedulingEndTime'] = self.scheduling_end_time
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_start_time is not None:
            result['schedulingStartTime'] = self.scheduling_start_time
        if self.shift_name is not None:
            result['shiftName'] = self.shift_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingEndTime') is not None:
            self.scheduling_end_time = m.get('schedulingEndTime')
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingStartTime') is not None:
            self.scheduling_start_time = m.get('schedulingStartTime')
        if m.get('shiftName') is not None:
            self.shift_name = m.get('shiftName')
        return self


class GetServiceGroupSchedulingPreviewRequestFineScheduling(TeaModel):
    def __init__(self, period=None, period_unit=None, scheduling_fine_shifts=None, shift_type=None):
        # 循环周期
        self.period = period  # type: int
        # 循环周期单位 HOUR 小时 DAY 天
        self.period_unit = period_unit  # type: str
        # 精细排班班次人员信息
        self.scheduling_fine_shifts = scheduling_fine_shifts  # type: list[GetServiceGroupSchedulingPreviewRequestFineSchedulingSchedulingFineShifts]
        # 班次类型 MORNING_NIGHT 早晚班 MORNING_NOON_NIGHT 早中晚班 CUSTOM 自定义
        self.shift_type = shift_type  # type: str

    def validate(self):
        if self.scheduling_fine_shifts:
            for k in self.scheduling_fine_shifts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceGroupSchedulingPreviewRequestFineScheduling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['periodUnit'] = self.period_unit
        result['schedulingFineShifts'] = []
        if self.scheduling_fine_shifts is not None:
            for k in self.scheduling_fine_shifts:
                result['schedulingFineShifts'].append(k.to_map() if k else None)
        if self.shift_type is not None:
            result['shiftType'] = self.shift_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodUnit') is not None:
            self.period_unit = m.get('periodUnit')
        self.scheduling_fine_shifts = []
        if m.get('schedulingFineShifts') is not None:
            for k in m.get('schedulingFineShifts'):
                temp_model = GetServiceGroupSchedulingPreviewRequestFineSchedulingSchedulingFineShifts()
                self.scheduling_fine_shifts.append(temp_model.from_map(k))
        if m.get('shiftType') is not None:
            self.shift_type = m.get('shiftType')
        return self


class GetServiceGroupSchedulingPreviewRequest(TeaModel):
    def __init__(self, client_token=None, end_time=None, fast_scheduling=None, fine_scheduling=None,
                 scheduling_way=None, service_group_id=None, start_time=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 排班结束时间
        self.end_time = end_time  # type: str
        # 快速排班
        self.fast_scheduling = fast_scheduling  # type: GetServiceGroupSchedulingPreviewRequestFastScheduling
        # 精细排
        self.fine_scheduling = fine_scheduling  # type: GetServiceGroupSchedulingPreviewRequestFineScheduling
        # 排班方式 FAST 快速排班 FINE 精细排班
        self.scheduling_way = scheduling_way  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 排班开始时间
        self.start_time = start_time  # type: str

    def validate(self):
        if self.fast_scheduling:
            self.fast_scheduling.validate()
        if self.fine_scheduling:
            self.fine_scheduling.validate()

    def to_map(self):
        _map = super(GetServiceGroupSchedulingPreviewRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.fast_scheduling is not None:
            result['fastScheduling'] = self.fast_scheduling.to_map()
        if self.fine_scheduling is not None:
            result['fineScheduling'] = self.fine_scheduling.to_map()
        if self.scheduling_way is not None:
            result['schedulingWay'] = self.scheduling_way
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('fastScheduling') is not None:
            temp_model = GetServiceGroupSchedulingPreviewRequestFastScheduling()
            self.fast_scheduling = temp_model.from_map(m['fastScheduling'])
        if m.get('fineScheduling') is not None:
            temp_model = GetServiceGroupSchedulingPreviewRequestFineScheduling()
            self.fine_scheduling = temp_model.from_map(m['fineScheduling'])
        if m.get('schedulingWay') is not None:
            self.scheduling_way = m.get('schedulingWay')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class GetServiceGroupSchedulingPreviewResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 服务组排班信息
        self.data = data  # type: dict[str, any]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSchedulingPreviewResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetServiceGroupSchedulingPreviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceGroupSchedulingPreviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceGroupSchedulingPreviewResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetServiceGroupSchedulingPreviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceGroupSpecialPersonSchedulingRequest(TeaModel):
    def __init__(self, client_token=None, service_group_id=None, user_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 用户ID
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSpecialPersonSchedulingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetServiceGroupSpecialPersonSchedulingResponseBodyData(TeaModel):
    def __init__(self, scheduling_date=None, scheduling_end_time=None, scheduling_start_time=None,
                 scheduling_user_id=None, service_group_id=None, service_group_name=None):
        # 排班日期
        self.scheduling_date = scheduling_date  # type: str
        # 排班结束时间
        self.scheduling_end_time = scheduling_end_time  # type: str
        # 排班开始时间
        self.scheduling_start_time = scheduling_start_time  # type: str
        # 排班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long
        # 服务组id
        self.service_group_id = service_group_id  # type: long
        # 服务组名字
        self.service_group_name = service_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceGroupSpecialPersonSchedulingResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_date is not None:
            result['schedulingDate'] = self.scheduling_date
        if self.scheduling_end_time is not None:
            result['schedulingEndTime'] = self.scheduling_end_time
        if self.scheduling_start_time is not None:
            result['schedulingStartTime'] = self.scheduling_start_time
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingDate') is not None:
            self.scheduling_date = m.get('schedulingDate')
        if m.get('schedulingEndTime') is not None:
            self.scheduling_end_time = m.get('schedulingEndTime')
        if m.get('schedulingStartTime') is not None:
            self.scheduling_start_time = m.get('schedulingStartTime')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        return self


class GetServiceGroupSpecialPersonSchedulingResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 人员排班信息
        self.data = data  # type: list[GetServiceGroupSpecialPersonSchedulingResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceGroupSpecialPersonSchedulingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetServiceGroupSpecialPersonSchedulingResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetServiceGroupSpecialPersonSchedulingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceGroupSpecialPersonSchedulingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceGroupSpecialPersonSchedulingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetServiceGroupSpecialPersonSchedulingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSimilarIncidentStatisticsRequest(TeaModel):
    def __init__(self, client_token=None, create_time=None, events=None, incident_id=None, incident_title=None,
                 related_service_id=None):
        # 幂等标识
        self.client_token = client_token  # type: str
        # 触发时间
        self.create_time = create_time  # type: str
        # 事件告警内容
        self.events = events  # type: list[str]
        # 事件id
        self.incident_id = incident_id  # type: long
        # 事件标题
        self.incident_title = incident_title  # type: str
        # 关联服务id
        self.related_service_id = related_service_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSimilarIncidentStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.events is not None:
            result['events'] = self.events
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_title is not None:
            result['incidentTitle'] = self.incident_title
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('events') is not None:
            self.events = m.get('events')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentTitle') is not None:
            self.incident_title = m.get('incidentTitle')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        return self


class GetSimilarIncidentStatisticsResponseBodyDataDailySimilarIncidentsSimilarIncidents(TeaModel):
    def __init__(self, assign_user_id=None, assign_user_name=None, create_time=None, duration_time=None,
                 finish_reason=None, finish_reason_description=None, finish_solution_description=None,
                 incident_finish_solution=None, incident_id=None, incident_number=None, incident_title=None, related_route_rule_id=None,
                 related_route_rule_name=None, similar_score=None):
        # 分派人id
        self.assign_user_id = assign_user_id  # type: long
        # 分派人
        self.assign_user_name = assign_user_name  # type: str
        # 触发时间
        self.create_time = create_time  # type: str
        # 持续时间
        self.duration_time = duration_time  # type: long
        # 触发原因
        self.finish_reason = finish_reason  # type: long
        # 触发原因描述
        self.finish_reason_description = finish_reason_description  # type: str
        # 解决方案描述
        self.finish_solution_description = finish_solution_description  # type: str
        # 解决方案
        self.incident_finish_solution = incident_finish_solution  # type: long
        # 事件id
        self.incident_id = incident_id  # type: long
        # 事件编号
        self.incident_number = incident_number  # type: str
        # 事件名称
        self.incident_title = incident_title  # type: str
        # 流转规则id
        self.related_route_rule_id = related_route_rule_id  # type: long
        # 流转规则名称
        self.related_route_rule_name = related_route_rule_name  # type: str
        # 相似度
        self.similar_score = similar_score  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSimilarIncidentStatisticsResponseBodyDataDailySimilarIncidentsSimilarIncidents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_user_id is not None:
            result['assignUserId'] = self.assign_user_id
        if self.assign_user_name is not None:
            result['assignUserName'] = self.assign_user_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.duration_time is not None:
            result['durationTime'] = self.duration_time
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.finish_reason_description is not None:
            result['finishReasonDescription'] = self.finish_reason_description
        if self.finish_solution_description is not None:
            result['finishSolutionDescription'] = self.finish_solution_description
        if self.incident_finish_solution is not None:
            result['incidentFinishSolution'] = self.incident_finish_solution
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_number is not None:
            result['incidentNumber'] = self.incident_number
        if self.incident_title is not None:
            result['incidentTitle'] = self.incident_title
        if self.related_route_rule_id is not None:
            result['relatedRouteRuleId'] = self.related_route_rule_id
        if self.related_route_rule_name is not None:
            result['relatedRouteRuleName'] = self.related_route_rule_name
        if self.similar_score is not None:
            result['similarScore'] = self.similar_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignUserId') is not None:
            self.assign_user_id = m.get('assignUserId')
        if m.get('assignUserName') is not None:
            self.assign_user_name = m.get('assignUserName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('durationTime') is not None:
            self.duration_time = m.get('durationTime')
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('finishReasonDescription') is not None:
            self.finish_reason_description = m.get('finishReasonDescription')
        if m.get('finishSolutionDescription') is not None:
            self.finish_solution_description = m.get('finishSolutionDescription')
        if m.get('incidentFinishSolution') is not None:
            self.incident_finish_solution = m.get('incidentFinishSolution')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentNumber') is not None:
            self.incident_number = m.get('incidentNumber')
        if m.get('incidentTitle') is not None:
            self.incident_title = m.get('incidentTitle')
        if m.get('relatedRouteRuleId') is not None:
            self.related_route_rule_id = m.get('relatedRouteRuleId')
        if m.get('relatedRouteRuleName') is not None:
            self.related_route_rule_name = m.get('relatedRouteRuleName')
        if m.get('similarScore') is not None:
            self.similar_score = m.get('similarScore')
        return self


class GetSimilarIncidentStatisticsResponseBodyDataDailySimilarIncidents(TeaModel):
    def __init__(self, commitment=None, date=None, day=None, month=None, similar_incidents=None, week=None):
        # 数量
        self.commitment = commitment  # type: long
        # 日期
        self.date = date  # type: str
        # 星期几
        self.day = day  # type: long
        # 月份
        self.month = month  # type: long
        # 相似事件列表
        self.similar_incidents = similar_incidents  # type: list[GetSimilarIncidentStatisticsResponseBodyDataDailySimilarIncidentsSimilarIncidents]
        # 周
        self.week = week  # type: str

    def validate(self):
        if self.similar_incidents:
            for k in self.similar_incidents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSimilarIncidentStatisticsResponseBodyDataDailySimilarIncidents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commitment is not None:
            result['commitment'] = self.commitment
        if self.date is not None:
            result['date'] = self.date
        if self.day is not None:
            result['day'] = self.day
        if self.month is not None:
            result['month'] = self.month
        result['similarIncidents'] = []
        if self.similar_incidents is not None:
            for k in self.similar_incidents:
                result['similarIncidents'].append(k.to_map() if k else None)
        if self.week is not None:
            result['week'] = self.week
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commitment') is not None:
            self.commitment = m.get('commitment')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('day') is not None:
            self.day = m.get('day')
        if m.get('month') is not None:
            self.month = m.get('month')
        self.similar_incidents = []
        if m.get('similarIncidents') is not None:
            for k in m.get('similarIncidents'):
                temp_model = GetSimilarIncidentStatisticsResponseBodyDataDailySimilarIncidentsSimilarIncidents()
                self.similar_incidents.append(temp_model.from_map(k))
        if m.get('week') is not None:
            self.week = m.get('week')
        return self


class GetSimilarIncidentStatisticsResponseBodyDataTopFiveIncidents(TeaModel):
    def __init__(self, assign_user_id=None, assign_user_name=None, create_time=None, duration_time=None,
                 finish_reason=None, finish_reason_description=None, finish_solution_description=None,
                 incident_finish_solution=None, incident_id=None, incident_number=None, incident_title=None, related_route_rule_id=None,
                 related_route_rule_name=None, similar_score=None):
        # 分派人id
        self.assign_user_id = assign_user_id  # type: str
        # 分派人
        self.assign_user_name = assign_user_name  # type: str
        # 触发时间
        self.create_time = create_time  # type: str
        # 持续时间
        self.duration_time = duration_time  # type: long
        # 触发原因
        self.finish_reason = finish_reason  # type: long
        # 触发原因描述
        self.finish_reason_description = finish_reason_description  # type: str
        # 解决方案描述
        self.finish_solution_description = finish_solution_description  # type: str
        # 解决方案
        self.incident_finish_solution = incident_finish_solution  # type: long
        # 事件id
        self.incident_id = incident_id  # type: long
        # 事件编号
        self.incident_number = incident_number  # type: str
        # 事件标题
        self.incident_title = incident_title  # type: str
        # 流转规则id
        self.related_route_rule_id = related_route_rule_id  # type: long
        # 流转规则名称
        self.related_route_rule_name = related_route_rule_name  # type: str
        # 相似度
        self.similar_score = similar_score  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSimilarIncidentStatisticsResponseBodyDataTopFiveIncidents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_user_id is not None:
            result['assignUserId'] = self.assign_user_id
        if self.assign_user_name is not None:
            result['assignUserName'] = self.assign_user_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.duration_time is not None:
            result['durationTime'] = self.duration_time
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.finish_reason_description is not None:
            result['finishReasonDescription'] = self.finish_reason_description
        if self.finish_solution_description is not None:
            result['finishSolutionDescription'] = self.finish_solution_description
        if self.incident_finish_solution is not None:
            result['incidentFinishSolution'] = self.incident_finish_solution
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_number is not None:
            result['incidentNumber'] = self.incident_number
        if self.incident_title is not None:
            result['incidentTitle'] = self.incident_title
        if self.related_route_rule_id is not None:
            result['relatedRouteRuleId'] = self.related_route_rule_id
        if self.related_route_rule_name is not None:
            result['relatedRouteRuleName'] = self.related_route_rule_name
        if self.similar_score is not None:
            result['similarScore'] = self.similar_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignUserId') is not None:
            self.assign_user_id = m.get('assignUserId')
        if m.get('assignUserName') is not None:
            self.assign_user_name = m.get('assignUserName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('durationTime') is not None:
            self.duration_time = m.get('durationTime')
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('finishReasonDescription') is not None:
            self.finish_reason_description = m.get('finishReasonDescription')
        if m.get('finishSolutionDescription') is not None:
            self.finish_solution_description = m.get('finishSolutionDescription')
        if m.get('incidentFinishSolution') is not None:
            self.incident_finish_solution = m.get('incidentFinishSolution')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentNumber') is not None:
            self.incident_number = m.get('incidentNumber')
        if m.get('incidentTitle') is not None:
            self.incident_title = m.get('incidentTitle')
        if m.get('relatedRouteRuleId') is not None:
            self.related_route_rule_id = m.get('relatedRouteRuleId')
        if m.get('relatedRouteRuleName') is not None:
            self.related_route_rule_name = m.get('relatedRouteRuleName')
        if m.get('similarScore') is not None:
            self.similar_score = m.get('similarScore')
        return self


class GetSimilarIncidentStatisticsResponseBodyData(TeaModel):
    def __init__(self, count_in_seven_days=None, count_in_six_months=None, daily_similar_incidents=None,
                 request_id=None, top_five_incidents=None):
        # 7天内相似事件数量
        self.count_in_seven_days = count_in_seven_days  # type: long
        # 6月内相似事件数量
        self.count_in_six_months = count_in_six_months  # type: long
        # 根据日期分类
        self.daily_similar_incidents = daily_similar_incidents  # type: list[GetSimilarIncidentStatisticsResponseBodyDataDailySimilarIncidents]
        # id of the request
        self.request_id = request_id  # type: str
        # topFiveIncidents
        self.top_five_incidents = top_five_incidents  # type: list[GetSimilarIncidentStatisticsResponseBodyDataTopFiveIncidents]

    def validate(self):
        if self.daily_similar_incidents:
            for k in self.daily_similar_incidents:
                if k:
                    k.validate()
        if self.top_five_incidents:
            for k in self.top_five_incidents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSimilarIncidentStatisticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_in_seven_days is not None:
            result['countInSevenDays'] = self.count_in_seven_days
        if self.count_in_six_months is not None:
            result['countInSixMonths'] = self.count_in_six_months
        result['dailySimilarIncidents'] = []
        if self.daily_similar_incidents is not None:
            for k in self.daily_similar_incidents:
                result['dailySimilarIncidents'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['topFiveIncidents'] = []
        if self.top_five_incidents is not None:
            for k in self.top_five_incidents:
                result['topFiveIncidents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('countInSevenDays') is not None:
            self.count_in_seven_days = m.get('countInSevenDays')
        if m.get('countInSixMonths') is not None:
            self.count_in_six_months = m.get('countInSixMonths')
        self.daily_similar_incidents = []
        if m.get('dailySimilarIncidents') is not None:
            for k in m.get('dailySimilarIncidents'):
                temp_model = GetSimilarIncidentStatisticsResponseBodyDataDailySimilarIncidents()
                self.daily_similar_incidents.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.top_five_incidents = []
        if m.get('topFiveIncidents') is not None:
            for k in m.get('topFiveIncidents'):
                temp_model = GetSimilarIncidentStatisticsResponseBodyDataTopFiveIncidents()
                self.top_five_incidents.append(temp_model.from_map(k))
        return self


class GetSimilarIncidentStatisticsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: GetSimilarIncidentStatisticsResponseBodyData
        # id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSimilarIncidentStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetSimilarIncidentStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetSimilarIncidentStatisticsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSimilarIncidentStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSimilarIncidentStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSimilarIncidentStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubscriptionRequest(TeaModel):
    def __init__(self, subscription_id=None):
        self.subscription_id = subscription_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubscriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        return self


class GetSubscriptionResponseBodyDataNotifyObjectList(TeaModel):
    def __init__(self, id=None, name=None, notify_object_id=None, notify_object_type=None):
        # id主键
        self.id = id  # type: long
        # 通知对象名
        self.name = name  # type: str
        # 关联主键id
        self.notify_object_id = notify_object_id  # type: long
        # 通知对象类型0服务组 1个人
        self.notify_object_type = notify_object_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubscriptionResponseBodyDataNotifyObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.notify_object_id is not None:
            result['notifyObjectId'] = self.notify_object_id
        if self.notify_object_type is not None:
            result['notifyObjectType'] = self.notify_object_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notifyObjectId') is not None:
            self.notify_object_id = m.get('notifyObjectId')
        if m.get('notifyObjectType') is not None:
            self.notify_object_type = m.get('notifyObjectType')
        return self


class GetSubscriptionResponseBodyDataNotifyStrategyListStrategiesConditions(TeaModel):
    def __init__(self, action=None, effection=None, level=None, problem_notify_type=None):
        # 事件动作
        self.action = action  # type: str
        # 影响范围
        self.effection = effection  # type: str
        # 等级
        self.level = level  # type: str
        # 故障通知类型
        self.problem_notify_type = problem_notify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubscriptionResponseBodyDataNotifyStrategyListStrategiesConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.effection is not None:
            result['effection'] = self.effection
        if self.level is not None:
            result['level'] = self.level
        if self.problem_notify_type is not None:
            result['problemNotifyType'] = self.problem_notify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('problemNotifyType') is not None:
            self.problem_notify_type = m.get('problemNotifyType')
        return self


class GetSubscriptionResponseBodyDataNotifyStrategyListStrategiesPeriodChannel(TeaModel):
    def __init__(self, non_workday=None, workday=None):
        # 非工作时间
        self.non_workday = non_workday  # type: str
        # 工作时间
        self.workday = workday  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubscriptionResponseBodyDataNotifyStrategyListStrategiesPeriodChannel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_workday is not None:
            result['nonWorkday'] = self.non_workday
        if self.workday is not None:
            result['workday'] = self.workday
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nonWorkday') is not None:
            self.non_workday = m.get('nonWorkday')
        if m.get('workday') is not None:
            self.workday = m.get('workday')
        return self


class GetSubscriptionResponseBodyDataNotifyStrategyListStrategies(TeaModel):
    def __init__(self, channels=None, conditions=None, id=None, period_channel=None):
        # 通知渠道
        self.channels = channels  # type: str
        # 条件
        self.conditions = conditions  # type: list[GetSubscriptionResponseBodyDataNotifyStrategyListStrategiesConditions]
        # 策略主键
        self.id = id  # type: long
        # 分时间段渠道
        self.period_channel = period_channel  # type: GetSubscriptionResponseBodyDataNotifyStrategyListStrategiesPeriodChannel

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.period_channel:
            self.period_channel.validate()

    def to_map(self):
        _map = super(GetSubscriptionResponseBodyDataNotifyStrategyListStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['channels'] = self.channels
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.period_channel is not None:
            result['periodChannel'] = self.period_channel.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('channels') is not None:
            self.channels = m.get('channels')
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = GetSubscriptionResponseBodyDataNotifyStrategyListStrategiesConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('periodChannel') is not None:
            temp_model = GetSubscriptionResponseBodyDataNotifyStrategyListStrategiesPeriodChannel()
            self.period_channel = temp_model.from_map(m['periodChannel'])
        return self


class GetSubscriptionResponseBodyDataNotifyStrategyList(TeaModel):
    def __init__(self, instance_type=None, strategies=None):
        # 订阅实例类型，0事件、1报警、2故障
        self.instance_type = instance_type  # type: long
        # 策略
        self.strategies = strategies  # type: list[GetSubscriptionResponseBodyDataNotifyStrategyListStrategies]

    def validate(self):
        if self.strategies:
            for k in self.strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSubscriptionResponseBodyDataNotifyStrategyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        result['strategies'] = []
        if self.strategies is not None:
            for k in self.strategies:
                result['strategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        self.strategies = []
        if m.get('strategies') is not None:
            for k in m.get('strategies'):
                temp_model = GetSubscriptionResponseBodyDataNotifyStrategyListStrategies()
                self.strategies.append(temp_model.from_map(k))
        return self


class GetSubscriptionResponseBodyDataScopeObjectList(TeaModel):
    def __init__(self, id=None, scope=None, scope_object=None, scope_object_id=None):
        # id主键
        self.id = id  # type: long
        # 订阅范围类型 0 全部 1服务 2 流转规则
        self.scope = scope  # type: str
        # 订阅范围对象名称
        self.scope_object = scope_object  # type: str
        # 订阅范围对象关联表主键id
        self.scope_object_id = scope_object_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSubscriptionResponseBodyDataScopeObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.scope is not None:
            result['scope'] = self.scope
        if self.scope_object is not None:
            result['scopeObject'] = self.scope_object
        if self.scope_object_id is not None:
            result['scopeObjectId'] = self.scope_object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scopeObject') is not None:
            self.scope_object = m.get('scopeObject')
        if m.get('scopeObjectId') is not None:
            self.scope_object_id = m.get('scopeObjectId')
        return self


class GetSubscriptionResponseBodyData(TeaModel):
    def __init__(self, end_time=None, expired_type=None, notify_object_list=None, notify_object_type=None,
                 notify_strategy_list=None, period=None, scope=None, scope_object_list=None, start_time=None, status=None,
                 subscription_id=None, subscription_title=None):
        # 时效结束时间
        self.end_time = end_time  # type: str
        # 有效期类型 0 长期 1短期
        self.expired_type = expired_type  # type: str
        # 通知对象列表
        self.notify_object_list = notify_object_list  # type: list[GetSubscriptionResponseBodyDataNotifyObjectList]
        # 0服务组 1个人
        self.notify_object_type = notify_object_type  # type: str
        # 通知策略列表
        self.notify_strategy_list = notify_strategy_list  # type: list[GetSubscriptionResponseBodyDataNotifyStrategyList]
        # 时间段字符串
        self.period = period  # type: str
        # 0 全部 1服务 2 流转规则
        self.scope = scope  # type: str
        self.scope_object_list = scope_object_list  # type: list[GetSubscriptionResponseBodyDataScopeObjectList]
        # 时效开始时间
        self.start_time = start_time  # type: str
        # 1 启用 0禁用
        self.status = status  # type: str
        self.subscription_id = subscription_id  # type: long
        # 通知订阅名称
        self.subscription_title = subscription_title  # type: str

    def validate(self):
        if self.notify_object_list:
            for k in self.notify_object_list:
                if k:
                    k.validate()
        if self.notify_strategy_list:
            for k in self.notify_strategy_list:
                if k:
                    k.validate()
        if self.scope_object_list:
            for k in self.scope_object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSubscriptionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.expired_type is not None:
            result['expiredType'] = self.expired_type
        result['notifyObjectList'] = []
        if self.notify_object_list is not None:
            for k in self.notify_object_list:
                result['notifyObjectList'].append(k.to_map() if k else None)
        if self.notify_object_type is not None:
            result['notifyObjectType'] = self.notify_object_type
        result['notifyStrategyList'] = []
        if self.notify_strategy_list is not None:
            for k in self.notify_strategy_list:
                result['notifyStrategyList'].append(k.to_map() if k else None)
        if self.period is not None:
            result['period'] = self.period
        if self.scope is not None:
            result['scope'] = self.scope
        result['scopeObjectList'] = []
        if self.scope_object_list is not None:
            for k in self.scope_object_list:
                result['scopeObjectList'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        if self.subscription_title is not None:
            result['subscriptionTitle'] = self.subscription_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('expiredType') is not None:
            self.expired_type = m.get('expiredType')
        self.notify_object_list = []
        if m.get('notifyObjectList') is not None:
            for k in m.get('notifyObjectList'):
                temp_model = GetSubscriptionResponseBodyDataNotifyObjectList()
                self.notify_object_list.append(temp_model.from_map(k))
        if m.get('notifyObjectType') is not None:
            self.notify_object_type = m.get('notifyObjectType')
        self.notify_strategy_list = []
        if m.get('notifyStrategyList') is not None:
            for k in m.get('notifyStrategyList'):
                temp_model = GetSubscriptionResponseBodyDataNotifyStrategyList()
                self.notify_strategy_list.append(temp_model.from_map(k))
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        self.scope_object_list = []
        if m.get('scopeObjectList') is not None:
            for k in m.get('scopeObjectList'):
                temp_model = GetSubscriptionResponseBodyDataScopeObjectList()
                self.scope_object_list.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        if m.get('subscriptionTitle') is not None:
            self.subscription_title = m.get('subscriptionTitle')
        return self


class GetSubscriptionResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetSubscriptionResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSubscriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetSubscriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSubscriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSubscriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTenantApplicationRequest(TeaModel):
    def __init__(self, client_token=None):
        # 幂等标识
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTenantApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class GetTenantApplicationResponseBodyData(TeaModel):
    def __init__(self, biz_id=None, channel=None, corporation_id=None, progress=None):
        # 业务id
        self.biz_id = biz_id  # type: str
        # 云钉协同渠道
        self.channel = channel  # type: str
        # 企业id
        self.corporation_id = corporation_id  # type: str
        # 进度
        self.progress = progress  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTenantApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.channel is not None:
            result['channel'] = self.channel
        if self.corporation_id is not None:
            result['corporationId'] = self.corporation_id
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('corporationId') is not None:
            self.corporation_id = m.get('corporationId')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class GetTenantApplicationResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: GetTenantApplicationResponseBodyData
        # id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTenantApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetTenantApplicationResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetTenantApplicationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTenantApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTenantApplicationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTenantApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(self, client_token=None, user_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 用户ID
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetUserResponseBodyDataServiceGroups(TeaModel):
    def __init__(self, name=None, service_group_id=None):
        # 服务组名称
        self.name = name  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyDataServiceGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class GetUserResponseBodyData(TeaModel):
    def __init__(self, account_type=None, create_time=None, email=None, is_editable_user=None, is_related=None,
                 phone=None, ram_id=None, service_groups=None, user_id=None, username=None):
        # CUSTOMER:主账号，SUB:子账号
        self.account_type = account_type  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # email
        self.email = email  # type: str
        # 是否可编辑
        self.is_editable_user = is_editable_user  # type: bool
        # 是否关联
        self.is_related = is_related  # type: str
        # 用户手机号
        self.phone = phone  # type: str
        # ramId
        self.ram_id = ram_id  # type: str
        # 所属服务组
        self.service_groups = service_groups  # type: list[GetUserResponseBodyDataServiceGroups]
        # 用户ID
        self.user_id = user_id  # type: long
        # 用户昵称
        self.username = username  # type: str

    def validate(self):
        if self.service_groups:
            for k in self.service_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.email is not None:
            result['email'] = self.email
        if self.is_editable_user is not None:
            result['isEditableUser'] = self.is_editable_user
        if self.is_related is not None:
            result['isRelated'] = self.is_related
        if self.phone is not None:
            result['phone'] = self.phone
        if self.ram_id is not None:
            result['ramId'] = self.ram_id
        result['serviceGroups'] = []
        if self.service_groups is not None:
            for k in self.service_groups:
                result['serviceGroups'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('isEditableUser') is not None:
            self.is_editable_user = m.get('isEditableUser')
        if m.get('isRelated') is not None:
            self.is_related = m.get('isRelated')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('ramId') is not None:
            self.ram_id = m.get('ramId')
        self.service_groups = []
        if m.get('serviceGroups') is not None:
            for k in m.get('serviceGroups'):
                temp_model = GetUserResponseBodyDataServiceGroups()
                self.service_groups.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 用户
        self.data = data  # type: GetUserResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetUserResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGuideStatusRequest(TeaModel):
    def __init__(self, client_token=None):
        # 幂等校验
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserGuideStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class GetUserGuideStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # map
        self.data = data  # type: dict[str, any]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserGuideStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetUserGuideStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserGuideStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserGuideStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserGuideStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlertsRequest(TeaModel):
    def __init__(self, alert_level=None, alert_name=None, alert_source_name=None, end_time=None, page_number=None,
                 page_size=None, related_service_id=None, rule_name=None, start_time=None):
        # 报警等级 P1 P2 P3 P4
        self.alert_level = alert_level  # type: str
        # 报警名称
        self.alert_name = alert_name  # type: str
        # 报警来源
        self.alert_source_name = alert_source_name  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # 服务id
        self.related_service_id = related_service_id  # type: long
        # 流转规则名字
        self.rule_name = rule_name  # type: str
        # 开始时间
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlertsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_level is not None:
            result['alertLevel'] = self.alert_level
        if self.alert_name is not None:
            result['alertName'] = self.alert_name
        if self.alert_source_name is not None:
            result['alertSourceName'] = self.alert_source_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alertLevel') is not None:
            self.alert_level = m.get('alertLevel')
        if m.get('alertName') is not None:
            self.alert_name = m.get('alertName')
        if m.get('alertSourceName') is not None:
            self.alert_source_name = m.get('alertSourceName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListAlertsResponseBodyData(TeaModel):
    def __init__(self, alert_id=None, alert_level=None, alert_number=None, alert_source_name=None, create_time=None,
                 first_event_time=None, related_service_name=None, route_rule_id=None, route_rule_name=None,
                 source_event_count=None, title=None):
        # 报警ID
        self.alert_id = alert_id  # type: long
        # 告警优先级  1，2，3，4  对应 p1,p2,p3,p4
        self.alert_level = alert_level  # type: str
        # 报警编号
        self.alert_number = alert_number  # type: str
        # 报警源
        self.alert_source_name = alert_source_name  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 第一次告警上报时间
        self.first_event_time = first_event_time  # type: str
        # 关联服务名称
        self.related_service_name = related_service_name  # type: str
        # 关联流转规则ID
        self.route_rule_id = route_rule_id  # type: long
        # 流转规则名字
        self.route_rule_name = route_rule_name  # type: str
        # 收敛量
        self.source_event_count = source_event_count  # type: long
        # 报警标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAlertsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['alertId'] = self.alert_id
        if self.alert_level is not None:
            result['alertLevel'] = self.alert_level
        if self.alert_number is not None:
            result['alertNumber'] = self.alert_number
        if self.alert_source_name is not None:
            result['alertSourceName'] = self.alert_source_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.first_event_time is not None:
            result['firstEventTime'] = self.first_event_time
        if self.related_service_name is not None:
            result['relatedServiceName'] = self.related_service_name
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        if self.route_rule_name is not None:
            result['routeRuleName'] = self.route_rule_name
        if self.source_event_count is not None:
            result['sourceEventCount'] = self.source_event_count
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('alertId') is not None:
            self.alert_id = m.get('alertId')
        if m.get('alertLevel') is not None:
            self.alert_level = m.get('alertLevel')
        if m.get('alertNumber') is not None:
            self.alert_number = m.get('alertNumber')
        if m.get('alertSourceName') is not None:
            self.alert_source_name = m.get('alertSourceName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('firstEventTime') is not None:
            self.first_event_time = m.get('firstEventTime')
        if m.get('relatedServiceName') is not None:
            self.related_service_name = m.get('relatedServiceName')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('routeRuleName') is not None:
            self.route_rule_name = m.get('routeRuleName')
        if m.get('sourceEventCount') is not None:
            self.source_event_count = m.get('sourceEventCount')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListAlertsResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # 报警列表
        self.data = data  # type: list[ListAlertsResponseBodyData]
        # 当前页
        self.page_number = page_number  # type: int
        # 页的大小
        self.page_size = page_size  # type: int
        # 请求ID
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAlertsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListAlertsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAlertsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAlertsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAlertsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartDataForServiceGroupRequest(TeaModel):
    def __init__(self, client_token=None, end_time=None, start_time=None):
        self.client_token = client_token  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 开始时间
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartDataForServiceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListChartDataForServiceGroupResponseBodyData(TeaModel):
    def __init__(self, effection_level=None, escalation_incident_count=None, incident_count=None,
                 mean_time_to_acknowledge=None, mean_time_to_repair=None, time=None, total_mean_time_to_acknowledge=None,
                 total_mean_time_to_repair=None, un_acknowledged_escalation_incident_count=None, un_finish_escalation_incident_count=None):
        # 根据影响等级时间等级分组统计数量
        self.effection_level = effection_level  # type: dict[str, any]
        # 升级事件数
        self.escalation_incident_count = escalation_incident_count  # type: long
        # 时间总数
        self.incident_count = incident_count  # type: long
        # 当日平均响应时间单位秒
        self.mean_time_to_acknowledge = mean_time_to_acknowledge  # type: long
        # 当日平均完结时间单位秒
        self.mean_time_to_repair = mean_time_to_repair  # type: long
        # 时间
        self.time = time  # type: str
        # 总平均响应时间
        self.total_mean_time_to_acknowledge = total_mean_time_to_acknowledge  # type: long
        # 总平均完结时间
        self.total_mean_time_to_repair = total_mean_time_to_repair  # type: long
        # 未响应升级事件数
        self.un_acknowledged_escalation_incident_count = un_acknowledged_escalation_incident_count  # type: long
        # 未完结升级事件数
        self.un_finish_escalation_incident_count = un_finish_escalation_incident_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartDataForServiceGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effection_level is not None:
            result['effectionLevel'] = self.effection_level
        if self.escalation_incident_count is not None:
            result['escalationIncidentCount'] = self.escalation_incident_count
        if self.incident_count is not None:
            result['incidentCount'] = self.incident_count
        if self.mean_time_to_acknowledge is not None:
            result['meanTimeToAcknowledge'] = self.mean_time_to_acknowledge
        if self.mean_time_to_repair is not None:
            result['meanTimeToRepair'] = self.mean_time_to_repair
        if self.time is not None:
            result['time'] = self.time
        if self.total_mean_time_to_acknowledge is not None:
            result['totalMeanTimeToAcknowledge'] = self.total_mean_time_to_acknowledge
        if self.total_mean_time_to_repair is not None:
            result['totalMeanTimeToRepair'] = self.total_mean_time_to_repair
        if self.un_acknowledged_escalation_incident_count is not None:
            result['unAcknowledgedEscalationIncidentCount'] = self.un_acknowledged_escalation_incident_count
        if self.un_finish_escalation_incident_count is not None:
            result['unFinishEscalationIncidentCount'] = self.un_finish_escalation_incident_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effectionLevel') is not None:
            self.effection_level = m.get('effectionLevel')
        if m.get('escalationIncidentCount') is not None:
            self.escalation_incident_count = m.get('escalationIncidentCount')
        if m.get('incidentCount') is not None:
            self.incident_count = m.get('incidentCount')
        if m.get('meanTimeToAcknowledge') is not None:
            self.mean_time_to_acknowledge = m.get('meanTimeToAcknowledge')
        if m.get('meanTimeToRepair') is not None:
            self.mean_time_to_repair = m.get('meanTimeToRepair')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('totalMeanTimeToAcknowledge') is not None:
            self.total_mean_time_to_acknowledge = m.get('totalMeanTimeToAcknowledge')
        if m.get('totalMeanTimeToRepair') is not None:
            self.total_mean_time_to_repair = m.get('totalMeanTimeToRepair')
        if m.get('unAcknowledgedEscalationIncidentCount') is not None:
            self.un_acknowledged_escalation_incident_count = m.get('unAcknowledgedEscalationIncidentCount')
        if m.get('unFinishEscalationIncidentCount') is not None:
            self.un_finish_escalation_incident_count = m.get('unFinishEscalationIncidentCount')
        return self


class ListChartDataForServiceGroupResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: list[ListChartDataForServiceGroupResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChartDataForServiceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListChartDataForServiceGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListChartDataForServiceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListChartDataForServiceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChartDataForServiceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListChartDataForServiceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartDataForUserRequest(TeaModel):
    def __init__(self, client_token=None, end_time=None, start_time=None):
        self.client_token = client_token  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 开始时间
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartDataForUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListChartDataForUserResponseBodyData(TeaModel):
    def __init__(self, effection_level=None, escalation_incident_count=None, incident_count=None,
                 mean_time_to_acknowledge=None, mean_time_to_repair=None, time=None, total_mean_time_to_acknowledge=None,
                 total_mean_time_to_repair=None, un_acknowledged_escalation_incident_count=None, un_finish_escalation_incident_count=None):
        # 根据影响等级时间等级分组统计数量
        self.effection_level = effection_level  # type: dict[str, any]
        # 升级事件数
        self.escalation_incident_count = escalation_incident_count  # type: long
        # 时间总数
        self.incident_count = incident_count  # type: long
        # 当日平均响应时间单位秒
        self.mean_time_to_acknowledge = mean_time_to_acknowledge  # type: long
        # 当日平均完结时间单位秒
        self.mean_time_to_repair = mean_time_to_repair  # type: long
        # 时间
        self.time = time  # type: str
        # 总平均响应时间
        self.total_mean_time_to_acknowledge = total_mean_time_to_acknowledge  # type: long
        # 总平均完结时间
        self.total_mean_time_to_repair = total_mean_time_to_repair  # type: long
        # 未响应升级事件数
        self.un_acknowledged_escalation_incident_count = un_acknowledged_escalation_incident_count  # type: long
        # 未完结升级事件数
        self.un_finish_escalation_incident_count = un_finish_escalation_incident_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChartDataForUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effection_level is not None:
            result['effectionLevel'] = self.effection_level
        if self.escalation_incident_count is not None:
            result['escalationIncidentCount'] = self.escalation_incident_count
        if self.incident_count is not None:
            result['incidentCount'] = self.incident_count
        if self.mean_time_to_acknowledge is not None:
            result['meanTimeToAcknowledge'] = self.mean_time_to_acknowledge
        if self.mean_time_to_repair is not None:
            result['meanTimeToRepair'] = self.mean_time_to_repair
        if self.time is not None:
            result['time'] = self.time
        if self.total_mean_time_to_acknowledge is not None:
            result['totalMeanTimeToAcknowledge'] = self.total_mean_time_to_acknowledge
        if self.total_mean_time_to_repair is not None:
            result['totalMeanTimeToRepair'] = self.total_mean_time_to_repair
        if self.un_acknowledged_escalation_incident_count is not None:
            result['unAcknowledgedEscalationIncidentCount'] = self.un_acknowledged_escalation_incident_count
        if self.un_finish_escalation_incident_count is not None:
            result['unFinishEscalationIncidentCount'] = self.un_finish_escalation_incident_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effectionLevel') is not None:
            self.effection_level = m.get('effectionLevel')
        if m.get('escalationIncidentCount') is not None:
            self.escalation_incident_count = m.get('escalationIncidentCount')
        if m.get('incidentCount') is not None:
            self.incident_count = m.get('incidentCount')
        if m.get('meanTimeToAcknowledge') is not None:
            self.mean_time_to_acknowledge = m.get('meanTimeToAcknowledge')
        if m.get('meanTimeToRepair') is not None:
            self.mean_time_to_repair = m.get('meanTimeToRepair')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('totalMeanTimeToAcknowledge') is not None:
            self.total_mean_time_to_acknowledge = m.get('totalMeanTimeToAcknowledge')
        if m.get('totalMeanTimeToRepair') is not None:
            self.total_mean_time_to_repair = m.get('totalMeanTimeToRepair')
        if m.get('unAcknowledgedEscalationIncidentCount') is not None:
            self.un_acknowledged_escalation_incident_count = m.get('unAcknowledgedEscalationIncidentCount')
        if m.get('unFinishEscalationIncidentCount') is not None:
            self.un_finish_escalation_incident_count = m.get('unFinishEscalationIncidentCount')
        return self


class ListChartDataForUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: list[ListChartDataForUserResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChartDataForUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListChartDataForUserResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListChartDataForUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListChartDataForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChartDataForUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListChartDataForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigsRequest(TeaModel):
    def __init__(self, client_token=None):
        # 幂等校验token
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ListConfigsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: dict[str, list[DataValue]]
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for v in self.data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ListConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['data'][k] = l1
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = {}
        if m.get('data') is not None:
            for k, v in m.get('data').items():
                l1 = []
                for k1 in v:
                    temp_model = DataValue()
                    l1.append(temp_model.from_map(k1))
                self.data['k'] = l1
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataReportForServiceGroupRequest(TeaModel):
    def __init__(self, end_time=None, service_group_name=None, start_time=None):
        # 结束时间
        self.end_time = end_time  # type: str
        # 服务组名称
        self.service_group_name = service_group_name  # type: str
        # 开始时间
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataReportForServiceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListDataReportForServiceGroupResponseBodyData(TeaModel):
    def __init__(self, escalation_incident_count=None, finish_incident_count=None, finish_proportion=None,
                 incident_count=None, mean_time_to_acknowledge=None, mean_time_to_repair=None, service_group_id=None,
                 service_group_name=None, un_acknowledged_escalation_incident_count=None, un_finish_escalation_incident_count=None):
        # 升级事件数量
        self.escalation_incident_count = escalation_incident_count  # type: long
        # 事件完结数
        self.finish_incident_count = finish_incident_count  # type: long
        # 完结率
        self.finish_proportion = finish_proportion  # type: str
        # 事件数量
        self.incident_count = incident_count  # type: long
        # MRRA
        self.mean_time_to_acknowledge = mean_time_to_acknowledge  # type: long
        # MTTR
        self.mean_time_to_repair = mean_time_to_repair  # type: long
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 服务组名字
        self.service_group_name = service_group_name  # type: str
        # 未响应升级事件数量
        self.un_acknowledged_escalation_incident_count = un_acknowledged_escalation_incident_count  # type: long
        # 未完成升级事件数量
        self.un_finish_escalation_incident_count = un_finish_escalation_incident_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataReportForServiceGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_incident_count is not None:
            result['escalationIncidentCount'] = self.escalation_incident_count
        if self.finish_incident_count is not None:
            result['finishIncidentCount'] = self.finish_incident_count
        if self.finish_proportion is not None:
            result['finishProportion'] = self.finish_proportion
        if self.incident_count is not None:
            result['incidentCount'] = self.incident_count
        if self.mean_time_to_acknowledge is not None:
            result['meanTimeToAcknowledge'] = self.mean_time_to_acknowledge
        if self.mean_time_to_repair is not None:
            result['meanTimeToRepair'] = self.mean_time_to_repair
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        if self.un_acknowledged_escalation_incident_count is not None:
            result['unAcknowledgedEscalationIncidentCount'] = self.un_acknowledged_escalation_incident_count
        if self.un_finish_escalation_incident_count is not None:
            result['unFinishEscalationIncidentCount'] = self.un_finish_escalation_incident_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('escalationIncidentCount') is not None:
            self.escalation_incident_count = m.get('escalationIncidentCount')
        if m.get('finishIncidentCount') is not None:
            self.finish_incident_count = m.get('finishIncidentCount')
        if m.get('finishProportion') is not None:
            self.finish_proportion = m.get('finishProportion')
        if m.get('incidentCount') is not None:
            self.incident_count = m.get('incidentCount')
        if m.get('meanTimeToAcknowledge') is not None:
            self.mean_time_to_acknowledge = m.get('meanTimeToAcknowledge')
        if m.get('meanTimeToRepair') is not None:
            self.mean_time_to_repair = m.get('meanTimeToRepair')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        if m.get('unAcknowledgedEscalationIncidentCount') is not None:
            self.un_acknowledged_escalation_incident_count = m.get('unAcknowledgedEscalationIncidentCount')
        if m.get('unFinishEscalationIncidentCount') is not None:
            self.un_finish_escalation_incident_count = m.get('unFinishEscalationIncidentCount')
        return self


class ListDataReportForServiceGroupResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # 统计数据
        self.data = data  # type: list[ListDataReportForServiceGroupResponseBodyData]
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        # 总数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataReportForServiceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSIze'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListDataReportForServiceGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSIze') is not None:
            self.page_size = m.get('pageSIze')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDataReportForServiceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataReportForServiceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataReportForServiceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataReportForServiceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataReportForUserRequest(TeaModel):
    def __init__(self, end_time=None, page_number=None, page_size=None, start_time=None):
        # 结束时间
        self.end_time = end_time  # type: str
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # 开始时间
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataReportForUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListDataReportForUserResponseBodyData(TeaModel):
    def __init__(self, distribution_incident_count=None, escalation_incident_count=None,
                 finish_incident_number=None, finish_proportion=None, mean_time_to_acknowledge=None, mean_time_to_repair=None,
                 un_acknowledged_escalation_incident_count=None, un_distribution_incident_count=None, un_finish_escalation_incident_count=None,
                 user_id=None, user_name=None):
        # 分配事件数量
        self.distribution_incident_count = distribution_incident_count  # type: long
        # 升级事件数量
        self.escalation_incident_count = escalation_incident_count  # type: long
        # 完结事件数量
        self.finish_incident_number = finish_incident_number  # type: long
        # 完结率
        self.finish_proportion = finish_proportion  # type: str
        # MRRA
        self.mean_time_to_acknowledge = mean_time_to_acknowledge  # type: str
        # MTTA
        self.mean_time_to_repair = mean_time_to_repair  # type: str
        # 未响应升级数
        self.un_acknowledged_escalation_incident_count = un_acknowledged_escalation_incident_count  # type: long
        # 非分配完结数
        self.un_distribution_incident_count = un_distribution_incident_count  # type: long
        # 未完结事件数
        self.un_finish_escalation_incident_count = un_finish_escalation_incident_count  # type: long
        # 用户ID
        self.user_id = user_id  # type: long
        # 用户名字
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDataReportForUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_incident_count is not None:
            result['distributionIncidentCount'] = self.distribution_incident_count
        if self.escalation_incident_count is not None:
            result['escalationIncidentCount'] = self.escalation_incident_count
        if self.finish_incident_number is not None:
            result['finishIncidentNumber'] = self.finish_incident_number
        if self.finish_proportion is not None:
            result['finishProportion'] = self.finish_proportion
        if self.mean_time_to_acknowledge is not None:
            result['meanTimeToAcknowledge'] = self.mean_time_to_acknowledge
        if self.mean_time_to_repair is not None:
            result['meanTimeToRepair'] = self.mean_time_to_repair
        if self.un_acknowledged_escalation_incident_count is not None:
            result['unAcknowledgedEscalationIncidentCount'] = self.un_acknowledged_escalation_incident_count
        if self.un_distribution_incident_count is not None:
            result['unDistributionIncidentCount'] = self.un_distribution_incident_count
        if self.un_finish_escalation_incident_count is not None:
            result['unFinishEscalationIncidentCount'] = self.un_finish_escalation_incident_count
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('distributionIncidentCount') is not None:
            self.distribution_incident_count = m.get('distributionIncidentCount')
        if m.get('escalationIncidentCount') is not None:
            self.escalation_incident_count = m.get('escalationIncidentCount')
        if m.get('finishIncidentNumber') is not None:
            self.finish_incident_number = m.get('finishIncidentNumber')
        if m.get('finishProportion') is not None:
            self.finish_proportion = m.get('finishProportion')
        if m.get('meanTimeToAcknowledge') is not None:
            self.mean_time_to_acknowledge = m.get('meanTimeToAcknowledge')
        if m.get('meanTimeToRepair') is not None:
            self.mean_time_to_repair = m.get('meanTimeToRepair')
        if m.get('unAcknowledgedEscalationIncidentCount') is not None:
            self.un_acknowledged_escalation_incident_count = m.get('unAcknowledgedEscalationIncidentCount')
        if m.get('unDistributionIncidentCount') is not None:
            self.un_distribution_incident_count = m.get('unDistributionIncidentCount')
        if m.get('unFinishEscalationIncidentCount') is not None:
            self.un_finish_escalation_incident_count = m.get('unFinishEscalationIncidentCount')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class ListDataReportForUserResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, total_count=None):
        # 个人统计数据
        self.data = data  # type: list[ListDataReportForUserResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDataReportForUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListDataReportForUserResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDataReportForUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDataReportForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDataReportForUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDataReportForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDictionariesRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDictionariesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ListDictionariesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: dict[str, list[DataValue]]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for v in self.data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(ListDictionariesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['data'][k] = l1
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = {}
        if m.get('data') is not None:
            for k, v in m.get('data').items():
                l1 = []
                for k1 in v:
                    temp_model = DataValue()
                    l1.append(temp_model.from_map(k1))
                self.data['k'] = l1
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListDictionariesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDictionariesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDictionariesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDictionariesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEscalationPlanServicesRequest(TeaModel):
    def __init__(self, client_token=None):
        # clientToken
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEscalationPlanServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ListEscalationPlanServicesResponseBodyData(TeaModel):
    def __init__(self, scope=None, scope_object_id=None):
        # 范围类型
        self.scope = scope  # type: str
        # 范围对象id
        self.scope_object_id = scope_object_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEscalationPlanServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        if self.scope_object_id is not None:
            result['scopeObjectId'] = self.scope_object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scopeObjectId') is not None:
            self.scope_object_id = m.get('scopeObjectId')
        return self


class ListEscalationPlanServicesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: list[ListEscalationPlanServicesResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEscalationPlanServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListEscalationPlanServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListEscalationPlanServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEscalationPlanServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEscalationPlanServicesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEscalationPlanServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEscalationPlansRequest(TeaModel):
    def __init__(self, client_token=None, escalation_plan_name=None, page_number=None, page_size=None,
                 service_name=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 升级计划名
        self.escalation_plan_name = escalation_plan_name  # type: str
        # pageNumber
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        # 服务名称
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEscalationPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.escalation_plan_name is not None:
            result['escalationPlanName'] = self.escalation_plan_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('escalationPlanName') is not None:
            self.escalation_plan_name = m.get('escalationPlanName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListEscalationPlansResponseBodyDataEscalationPlanScopeObjects(TeaModel):
    def __init__(self, scope=None, scope_object_id=None, scope_object_name=None):
        # 范围对象类型
        self.scope = scope  # type: str
        # 范围对象id（服务id）
        self.scope_object_id = scope_object_id  # type: long
        # 范围对象名称
        self.scope_object_name = scope_object_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEscalationPlansResponseBodyDataEscalationPlanScopeObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        if self.scope_object_id is not None:
            result['scopeObjectId'] = self.scope_object_id
        if self.scope_object_name is not None:
            result['scopeObjectName'] = self.scope_object_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scopeObjectId') is not None:
            self.scope_object_id = m.get('scopeObjectId')
        if m.get('scopeObjectName') is not None:
            self.scope_object_name = m.get('scopeObjectName')
        return self


class ListEscalationPlansResponseBodyData(TeaModel):
    def __init__(self, escalation_plan_id=None, escalation_plan_name=None, escalation_plan_scope_objects=None,
                 modify_time=None, status=None):
        # 升级计划id
        self.escalation_plan_id = escalation_plan_id  # type: long
        # 升级计划名称
        self.escalation_plan_name = escalation_plan_name  # type: str
        # 升级计划范围对象
        self.escalation_plan_scope_objects = escalation_plan_scope_objects  # type: list[ListEscalationPlansResponseBodyDataEscalationPlanScopeObjects]
        # 修改时间
        self.modify_time = modify_time  # type: str
        # 启用ENABLE 禁用DISABLE
        self.status = status  # type: str

    def validate(self):
        if self.escalation_plan_scope_objects:
            for k in self.escalation_plan_scope_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEscalationPlansResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        if self.escalation_plan_name is not None:
            result['escalationPlanName'] = self.escalation_plan_name
        result['escalationPlanScopeObjects'] = []
        if self.escalation_plan_scope_objects is not None:
            for k in self.escalation_plan_scope_objects:
                result['escalationPlanScopeObjects'].append(k.to_map() if k else None)
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        if m.get('escalationPlanName') is not None:
            self.escalation_plan_name = m.get('escalationPlanName')
        self.escalation_plan_scope_objects = []
        if m.get('escalationPlanScopeObjects') is not None:
            for k in m.get('escalationPlanScopeObjects'):
                temp_model = ListEscalationPlansResponseBodyDataEscalationPlanScopeObjects()
                self.escalation_plan_scope_objects.append(temp_model.from_map(k))
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListEscalationPlansResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # data
        self.data = data  # type: list[ListEscalationPlansResponseBodyData]
        # 分页参数
        self.page_number = page_number  # type: long
        # 分页参数
        self.page_size = page_size  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEscalationPlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListEscalationPlansResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListEscalationPlansResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEscalationPlansResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEscalationPlansResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEscalationPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIncidentDetailEscalationPlansRequest(TeaModel):
    def __init__(self, client_token=None, incident_id=None):
        # 幂等校验
        self.client_token = client_token  # type: str
        # 事件ID
        self.incident_id = incident_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        return self


class ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlanNoticeObjectList(TeaModel):
    def __init__(self, notice_object_id=None, notice_object_name=None, notice_object_phone=None):
        # 分配对象id
        self.notice_object_id = notice_object_id  # type: long
        # 分配对象名称
        self.notice_object_name = notice_object_name  # type: str
        # 分配对象手机号
        self.notice_object_phone = notice_object_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlanNoticeObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notice_object_id is not None:
            result['noticeObjectId'] = self.notice_object_id
        if self.notice_object_name is not None:
            result['noticeObjectName'] = self.notice_object_name
        if self.notice_object_phone is not None:
            result['noticeObjectPhone'] = self.notice_object_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('noticeObjectId') is not None:
            self.notice_object_id = m.get('noticeObjectId')
        if m.get('noticeObjectName') is not None:
            self.notice_object_name = m.get('noticeObjectName')
        if m.get('noticeObjectPhone') is not None:
            self.notice_object_phone = m.get('noticeObjectPhone')
        return self


class ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlanServiceGroupList(TeaModel):
    def __init__(self, id=None, name=None):
        # 服务组id
        self.id = id  # type: long
        # 服务组名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlanServiceGroupList, self).to_map()
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


class ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlan(TeaModel):
    def __init__(self, escalation_plan_type=None, notice_channels=None, notice_object_list=None, notice_time=None,
                 service_group_list=None, start_time=None, status=None):
        # 升级策略类型 UN_ACKNOWLEDGE
        self.escalation_plan_type = escalation_plan_type  # type: str
        # 分配渠道
        self.notice_channels = notice_channels  # type: list[str]
        # 用户信息
        self.notice_object_list = notice_object_list  # type: list[ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlanNoticeObjectList]
        # 延迟时间
        self.notice_time = notice_time  # type: long
        # 通知群
        self.service_group_list = service_group_list  # type: list[ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlanServiceGroupList]
        # 开始时间
        self.start_time = start_time  # type: long
        # 规则触发状态
        self.status = status  # type: str

    def validate(self):
        if self.notice_object_list:
            for k in self.notice_object_list:
                if k:
                    k.validate()
        if self.service_group_list:
            for k in self.service_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlan, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_plan_type is not None:
            result['escalationPlanType'] = self.escalation_plan_type
        if self.notice_channels is not None:
            result['noticeChannels'] = self.notice_channels
        result['noticeObjectList'] = []
        if self.notice_object_list is not None:
            for k in self.notice_object_list:
                result['noticeObjectList'].append(k.to_map() if k else None)
        if self.notice_time is not None:
            result['noticeTime'] = self.notice_time
        result['serviceGroupList'] = []
        if self.service_group_list is not None:
            for k in self.service_group_list:
                result['serviceGroupList'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('escalationPlanType') is not None:
            self.escalation_plan_type = m.get('escalationPlanType')
        if m.get('noticeChannels') is not None:
            self.notice_channels = m.get('noticeChannels')
        self.notice_object_list = []
        if m.get('noticeObjectList') is not None:
            for k in m.get('noticeObjectList'):
                temp_model = ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlanNoticeObjectList()
                self.notice_object_list.append(temp_model.from_map(k))
        if m.get('noticeTime') is not None:
            self.notice_time = m.get('noticeTime')
        self.service_group_list = []
        if m.get('serviceGroupList') is not None:
            for k in m.get('serviceGroupList'):
                temp_model = ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlanServiceGroupList()
                self.service_group_list.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlanNoticeObjectList(TeaModel):
    def __init__(self, notice_object_id=None, notice_object_name=None, notice_object_phone=None):
        # 分配对象id
        self.notice_object_id = notice_object_id  # type: long
        # 分配对象名称
        self.notice_object_name = notice_object_name  # type: str
        # 手机号
        self.notice_object_phone = notice_object_phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlanNoticeObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notice_object_id is not None:
            result['noticeObjectId'] = self.notice_object_id
        if self.notice_object_name is not None:
            result['noticeObjectName'] = self.notice_object_name
        if self.notice_object_phone is not None:
            result['noticeObjectPhone'] = self.notice_object_phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('noticeObjectId') is not None:
            self.notice_object_id = m.get('noticeObjectId')
        if m.get('noticeObjectName') is not None:
            self.notice_object_name = m.get('noticeObjectName')
        if m.get('noticeObjectPhone') is not None:
            self.notice_object_phone = m.get('noticeObjectPhone')
        return self


class ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlanServiceGroupList(TeaModel):
    def __init__(self, id=None, name=None):
        # 服务组id
        self.id = id  # type: long
        # 服务组名称
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlanServiceGroupList, self).to_map()
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


class ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlan(TeaModel):
    def __init__(self, escalation_plan_type=None, notice_channels=None, notice_object_list=None, notice_time=None,
                 service_group_list=None, start_time=None, status=None):
        # 升级策略类型 UN_ACKNOWLEDGE
        self.escalation_plan_type = escalation_plan_type  # type: str
        # 分配渠道
        self.notice_channels = notice_channels  # type: list[str]
        # 用户信息
        self.notice_object_list = notice_object_list  # type: list[ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlanNoticeObjectList]
        # 延迟时间
        self.notice_time = notice_time  # type: int
        # 消息群
        self.service_group_list = service_group_list  # type: list[ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlanServiceGroupList]
        # 开始时间
        self.start_time = start_time  # type: long
        # 规则触发状态
        self.status = status  # type: str

    def validate(self):
        if self.notice_object_list:
            for k in self.notice_object_list:
                if k:
                    k.validate()
        if self.service_group_list:
            for k in self.service_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlan, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_plan_type is not None:
            result['escalationPlanType'] = self.escalation_plan_type
        if self.notice_channels is not None:
            result['noticeChannels'] = self.notice_channels
        result['noticeObjectList'] = []
        if self.notice_object_list is not None:
            for k in self.notice_object_list:
                result['noticeObjectList'].append(k.to_map() if k else None)
        if self.notice_time is not None:
            result['noticeTime'] = self.notice_time
        result['serviceGroupList'] = []
        if self.service_group_list is not None:
            for k in self.service_group_list:
                result['serviceGroupList'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('escalationPlanType') is not None:
            self.escalation_plan_type = m.get('escalationPlanType')
        if m.get('noticeChannels') is not None:
            self.notice_channels = m.get('noticeChannels')
        self.notice_object_list = []
        if m.get('noticeObjectList') is not None:
            for k in m.get('noticeObjectList'):
                temp_model = ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlanNoticeObjectList()
                self.notice_object_list.append(temp_model.from_map(k))
        if m.get('noticeTime') is not None:
            self.notice_time = m.get('noticeTime')
        self.service_group_list = []
        if m.get('serviceGroupList') is not None:
            for k in m.get('serviceGroupList'):
                temp_model = ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlanServiceGroupList()
                self.service_group_list.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListIncidentDetailEscalationPlansResponseBodyData(TeaModel):
    def __init__(self, escalation_plan_id=None, escalation_plan_name=None, nu_acknowledge_escalation_plan=None,
                 un_finish_escalation_plan=None):
        # 升级策略ID
        self.escalation_plan_id = escalation_plan_id  # type: long
        # 升级策略名称
        self.escalation_plan_name = escalation_plan_name  # type: str
        # 未响应升级策略
        self.nu_acknowledge_escalation_plan = nu_acknowledge_escalation_plan  # type: list[ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlan]
        # 未完结升级策略规则列表
        self.un_finish_escalation_plan = un_finish_escalation_plan  # type: list[ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlan]

    def validate(self):
        if self.nu_acknowledge_escalation_plan:
            for k in self.nu_acknowledge_escalation_plan:
                if k:
                    k.validate()
        if self.un_finish_escalation_plan:
            for k in self.un_finish_escalation_plan:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        if self.escalation_plan_name is not None:
            result['escalationPlanName'] = self.escalation_plan_name
        result['nuAcknowledgeEscalationPlan'] = []
        if self.nu_acknowledge_escalation_plan is not None:
            for k in self.nu_acknowledge_escalation_plan:
                result['nuAcknowledgeEscalationPlan'].append(k.to_map() if k else None)
        result['unFinishEscalationPlan'] = []
        if self.un_finish_escalation_plan is not None:
            for k in self.un_finish_escalation_plan:
                result['unFinishEscalationPlan'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        if m.get('escalationPlanName') is not None:
            self.escalation_plan_name = m.get('escalationPlanName')
        self.nu_acknowledge_escalation_plan = []
        if m.get('nuAcknowledgeEscalationPlan') is not None:
            for k in m.get('nuAcknowledgeEscalationPlan'):
                temp_model = ListIncidentDetailEscalationPlansResponseBodyDataNuAcknowledgeEscalationPlan()
                self.nu_acknowledge_escalation_plan.append(temp_model.from_map(k))
        self.un_finish_escalation_plan = []
        if m.get('unFinishEscalationPlan') is not None:
            for k in m.get('unFinishEscalationPlan'):
                temp_model = ListIncidentDetailEscalationPlansResponseBodyDataUnFinishEscalationPlan()
                self.un_finish_escalation_plan.append(temp_model.from_map(k))
        return self


class ListIncidentDetailEscalationPlansResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: ListIncidentDetailEscalationPlansResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListIncidentDetailEscalationPlansResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListIncidentDetailEscalationPlansResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIncidentDetailEscalationPlansResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIncidentDetailEscalationPlansResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIncidentDetailEscalationPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIncidentDetailTimelinesRequest(TeaModel):
    def __init__(self, client_token=None, incident_id=None, page_number=None, page_size=None):
        # 幂等校验
        self.client_token = client_token  # type: str
        # 事件ID
        self.incident_id = incident_id  # type: long
        # 页
        self.page_number = page_number  # type: long
        # 行
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentDetailTimelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListIncidentDetailTimelinesResponseBodyData(TeaModel):
    def __init__(self, action=None, create_time=None, description=None, incident_id=None, related_service_name=None,
                 remark=None, snapshot_data=None, title=None):
        # 事件action
        self.action = action  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 事件Id
        self.incident_id = incident_id  # type: long
        # 服务名称
        self.related_service_name = related_service_name  # type: str
        # 备注
        self.remark = remark  # type: str
        # 快照数据
        self.snapshot_data = snapshot_data  # type: str
        # 主题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentDetailTimelinesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.related_service_name is not None:
            result['relatedServiceName'] = self.related_service_name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.snapshot_data is not None:
            result['snapshotData'] = self.snapshot_data
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('relatedServiceName') is not None:
            self.related_service_name = m.get('relatedServiceName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('snapshotData') is not None:
            self.snapshot_data = m.get('snapshotData')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListIncidentDetailTimelinesResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[ListIncidentDetailTimelinesResponseBodyData]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        # 总数
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIncidentDetailTimelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListIncidentDetailTimelinesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListIncidentDetailTimelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIncidentDetailTimelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIncidentDetailTimelinesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIncidentDetailTimelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIncidentSubtotalsRequest(TeaModel):
    def __init__(self, client_token=None, incident_id=None):
        # 幂等校验
        self.client_token = client_token  # type: str
        # 事件ID
        self.incident_id = incident_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentSubtotalsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        return self


class ListIncidentSubtotalsResponseBodyData(TeaModel):
    def __init__(self, create_time=None, create_user_id=None, create_user_name=None, create_user_phone=None,
                 description=None):
        # 创建时间
        self.create_time = create_time  # type: str
        # 操作人Id
        self.create_user_id = create_user_id  # type: long
        # 操作人
        self.create_user_name = create_user_name  # type: str
        # 操作人手机号
        self.create_user_phone = create_user_phone  # type: str
        # 描述
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentSubtotalsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.create_user_id is not None:
            result['createUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['createUserName'] = self.create_user_name
        if self.create_user_phone is not None:
            result['createUserPhone'] = self.create_user_phone
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('createUserId') is not None:
            self.create_user_id = m.get('createUserId')
        if m.get('createUserName') is not None:
            self.create_user_name = m.get('createUserName')
        if m.get('createUserPhone') is not None:
            self.create_user_phone = m.get('createUserPhone')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class ListIncidentSubtotalsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[ListIncidentSubtotalsResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIncidentSubtotalsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListIncidentSubtotalsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListIncidentSubtotalsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIncidentSubtotalsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIncidentSubtotalsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIncidentSubtotalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIncidentTimelinesRequest(TeaModel):
    def __init__(self, client_token=None, page_number=None, page_size=None):
        # 幂等校验Id
        self.client_token = client_token  # type: str
        # 页
        self.page_number = page_number  # type: long
        # 行
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentTimelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListIncidentTimelinesResponseBodyData(TeaModel):
    def __init__(self, action=None, create_time=None, description=None, incident_id=None, incident_number=None,
                 incident_title=None, related_service_name=None, remark=None, snapshot_data=None, title=None):
        # 动态类型  触发新增 INCIDENT_ADD 响应 INCIDENT_RESPONSE 转交 INCIDENT_DELIVER 变更 INCIDENT_UPDATE 添加小计 INCIDENT_ADD_SUBTOTAL 完结 INCIDENT_FINISH 分配 INCIDENT_ASSIGN 升级 INCIDENT_UPGRAD
        self.action = action  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: long
        # 事件Id
        self.incident_id = incident_id  # type: long
        # 事件编号
        self.incident_number = incident_number  # type: str
        # 事件标题
        self.incident_title = incident_title  # type: str
        # 服务名称
        self.related_service_name = related_service_name  # type: str
        # 备注
        self.remark = remark  # type: str
        # 动态快照数据
        self.snapshot_data = snapshot_data  # type: str
        # 动态
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentTimelinesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_number is not None:
            result['incidentNumber'] = self.incident_number
        if self.incident_title is not None:
            result['incidentTitle'] = self.incident_title
        if self.related_service_name is not None:
            result['relatedServiceName'] = self.related_service_name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.snapshot_data is not None:
            result['snapshotData'] = self.snapshot_data
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentNumber') is not None:
            self.incident_number = m.get('incidentNumber')
        if m.get('incidentTitle') is not None:
            self.incident_title = m.get('incidentTitle')
        if m.get('relatedServiceName') is not None:
            self.related_service_name = m.get('relatedServiceName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('snapshotData') is not None:
            self.snapshot_data = m.get('snapshotData')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListIncidentTimelinesResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[ListIncidentTimelinesResponseBodyData]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        # 总数
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIncidentTimelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListIncidentTimelinesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListIncidentTimelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIncidentTimelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIncidentTimelinesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIncidentTimelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIncidentsRequest(TeaModel):
    def __init__(self, client_token=None, create_end_time=None, create_start_time=None, effect=None,
                 incident_level=None, incident_status=None, me=None, page_number=None, page_size=None, relation_service_id=None,
                 rule_name=None):
        # 幂等校验id
        self.client_token = client_token  # type: str
        # 创建结束时间
        self.create_end_time = create_end_time  # type: str
        # 创建开始时间
        self.create_start_time = create_start_time  # type: str
        # 影响等级 高：HIGH 低 LOW
        self.effect = effect  # type: str
        # 事件级别 P1 P2 P3 P4
        self.incident_level = incident_level  # type: str
        # 事件状态 ASSIGNED已分派 RESPONDED已响应  FINISHED已完结
        self.incident_status = incident_status  # type: str
        # 是否自己 1是 0不是
        self.me = me  # type: int
        # 页
        self.page_number = page_number  # type: int
        # 行
        self.page_size = page_size  # type: int
        # 关联服务ID
        self.relation_service_id = relation_service_id  # type: long
        # 流转规则名字
        self.rule_name = rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.create_end_time is not None:
            result['createEndTime'] = self.create_end_time
        if self.create_start_time is not None:
            result['createStartTime'] = self.create_start_time
        if self.effect is not None:
            result['effect'] = self.effect
        if self.incident_level is not None:
            result['incidentLevel'] = self.incident_level
        if self.incident_status is not None:
            result['incidentStatus'] = self.incident_status
        if self.me is not None:
            result['me'] = self.me
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.relation_service_id is not None:
            result['relationServiceId'] = self.relation_service_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('createEndTime') is not None:
            self.create_end_time = m.get('createEndTime')
        if m.get('createStartTime') is not None:
            self.create_start_time = m.get('createStartTime')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('incidentLevel') is not None:
            self.incident_level = m.get('incidentLevel')
        if m.get('incidentStatus') is not None:
            self.incident_status = m.get('incidentStatus')
        if m.get('me') is not None:
            self.me = m.get('me')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('relationServiceId') is not None:
            self.relation_service_id = m.get('relationServiceId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        return self


class ListIncidentsResponseBodyData(TeaModel):
    def __init__(self, assign_user_id=None, assign_user_name=None, assign_user_phone=None, create_time=None,
                 effect=None, incident_id=None, incident_level=None, incident_number=None, incident_status=None,
                 incident_title=None, is_manual=None, related_service_id=None, related_service_name=None, route_rule_id=None,
                 route_rule_name=None):
        # 分派的用户ID
        self.assign_user_id = assign_user_id  # type: long
        # 分派的用户姓名
        self.assign_user_name = assign_user_name  # type: str
        # 分派人手机号
        self.assign_user_phone = assign_user_phone  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 影响等级 高：HIGH 低 LOW
        self.effect = effect  # type: str
        self.incident_id = incident_id  # type: long
        # 事件级别 P1 P2 P3 P4
        self.incident_level = incident_level  # type: str
        # 事件编号
        self.incident_number = incident_number  # type: str
        # 事件状态 0已分派 1已响应 2已完结
        self.incident_status = incident_status  # type: str
        # 事件标题
        self.incident_title = incident_title  # type: str
        # 事件来源 是=手动 否=自动
        self.is_manual = is_manual  # type: bool
        # 关联服务ID
        self.related_service_id = related_service_id  # type: long
        # 关联服务名称
        self.related_service_name = related_service_name  # type: str
        # 流转规则ID
        self.route_rule_id = route_rule_id  # type: long
        # 流转规则
        self.route_rule_name = route_rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIncidentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_user_id is not None:
            result['assignUserId'] = self.assign_user_id
        if self.assign_user_name is not None:
            result['assignUserName'] = self.assign_user_name
        if self.assign_user_phone is not None:
            result['assignUserPhone'] = self.assign_user_phone
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.effect is not None:
            result['effect'] = self.effect
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_level is not None:
            result['incidentLevel'] = self.incident_level
        if self.incident_number is not None:
            result['incidentNumber'] = self.incident_number
        if self.incident_status is not None:
            result['incidentStatus'] = self.incident_status
        if self.incident_title is not None:
            result['incidentTitle'] = self.incident_title
        if self.is_manual is not None:
            result['isManual'] = self.is_manual
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.related_service_name is not None:
            result['relatedServiceName'] = self.related_service_name
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        if self.route_rule_name is not None:
            result['routeRuleName'] = self.route_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignUserId') is not None:
            self.assign_user_id = m.get('assignUserId')
        if m.get('assignUserName') is not None:
            self.assign_user_name = m.get('assignUserName')
        if m.get('assignUserPhone') is not None:
            self.assign_user_phone = m.get('assignUserPhone')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentLevel') is not None:
            self.incident_level = m.get('incidentLevel')
        if m.get('incidentNumber') is not None:
            self.incident_number = m.get('incidentNumber')
        if m.get('incidentStatus') is not None:
            self.incident_status = m.get('incidentStatus')
        if m.get('incidentTitle') is not None:
            self.incident_title = m.get('incidentTitle')
        if m.get('isManual') is not None:
            self.is_manual = m.get('isManual')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('relatedServiceName') is not None:
            self.related_service_name = m.get('relatedServiceName')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('routeRuleName') is not None:
            self.route_rule_name = m.get('routeRuleName')
        return self


class ListIncidentsResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[ListIncidentsResponseBodyData]
        # 页
        self.page_number = page_number  # type: int
        # 行
        self.page_size = page_size  # type: int
        # requestId
        self.request_id = request_id  # type: str
        # 总数
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIncidentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListIncidentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListIncidentsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIncidentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIncidentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIncidentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntegrationConfigTimelinesRequest(TeaModel):
    def __init__(self, client_token=None, integration_config_id=None, page_number=None, page_size=None):
        # 幂等参数
        self.client_token = client_token  # type: str
        # 集成配置id
        self.integration_config_id = integration_config_id  # type: long
        # 分页参数
        self.page_number = page_number  # type: long
        # 分页参数
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntegrationConfigTimelinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListIntegrationConfigTimelinesResponseBodyData(TeaModel):
    def __init__(self, create_time=None, description=None, title=None):
        # 创建时间
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 主题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntegrationConfigTimelinesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListIntegrationConfigTimelinesResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[ListIntegrationConfigTimelinesResponseBodyData]
        # pageNumber
        self.page_number = page_number  # type: long
        # pageSize
        self.page_size = page_size  # type: long
        # requestId
        self.request_id = request_id  # type: str
        # totalCount
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIntegrationConfigTimelinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListIntegrationConfigTimelinesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListIntegrationConfigTimelinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIntegrationConfigTimelinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIntegrationConfigTimelinesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIntegrationConfigTimelinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntegrationConfigsRequest(TeaModel):
    def __init__(self, client_token=None, monitor_source_name=None):
        # 幂等id
        self.client_token = client_token  # type: str
        self.monitor_source_name = monitor_source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntegrationConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        return self


class ListIntegrationConfigsResponseBodyData(TeaModel):
    def __init__(self, integration_config_id=None, is_received_event=None, monitor_source_id=None,
                 monitor_source_name=None, monitor_source_short_name=None, status=None):
        # 集成配置id
        self.integration_config_id = integration_config_id  # type: long
        # 是否已接受报警
        self.is_received_event = is_received_event  # type: bool
        # 监控源id
        self.monitor_source_id = monitor_source_id  # type: long
        # 监控源名城
        self.monitor_source_name = monitor_source_name  # type: str
        # 监控源简称
        self.monitor_source_short_name = monitor_source_short_name  # type: str
        # 集成配置状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntegrationConfigsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        if self.is_received_event is not None:
            result['isReceivedEvent'] = self.is_received_event
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        if self.monitor_source_short_name is not None:
            result['monitorSourceShortName'] = self.monitor_source_short_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        if m.get('isReceivedEvent') is not None:
            self.is_received_event = m.get('isReceivedEvent')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        if m.get('monitorSourceShortName') is not None:
            self.monitor_source_short_name = m.get('monitorSourceShortName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListIntegrationConfigsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[ListIntegrationConfigsResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIntegrationConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListIntegrationConfigsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListIntegrationConfigsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListIntegrationConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIntegrationConfigsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIntegrationConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMonitorSourcesRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMonitorSourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ListMonitorSourcesResponseBodyData(TeaModel):
    def __init__(self, field_keys=None, monitor_source_id=None, monitor_source_name=None):
        self.field_keys = field_keys  # type: list[str]
        self.monitor_source_id = monitor_source_id  # type: long
        self.monitor_source_name = monitor_source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMonitorSourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_keys is not None:
            result['fieldKeys'] = self.field_keys
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fieldKeys') is not None:
            self.field_keys = m.get('fieldKeys')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        return self


class ListMonitorSourcesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[ListMonitorSourcesResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMonitorSourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListMonitorSourcesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListMonitorSourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListMonitorSourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMonitorSourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMonitorSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProblemDetailOperationsRequest(TeaModel):
    def __init__(self, client_token=None, create_time_sort=None, page_number=None, page_size=None, problem_id=None):
        # 幂等校验
        self.client_token = client_token  # type: str
        # 时间排序
        self.create_time_sort = create_time_sort  # type: str
        # 页
        self.page_number = page_number  # type: int
        # 行
        self.page_size = page_size  # type: int
        # 故障id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemDetailOperationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.create_time_sort is not None:
            result['createTimeSort'] = self.create_time_sort
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('createTimeSort') is not None:
            self.create_time_sort = m.get('createTimeSort')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class ListProblemDetailOperationsResponseBodyData(TeaModel):
    def __init__(self, action=None, create_time=None, description=None, related_service_name=None, remark=None,
                 snapshot_data=None, title=None):
        # 升级 PROBLEM_UPGRADE 撤销 PROBLEM_REVOKE 恢复 PROBLEM_RESTORE 复盘 PROBLEM_IN_REVIEW 完结 PROBLEM_REOPENED 取消 PROBLEM_CANCEL 更新故障通告 PROBLEM_UPDATE_NOTIFY 添加故障小计 PROBLEM_ADD_SUBTOTAL 更新故障 PROBLEM_UPDATE
        self.action = action  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 服务
        self.related_service_name = related_service_name  # type: str
        # 备注
        self.remark = remark  # type: str
        # 快照数据
        self.snapshot_data = snapshot_data  # type: str
        # 动态标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemDetailOperationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.related_service_name is not None:
            result['relatedServiceName'] = self.related_service_name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.snapshot_data is not None:
            result['snapshotData'] = self.snapshot_data
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('relatedServiceName') is not None:
            self.related_service_name = m.get('relatedServiceName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('snapshotData') is not None:
            self.snapshot_data = m.get('snapshotData')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListProblemDetailOperationsResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # data
        self.data = data  # type: list[ListProblemDetailOperationsResponseBodyData]
        # 页
        self.page_number = page_number  # type: int
        # 行
        self.page_size = page_size  # type: int
        # requestId
        self.request_id = request_id  # type: str
        # 总数
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProblemDetailOperationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProblemDetailOperationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProblemDetailOperationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProblemDetailOperationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProblemDetailOperationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProblemDetailOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProblemOperationsRequest(TeaModel):
    def __init__(self, client_token=None, page_number=None, page_size=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 页
        self.page_number = page_number  # type: int
        # 行
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemOperationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListProblemOperationsResponseBodyData(TeaModel):
    def __init__(self, action=None, create_time=None, description=None, problem_id=None, problem_name=None,
                 problem_number=None, related_service_name=None, snapshot_data=None, title=None):
        # 升级    PROBLEM_UPGRADE      撤销     PROBLEM_REVOKE      恢复     PROBLEM_RESTORE       复盘     PROBLEM_IN_REVIEW       完结     PROBLEM_REOPENED       取消     PROBLEM_CANCEL       更新故障通告     PROBLEM_UPDATE_NOTIFY       添加故障小计     PROBLEM_ADD_SUBTOTAL       更新故障     PROBLEM_UPDATE
        self.action = action  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 描述
        self.description = description  # type: str
        # 故障Id
        self.problem_id = problem_id  # type: long
        # 故障名称
        self.problem_name = problem_name  # type: str
        # 故障编号
        self.problem_number = problem_number  # type: str
        # 服务名称
        self.related_service_name = related_service_name  # type: str
        # 快照数据
        self.snapshot_data = snapshot_data  # type: str
        # 动态标题
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemOperationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_name is not None:
            result['problemName'] = self.problem_name
        if self.problem_number is not None:
            result['problemNumber'] = self.problem_number
        if self.related_service_name is not None:
            result['relatedServiceName'] = self.related_service_name
        if self.snapshot_data is not None:
            result['snapshotData'] = self.snapshot_data
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemName') is not None:
            self.problem_name = m.get('problemName')
        if m.get('problemNumber') is not None:
            self.problem_number = m.get('problemNumber')
        if m.get('relatedServiceName') is not None:
            self.related_service_name = m.get('relatedServiceName')
        if m.get('snapshotData') is not None:
            self.snapshot_data = m.get('snapshotData')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListProblemOperationsResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # data
        self.data = data  # type: list[ListProblemOperationsResponseBodyData]
        # 页
        self.page_number = page_number  # type: int
        # 行
        self.page_size = page_size  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        # 总数
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProblemOperationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProblemOperationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProblemOperationsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProblemOperationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProblemOperationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProblemOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProblemSubtotalsRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 故障Id
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemSubtotalsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class ListProblemSubtotalsResponseBodyData(TeaModel):
    def __init__(self, create_ram_name=None, create_time=None, create_user_id=None, create_user_phone=None,
                 description=None):
        # 操作人
        self.create_ram_name = create_ram_name  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 人员id
        self.create_user_id = create_user_id  # type: long
        # 操作人手机号
        self.create_user_phone = create_user_phone  # type: str
        # 描述
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemSubtotalsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_ram_name is not None:
            result['createRamName'] = self.create_ram_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.create_user_id is not None:
            result['createUserId'] = self.create_user_id
        if self.create_user_phone is not None:
            result['createUserPhone'] = self.create_user_phone
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('createRamName') is not None:
            self.create_ram_name = m.get('createRamName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('createUserId') is not None:
            self.create_user_id = m.get('createUserId')
        if m.get('createUserPhone') is not None:
            self.create_user_phone = m.get('createUserPhone')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class ListProblemSubtotalsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[ListProblemSubtotalsResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProblemSubtotalsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProblemSubtotalsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProblemSubtotalsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProblemSubtotalsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProblemSubtotalsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProblemSubtotalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProblemTimeLinesRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 故障ID
        self.problem_id = problem_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemTimeLinesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        return self


class ListProblemTimeLinesResponseBodyDataUsersInContent(TeaModel):
    def __init__(self, user_id=None, username=None):
        # 用户id
        self.user_id = user_id  # type: long
        # 用户名
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemTimeLinesResponseBodyDataUsersInContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListProblemTimeLinesResponseBodyData(TeaModel):
    def __init__(self, content=None, create_time=None, is_key=None, key_node=None, problem_timeline_id=None,
                 time=None, update_time=None, users_in_content=None):
        # 内容
        self.content = content  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 是否是关键字 true是 false不是 默认 false
        self.is_key = is_key  # type: bool
        # 关键节点 码表:PROBLEM_KEY_NODE (逗号分隔)
        self.key_node = key_node  # type: str
        # 时间线id
        self.problem_timeline_id = problem_timeline_id  # type: long
        # 展示时间
        self.time = time  # type: str
        # 修改时间
        self.update_time = update_time  # type: str
        # 内容中的用户信息
        self.users_in_content = users_in_content  # type: list[ListProblemTimeLinesResponseBodyDataUsersInContent]

    def validate(self):
        if self.users_in_content:
            for k in self.users_in_content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProblemTimeLinesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.is_key is not None:
            result['isKey'] = self.is_key
        if self.key_node is not None:
            result['keyNode'] = self.key_node
        if self.problem_timeline_id is not None:
            result['problemTimelineId'] = self.problem_timeline_id
        if self.time is not None:
            result['time'] = self.time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        result['usersInContent'] = []
        if self.users_in_content is not None:
            for k in self.users_in_content:
                result['usersInContent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('isKey') is not None:
            self.is_key = m.get('isKey')
        if m.get('keyNode') is not None:
            self.key_node = m.get('keyNode')
        if m.get('problemTimelineId') is not None:
            self.problem_timeline_id = m.get('problemTimelineId')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        self.users_in_content = []
        if m.get('usersInContent') is not None:
            for k in m.get('usersInContent'):
                temp_model = ListProblemTimeLinesResponseBodyDataUsersInContent()
                self.users_in_content.append(temp_model.from_map(k))
        return self


class ListProblemTimeLinesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[ListProblemTimeLinesResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProblemTimeLinesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProblemTimeLinesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProblemTimeLinesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProblemTimeLinesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProblemTimeLinesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProblemTimeLinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProblemsRequest(TeaModel):
    def __init__(self, affect_service_id=None, client_token=None, discovery_end_time=None,
                 discovery_start_time=None, main_handler_id=None, page_number=None, page_size=None, problem_level=None,
                 problem_status=None, query_type=None, repeater_id=None, restore_end_time=None, restore_start_time=None,
                 service_group_id=None):
        # 影响服务ID
        self.affect_service_id = affect_service_id  # type: long
        # 幂等号
        self.client_token = client_token  # type: str
        # 发现结束时间
        self.discovery_end_time = discovery_end_time  # type: str
        # 发现开始时间
        self.discovery_start_time = discovery_start_time  # type: str
        # 主要处理人
        self.main_handler_id = main_handler_id  # type: long
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # 故障等级 1=P1 2=P2 3=P3 4=P4
        self.problem_level = problem_level  # type: str
        # 故障状态  HANDLING   处理中 RECOVERED 已恢复  REPLAYING   复盘中  REPLAYED     已复盘 CANCEL        已取消
        self.problem_status = problem_status  # type: str
        # RESPONSIBLE 我负责的       PARTICIPATED 我参与的  ALL 全部
        self.query_type = query_type  # type: str
        # 复盘负责人
        self.repeater_id = repeater_id  # type: long
        # 恢复结束时间
        self.restore_end_time = restore_end_time  # type: str
        # 恢复开始时间
        self.restore_start_time = restore_start_time  # type: str
        # 应急协同组
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_service_id is not None:
            result['affectServiceId'] = self.affect_service_id
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.discovery_end_time is not None:
            result['discoveryEndTime'] = self.discovery_end_time
        if self.discovery_start_time is not None:
            result['discoveryStartTime'] = self.discovery_start_time
        if self.main_handler_id is not None:
            result['mainHandlerId'] = self.main_handler_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.problem_level is not None:
            result['problemLevel'] = self.problem_level
        if self.problem_status is not None:
            result['problemStatus'] = self.problem_status
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.repeater_id is not None:
            result['repeaterId'] = self.repeater_id
        if self.restore_end_time is not None:
            result['restoreEndTime'] = self.restore_end_time
        if self.restore_start_time is not None:
            result['restoreStartTime'] = self.restore_start_time
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('affectServiceId') is not None:
            self.affect_service_id = m.get('affectServiceId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('discoveryEndTime') is not None:
            self.discovery_end_time = m.get('discoveryEndTime')
        if m.get('discoveryStartTime') is not None:
            self.discovery_start_time = m.get('discoveryStartTime')
        if m.get('mainHandlerId') is not None:
            self.main_handler_id = m.get('mainHandlerId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('problemLevel') is not None:
            self.problem_level = m.get('problemLevel')
        if m.get('problemStatus') is not None:
            self.problem_status = m.get('problemStatus')
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('repeaterId') is not None:
            self.repeater_id = m.get('repeaterId')
        if m.get('restoreEndTime') is not None:
            self.restore_end_time = m.get('restoreEndTime')
        if m.get('restoreStartTime') is not None:
            self.restore_start_time = m.get('restoreStartTime')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class ListProblemsResponseBodyDataAffectServices(TeaModel):
    def __init__(self, service_description=None, service_id=None, service_name=None, update_time=None):
        # 服务描述
        self.service_description = service_description  # type: str
        # 影响服务ID
        self.service_id = service_id  # type: long
        # 服务名字
        self.service_name = service_name  # type: str
        # 修改时间
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProblemsResponseBodyDataAffectServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_description is not None:
            result['serviceDescription'] = self.service_description
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceDescription') is not None:
            self.service_description = m.get('serviceDescription')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListProblemsResponseBodyData(TeaModel):
    def __init__(self, affect_services=None, cancel_time=None, create_time=None, discover_time=None,
                 finish_time=None, incident_id=None, is_manual=None, is_upgrade=None, main_handler_id=None,
                 main_handler_name=None, problem_id=None, problem_level=None, problem_name=None, problem_number=None,
                 problem_status=None, recovery_time=None, related_service_id=None, replay_time=None, service_name=None,
                 update_time=None):
        self.affect_services = affect_services  # type: list[ListProblemsResponseBodyDataAffectServices]
        # 取消时间
        self.cancel_time = cancel_time  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 发现时间
        self.discover_time = discover_time  # type: str
        # 完结时间
        self.finish_time = finish_time  # type: str
        # 事件ID
        self.incident_id = incident_id  # type: long
        # 是否手动
        self.is_manual = is_manual  # type: bool
        # 是否升级
        self.is_upgrade = is_upgrade  # type: bool
        # 主要处理人ID
        self.main_handler_id = main_handler_id  # type: long
        # 主要处理人名称
        self.main_handler_name = main_handler_name  # type: str
        # 故障id
        self.problem_id = problem_id  # type: long
        # 故障等级 1=P1 2=P2 3=P3 4=P4
        self.problem_level = problem_level  # type: str
        # 故障名称
        self.problem_name = problem_name  # type: str
        # 故障编号
        self.problem_number = problem_number  # type: str
        # 故障状态  HANDLING    处理中 RECOVERED  已恢复  REPLAYING   复盘中  REPLAYED     已复盘 CANCEL        已取消
        self.problem_status = problem_status  # type: str
        # 恢复时间
        self.recovery_time = recovery_time  # type: str
        # 关联服务ID
        self.related_service_id = related_service_id  # type: str
        # 复盘时间
        self.replay_time = replay_time  # type: str
        # 关联服务名称
        self.service_name = service_name  # type: str
        # 修改时间
        self.update_time = update_time  # type: str

    def validate(self):
        if self.affect_services:
            for k in self.affect_services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProblemsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['affectServices'] = []
        if self.affect_services is not None:
            for k in self.affect_services:
                result['affectServices'].append(k.to_map() if k else None)
        if self.cancel_time is not None:
            result['cancelTime'] = self.cancel_time
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.discover_time is not None:
            result['discoverTime'] = self.discover_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.is_manual is not None:
            result['isManual'] = self.is_manual
        if self.is_upgrade is not None:
            result['isUpgrade'] = self.is_upgrade
        if self.main_handler_id is not None:
            result['mainHandlerId'] = self.main_handler_id
        if self.main_handler_name is not None:
            result['mainHandlerName'] = self.main_handler_name
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_level is not None:
            result['problemLevel'] = self.problem_level
        if self.problem_name is not None:
            result['problemName'] = self.problem_name
        if self.problem_number is not None:
            result['problemNumber'] = self.problem_number
        if self.problem_status is not None:
            result['problemStatus'] = self.problem_status
        if self.recovery_time is not None:
            result['recoveryTime'] = self.recovery_time
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.replay_time is not None:
            result['replayTime'] = self.replay_time
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.affect_services = []
        if m.get('affectServices') is not None:
            for k in m.get('affectServices'):
                temp_model = ListProblemsResponseBodyDataAffectServices()
                self.affect_services.append(temp_model.from_map(k))
        if m.get('cancelTime') is not None:
            self.cancel_time = m.get('cancelTime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('discoverTime') is not None:
            self.discover_time = m.get('discoverTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('isManual') is not None:
            self.is_manual = m.get('isManual')
        if m.get('isUpgrade') is not None:
            self.is_upgrade = m.get('isUpgrade')
        if m.get('mainHandlerId') is not None:
            self.main_handler_id = m.get('mainHandlerId')
        if m.get('mainHandlerName') is not None:
            self.main_handler_name = m.get('mainHandlerName')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemLevel') is not None:
            self.problem_level = m.get('problemLevel')
        if m.get('problemName') is not None:
            self.problem_name = m.get('problemName')
        if m.get('problemNumber') is not None:
            self.problem_number = m.get('problemNumber')
        if m.get('problemStatus') is not None:
            self.problem_status = m.get('problemStatus')
        if m.get('recoveryTime') is not None:
            self.recovery_time = m.get('recoveryTime')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('replayTime') is not None:
            self.replay_time = m.get('replayTime')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListProblemsResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[ListProblemsResponseBodyData]
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProblemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProblemsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProblemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProblemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProblemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProblemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRouteRulesRequest(TeaModel):
    def __init__(self, client_token=None, page_number=None, page_size=None, route_type=None, rule_name=None,
                 service_name=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 第几页
        self.page_number = page_number  # type: int
        # 页的大小
        self.page_size = page_size  # type: int
        # 路由类型：0触发事件 1仅触发报警 r
        self.route_type = route_type  # type: long
        # 规则名称
        self.rule_name = rule_name  # type: bytes
        # 服务名称
        self.service_name = service_name  # type: bytes

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRouteRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListRouteRulesResponseBodyData(TeaModel):
    def __init__(self, assign_object_id=None, assign_object_type=None, create_time=None, effection=None,
                 enable_status=None, incident_level=None, match_count=None, monitor_source_names=None, related_service_id=None,
                 related_service_name=None, route_rule_id=None, route_type=None, rule_name=None, tenant_ram_id=None, time_window=None,
                 time_window_unit=None, update_time=None):
        # 事件分派对象ID（服务组ID 或用户ID）
        self.assign_object_id = assign_object_id  # type: long
        # 事件分派对象类型 SERVICEGROUP 服务组  USER 单个用户
        self.assign_object_type = assign_object_type  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 影响程度 LOW-一般 HIGH-严重
        self.effection = effection  # type: str
        # 是否启用  DISABLE禁用. ENABLE 启用
        self.enable_status = enable_status  # type: str
        # 事件级别 P1 P2 P3 P4
        self.incident_level = incident_level  # type: str
        # 命中次数
        self.match_count = match_count  # type: long
        # 监控源名称
        self.monitor_source_names = monitor_source_names  # type: str
        # 关联服务ID
        self.related_service_id = related_service_id  # type: long
        # 服务名称
        self.related_service_name = related_service_name  # type: str
        # 规则ID
        self.route_rule_id = route_rule_id  # type: long
        # 路由类型：INCIDENT 触发事件 ALERT 仅触发报警
        self.route_type = route_type  # type: str
        # 规则名称
        self.rule_name = rule_name  # type: str
        # 租户ID
        self.tenant_ram_id = tenant_ram_id  # type: long
        # 时间窗口
        self.time_window = time_window  # type: long
        # 时间窗口单位 MINUTE 分钟  SECOND 秒
        self.time_window_unit = time_window_unit  # type: long
        # 修改时间
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRouteRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_object_id is not None:
            result['assignObjectId'] = self.assign_object_id
        if self.assign_object_type is not None:
            result['assignObjectType'] = self.assign_object_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.effection is not None:
            result['effection'] = self.effection
        if self.enable_status is not None:
            result['enableStatus'] = self.enable_status
        if self.incident_level is not None:
            result['incidentLevel'] = self.incident_level
        if self.match_count is not None:
            result['matchCount'] = self.match_count
        if self.monitor_source_names is not None:
            result['monitorSourceNames'] = self.monitor_source_names
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.related_service_name is not None:
            result['relatedServiceName'] = self.related_service_name
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.tenant_ram_id is not None:
            result['tenantRamId'] = self.tenant_ram_id
        if self.time_window is not None:
            result['timeWindow'] = self.time_window
        if self.time_window_unit is not None:
            result['timeWindowUnit'] = self.time_window_unit
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignObjectId') is not None:
            self.assign_object_id = m.get('assignObjectId')
        if m.get('assignObjectType') is not None:
            self.assign_object_type = m.get('assignObjectType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('enableStatus') is not None:
            self.enable_status = m.get('enableStatus')
        if m.get('incidentLevel') is not None:
            self.incident_level = m.get('incidentLevel')
        if m.get('matchCount') is not None:
            self.match_count = m.get('matchCount')
        if m.get('monitorSourceNames') is not None:
            self.monitor_source_names = m.get('monitorSourceNames')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('relatedServiceName') is not None:
            self.related_service_name = m.get('relatedServiceName')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('tenantRamId') is not None:
            self.tenant_ram_id = m.get('tenantRamId')
        if m.get('timeWindow') is not None:
            self.time_window = m.get('timeWindow')
        if m.get('timeWindowUnit') is not None:
            self.time_window_unit = m.get('timeWindowUnit')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListRouteRulesResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # 规则列表
        self.data = data  # type: list[ListRouteRulesResponseBodyData]
        # 第几页
        self.page_number = page_number  # type: long
        # 分页大小
        self.page_size = page_size  # type: long
        # 请求ID
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRouteRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListRouteRulesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListRouteRulesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRouteRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRouteRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRouteRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceGroupMonitorSourceTemplatesRequest(TeaModel):
    def __init__(self, client_token=None, request_id=None, service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceGroupMonitorSourceTemplatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class ListServiceGroupMonitorSourceTemplatesResponseBodyData(TeaModel):
    def __init__(self, fields=None, monitor_source_id=None, monitor_source_name=None, template_content=None,
                 template_id=None):
        # 字段
        self.fields = fields  # type: list[str]
        # 监控源ID
        self.monitor_source_id = monitor_source_id  # type: long
        # 监控报警源名字
        self.monitor_source_name = monitor_source_name  # type: str
        # 模板内容
        self.template_content = template_content  # type: str
        # 消息模版ID
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceGroupMonitorSourceTemplatesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['fields'] = self.fields
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        if self.template_content is not None:
            result['templateContent'] = self.template_content
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        if m.get('templateContent') is not None:
            self.template_content = m.get('templateContent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class ListServiceGroupMonitorSourceTemplatesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: list[ListServiceGroupMonitorSourceTemplatesResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceGroupMonitorSourceTemplatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListServiceGroupMonitorSourceTemplatesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListServiceGroupMonitorSourceTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceGroupMonitorSourceTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceGroupMonitorSourceTemplatesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServiceGroupMonitorSourceTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceGroupsRequest(TeaModel):
    def __init__(self, client_token=None, is_scheduled=None, order_by_schedule_status=None, page_number=None,
                 page_size=None, query_name=None, query_type=None, user_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 是否已经排班
        self.is_scheduled = is_scheduled  # type: bool
        # 是否根据排班状态排序
        self.order_by_schedule_status = order_by_schedule_status  # type: bool
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # 搜索名称
        self.query_name = query_name  # type: str
        # 搜索类型。USER用户 SERVICEGROUP服务组
        self.query_type = query_type  # type: str
        # 用户ID
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.is_scheduled is not None:
            result['isScheduled'] = self.is_scheduled
        if self.order_by_schedule_status is not None:
            result['orderByScheduleStatus'] = self.order_by_schedule_status
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query_name is not None:
            result['queryName'] = self.query_name
        if self.query_type is not None:
            result['queryType'] = self.query_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('isScheduled') is not None:
            self.is_scheduled = m.get('isScheduled')
        if m.get('orderByScheduleStatus') is not None:
            self.order_by_schedule_status = m.get('orderByScheduleStatus')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')
        if m.get('queryType') is not None:
            self.query_type = m.get('queryType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListServiceGroupsResponseBodyDataUsers(TeaModel):
    def __init__(self, email=None, phone=None, service_group_id=None, user_id=None, user_name=None):
        # 邮箱
        self.email = email  # type: str
        # 手机号
        self.phone = phone  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 用户ID
        self.user_id = user_id  # type: long
        # 用户名字
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServiceGroupsResponseBodyDataUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.phone is not None:
            result['phone'] = self.phone
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class ListServiceGroupsResponseBodyData(TeaModel):
    def __init__(self, enable_webhook=None, is_scheduled=None, service_group_description=None,
                 service_group_id=None, service_group_name=None, update_time=None, users=None, webhook_link=None, webhook_type=None):
        # ENABLE 启用 DISABLE 禁用
        self.enable_webhook = enable_webhook  # type: str
        # 是否已经排班
        self.is_scheduled = is_scheduled  # type: bool
        # 服务组描述
        self.service_group_description = service_group_description  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 服务组名字
        self.service_group_name = service_group_name  # type: str
        # 修改时间
        self.update_time = update_time  # type: str
        # 服务组用户列表
        self.users = users  # type: list[ListServiceGroupsResponseBodyDataUsers]
        # webhook 跳转地址
        self.webhook_link = webhook_link  # type: str
        # WEIXIN_GROUP微信DING_GROUP钉钉FEISHU_GROUP飞书
        self.webhook_type = webhook_type  # type: str

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_webhook is not None:
            result['enableWebhook'] = self.enable_webhook
        if self.is_scheduled is not None:
            result['isScheduled'] = self.is_scheduled
        if self.service_group_description is not None:
            result['serviceGroupDescription'] = self.service_group_description
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        if self.webhook_link is not None:
            result['webhookLink'] = self.webhook_link
        if self.webhook_type is not None:
            result['webhookType'] = self.webhook_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableWebhook') is not None:
            self.enable_webhook = m.get('enableWebhook')
        if m.get('isScheduled') is not None:
            self.is_scheduled = m.get('isScheduled')
        if m.get('serviceGroupDescription') is not None:
            self.service_group_description = m.get('serviceGroupDescription')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListServiceGroupsResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        if m.get('webhookLink') is not None:
            self.webhook_link = m.get('webhookLink')
        if m.get('webhookType') is not None:
            self.webhook_type = m.get('webhookType')
        return self


class ListServiceGroupsResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # 服务组列表
        self.data = data  # type: list[ListServiceGroupsResponseBodyData]
        # 当前页
        self.page_number = page_number  # type: long
        # 分页大小
        self.page_size = page_size  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServiceGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListServiceGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListServiceGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServiceGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServiceGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServiceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(self, client_token=None, page_number=None, page_size=None, service_name=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # 服务名称
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListServicesResponseBodyData(TeaModel):
    def __init__(self, service_description=None, service_id=None, service_name=None, update_time=None):
        # 服务描述
        self.service_description = service_description  # type: str
        # 服务ID
        self.service_id = service_id  # type: long
        # 服务名字
        self.service_name = service_name  # type: str
        # 修改时间
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_description is not None:
            result['serviceDescription'] = self.service_description
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceDescription') is not None:
            self.service_description = m.get('serviceDescription')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[ListServicesResponseBodyData]
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # Id of the request
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServicesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSourceEventsRequest(TeaModel):
    def __init__(self, client_token=None, end_time=None, instance_id=None, instance_type=None, page_number=None,
                 page_size=None, start_row_key=None, start_time=None, stop_row_key=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 结束时间
        self.end_time = end_time  # type: str
        # 报警或者事件ID
        self.instance_id = instance_id  # type: long
        # INCIDENT 事件、ALERT 报警、PROBLEM 故障
        self.instance_type = instance_type  # type: str
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # startRowKey 用来查询下一页的数据
        self.start_row_key = start_row_key  # type: str
        # 开始时间
        self.start_time = start_time  # type: str
        # stopRowKey 用来查询上一页的数据
        self.stop_row_key = stop_row_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSourceEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.start_row_key is not None:
            result['startRowKey'] = self.start_row_key
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.stop_row_key is not None:
            result['stopRowKey'] = self.stop_row_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('startRowKey') is not None:
            self.start_row_key = m.get('startRowKey')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('stopRowKey') is not None:
            self.stop_row_key = m.get('stopRowKey')
        return self


class ListSourceEventsResponseBodyData(TeaModel):
    def __init__(self, event_json=None, event_time=None, instance_id=None, instance_type=None,
                 monitor_source_id=None, monitor_source_name=None, route_rule_id=None, tenant_ram_id=None):
        # 告警内容json
        self.event_json = event_json  # type: str
        # 告警上报时间
        self.event_time = event_time  # type: str
        # 关联对象ID
        self.instance_id = instance_id  # type: long
        # INCIDENT 事件、ALERT 报警、PROBLEM 故障
        self.instance_type = instance_type  # type: str
        # 监控告警源ID
        self.monitor_source_id = monitor_source_id  # type: long
        # 监控告警源名称
        self.monitor_source_name = monitor_source_name  # type: str
        # 规则ID
        self.route_rule_id = route_rule_id  # type: long
        # 租户ID
        self.tenant_ram_id = tenant_ram_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSourceEventsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_json is not None:
            result['eventJson'] = self.event_json
        if self.event_time is not None:
            result['eventTime'] = self.event_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        if self.tenant_ram_id is not None:
            result['tenantRamId'] = self.tenant_ram_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eventJson') is not None:
            self.event_json = m.get('eventJson')
        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('tenantRamId') is not None:
            self.tenant_ram_id = m.get('tenantRamId')
        return self


class ListSourceEventsResponseBody(TeaModel):
    def __init__(self, data=None, first_row_key=None, last_row_key=None, page_number=None, page_size=None,
                 request_id=None, total_count=None):
        self.data = data  # type: list[ListSourceEventsResponseBodyData]
        # firstRowKey
        self.first_row_key = first_row_key  # type: str
        # lastRowKey
        self.last_row_key = last_row_key  # type: str
        # 当前页
        self.page_number = page_number  # type: long
        # 页大小
        self.page_size = page_size  # type: long
        # 请求ID
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSourceEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.first_row_key is not None:
            result['firstRowKey'] = self.first_row_key
        if self.last_row_key is not None:
            result['lastRowKey'] = self.last_row_key
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListSourceEventsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('firstRowKey') is not None:
            self.first_row_key = m.get('firstRowKey')
        if m.get('lastRowKey') is not None:
            self.last_row_key = m.get('lastRowKey')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListSourceEventsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSourceEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSourceEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSourceEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSourceEventsForMonitorSourceRequest(TeaModel):
    def __init__(self, monitor_source_id=None):
        # 监控源ID
        self.monitor_source_id = monitor_source_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSourceEventsForMonitorSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        return self


class ListSourceEventsForMonitorSourceResponseBodyData(TeaModel):
    def __init__(self, event_json=None, event_time=None, monitor_source_id=None, monitor_source_name=None):
        # 告警内容
        self.event_json = event_json  # type: str
        # 告警上报时间
        self.event_time = event_time  # type: str
        # 监控源ID
        self.monitor_source_id = monitor_source_id  # type: bool
        # 监控源名称
        self.monitor_source_name = monitor_source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSourceEventsForMonitorSourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_json is not None:
            result['eventJson'] = self.event_json
        if self.event_time is not None:
            result['eventTime'] = self.event_time
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eventJson') is not None:
            self.event_json = m.get('eventJson')
        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        return self


class ListSourceEventsForMonitorSourceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 告警列表
        self.data = data  # type: list[ListSourceEventsForMonitorSourceResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSourceEventsForMonitorSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListSourceEventsForMonitorSourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListSourceEventsForMonitorSourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSourceEventsForMonitorSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSourceEventsForMonitorSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSourceEventsForMonitorSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscriptionServiceGroupsRequest(TeaModel):
    def __init__(self, client_token=None, service_ids=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 服务列表
        self.service_ids = service_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionServiceGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_ids is not None:
            result['serviceIds'] = self.service_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceIds') is not None:
            self.service_ids = m.get('serviceIds')
        return self


class ListSubscriptionServiceGroupsResponseBodyData(TeaModel):
    def __init__(self, service_group_description=None, service_id=None, service_name=None):
        # 服务组描述
        self.service_group_description = service_group_description  # type: str
        # 主键
        self.service_id = service_id  # type: long
        # 服务组名称
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionServiceGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_group_description is not None:
            result['serviceGroupDescription'] = self.service_group_description
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceGroupDescription') is not None:
            self.service_group_description = m.get('serviceGroupDescription')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class ListSubscriptionServiceGroupsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[ListSubscriptionServiceGroupsResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubscriptionServiceGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListSubscriptionServiceGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListSubscriptionServiceGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSubscriptionServiceGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubscriptionServiceGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSubscriptionServiceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscriptionsRequest(TeaModel):
    def __init__(self, client_token=None, notify_object=None, notify_object_type=None, page_number=None,
                 page_size=None, scope=None, scope_object=None, subscription_title=None):
        # 幂等参数
        self.client_token = client_token  # type: str
        # 通知对象名
        self.notify_object = notify_object  # type: str
        # 通知对象类型notifyWhoType:0服务组 1个人
        self.notify_object_type = notify_object_type  # type: str
        # 第几页
        self.page_number = page_number  # type: int
        # 一页几条
        self.page_size = page_size  # type: int
        # 订阅范围类型 0全部1服务2流转规则
        self.scope = scope  # type: str
        # 订阅范围对象名称
        self.scope_object = scope_object  # type: str
        # 通知订阅名
        self.subscription_title = subscription_title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.notify_object is not None:
            result['notifyObject'] = self.notify_object
        if self.notify_object_type is not None:
            result['notifyObjectType'] = self.notify_object_type
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.scope is not None:
            result['scope'] = self.scope
        if self.scope_object is not None:
            result['scopeObject'] = self.scope_object
        if self.subscription_title is not None:
            result['subscriptionTitle'] = self.subscription_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('notifyObject') is not None:
            self.notify_object = m.get('notifyObject')
        if m.get('notifyObjectType') is not None:
            self.notify_object_type = m.get('notifyObjectType')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scopeObject') is not None:
            self.scope_object = m.get('scopeObject')
        if m.get('subscriptionTitle') is not None:
            self.subscription_title = m.get('subscriptionTitle')
        return self


class ListSubscriptionsResponseBodyDataNotifyObjectList(TeaModel):
    def __init__(self, id=None, name=None, notify_object_id=None, notify_object_type=None):
        # id主键
        self.id = id  # type: long
        # 通知对象名
        self.name = name  # type: str
        # 关联主键id
        self.notify_object_id = notify_object_id  # type: long
        # 通知对象类型0服务组 1个人
        self.notify_object_type = notify_object_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionsResponseBodyDataNotifyObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.notify_object_id is not None:
            result['notifyObjectId'] = self.notify_object_id
        if self.notify_object_type is not None:
            result['notifyObjectType'] = self.notify_object_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('notifyObjectId') is not None:
            self.notify_object_id = m.get('notifyObjectId')
        if m.get('notifyObjectType') is not None:
            self.notify_object_type = m.get('notifyObjectType')
        return self


class ListSubscriptionsResponseBodyDataScopeObjectList(TeaModel):
    def __init__(self, id=None, scope=None, scope_object=None, scope_object_id=None):
        # id主键
        self.id = id  # type: long
        # 订阅范围类型 ALL全部 SERVICE服务 ROUTETULE流转规则
        self.scope = scope  # type: long
        # 订阅范围对象名称
        self.scope_object = scope_object  # type: str
        # 订阅范围对象关联表主键id
        self.scope_object_id = scope_object_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSubscriptionsResponseBodyDataScopeObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.scope is not None:
            result['scope'] = self.scope
        if self.scope_object is not None:
            result['scopeObject'] = self.scope_object
        if self.scope_object_id is not None:
            result['scopeObjectId'] = self.scope_object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scopeObject') is not None:
            self.scope_object = m.get('scopeObject')
        if m.get('scopeObjectId') is not None:
            self.scope_object_id = m.get('scopeObjectId')
        return self


class ListSubscriptionsResponseBodyData(TeaModel):
    def __init__(self, end_time=None, expired_type=None, notify_object_list=None, notify_object_type=None,
                 scope=None, scope_object_list=None, start_time=None, status=None, subscription_id=None,
                 subscription_title=None):
        # 时效结束时间
        self.end_time = end_time  # type: str
        # 有效期类型 0 长期 1短期
        self.expired_type = expired_type  # type: str
        # 通知对象列表
        self.notify_object_list = notify_object_list  # type: list[ListSubscriptionsResponseBodyDataNotifyObjectList]
        # 0服务组 1个人
        self.notify_object_type = notify_object_type  # type: long
        # 0 全部 1服务 2 流转规则
        self.scope = scope  # type: long
        # 订阅范围列表
        self.scope_object_list = scope_object_list  # type: list[ListSubscriptionsResponseBodyDataScopeObjectList]
        # 时效开始时间
        self.start_time = start_time  # type: str
        # ENABLE 启用 DISABLE禁用
        self.status = status  # type: str
        # 订阅id
        self.subscription_id = subscription_id  # type: long
        # 通知订阅名称
        self.subscription_title = subscription_title  # type: str

    def validate(self):
        if self.notify_object_list:
            for k in self.notify_object_list:
                if k:
                    k.validate()
        if self.scope_object_list:
            for k in self.scope_object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubscriptionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.expired_type is not None:
            result['expiredType'] = self.expired_type
        result['notifyObjectList'] = []
        if self.notify_object_list is not None:
            for k in self.notify_object_list:
                result['notifyObjectList'].append(k.to_map() if k else None)
        if self.notify_object_type is not None:
            result['notifyObjectType'] = self.notify_object_type
        if self.scope is not None:
            result['scope'] = self.scope
        result['scopeObjectList'] = []
        if self.scope_object_list is not None:
            for k in self.scope_object_list:
                result['scopeObjectList'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        if self.subscription_title is not None:
            result['subscriptionTitle'] = self.subscription_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('expiredType') is not None:
            self.expired_type = m.get('expiredType')
        self.notify_object_list = []
        if m.get('notifyObjectList') is not None:
            for k in m.get('notifyObjectList'):
                temp_model = ListSubscriptionsResponseBodyDataNotifyObjectList()
                self.notify_object_list.append(temp_model.from_map(k))
        if m.get('notifyObjectType') is not None:
            self.notify_object_type = m.get('notifyObjectType')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        self.scope_object_list = []
        if m.get('scopeObjectList') is not None:
            for k in m.get('scopeObjectList'):
                temp_model = ListSubscriptionsResponseBodyDataScopeObjectList()
                self.scope_object_list.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        if m.get('subscriptionTitle') is not None:
            self.subscription_title = m.get('subscriptionTitle')
        return self


class ListSubscriptionsResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[ListSubscriptionsResponseBodyData]
        # 分页参数
        self.page_number = page_number  # type: long
        # 分页参数
        self.page_size = page_size  # type: long
        # id of the request
        self.request_id = request_id  # type: str
        # 分页参数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSubscriptionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListSubscriptionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListSubscriptionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListSubscriptionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSubscriptionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSubscriptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTrendForSourceEventRequest(TeaModel):
    def __init__(self, end_time=None, instance_id=None, instance_type=None, request_id=None, start_time=None,
                 time_unit=None):
        # 结束时间
        self.end_time = end_time  # type: str
        # 报警ID
        self.instance_id = instance_id  # type: long
        # 类型
        self.instance_type = instance_type  # type: str
        # 请求ID
        self.request_id = request_id  # type: str
        # 开始时间
        self.start_time = start_time  # type: str
        # 时间单位毫秒
        self.time_unit = time_unit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrendForSourceEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        return self


class ListTrendForSourceEventResponseBodyData(TeaModel):
    def __init__(self, convergence_rate=None, max_sustain_time=None, skip_day=None, source_events_stat_map=None,
                 unit=None):
        # 收敛率
        self.convergence_rate = convergence_rate  # type: str
        # 最大持续时长
        self.max_sustain_time = max_sustain_time  # type: long
        # 是否跨天
        self.skip_day = skip_day  # type: bool
        # 按监控源分组统计数据
        self.source_events_stat_map = source_events_stat_map  # type: dict[str, any]
        # 时间单位
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTrendForSourceEventResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.convergence_rate is not None:
            result['convergenceRate'] = self.convergence_rate
        if self.max_sustain_time is not None:
            result['maxSustainTime'] = self.max_sustain_time
        if self.skip_day is not None:
            result['skipDay'] = self.skip_day
        if self.source_events_stat_map is not None:
            result['sourceEventsStatMap'] = self.source_events_stat_map
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('convergenceRate') is not None:
            self.convergence_rate = m.get('convergenceRate')
        if m.get('maxSustainTime') is not None:
            self.max_sustain_time = m.get('maxSustainTime')
        if m.get('skipDay') is not None:
            self.skip_day = m.get('skipDay')
        if m.get('sourceEventsStatMap') is not None:
            self.source_events_stat_map = m.get('sourceEventsStatMap')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        return self


class ListTrendForSourceEventResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 统计列表
        self.data = data  # type: list[ListTrendForSourceEventResponseBodyData]
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTrendForSourceEventResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListTrendForSourceEventResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListTrendForSourceEventResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTrendForSourceEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTrendForSourceEventResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTrendForSourceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserSerivceGroupsRequest(TeaModel):
    def __init__(self, client_token=None, user_id=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 用户ID
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserSerivceGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class ListUserSerivceGroupsResponseBodyDataServiceGroups(TeaModel):
    def __init__(self, service_group_description=None, service_group_id=None, service_group_name=None):
        # 服务组描述
        self.service_group_description = service_group_description  # type: str
        # 服务组id
        self.service_group_id = service_group_id  # type: long
        # 服务组名称
        self.service_group_name = service_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserSerivceGroupsResponseBodyDataServiceGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_group_description is not None:
            result['serviceGroupDescription'] = self.service_group_description
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('serviceGroupDescription') is not None:
            self.service_group_description = m.get('serviceGroupDescription')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        return self


class ListUserSerivceGroupsResponseBodyData(TeaModel):
    def __init__(self, email=None, phone=None, ram_id=None, service_groups=None, user_id=None, username=None):
        # 邮箱
        self.email = email  # type: str
        # 手机号
        self.phone = phone  # type: str
        # RAM子账号ID
        self.ram_id = ram_id  # type: long
        # 人员所属服务组
        self.service_groups = service_groups  # type: list[ListUserSerivceGroupsResponseBodyDataServiceGroups]
        # 用户ID
        self.user_id = user_id  # type: long
        # 用户昵称
        self.username = username  # type: str

    def validate(self):
        if self.service_groups:
            for k in self.service_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserSerivceGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.phone is not None:
            result['phone'] = self.phone
        if self.ram_id is not None:
            result['ramId'] = self.ram_id
        result['serviceGroups'] = []
        if self.service_groups is not None:
            for k in self.service_groups:
                result['serviceGroups'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('ramId') is not None:
            self.ram_id = m.get('ramId')
        self.service_groups = []
        if m.get('serviceGroups') is not None:
            for k in m.get('serviceGroups'):
                temp_model = ListUserSerivceGroupsResponseBodyDataServiceGroups()
                self.service_groups.append(temp_model.from_map(k))
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListUserSerivceGroupsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListUserSerivceGroupsResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListUserSerivceGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListUserSerivceGroupsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUserSerivceGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserSerivceGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserSerivceGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserSerivceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, client_token=None, page_number=None, page_size=None, phone=None, ram_id=None, scene=None,
                 synergy_channel=None, username=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 分页参数
        self.page_number = page_number  # type: long
        # 分页参数
        self.page_size = page_size  # type: long
        # 人员手机号
        self.phone = phone  # type: str
        # ramID
        self.ram_id = ram_id  # type: str
        # USER_LIST列表 ALL_USERS下拉
        self.scene = scene  # type: long
        # 移动应用协同渠道
        self.synergy_channel = synergy_channel  # type: str
        # 人员名称
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.phone is not None:
            result['phone'] = self.phone
        if self.ram_id is not None:
            result['ramId'] = self.ram_id
        if self.scene is not None:
            result['scene'] = self.scene
        if self.synergy_channel is not None:
            result['synergyChannel'] = self.synergy_channel
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('ramId') is not None:
            self.ram_id = m.get('ramId')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('synergyChannel') is not None:
            self.synergy_channel = m.get('synergyChannel')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(self, account_type=None, app_account=None, email=None, is_editable_user=None, is_related=None,
                 phone=None, ram_id=None, synergy_channel=None, user_id=None, username=None):
        # 账户类型
        self.account_type = account_type  # type: long
        # 移动应用账户
        self.app_account = app_account  # type: str
        # 邮箱
        self.email = email  # type: str
        # 是否可编辑
        self.is_editable_user = is_editable_user  # type: long
        # 是否关联
        self.is_related = is_related  # type: str
        # 手机
        self.phone = phone  # type: str
        # 子账号ramId
        self.ram_id = ram_id  # type: long
        # 移动应用协同渠道
        self.synergy_channel = synergy_channel  # type: str
        # 用户id
        self.user_id = user_id  # type: long
        # 用户名
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.app_account is not None:
            result['appAccount'] = self.app_account
        if self.email is not None:
            result['email'] = self.email
        if self.is_editable_user is not None:
            result['isEditableUser'] = self.is_editable_user
        if self.is_related is not None:
            result['isRelated'] = self.is_related
        if self.phone is not None:
            result['phone'] = self.phone
        if self.ram_id is not None:
            result['ramId'] = self.ram_id
        if self.synergy_channel is not None:
            result['synergyChannel'] = self.synergy_channel
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('appAccount') is not None:
            self.app_account = m.get('appAccount')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('isEditableUser') is not None:
            self.is_editable_user = m.get('isEditableUser')
        if m.get('isRelated') is not None:
            self.is_related = m.get('isRelated')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('ramId') is not None:
            self.ram_id = m.get('ramId')
        if m.get('synergyChannel') is not None:
            self.synergy_channel = m.get('synergyChannel')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        # data
        self.data = data  # type: list[ListUsersResponseBodyData]
        # 分页
        self.page_number = page_number  # type: long
        # 分页
        self.page_size = page_size  # type: long
        # id of the request
        self.request_id = request_id  # type: str
        # 总条数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverProblemRequest(TeaModel):
    def __init__(self, problem_id=None, problem_notify_type=None, recovery_time=None):
        # 故障ID
        self.problem_id = problem_id  # type: long
        # 通告类型 PROBLEM_NOTIFY：故障通告 PROBLEM_UPDATE：故障更新 PROBLEM_UPGRADE：故障升级 PROBLEM_DEGRADE：故障降级 PROBLEM_RECOVER：故障恢复 PROBLEM_REISSUE： 故障补发 PROBLEM_CANCEL：故障取消
        self.problem_notify_type = problem_notify_type  # type: str
        # 恢复时间
        self.recovery_time = recovery_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoverProblemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_notify_type is not None:
            result['problemNotifyType'] = self.problem_notify_type
        if self.recovery_time is not None:
            result['recoveryTime'] = self.recovery_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemNotifyType') is not None:
            self.problem_notify_type = m.get('problemNotifyType')
        if m.get('recoveryTime') is not None:
            self.recovery_time = m.get('recoveryTime')
        return self


class RecoverProblemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecoverProblemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RecoverProblemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecoverProblemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecoverProblemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RecoverProblemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshIntegrationConfigKeyRequest(TeaModel):
    def __init__(self, client_token=None, integration_config_id=None):
        # 幂等id
        self.client_token = client_token  # type: str
        self.integration_config_id = integration_config_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshIntegrationConfigKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        return self


class RefreshIntegrationConfigKeyResponseBodyData(TeaModel):
    def __init__(self, key=None):
        # 集成秘钥
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshIntegrationConfigKeyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class RefreshIntegrationConfigKeyResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: RefreshIntegrationConfigKeyResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RefreshIntegrationConfigKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = RefreshIntegrationConfigKeyResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RefreshIntegrationConfigKeyResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefreshIntegrationConfigKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshIntegrationConfigKeyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshIntegrationConfigKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveProblemServiceGroupRequest(TeaModel):
    def __init__(self, problem_id=None, service_group_ids=None):
        # 故障ID
        self.problem_id = problem_id  # type: long
        # 应急协同组
        self.service_group_ids = service_group_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveProblemServiceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.service_group_ids is not None:
            result['serviceGroupIds'] = self.service_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('serviceGroupIds') is not None:
            self.service_group_ids = m.get('serviceGroupIds')
        return self


class RemoveProblemServiceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveProblemServiceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RemoveProblemServiceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveProblemServiceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveProblemServiceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveProblemServiceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplayProblemRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None, replay_duty_user_id=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 故障ID
        self.problem_id = problem_id  # type: long
        # 复盘负责人ID
        self.replay_duty_user_id = replay_duty_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplayProblemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.replay_duty_user_id is not None:
            result['replayDutyUserId'] = self.replay_duty_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('replayDutyUserId') is not None:
            self.replay_duty_user_id = m.get('replayDutyUserId')
        return self


class ReplayProblemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplayProblemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ReplayProblemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReplayProblemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReplayProblemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReplayProblemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RespondIncidentRequest(TeaModel):
    def __init__(self, client_token=None, incident_ids=None):
        # 幂等校验Id
        self.client_token = client_token  # type: str
        # 事件ID数组
        self.incident_ids = incident_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RespondIncidentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.incident_ids is not None:
            result['incidentIds'] = self.incident_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('incidentIds') is not None:
            self.incident_ids = m.get('incidentIds')
        return self


class RespondIncidentResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RespondIncidentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RespondIncidentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RespondIncidentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RespondIncidentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RespondIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeProblemRecoveryRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None, problem_notify_type=None):
        # 幂等校验Id
        self.client_token = client_token  # type: str
        # 故障ID
        self.problem_id = problem_id  # type: long
        # 通告类型 PROBLEM_NOTIFY：故障通告 PROBLEM_UPDATE：故障更新 PROBLEM_UPGRADE：故障升级 PROBLEM_DEGRADE：故障降级 PROBLEM_RECOVER：故障恢复 PROBLEM_REISSUE： 故障补发 PROBLEM_CANCEL：故障取消
        self.problem_notify_type = problem_notify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeProblemRecoveryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_notify_type is not None:
            result['problemNotifyType'] = self.problem_notify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemNotifyType') is not None:
            self.problem_notify_type = m.get('problemNotifyType')
        return self


class RevokeProblemRecoveryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeProblemRecoveryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RevokeProblemRecoveryResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RevokeProblemRecoveryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeProblemRecoveryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RevokeProblemRecoveryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEscalationPlanRequestEscalationPlanRulesEscalationPlanConditions(TeaModel):
    def __init__(self, effection=None, level=None):
        # LOW HIGH
        self.effection = effection  # type: str
        # P1 P2 P3 P4
        self.level = level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEscalationPlanRequestEscalationPlanRulesEscalationPlanConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effection is not None:
            result['effection'] = self.effection
        if self.level is not None:
            result['level'] = self.level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('level') is not None:
            self.level = m.get('level')
        return self


class UpdateEscalationPlanRequestEscalationPlanRulesEscalationPlanStrategies(TeaModel):
    def __init__(self, enable_webhook=None, notice_channels=None, notice_objects=None, notice_time=None,
                 service_group_ids=None):
        # 是否支持群通知
        self.enable_webhook = enable_webhook  # type: bool
        # 通知渠道
        self.notice_channels = notice_channels  # type: list[str]
        # 通知对象id
        self.notice_objects = notice_objects  # type: list[long]
        # 通知时间
        self.notice_time = notice_time  # type: long
        # 服务组id
        self.service_group_ids = service_group_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEscalationPlanRequestEscalationPlanRulesEscalationPlanStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_webhook is not None:
            result['enableWebhook'] = self.enable_webhook
        if self.notice_channels is not None:
            result['noticeChannels'] = self.notice_channels
        if self.notice_objects is not None:
            result['noticeObjects'] = self.notice_objects
        if self.notice_time is not None:
            result['noticeTime'] = self.notice_time
        if self.service_group_ids is not None:
            result['serviceGroupIds'] = self.service_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('enableWebhook') is not None:
            self.enable_webhook = m.get('enableWebhook')
        if m.get('noticeChannels') is not None:
            self.notice_channels = m.get('noticeChannels')
        if m.get('noticeObjects') is not None:
            self.notice_objects = m.get('noticeObjects')
        if m.get('noticeTime') is not None:
            self.notice_time = m.get('noticeTime')
        if m.get('serviceGroupIds') is not None:
            self.service_group_ids = m.get('serviceGroupIds')
        return self


class UpdateEscalationPlanRequestEscalationPlanRules(TeaModel):
    def __init__(self, escalation_plan_conditions=None, escalation_plan_strategies=None,
                 escalation_plan_type=None, id=None):
        # 升级计划条件列表
        self.escalation_plan_conditions = escalation_plan_conditions  # type: list[UpdateEscalationPlanRequestEscalationPlanRulesEscalationPlanConditions]
        # 升级策略列表
        self.escalation_plan_strategies = escalation_plan_strategies  # type: list[UpdateEscalationPlanRequestEscalationPlanRulesEscalationPlanStrategies]
        # UN_ACKNOWLEDGE 未响应 UN_FINISH 未完结
        self.escalation_plan_type = escalation_plan_type  # type: str
        # 主键
        self.id = id  # type: long

    def validate(self):
        if self.escalation_plan_conditions:
            for k in self.escalation_plan_conditions:
                if k:
                    k.validate()
        if self.escalation_plan_strategies:
            for k in self.escalation_plan_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEscalationPlanRequestEscalationPlanRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['escalationPlanConditions'] = []
        if self.escalation_plan_conditions is not None:
            for k in self.escalation_plan_conditions:
                result['escalationPlanConditions'].append(k.to_map() if k else None)
        result['escalationPlanStrategies'] = []
        if self.escalation_plan_strategies is not None:
            for k in self.escalation_plan_strategies:
                result['escalationPlanStrategies'].append(k.to_map() if k else None)
        if self.escalation_plan_type is not None:
            result['escalationPlanType'] = self.escalation_plan_type
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.escalation_plan_conditions = []
        if m.get('escalationPlanConditions') is not None:
            for k in m.get('escalationPlanConditions'):
                temp_model = UpdateEscalationPlanRequestEscalationPlanRulesEscalationPlanConditions()
                self.escalation_plan_conditions.append(temp_model.from_map(k))
        self.escalation_plan_strategies = []
        if m.get('escalationPlanStrategies') is not None:
            for k in m.get('escalationPlanStrategies'):
                temp_model = UpdateEscalationPlanRequestEscalationPlanRulesEscalationPlanStrategies()
                self.escalation_plan_strategies.append(temp_model.from_map(k))
        if m.get('escalationPlanType') is not None:
            self.escalation_plan_type = m.get('escalationPlanType')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class UpdateEscalationPlanRequestEscalationPlanScopeObjects(TeaModel):
    def __init__(self, id=None, scope=None, scope_object_id=None):
        # 主键
        self.id = id  # type: long
        # 范围对象类型
        self.scope = scope  # type: str
        # 范围对象id
        self.scope_object_id = scope_object_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEscalationPlanRequestEscalationPlanScopeObjects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.scope is not None:
            result['scope'] = self.scope
        if self.scope_object_id is not None:
            result['scopeObjectId'] = self.scope_object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('scopeObjectId') is not None:
            self.scope_object_id = m.get('scopeObjectId')
        return self


class UpdateEscalationPlanRequest(TeaModel):
    def __init__(self, client_token=None, escalation_plan_description=None, escalation_plan_id=None,
                 escalation_plan_name=None, escalation_plan_rules=None, escalation_plan_scope_objects=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 升级计划描述
        self.escalation_plan_description = escalation_plan_description  # type: str
        # 升级计划id
        self.escalation_plan_id = escalation_plan_id  # type: long
        # 升级计划名称
        self.escalation_plan_name = escalation_plan_name  # type: str
        # 升级计划规则
        self.escalation_plan_rules = escalation_plan_rules  # type: list[UpdateEscalationPlanRequestEscalationPlanRules]
        # 关联范围列表（服务）
        self.escalation_plan_scope_objects = escalation_plan_scope_objects  # type: list[UpdateEscalationPlanRequestEscalationPlanScopeObjects]

    def validate(self):
        if self.escalation_plan_rules:
            for k in self.escalation_plan_rules:
                if k:
                    k.validate()
        if self.escalation_plan_scope_objects:
            for k in self.escalation_plan_scope_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEscalationPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.escalation_plan_description is not None:
            result['escalationPlanDescription'] = self.escalation_plan_description
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        if self.escalation_plan_name is not None:
            result['escalationPlanName'] = self.escalation_plan_name
        result['escalationPlanRules'] = []
        if self.escalation_plan_rules is not None:
            for k in self.escalation_plan_rules:
                result['escalationPlanRules'].append(k.to_map() if k else None)
        result['escalationPlanScopeObjects'] = []
        if self.escalation_plan_scope_objects is not None:
            for k in self.escalation_plan_scope_objects:
                result['escalationPlanScopeObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('escalationPlanDescription') is not None:
            self.escalation_plan_description = m.get('escalationPlanDescription')
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        if m.get('escalationPlanName') is not None:
            self.escalation_plan_name = m.get('escalationPlanName')
        self.escalation_plan_rules = []
        if m.get('escalationPlanRules') is not None:
            for k in m.get('escalationPlanRules'):
                temp_model = UpdateEscalationPlanRequestEscalationPlanRules()
                self.escalation_plan_rules.append(temp_model.from_map(k))
        self.escalation_plan_scope_objects = []
        if m.get('escalationPlanScopeObjects') is not None:
            for k in m.get('escalationPlanScopeObjects'):
                temp_model = UpdateEscalationPlanRequestEscalationPlanScopeObjects()
                self.escalation_plan_scope_objects.append(temp_model.from_map(k))
        return self


class UpdateEscalationPlanResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEscalationPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateEscalationPlanResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateEscalationPlanResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEscalationPlanResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEscalationPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIncidentRequest(TeaModel):
    def __init__(self, client_token=None, effect=None, incident_id=None, incident_level=None, incident_title=None):
        # 幂等校验Id
        self.client_token = client_token  # type: str
        # 影响程度
        self.effect = effect  # type: str
        # 事件Id
        self.incident_id = incident_id  # type: long
        # 级别
        self.incident_level = incident_level  # type: str
        # 事件标题
        self.incident_title = incident_title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIncidentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.effect is not None:
            result['effect'] = self.effect
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_level is not None:
            result['incidentLevel'] = self.incident_level
        if self.incident_title is not None:
            result['incidentTitle'] = self.incident_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentLevel') is not None:
            self.incident_level = m.get('incidentLevel')
        if m.get('incidentTitle') is not None:
            self.incident_title = m.get('incidentTitle')
        return self


class UpdateIncidentResponseBodyData(TeaModel):
    def __init__(self, incident_id=None):
        # 事件id
        self.incident_id = incident_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIncidentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        return self


class UpdateIncidentResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: UpdateIncidentResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateIncidentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UpdateIncidentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateIncidentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIncidentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIncidentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIntegrationConfigRequest(TeaModel):
    def __init__(self, access_key=None, client_token=None, integration_config_id=None):
        # 集成秘钥
        self.access_key = access_key  # type: str
        # 幂等id
        self.client_token = client_token  # type: str
        self.integration_config_id = integration_config_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIntegrationConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.integration_config_id is not None:
            result['integrationConfigId'] = self.integration_config_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('integrationConfigId') is not None:
            self.integration_config_id = m.get('integrationConfigId')
        return self


class UpdateIntegrationConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIntegrationConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateIntegrationConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIntegrationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIntegrationConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateIntegrationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProblemRequest(TeaModel):
    def __init__(self, feedback=None, level=None, main_handler_id=None, preliminary_reason=None, problem_id=None,
                 problem_name=None, progress_summary=None, progress_summary_rich_text_id=None, related_service_id=None,
                 service_group_ids=None):
        # 舆情反馈
        self.feedback = feedback  # type: str
        # 故障等级
        self.level = level  # type: str
        # 主要处理人
        self.main_handler_id = main_handler_id  # type: long
        # 初步原因
        self.preliminary_reason = preliminary_reason  # type: str
        # 故障ID
        self.problem_id = problem_id  # type: long
        # 故障名
        self.problem_name = problem_name  # type: str
        # 进展摘要
        self.progress_summary = progress_summary  # type: str
        # 进展摘要富文本id
        self.progress_summary_rich_text_id = progress_summary_rich_text_id  # type: long
        # 所属服务
        self.related_service_id = related_service_id  # type: long
        # 应急协同组
        self.service_group_ids = service_group_ids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['feedback'] = self.feedback
        if self.level is not None:
            result['level'] = self.level
        if self.main_handler_id is not None:
            result['mainHandlerId'] = self.main_handler_id
        if self.preliminary_reason is not None:
            result['preliminaryReason'] = self.preliminary_reason
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_name is not None:
            result['problemName'] = self.problem_name
        if self.progress_summary is not None:
            result['progressSummary'] = self.progress_summary
        if self.progress_summary_rich_text_id is not None:
            result['progressSummaryRichTextId'] = self.progress_summary_rich_text_id
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        if self.service_group_ids is not None:
            result['serviceGroupIds'] = self.service_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('feedback') is not None:
            self.feedback = m.get('feedback')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('mainHandlerId') is not None:
            self.main_handler_id = m.get('mainHandlerId')
        if m.get('preliminaryReason') is not None:
            self.preliminary_reason = m.get('preliminaryReason')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemName') is not None:
            self.problem_name = m.get('problemName')
        if m.get('progressSummary') is not None:
            self.progress_summary = m.get('progressSummary')
        if m.get('progressSummaryRichTextId') is not None:
            self.progress_summary_rich_text_id = m.get('progressSummaryRichTextId')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        if m.get('serviceGroupIds') is not None:
            self.service_group_ids = m.get('serviceGroupIds')
        return self


class UpdateProblemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProblemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProblemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProblemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProblemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProblemEffectionServiceRequest(TeaModel):
    def __init__(self, client_token=None, description=None, effection_service_id=None, level=None, pic_url=None,
                 problem_id=None, service_id=None, status=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 影响描述
        self.description = description  # type: str
        # 影响服务id
        self.effection_service_id = effection_service_id  # type: long
        # 影响等级
        self.level = level  # type: str
        # 图片地址
        self.pic_url = pic_url  # type: list[str]
        # 故障id
        self.problem_id = problem_id  # type: long
        # 关联服务id
        self.service_id = service_id  # type: long
        # 影响状态 UN_RECOVERED 未恢复 RECOVERED已恢复
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemEffectionServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.effection_service_id is not None:
            result['effectionServiceId'] = self.effection_service_id
        if self.level is not None:
            result['level'] = self.level
        if self.pic_url is not None:
            result['picUrl'] = self.pic_url
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('effectionServiceId') is not None:
            self.effection_service_id = m.get('effectionServiceId')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('picUrl') is not None:
            self.pic_url = m.get('picUrl')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateProblemEffectionServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # requestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemEffectionServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProblemEffectionServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProblemEffectionServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProblemEffectionServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProblemEffectionServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProblemImprovementRequest(TeaModel):
    def __init__(self, client_token=None, discover_source=None, duty_department_id=None, duty_department_name=None,
                 duty_user_id=None, injection_mode=None, monitor_source_name=None, problem_id=None, problem_reason=None,
                 recent_activity=None, recovery_mode=None, relation_changes=None, remark=None, replay_duty_user_id=None,
                 user_report=None):
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 发现来源 码表:PROBLEM_DISCOVER_SOURCE
        self.discover_source = discover_source  # type: long
        # 故障责任部门ID
        self.duty_department_id = duty_department_id  # type: long
        # 故障责任部门
        self.duty_department_name = duty_department_name  # type: str
        # 故障责任人id
        self.duty_user_id = duty_user_id  # type: long
        # 注入方式 码表:PROBLEM_INJECTION_MODE
        self.injection_mode = injection_mode  # type: str
        # 监控源
        self.monitor_source_name = monitor_source_name  # type: str
        # 故障ID
        self.problem_id = problem_id  # type: long
        # 故障原因
        self.problem_reason = problem_reason  # type: str
        # 最近活动 码表:PROBLEM_RECENT_ACTIVITY
        self.recent_activity = recent_activity  # type: str
        # 恢复方式  码表:PROBLEM_RECOVERY_MODE
        self.recovery_mode = recovery_mode  # type: str
        # 关联变更
        self.relation_changes = relation_changes  # type: str
        # 备注
        self.remark = remark  # type: str
        # 复盘负责人id
        self.replay_duty_user_id = replay_duty_user_id  # type: long
        # 用户上报 码表:PROBLEM_USER_REPORT
        self.user_report = user_report  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemImprovementRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.discover_source is not None:
            result['discoverSource'] = self.discover_source
        if self.duty_department_id is not None:
            result['dutyDepartmentId'] = self.duty_department_id
        if self.duty_department_name is not None:
            result['dutyDepartmentName'] = self.duty_department_name
        if self.duty_user_id is not None:
            result['dutyUserId'] = self.duty_user_id
        if self.injection_mode is not None:
            result['injectionMode'] = self.injection_mode
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_reason is not None:
            result['problemReason'] = self.problem_reason
        if self.recent_activity is not None:
            result['recentActivity'] = self.recent_activity
        if self.recovery_mode is not None:
            result['recoveryMode'] = self.recovery_mode
        if self.relation_changes is not None:
            result['relationChanges'] = self.relation_changes
        if self.remark is not None:
            result['remark'] = self.remark
        if self.replay_duty_user_id is not None:
            result['replayDutyUserId'] = self.replay_duty_user_id
        if self.user_report is not None:
            result['userReport'] = self.user_report
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('discoverSource') is not None:
            self.discover_source = m.get('discoverSource')
        if m.get('dutyDepartmentId') is not None:
            self.duty_department_id = m.get('dutyDepartmentId')
        if m.get('dutyDepartmentName') is not None:
            self.duty_department_name = m.get('dutyDepartmentName')
        if m.get('dutyUserId') is not None:
            self.duty_user_id = m.get('dutyUserId')
        if m.get('injectionMode') is not None:
            self.injection_mode = m.get('injectionMode')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemReason') is not None:
            self.problem_reason = m.get('problemReason')
        if m.get('recentActivity') is not None:
            self.recent_activity = m.get('recentActivity')
        if m.get('recoveryMode') is not None:
            self.recovery_mode = m.get('recoveryMode')
        if m.get('relationChanges') is not None:
            self.relation_changes = m.get('relationChanges')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('replayDutyUserId') is not None:
            self.replay_duty_user_id = m.get('replayDutyUserId')
        if m.get('userReport') is not None:
            self.user_report = m.get('userReport')
        return self


class UpdateProblemImprovementResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemImprovementResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProblemImprovementResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProblemImprovementResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProblemImprovementResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProblemImprovementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProblemMeasureRequest(TeaModel):
    def __init__(self, check_standard=None, check_user_id=None, client_token=None, content=None, director_id=None,
                 measure_id=None, plan_finish_time=None, problem_id=None, stalker_id=None, status=None, type=None):
        # 验收标准
        self.check_standard = check_standard  # type: str
        # 验收人id
        self.check_user_id = check_user_id  # type: long
        # 幂等校验token
        self.client_token = client_token  # type: str
        # 措施内容
        self.content = content  # type: str
        # 负责人id
        self.director_id = director_id  # type: long
        # 措施Id
        self.measure_id = measure_id  # type: long
        # 计划完成时间
        self.plan_finish_time = plan_finish_time  # type: str
        # 故障Id
        self.problem_id = problem_id  # type: long
        # 跟踪人id
        self.stalker_id = stalker_id  # type: long
        # 状态 IMPROVED 改进 2 未改进UNIMPROVED
        self.status = status  # type: str
        # 措施类型 码表 PROBLEM_REPLAY_IMPROVEMENT
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemMeasureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_standard is not None:
            result['checkStandard'] = self.check_standard
        if self.check_user_id is not None:
            result['checkUserId'] = self.check_user_id
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.content is not None:
            result['content'] = self.content
        if self.director_id is not None:
            result['directorId'] = self.director_id
        if self.measure_id is not None:
            result['measureId'] = self.measure_id
        if self.plan_finish_time is not None:
            result['planFinishTime'] = self.plan_finish_time
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.stalker_id is not None:
            result['stalkerId'] = self.stalker_id
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('checkStandard') is not None:
            self.check_standard = m.get('checkStandard')
        if m.get('checkUserId') is not None:
            self.check_user_id = m.get('checkUserId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('directorId') is not None:
            self.director_id = m.get('directorId')
        if m.get('measureId') is not None:
            self.measure_id = m.get('measureId')
        if m.get('planFinishTime') is not None:
            self.plan_finish_time = m.get('planFinishTime')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('stalkerId') is not None:
            self.stalker_id = m.get('stalkerId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateProblemMeasureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemMeasureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProblemMeasureResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProblemMeasureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProblemMeasureResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProblemMeasureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProblemNoticeRequest(TeaModel):
    def __init__(self, client_token=None, problem_id=None, problem_notify_type=None):
        # 幂等校验Id
        self.client_token = client_token  # type: str
        # 故障Id
        self.problem_id = problem_id  # type: long
        # 通告类型 PROBLEM_NOTIFY：故障通告 PROBLEM_UPDATE：故障更新 PROBLEM_UPGRADE：故障升级 PROBLEM_DEGRADE：故障降级 PROBLEM_RECOVER：故障恢复 PROBLEM_REISSUE： 故障补发 PROBLEM_CANCEL：故障取消
        self.problem_notify_type = problem_notify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemNoticeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_notify_type is not None:
            result['problemNotifyType'] = self.problem_notify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemNotifyType') is not None:
            self.problem_notify_type = m.get('problemNotifyType')
        return self


class UpdateProblemNoticeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemNoticeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProblemNoticeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProblemNoticeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProblemNoticeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProblemNoticeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProblemTimelineRequest(TeaModel):
    def __init__(self, client_token=None, content=None, key_node=None, problem_id=None, problem_timeline_id=None,
                 time=None):
        # clientToken
        self.client_token = client_token  # type: str
        # 节点内容
        self.content = content  # type: str
        # 关键节点 码表:PROBLEM_KEY_NODE (逗号分隔)
        self.key_node = key_node  # type: str
        # 故障id
        self.problem_id = problem_id  # type: long
        # 时间节点id
        self.problem_timeline_id = problem_timeline_id  # type: long
        # 发生时间
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemTimelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.content is not None:
            result['content'] = self.content
        if self.key_node is not None:
            result['keyNode'] = self.key_node
        if self.problem_id is not None:
            result['problemId'] = self.problem_id
        if self.problem_timeline_id is not None:
            result['problemTimelineId'] = self.problem_timeline_id
        if self.time is not None:
            result['time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('keyNode') is not None:
            self.key_node = m.get('keyNode')
        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')
        if m.get('problemTimelineId') is not None:
            self.problem_timeline_id = m.get('problemTimelineId')
        if m.get('time') is not None:
            self.time = m.get('time')
        return self


class UpdateProblemTimelineResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProblemTimelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProblemTimelineResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProblemTimelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProblemTimelineResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProblemTimelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRichTextRequest(TeaModel):
    def __init__(self, instance_id=None, instance_type=None, rich_text=None, rich_text_id=None):
        # 资源id
        self.instance_id = instance_id  # type: long
        # 资源类型
        self.instance_type = instance_type  # type: str
        # 文本内容
        self.rich_text = rich_text  # type: str
        # 富文本id
        self.rich_text_id = rich_text_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRichTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.rich_text is not None:
            result['richText'] = self.rich_text
        if self.rich_text_id is not None:
            result['richTextId'] = self.rich_text_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('richText') is not None:
            self.rich_text = m.get('richText')
        if m.get('richTextId') is not None:
            self.rich_text_id = m.get('richTextId')
        return self


class UpdateRichTextResponseBodyData(TeaModel):
    def __init__(self, id=None):
        # 富文本id
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRichTextResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class UpdateRichTextResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # data
        self.data = data  # type: UpdateRichTextResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateRichTextResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UpdateRichTextResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateRichTextResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateRichTextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRichTextResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRichTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRouteRuleRequestRouteChildRulesConditions(TeaModel):
    def __init__(self, key=None, operation_symbol=None, value=None):
        # 字段
        self.key = key  # type: str
        # 操作符
        self.operation_symbol = operation_symbol  # type: str
        # 字段取值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRouteRuleRequestRouteChildRulesConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operation_symbol is not None:
            result['operationSymbol'] = self.operation_symbol
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operationSymbol') is not None:
            self.operation_symbol = m.get('operationSymbol')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateRouteRuleRequestRouteChildRules(TeaModel):
    def __init__(self, child_condition_relation=None, child_route_rule_id=None, conditions=None,
                 is_valid_child_rule=None, monitor_source_id=None):
        # 子条件计算关系
        self.child_condition_relation = child_condition_relation  # type: long
        # 子规则ID 不填表示新增
        self.child_route_rule_id = child_route_rule_id  # type: long
        # 条件
        self.conditions = conditions  # type: list[UpdateRouteRuleRequestRouteChildRulesConditions]
        # true  删除子规则  false编辑子规则
        self.is_valid_child_rule = is_valid_child_rule  # type: bool
        # 监控源ID
        self.monitor_source_id = monitor_source_id  # type: long

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateRouteRuleRequestRouteChildRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_condition_relation is not None:
            result['childConditionRelation'] = self.child_condition_relation
        if self.child_route_rule_id is not None:
            result['childRouteRuleId'] = self.child_route_rule_id
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        if self.is_valid_child_rule is not None:
            result['isValidChildRule'] = self.is_valid_child_rule
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('childConditionRelation') is not None:
            self.child_condition_relation = m.get('childConditionRelation')
        if m.get('childRouteRuleId') is not None:
            self.child_route_rule_id = m.get('childRouteRuleId')
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = UpdateRouteRuleRequestRouteChildRulesConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('isValidChildRule') is not None:
            self.is_valid_child_rule = m.get('isValidChildRule')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        return self


class UpdateRouteRuleRequest(TeaModel):
    def __init__(self, assign_object_id=None, assign_object_type=None, child_rule_relation=None, client_token=None,
                 effection=None, incident_level=None, match_count=None, notify_channels=None, related_service_id=None,
                 route_child_rules=None, route_rule_id=None, route_type=None, rule_name=None, time_window=None, time_window_unit=None):
        # 事件分派对象ID（服务组ID 或用户ID）
        self.assign_object_id = assign_object_id  # type: long
        # 事件分派对象类型 SERVICEGROUP服务组  USER 单个用户
        self.assign_object_type = assign_object_type  # type: str
        # AND
        self.child_rule_relation = child_rule_relation  # type: str
        # 幂等号
        self.client_token = client_token  # type: str
        # 影响程度 LOW-一般 HIGH-严重
        self.effection = effection  # type: str
        # 事件级别 1-P1 2-P2 3-P3 4-P4
        self.incident_level = incident_level  # type: str
        # 命中次数
        self.match_count = match_count  # type: long
        # 通知渠道    SMS 短信  EMAIL  邮件  PHONE  电话  WEIXIN_GROUP 企微群 DING_GROUP 钉钉群
        self.notify_channels = notify_channels  # type: list[str]
        # 关联服务ID
        self.related_service_id = related_service_id  # type: long
        # 子规则
        self.route_child_rules = route_child_rules  # type: list[UpdateRouteRuleRequestRouteChildRules]
        # 规则ID
        self.route_rule_id = route_rule_id  # type: long
        # 路由类型：INCIDENT 触发事件 ALERT 仅触发报警
        self.route_type = route_type  # type: str
        # 规则名称
        self.rule_name = rule_name  # type: str
        # 时间窗口
        self.time_window = time_window  # type: int
        # 时间窗口单位 MINUTE 分钟  SECOND 秒
        self.time_window_unit = time_window_unit  # type: str

    def validate(self):
        if self.route_child_rules:
            for k in self.route_child_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateRouteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_object_id is not None:
            result['assignObjectId'] = self.assign_object_id
        if self.assign_object_type is not None:
            result['assignObjectType'] = self.assign_object_type
        if self.child_rule_relation is not None:
            result['childRuleRelation'] = self.child_rule_relation
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.effection is not None:
            result['effection'] = self.effection
        if self.incident_level is not None:
            result['incidentLevel'] = self.incident_level
        if self.match_count is not None:
            result['matchCount'] = self.match_count
        if self.notify_channels is not None:
            result['notifyChannels'] = self.notify_channels
        if self.related_service_id is not None:
            result['relatedServiceId'] = self.related_service_id
        result['routeChildRules'] = []
        if self.route_child_rules is not None:
            for k in self.route_child_rules:
                result['routeChildRules'].append(k.to_map() if k else None)
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        if self.route_type is not None:
            result['routeType'] = self.route_type
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.time_window is not None:
            result['timeWindow'] = self.time_window
        if self.time_window_unit is not None:
            result['timeWindowUnit'] = self.time_window_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('assignObjectId') is not None:
            self.assign_object_id = m.get('assignObjectId')
        if m.get('assignObjectType') is not None:
            self.assign_object_type = m.get('assignObjectType')
        if m.get('childRuleRelation') is not None:
            self.child_rule_relation = m.get('childRuleRelation')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('incidentLevel') is not None:
            self.incident_level = m.get('incidentLevel')
        if m.get('matchCount') is not None:
            self.match_count = m.get('matchCount')
        if m.get('notifyChannels') is not None:
            self.notify_channels = m.get('notifyChannels')
        if m.get('relatedServiceId') is not None:
            self.related_service_id = m.get('relatedServiceId')
        self.route_child_rules = []
        if m.get('routeChildRules') is not None:
            for k in m.get('routeChildRules'):
                temp_model = UpdateRouteRuleRequestRouteChildRules()
                self.route_child_rules.append(temp_model.from_map(k))
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('timeWindow') is not None:
            self.time_window = m.get('timeWindow')
        if m.get('timeWindowUnit') is not None:
            self.time_window_unit = m.get('timeWindowUnit')
        return self


class UpdateRouteRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: long
        # 请求ID
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRouteRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateRouteRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateRouteRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRouteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(self, client_token=None, service_description=None, service_id=None, service_name=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 服务描述
        self.service_description = service_description  # type: str
        # 服务ID
        self.service_id = service_id  # type: long
        # 服务名字
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.service_description is not None:
            result['serviceDescription'] = self.service_description
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('serviceDescription') is not None:
            self.service_description = m.get('serviceDescription')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: long
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceGroupRequestMonitorSourceTemplates(TeaModel):
    def __init__(self, monitor_source_id=None, monitor_source_name=None, template_content=None, template_id=None):
        # 监控报警源Id
        self.monitor_source_id = monitor_source_id  # type: long
        # 监控报警源
        self.monitor_source_name = monitor_source_name  # type: str
        # 消息模版内容
        self.template_content = template_content  # type: str
        # 消息模版ID
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceGroupRequestMonitorSourceTemplates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        if self.template_content is not None:
            result['templateContent'] = self.template_content
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        if m.get('templateContent') is not None:
            self.template_content = m.get('templateContent')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class UpdateServiceGroupRequest(TeaModel):
    def __init__(self, client_token=None, enable_webhook=None, monitor_source_templates=None,
                 service_group_description=None, service_group_id=None, service_group_name=None, user_ids=None, webhook_link=None,
                 webhook_type=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # ENABLE 启用 DISABLE 禁用
        self.enable_webhook = enable_webhook  # type: str
        # 监控源模版列表
        self.monitor_source_templates = monitor_source_templates  # type: list[UpdateServiceGroupRequestMonitorSourceTemplates]
        # 服务描述
        self.service_group_description = service_group_description  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long
        # 服务组名字
        self.service_group_name = service_group_name  # type: str
        # 用户ID列表修改后的
        self.user_ids = user_ids  # type: list[long]
        # webhook跳转地址
        self.webhook_link = webhook_link  # type: str
        # WEIXIN_GROUP微信DING_GROUP钉钉FEISHU_GROUP飞书
        self.webhook_type = webhook_type  # type: str

    def validate(self):
        if self.monitor_source_templates:
            for k in self.monitor_source_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateServiceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.enable_webhook is not None:
            result['enableWebhook'] = self.enable_webhook
        result['monitorSourceTemplates'] = []
        if self.monitor_source_templates is not None:
            for k in self.monitor_source_templates:
                result['monitorSourceTemplates'].append(k.to_map() if k else None)
        if self.service_group_description is not None:
            result['serviceGroupDescription'] = self.service_group_description
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        if self.service_group_name is not None:
            result['serviceGroupName'] = self.service_group_name
        if self.user_ids is not None:
            result['userIds'] = self.user_ids
        if self.webhook_link is not None:
            result['webhookLink'] = self.webhook_link
        if self.webhook_type is not None:
            result['webhookType'] = self.webhook_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('enableWebhook') is not None:
            self.enable_webhook = m.get('enableWebhook')
        self.monitor_source_templates = []
        if m.get('monitorSourceTemplates') is not None:
            for k in m.get('monitorSourceTemplates'):
                temp_model = UpdateServiceGroupRequestMonitorSourceTemplates()
                self.monitor_source_templates.append(temp_model.from_map(k))
        if m.get('serviceGroupDescription') is not None:
            self.service_group_description = m.get('serviceGroupDescription')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        if m.get('serviceGroupName') is not None:
            self.service_group_name = m.get('serviceGroupName')
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        if m.get('webhookLink') is not None:
            self.webhook_link = m.get('webhookLink')
        if m.get('webhookType') is not None:
            self.webhook_type = m.get('webhookType')
        return self


class UpdateServiceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateServiceGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateServiceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceGroupSchedulingRequestFastSchedulingSchedulingUsers(TeaModel):
    def __init__(self, scheduling_order=None, scheduling_user_id=None):
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: int
        # 轮班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceGroupSchedulingRequestFastSchedulingSchedulingUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        return self


class UpdateServiceGroupSchedulingRequestFastScheduling(TeaModel):
    def __init__(self, duty_plan=None, id=None, scheduling_users=None, single_duration=None,
                 single_duration_unit=None):
        # 值班方案 dutyPlan FAST_CHOICE 快速选择   CUSTOM  自定义
        self.duty_plan = duty_plan  # type: str
        # 快速排班ID
        self.id = id  # type: long
        # 快速轮班用户
        self.scheduling_users = scheduling_users  # type: list[UpdateServiceGroupSchedulingRequestFastSchedulingSchedulingUsers]
        # 每人排班时长
        self.single_duration = single_duration  # type: int
        # 每人排班时长单位 HOUR 小时 DAY 天
        self.single_duration_unit = single_duration_unit  # type: str

    def validate(self):
        if self.scheduling_users:
            for k in self.scheduling_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateServiceGroupSchedulingRequestFastScheduling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duty_plan is not None:
            result['dutyPlan'] = self.duty_plan
        if self.id is not None:
            result['id'] = self.id
        result['schedulingUsers'] = []
        if self.scheduling_users is not None:
            for k in self.scheduling_users:
                result['schedulingUsers'].append(k.to_map() if k else None)
        if self.single_duration is not None:
            result['singleDuration'] = self.single_duration
        if self.single_duration_unit is not None:
            result['singleDurationUnit'] = self.single_duration_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dutyPlan') is not None:
            self.duty_plan = m.get('dutyPlan')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.scheduling_users = []
        if m.get('schedulingUsers') is not None:
            for k in m.get('schedulingUsers'):
                temp_model = UpdateServiceGroupSchedulingRequestFastSchedulingSchedulingUsers()
                self.scheduling_users.append(temp_model.from_map(k))
        if m.get('singleDuration') is not None:
            self.single_duration = m.get('singleDuration')
        if m.get('singleDurationUnit') is not None:
            self.single_duration_unit = m.get('singleDurationUnit')
        return self


class UpdateServiceGroupSchedulingRequestFineSchedulingSchedulingFineShifts(TeaModel):
    def __init__(self, cycle_order=None, scheduling_end_time=None, scheduling_order=None,
                 scheduling_start_time=None, scheduling_user_id=None, shift_name=None, skip_one_day=None):
        # 轮训次序
        self.cycle_order = cycle_order  # type: int
        # 排班结束时间
        self.scheduling_end_time = scheduling_end_time  # type: str
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: long
        # 排班开始时间
        self.scheduling_start_time = scheduling_start_time  # type: str
        # 排班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long
        # 班次名称
        self.shift_name = shift_name  # type: str
        # 是否跨天
        self.skip_one_day = skip_one_day  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceGroupSchedulingRequestFineSchedulingSchedulingFineShifts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cycle_order is not None:
            result['cycleOrder'] = self.cycle_order
        if self.scheduling_end_time is not None:
            result['schedulingEndTime'] = self.scheduling_end_time
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_start_time is not None:
            result['schedulingStartTime'] = self.scheduling_start_time
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        if self.shift_name is not None:
            result['shiftName'] = self.shift_name
        if self.skip_one_day is not None:
            result['skipOneDay'] = self.skip_one_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cycleOrder') is not None:
            self.cycle_order = m.get('cycleOrder')
        if m.get('schedulingEndTime') is not None:
            self.scheduling_end_time = m.get('schedulingEndTime')
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingStartTime') is not None:
            self.scheduling_start_time = m.get('schedulingStartTime')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        if m.get('shiftName') is not None:
            self.shift_name = m.get('shiftName')
        if m.get('skipOneDay') is not None:
            self.skip_one_day = m.get('skipOneDay')
        return self


class UpdateServiceGroupSchedulingRequestFineSchedulingSchedulingTemplateFineShifts(TeaModel):
    def __init__(self, scheduling_end_time=None, scheduling_order=None, scheduling_start_time=None,
                 scheduling_user_id=None, shift_name=None, skip_one_day=None):
        # 排班结束时间
        self.scheduling_end_time = scheduling_end_time  # type: str
        # 排班顺序
        self.scheduling_order = scheduling_order  # type: int
        # 排班开始时间
        self.scheduling_start_time = scheduling_start_time  # type: str
        # 排班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long
        # 班次名称
        self.shift_name = shift_name  # type: str
        # 是否跨天
        self.skip_one_day = skip_one_day  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceGroupSchedulingRequestFineSchedulingSchedulingTemplateFineShifts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_end_time is not None:
            result['schedulingEndTime'] = self.scheduling_end_time
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_start_time is not None:
            result['schedulingStartTime'] = self.scheduling_start_time
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        if self.shift_name is not None:
            result['shiftName'] = self.shift_name
        if self.skip_one_day is not None:
            result['skipOneDay'] = self.skip_one_day
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingEndTime') is not None:
            self.scheduling_end_time = m.get('schedulingEndTime')
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingStartTime') is not None:
            self.scheduling_start_time = m.get('schedulingStartTime')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        if m.get('shiftName') is not None:
            self.shift_name = m.get('shiftName')
        if m.get('skipOneDay') is not None:
            self.skip_one_day = m.get('skipOneDay')
        return self


class UpdateServiceGroupSchedulingRequestFineScheduling(TeaModel):
    def __init__(self, id=None, period=None, period_unit=None, scheduling_fine_shifts=None,
                 scheduling_template_fine_shifts=None, shift_type=None):
        # 精细排班ID
        self.id = id  # type: long
        # 循环周期
        self.period = period  # type: int
        # 循环周期单位 HOUR 小时 DAY 天
        self.period_unit = period_unit  # type: str
        # 精细排班班次人员信息
        self.scheduling_fine_shifts = scheduling_fine_shifts  # type: list[UpdateServiceGroupSchedulingRequestFineSchedulingSchedulingFineShifts]
        # 精细排班模版
        self.scheduling_template_fine_shifts = scheduling_template_fine_shifts  # type: list[UpdateServiceGroupSchedulingRequestFineSchedulingSchedulingTemplateFineShifts]
        # 班次类型 MORNING_NIGHT 早晚班 MORNING_NOON_NIGHT 早中晚班 CUSTOM 自定义
        self.shift_type = shift_type  # type: str

    def validate(self):
        if self.scheduling_fine_shifts:
            for k in self.scheduling_fine_shifts:
                if k:
                    k.validate()
        if self.scheduling_template_fine_shifts:
            for k in self.scheduling_template_fine_shifts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateServiceGroupSchedulingRequestFineScheduling, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['periodUnit'] = self.period_unit
        result['schedulingFineShifts'] = []
        if self.scheduling_fine_shifts is not None:
            for k in self.scheduling_fine_shifts:
                result['schedulingFineShifts'].append(k.to_map() if k else None)
        result['schedulingTemplateFineShifts'] = []
        if self.scheduling_template_fine_shifts is not None:
            for k in self.scheduling_template_fine_shifts:
                result['schedulingTemplateFineShifts'].append(k.to_map() if k else None)
        if self.shift_type is not None:
            result['shiftType'] = self.shift_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodUnit') is not None:
            self.period_unit = m.get('periodUnit')
        self.scheduling_fine_shifts = []
        if m.get('schedulingFineShifts') is not None:
            for k in m.get('schedulingFineShifts'):
                temp_model = UpdateServiceGroupSchedulingRequestFineSchedulingSchedulingFineShifts()
                self.scheduling_fine_shifts.append(temp_model.from_map(k))
        self.scheduling_template_fine_shifts = []
        if m.get('schedulingTemplateFineShifts') is not None:
            for k in m.get('schedulingTemplateFineShifts'):
                temp_model = UpdateServiceGroupSchedulingRequestFineSchedulingSchedulingTemplateFineShifts()
                self.scheduling_template_fine_shifts.append(temp_model.from_map(k))
        if m.get('shiftType') is not None:
            self.shift_type = m.get('shiftType')
        return self


class UpdateServiceGroupSchedulingRequest(TeaModel):
    def __init__(self, client_token=None, fast_scheduling=None, fine_scheduling=None, scheduling_way=None,
                 service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 快速排班
        self.fast_scheduling = fast_scheduling  # type: UpdateServiceGroupSchedulingRequestFastScheduling
        # 精细排班
        self.fine_scheduling = fine_scheduling  # type: UpdateServiceGroupSchedulingRequestFineScheduling
        # 排班方式 FAST 快速排班 FINE 精细排班
        self.scheduling_way = scheduling_way  # type: str
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        if self.fast_scheduling:
            self.fast_scheduling.validate()
        if self.fine_scheduling:
            self.fine_scheduling.validate()

    def to_map(self):
        _map = super(UpdateServiceGroupSchedulingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.fast_scheduling is not None:
            result['fastScheduling'] = self.fast_scheduling.to_map()
        if self.fine_scheduling is not None:
            result['fineScheduling'] = self.fine_scheduling.to_map()
        if self.scheduling_way is not None:
            result['schedulingWay'] = self.scheduling_way
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('fastScheduling') is not None:
            temp_model = UpdateServiceGroupSchedulingRequestFastScheduling()
            self.fast_scheduling = temp_model.from_map(m['fastScheduling'])
        if m.get('fineScheduling') is not None:
            temp_model = UpdateServiceGroupSchedulingRequestFineScheduling()
            self.fine_scheduling = temp_model.from_map(m['fineScheduling'])
        if m.get('schedulingWay') is not None:
            self.scheduling_way = m.get('schedulingWay')
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class UpdateServiceGroupSchedulingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceGroupSchedulingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateServiceGroupSchedulingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceGroupSchedulingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceGroupSchedulingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateServiceGroupSchedulingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceGroupSpecialDaySchedulingRequestSchedulingSpecialDays(TeaModel):
    def __init__(self, scheduling_end_time=None, scheduling_order=None, scheduling_start_time=None,
                 scheduling_user_id=None):
        # 排班结束时间
        self.scheduling_end_time = scheduling_end_time  # type: str
        # 班次顺序
        self.scheduling_order = scheduling_order  # type: int
        # 排班开始时间
        self.scheduling_start_time = scheduling_start_time  # type: str
        # 排班用户ID
        self.scheduling_user_id = scheduling_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceGroupSpecialDaySchedulingRequestSchedulingSpecialDays, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheduling_end_time is not None:
            result['schedulingEndTime'] = self.scheduling_end_time
        if self.scheduling_order is not None:
            result['schedulingOrder'] = self.scheduling_order
        if self.scheduling_start_time is not None:
            result['schedulingStartTime'] = self.scheduling_start_time
        if self.scheduling_user_id is not None:
            result['schedulingUserId'] = self.scheduling_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schedulingEndTime') is not None:
            self.scheduling_end_time = m.get('schedulingEndTime')
        if m.get('schedulingOrder') is not None:
            self.scheduling_order = m.get('schedulingOrder')
        if m.get('schedulingStartTime') is not None:
            self.scheduling_start_time = m.get('schedulingStartTime')
        if m.get('schedulingUserId') is not None:
            self.scheduling_user_id = m.get('schedulingUserId')
        return self


class UpdateServiceGroupSpecialDaySchedulingRequest(TeaModel):
    def __init__(self, client_token=None, scheduling_date=None, scheduling_special_days=None,
                 service_group_id=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 排班日期
        self.scheduling_date = scheduling_date  # type: str
        # 特殊排班信息
        self.scheduling_special_days = scheduling_special_days  # type: list[UpdateServiceGroupSpecialDaySchedulingRequestSchedulingSpecialDays]
        # 服务组ID
        self.service_group_id = service_group_id  # type: long

    def validate(self):
        if self.scheduling_special_days:
            for k in self.scheduling_special_days:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateServiceGroupSpecialDaySchedulingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.scheduling_date is not None:
            result['schedulingDate'] = self.scheduling_date
        result['schedulingSpecialDays'] = []
        if self.scheduling_special_days is not None:
            for k in self.scheduling_special_days:
                result['schedulingSpecialDays'].append(k.to_map() if k else None)
        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('schedulingDate') is not None:
            self.scheduling_date = m.get('schedulingDate')
        self.scheduling_special_days = []
        if m.get('schedulingSpecialDays') is not None:
            for k in m.get('schedulingSpecialDays'):
                temp_model = UpdateServiceGroupSpecialDaySchedulingRequestSchedulingSpecialDays()
                self.scheduling_special_days.append(temp_model.from_map(k))
        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')
        return self


class UpdateServiceGroupSpecialDaySchedulingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServiceGroupSpecialDaySchedulingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateServiceGroupSpecialDaySchedulingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateServiceGroupSpecialDaySchedulingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServiceGroupSpecialDaySchedulingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateServiceGroupSpecialDaySchedulingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubscriptionRequestNotifyObjectList(TeaModel):
    def __init__(self, id=None, notify_object_id=None):
        # 主键id
        self.id = id  # type: long
        # 通知对象id
        self.notify_object_id = notify_object_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubscriptionRequestNotifyObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.notify_object_id is not None:
            result['notifyObjectId'] = self.notify_object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('notifyObjectId') is not None:
            self.notify_object_id = m.get('notifyObjectId')
        return self


class UpdateSubscriptionRequestNotifyStrategyListStrategiesConditions(TeaModel):
    def __init__(self, action=None, effection=None, level=None, problem_notify_type=None):
        # 事件动作
        self.action = action  # type: str
        # 影响程度
        self.effection = effection  # type: str
        # 等级
        self.level = level  # type: str
        # 故障通知类型
        self.problem_notify_type = problem_notify_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubscriptionRequestNotifyStrategyListStrategiesConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.effection is not None:
            result['effection'] = self.effection
        if self.level is not None:
            result['level'] = self.level
        if self.problem_notify_type is not None:
            result['problemNotifyType'] = self.problem_notify_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('effection') is not None:
            self.effection = m.get('effection')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('problemNotifyType') is not None:
            self.problem_notify_type = m.get('problemNotifyType')
        return self


class UpdateSubscriptionRequestNotifyStrategyListStrategiesPeriodChannel(TeaModel):
    def __init__(self, non_workday=None, workday=None):
        # 非工作时间
        self.non_workday = non_workday  # type: str
        # 工作时间
        self.workday = workday  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubscriptionRequestNotifyStrategyListStrategiesPeriodChannel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.non_workday is not None:
            result['nonWorkday'] = self.non_workday
        if self.workday is not None:
            result['workday'] = self.workday
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('nonWorkday') is not None:
            self.non_workday = m.get('nonWorkday')
        if m.get('workday') is not None:
            self.workday = m.get('workday')
        return self


class UpdateSubscriptionRequestNotifyStrategyListStrategies(TeaModel):
    def __init__(self, channels=None, conditions=None, id=None, period_channel=None):
        # 故障等级
        self.channels = channels  # type: str
        # 影响程度
        self.conditions = conditions  # type: list[UpdateSubscriptionRequestNotifyStrategyListStrategiesConditions]
        # id
        self.id = id  # type: str
        # 分时段通知渠道
        self.period_channel = period_channel  # type: UpdateSubscriptionRequestNotifyStrategyListStrategiesPeriodChannel

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.period_channel:
            self.period_channel.validate()

    def to_map(self):
        _map = super(UpdateSubscriptionRequestNotifyStrategyListStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['channels'] = self.channels
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.period_channel is not None:
            result['periodChannel'] = self.period_channel.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('channels') is not None:
            self.channels = m.get('channels')
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = UpdateSubscriptionRequestNotifyStrategyListStrategiesConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('periodChannel') is not None:
            temp_model = UpdateSubscriptionRequestNotifyStrategyListStrategiesPeriodChannel()
            self.period_channel = temp_model.from_map(m['periodChannel'])
        return self


class UpdateSubscriptionRequestNotifyStrategyList(TeaModel):
    def __init__(self, instance_type=None, strategies=None):
        # 订阅实例类型，事件、报警、故障
        self.instance_type = instance_type  # type: long
        # 通知策略
        self.strategies = strategies  # type: list[UpdateSubscriptionRequestNotifyStrategyListStrategies]

    def validate(self):
        if self.strategies:
            for k in self.strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateSubscriptionRequestNotifyStrategyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        result['strategies'] = []
        if self.strategies is not None:
            for k in self.strategies:
                result['strategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        self.strategies = []
        if m.get('strategies') is not None:
            for k in m.get('strategies'):
                temp_model = UpdateSubscriptionRequestNotifyStrategyListStrategies()
                self.strategies.append(temp_model.from_map(k))
        return self


class UpdateSubscriptionRequestScopeObjectList(TeaModel):
    def __init__(self, id=None, scope_object_id=None):
        # 主键id
        self.id = id  # type: long
        # 订阅范围对象id
        self.scope_object_id = scope_object_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubscriptionRequestScopeObjectList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.scope_object_id is not None:
            result['scopeObjectId'] = self.scope_object_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('scopeObjectId') is not None:
            self.scope_object_id = m.get('scopeObjectId')
        return self


class UpdateSubscriptionRequest(TeaModel):
    def __init__(self, end_time=None, expired_type=None, notify_object_list=None, notify_object_type=None,
                 notify_strategy_list=None, period=None, scope=None, scope_object_list=None, start_time=None, subscription_id=None,
                 subscription_title=None):
        # 结束时间
        self.end_time = end_time  # type: str
        # 订阅时效
        self.expired_type = expired_type  # type: str
        # 通知对象列表
        self.notify_object_list = notify_object_list  # type: list[UpdateSubscriptionRequestNotifyObjectList]
        # 通知对象类型
        self.notify_object_type = notify_object_type  # type: str
        # 通知策略列表
        self.notify_strategy_list = notify_strategy_list  # type: list[UpdateSubscriptionRequestNotifyStrategyList]
        # 时间段字符串
        self.period = period  # type: str
        # 订阅范围类型
        self.scope = scope  # type: str
        # 订阅范围列表
        self.scope_object_list = scope_object_list  # type: list[UpdateSubscriptionRequestScopeObjectList]
        # 开始时间
        self.start_time = start_time  # type: str
        # 主键
        self.subscription_id = subscription_id  # type: long
        # 通知订阅名称
        self.subscription_title = subscription_title  # type: str

    def validate(self):
        if self.notify_object_list:
            for k in self.notify_object_list:
                if k:
                    k.validate()
        if self.notify_strategy_list:
            for k in self.notify_strategy_list:
                if k:
                    k.validate()
        if self.scope_object_list:
            for k in self.scope_object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateSubscriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.expired_type is not None:
            result['expiredType'] = self.expired_type
        result['notifyObjectList'] = []
        if self.notify_object_list is not None:
            for k in self.notify_object_list:
                result['notifyObjectList'].append(k.to_map() if k else None)
        if self.notify_object_type is not None:
            result['notifyObjectType'] = self.notify_object_type
        result['notifyStrategyList'] = []
        if self.notify_strategy_list is not None:
            for k in self.notify_strategy_list:
                result['notifyStrategyList'].append(k.to_map() if k else None)
        if self.period is not None:
            result['period'] = self.period
        if self.scope is not None:
            result['scope'] = self.scope
        result['scopeObjectList'] = []
        if self.scope_object_list is not None:
            for k in self.scope_object_list:
                result['scopeObjectList'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        if self.subscription_title is not None:
            result['subscriptionTitle'] = self.subscription_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('expiredType') is not None:
            self.expired_type = m.get('expiredType')
        self.notify_object_list = []
        if m.get('notifyObjectList') is not None:
            for k in m.get('notifyObjectList'):
                temp_model = UpdateSubscriptionRequestNotifyObjectList()
                self.notify_object_list.append(temp_model.from_map(k))
        if m.get('notifyObjectType') is not None:
            self.notify_object_type = m.get('notifyObjectType')
        self.notify_strategy_list = []
        if m.get('notifyStrategyList') is not None:
            for k in m.get('notifyStrategyList'):
                temp_model = UpdateSubscriptionRequestNotifyStrategyList()
                self.notify_strategy_list.append(temp_model.from_map(k))
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        self.scope_object_list = []
        if m.get('scopeObjectList') is not None:
            for k in m.get('scopeObjectList'):
                temp_model = UpdateSubscriptionRequestScopeObjectList()
                self.scope_object_list.append(temp_model.from_map(k))
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        if m.get('subscriptionTitle') is not None:
            self.subscription_title = m.get('subscriptionTitle')
        return self


class UpdateSubscriptionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSubscriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateSubscriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateSubscriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSubscriptionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, client_token=None, email=None, phone=None, ram_id=None, user_id=None, username=None):
        # 幂等号
        self.client_token = client_token  # type: str
        # 邮件
        self.email = email  # type: str
        # 手机号
        self.phone = phone  # type: str
        # 用户ramId
        self.ram_id = ram_id  # type: long
        # 用户ID
        self.user_id = user_id  # type: long
        # 用户名
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.email is not None:
            result['email'] = self.email
        if self.phone is not None:
            result['phone'] = self.phone
        if self.ram_id is not None:
            result['ramId'] = self.ram_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('ramId') is not None:
            self.ram_id = m.get('ramId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserGuideStatusRequest(TeaModel):
    def __init__(self, client_token=None, guide_action=None):
        # 幂等校验
        self.client_token = client_token  # type: str
        # INCIDENT_GUIDE	事件线 INCIDENT_GUIDE配置人员 USER_GUIDE 服务组 SERVICE_GROUP_GUIDE 服务 SERVICE_GUIDE 集成配置 MONITOR_GUIDE 流转规则 ROUTE_RULE_GUIDE 通知订阅 NOTICE_GUIDE
        self.guide_action = guide_action  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserGuideStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.guide_action is not None:
            result['guideAction'] = self.guide_action
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('guideAction') is not None:
            self.guide_action = m.get('guideAction')
        return self


class UpdateUserGuideStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateUserGuideStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateUserGuideStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateUserGuideStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateUserGuideStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserGuideStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyRouteRuleRequestTestSourceEvents(TeaModel):
    def __init__(self, event_json=None, event_time=None, monitor_source_id=None, monitor_source_name=None):
        # 告警内容
        self.event_json = event_json  # type: str
        # 告警上报时间
        self.event_time = event_time  # type: str
        # 监控告警源ID
        self.monitor_source_id = monitor_source_id  # type: long
        # 监控告警源名称
        self.monitor_source_name = monitor_source_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyRouteRuleRequestTestSourceEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_json is not None:
            result['eventJson'] = self.event_json
        if self.event_time is not None:
            result['eventTime'] = self.event_time
        if self.monitor_source_id is not None:
            result['monitorSourceId'] = self.monitor_source_id
        if self.monitor_source_name is not None:
            result['monitorSourceName'] = self.monitor_source_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eventJson') is not None:
            self.event_json = m.get('eventJson')
        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')
        if m.get('monitorSourceId') is not None:
            self.monitor_source_id = m.get('monitorSourceId')
        if m.get('monitorSourceName') is not None:
            self.monitor_source_name = m.get('monitorSourceName')
        return self


class VerifyRouteRuleRequest(TeaModel):
    def __init__(self, route_rule_id=None, test_source_events=None):
        # 规则id
        self.route_rule_id = route_rule_id  # type: long
        # 测试告警
        self.test_source_events = test_source_events  # type: list[VerifyRouteRuleRequestTestSourceEvents]

    def validate(self):
        if self.test_source_events:
            for k in self.test_source_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VerifyRouteRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_rule_id is not None:
            result['routeRuleId'] = self.route_rule_id
        result['testSourceEvents'] = []
        if self.test_source_events is not None:
            for k in self.test_source_events:
                result['testSourceEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        self.test_source_events = []
        if m.get('testSourceEvents') is not None:
            for k in m.get('testSourceEvents'):
                temp_model = VerifyRouteRuleRequestTestSourceEvents()
                self.test_source_events.append(temp_model.from_map(k))
        return self


class VerifyRouteRuleResponseBodyDataEscalationPlans(TeaModel):
    def __init__(self, escalation_plan_id=None, escalation_plan_name=None):
        # 升级计划ID
        self.escalation_plan_id = escalation_plan_id  # type: long
        # 升级计划名称
        self.escalation_plan_name = escalation_plan_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyRouteRuleResponseBodyDataEscalationPlans, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_plan_id is not None:
            result['escalationPlanId'] = self.escalation_plan_id
        if self.escalation_plan_name is not None:
            result['escalationPlanName'] = self.escalation_plan_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('escalationPlanId') is not None:
            self.escalation_plan_id = m.get('escalationPlanId')
        if m.get('escalationPlanName') is not None:
            self.escalation_plan_name = m.get('escalationPlanName')
        return self


class VerifyRouteRuleResponseBodyDataNotifySubscriptionNames(TeaModel):
    def __init__(self, subscription_id=None, title=None):
        # 订阅ID
        self.subscription_id = subscription_id  # type: long
        # 订阅名称
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyRouteRuleResponseBodyDataNotifySubscriptionNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class VerifyRouteRuleResponseBodyData(TeaModel):
    def __init__(self, escalation_plans=None, is_valid_rule=None, monitor_source_ids=None,
                 notify_subscription_names=None, route_rule_fail_reason=None, route_type=None):
        # 升级策略名称
        self.escalation_plans = escalation_plans  # type: list[VerifyRouteRuleResponseBodyDataEscalationPlans]
        # 验证是否成功
        self.is_valid_rule = is_valid_rule  # type: bool
        # 验证失败监控源ID
        self.monitor_source_ids = monitor_source_ids  # type: list[long]
        # 订阅名称
        self.notify_subscription_names = notify_subscription_names  # type: list[VerifyRouteRuleResponseBodyDataNotifySubscriptionNames]
        # 流转规则验证失败的原因
        self.route_rule_fail_reason = route_rule_fail_reason  # type: list[str]
        # 事件或者报警
        self.route_type = route_type  # type: str

    def validate(self):
        if self.escalation_plans:
            for k in self.escalation_plans:
                if k:
                    k.validate()
        if self.notify_subscription_names:
            for k in self.notify_subscription_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(VerifyRouteRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['escalationPlans'] = []
        if self.escalation_plans is not None:
            for k in self.escalation_plans:
                result['escalationPlans'].append(k.to_map() if k else None)
        if self.is_valid_rule is not None:
            result['isValidRule'] = self.is_valid_rule
        if self.monitor_source_ids is not None:
            result['monitorSourceIds'] = self.monitor_source_ids
        result['notifySubscriptionNames'] = []
        if self.notify_subscription_names is not None:
            for k in self.notify_subscription_names:
                result['notifySubscriptionNames'].append(k.to_map() if k else None)
        if self.route_rule_fail_reason is not None:
            result['routeRuleFailReason'] = self.route_rule_fail_reason
        if self.route_type is not None:
            result['routeType'] = self.route_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.escalation_plans = []
        if m.get('escalationPlans') is not None:
            for k in m.get('escalationPlans'):
                temp_model = VerifyRouteRuleResponseBodyDataEscalationPlans()
                self.escalation_plans.append(temp_model.from_map(k))
        if m.get('isValidRule') is not None:
            self.is_valid_rule = m.get('isValidRule')
        if m.get('monitorSourceIds') is not None:
            self.monitor_source_ids = m.get('monitorSourceIds')
        self.notify_subscription_names = []
        if m.get('notifySubscriptionNames') is not None:
            for k in m.get('notifySubscriptionNames'):
                temp_model = VerifyRouteRuleResponseBodyDataNotifySubscriptionNames()
                self.notify_subscription_names.append(temp_model.from_map(k))
        if m.get('routeRuleFailReason') is not None:
            self.route_rule_fail_reason = m.get('routeRuleFailReason')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        return self


class VerifyRouteRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # 验证结果
        self.data = data  # type: VerifyRouteRuleResponseBodyData
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(VerifyRouteRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = VerifyRouteRuleResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class VerifyRouteRuleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyRouteRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyRouteRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyRouteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DataValue(TeaModel):
    def __init__(self, code=None, description=None, config_description=None, config_code=None, parent_code=None,
                 config_key=None, config_value=None, requirement=None):
        self.code = code  # type: str
        self.description = description  # type: str
        # 配置描述
        self.config_description = config_description  # type: str
        # 配置code
        self.config_code = config_code  # type: str
        # 配置父code
        self.parent_code = parent_code  # type: str
        # key (用于前后端值传递)
        self.config_key = config_key  # type: str
        # value (用于前端展示)
        self.config_value = config_value  # type: str
        # 是否必选
        self.requirement = requirement  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.config_description is not None:
            result['configDescription'] = self.config_description
        if self.config_code is not None:
            result['configCode'] = self.config_code
        if self.parent_code is not None:
            result['parentCode'] = self.parent_code
        if self.config_key is not None:
            result['configKey'] = self.config_key
        if self.config_value is not None:
            result['configValue'] = self.config_value
        if self.requirement is not None:
            result['requirement'] = self.requirement
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('configDescription') is not None:
            self.config_description = m.get('configDescription')
        if m.get('configCode') is not None:
            self.config_code = m.get('configCode')
        if m.get('parentCode') is not None:
            self.parent_code = m.get('parentCode')
        if m.get('configKey') is not None:
            self.config_key = m.get('configKey')
        if m.get('configValue') is not None:
            self.config_value = m.get('configValue')
        if m.get('requirement') is not None:
            self.requirement = m.get('requirement')
        return self


