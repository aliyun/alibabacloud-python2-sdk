# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApproveOtaTaskRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, biz_region_id=None, ota_type=None, start_time=None, task_id=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.biz_region_id = biz_region_id  # type: str
        self.ota_type = ota_type  # type: str
        self.start_time = start_time  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveOtaTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.ota_type is not None:
            result['OtaType'] = self.ota_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ApproveOtaTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveOtaTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApproveOtaTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApproveOtaTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApproveOtaTaskResponse, self).to_map()
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
            temp_model = ApproveOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeInstanceGroupRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, authorize_user_ids=None, product_type=None,
                 un_authorize_user_ids=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.authorize_user_ids = authorize_user_ids  # type: list[str]
        self.product_type = product_type  # type: str
        self.un_authorize_user_ids = un_authorize_user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.authorize_user_ids is not None:
            result['AuthorizeUserIds'] = self.authorize_user_ids
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.un_authorize_user_ids is not None:
            result['UnAuthorizeUserIds'] = self.un_authorize_user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AuthorizeUserIds') is not None:
            self.authorize_user_ids = m.get('AuthorizeUserIds')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('UnAuthorizeUserIds') is not None:
            self.un_authorize_user_ids = m.get('UnAuthorizeUserIds')
        return self


class AuthorizeInstanceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeInstanceGroupResponseBody, self).to_map()
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


class AuthorizeInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthorizeInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthorizeInstanceGroupResponse, self).to_map()
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
            temp_model = AuthorizeInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOtaTaskRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, task_id=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOtaTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelOtaTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOtaTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelOtaTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelOtaTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelOtaTaskResponse, self).to_map()
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
            temp_model = CancelOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppInstanceGroupRequestNetworkRoutes(TeaModel):
    def __init__(self, destination=None, mode=None):
        self.destination = destination  # type: str
        self.mode = mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNetworkRoutes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class CreateAppInstanceGroupRequestNetwork(TeaModel):
    def __init__(self, routes=None, strategy_type=None):
        self.routes = routes  # type: list[CreateAppInstanceGroupRequestNetworkRoutes]
        self.strategy_type = strategy_type  # type: str

    def validate(self):
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['Routes'].append(k.to_map() if k else None)
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.routes = []
        if m.get('Routes') is not None:
            for k in m.get('Routes'):
                temp_model = CreateAppInstanceGroupRequestNetworkRoutes()
                self.routes.append(temp_model.from_map(k))
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        return self


class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(self, amount=None, end_time=None, start_time=None):
        self.amount = amount  # type: int
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules(TeaModel):
    def __init__(self, recurrence_type=None, recurrence_values=None, timer_periods=None):
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_values = recurrence_values  # type: list[int]
        self.timer_periods = timer_periods  # type: list[CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods]

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class CreateAppInstanceGroupRequestNodePool(TeaModel):
    def __init__(self, max_scaling_amount=None, node_amount=None, node_capacity=None, node_instance_type=None,
                 recurrence_schedules=None, scaling_down_after_idle_minutes=None, scaling_step=None, scaling_usage_threshold=None,
                 strategy_disable_date=None, strategy_enable_date=None, strategy_type=None, warm_up=None):
        self.max_scaling_amount = max_scaling_amount  # type: int
        self.node_amount = node_amount  # type: int
        self.node_capacity = node_capacity  # type: int
        self.node_instance_type = node_instance_type  # type: str
        self.recurrence_schedules = recurrence_schedules  # type: list[CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules]
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes  # type: int
        self.scaling_step = scaling_step  # type: int
        self.scaling_usage_threshold = scaling_usage_threshold  # type: str
        self.strategy_disable_date = strategy_disable_date  # type: str
        self.strategy_enable_date = strategy_enable_date  # type: str
        self.strategy_type = strategy_type  # type: str
        self.warm_up = warm_up  # type: bool

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNodePool, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class CreateAppInstanceGroupRequestUserInfo(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_center_image_id=None, app_instance_group_name=None, auto_pay=None, auto_renew=None,
                 biz_region_id=None, charge_resource_mode=None, charge_type=None, network=None, node_pool=None, period=None,
                 period_unit=None, pre_open_app_id=None, product_type=None, promotion_id=None, session_timeout=None,
                 user_info=None, users=None):
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.biz_region_id = biz_region_id  # type: str
        self.charge_resource_mode = charge_resource_mode  # type: str
        self.charge_type = charge_type  # type: str
        self.network = network  # type: CreateAppInstanceGroupRequestNetwork
        self.node_pool = node_pool  # type: CreateAppInstanceGroupRequestNodePool
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.pre_open_app_id = pre_open_app_id  # type: str
        self.product_type = product_type  # type: str
        self.promotion_id = promotion_id  # type: str
        self.session_timeout = session_timeout  # type: int
        self.user_info = user_info  # type: CreateAppInstanceGroupRequestUserInfo
        self.users = users  # type: list[str]

    def validate(self):
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Network') is not None:
            temp_model = CreateAppInstanceGroupRequestNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('NodePool') is not None:
            temp_model = CreateAppInstanceGroupRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('UserInfo') is not None:
            temp_model = CreateAppInstanceGroupRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateAppInstanceGroupShrinkRequest(TeaModel):
    def __init__(self, app_center_image_id=None, app_instance_group_name=None, auto_pay=None, auto_renew=None,
                 biz_region_id=None, charge_resource_mode=None, charge_type=None, network_shrink=None, node_pool_shrink=None,
                 period=None, period_unit=None, pre_open_app_id=None, product_type=None, promotion_id=None,
                 session_timeout=None, user_info_shrink=None, users=None):
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.biz_region_id = biz_region_id  # type: str
        self.charge_resource_mode = charge_resource_mode  # type: str
        self.charge_type = charge_type  # type: str
        self.network_shrink = network_shrink  # type: str
        self.node_pool_shrink = node_pool_shrink  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.pre_open_app_id = pre_open_app_id  # type: str
        self.product_type = product_type  # type: str
        self.promotion_id = promotion_id  # type: str
        self.session_timeout = session_timeout  # type: int
        self.user_info_shrink = user_info_shrink  # type: str
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.network_shrink is not None:
            result['Network'] = self.network_shrink
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateAppInstanceGroupResponseBodyAppInstanceGroupModel(TeaModel):
    def __init__(self, app_instance_group_id=None, node_pool_id=None, order_id=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.node_pool_id = node_pool_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupResponseBodyAppInstanceGroupModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, app_instance_group_model=None, request_id=None):
        self.app_instance_group_model = app_instance_group_model  # type: CreateAppInstanceGroupResponseBodyAppInstanceGroupModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_instance_group_model:
            self.app_instance_group_model.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_model is not None:
            result['AppInstanceGroupModel'] = self.app_instance_group_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupModel') is not None:
            temp_model = CreateAppInstanceGroupResponseBodyAppInstanceGroupModel()
            self.app_instance_group_model = temp_model.from_map(m['AppInstanceGroupModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupResponse, self).to_map()
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
            temp_model = CreateAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DeleteAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppInstanceGroupResponseBody, self).to_map()
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


class DeleteAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppInstanceGroupResponse, self).to_map()
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
            temp_model = DeleteAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOtaTaskByTaskIdRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOtaTaskByTaskIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetOtaTaskByTaskIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, ota_version=None, release_note=None, request_id=None,
                 task_start_time=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.ota_version = ota_version  # type: str
        self.release_note = release_note  # type: str
        self.request_id = request_id  # type: str
        self.task_start_time = task_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOtaTaskByTaskIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        return self


class GetOtaTaskByTaskIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOtaTaskByTaskIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOtaTaskByTaskIdResponse, self).to_map()
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
            temp_model = GetOtaTaskByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcePriceRequest(TeaModel):
    def __init__(self, amount=None, biz_region_id=None, charge_type=None, node_instance_type=None, period=None,
                 period_unit=None, product_type=None):
        self.amount = amount  # type: long
        self.biz_region_id = biz_region_id  # type: str
        self.charge_type = charge_type  # type: str
        self.node_instance_type = node_instance_type  # type: str
        self.period = period  # type: long
        self.period_unit = period_unit  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetResourcePriceResponseBodyPriceModelPricePromotions(TeaModel):
    def __init__(self, option_code=None, promotion_desc=None, promotion_id=None, promotion_name=None, selected=None):
        self.option_code = option_code  # type: str
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: str
        self.promotion_name = promotion_name  # type: str
        self.selected = selected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceModelPricePromotions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourcePriceResponseBodyPriceModelPrice(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, promotions=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: str
        self.original_price = original_price  # type: str
        self.promotions = promotions  # type: list[GetResourcePriceResponseBodyPriceModelPricePromotions]
        self.trade_price = trade_price  # type: str

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceModelPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourcePriceResponseBodyPriceModelPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourcePriceResponseBodyPriceModelRules(TeaModel):
    def __init__(self, description=None, rule_id=None):
        self.description = description  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceModelRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourcePriceResponseBodyPriceModel(TeaModel):
    def __init__(self, price=None, rules=None):
        self.price = price  # type: GetResourcePriceResponseBodyPriceModelPrice
        self.rules = rules  # type: list[GetResourcePriceResponseBodyPriceModelRules]

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourcePriceResponseBodyPriceModelPrice()
            self.price = temp_model.from_map(m['Price'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourcePriceResponseBodyPriceModelRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourcePriceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, price_model=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.price_model = price_model  # type: GetResourcePriceResponseBodyPriceModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.price_model:
            self.price_model.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.price_model is not None:
            result['PriceModel'] = self.price_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PriceModel') is not None:
            temp_model = GetResourcePriceResponseBodyPriceModel()
            self.price_model = temp_model.from_map(m['PriceModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourcePriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourcePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponse, self).to_map()
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
            temp_model = GetResourcePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRenewPriceRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, period=None, period_unit=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.period = period  # type: long
        self.period_unit = period_unit  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceRenewPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetResourceRenewPriceResponseBodyDataPricePromotions(TeaModel):
    def __init__(self, option_code=None, promotion_desc=None, promotion_id=None, promotion_name=None, selected=None):
        self.option_code = option_code  # type: str
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: str
        self.promotion_name = promotion_name  # type: str
        self.selected = selected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBodyDataPricePromotions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourceRenewPriceResponseBodyDataPrice(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, promotions=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: str
        self.original_price = original_price  # type: str
        self.promotions = promotions  # type: list[GetResourceRenewPriceResponseBodyDataPricePromotions]
        self.trade_price = trade_price  # type: str

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBodyDataPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourceRenewPriceResponseBodyDataPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourceRenewPriceResponseBodyDataRules(TeaModel):
    def __init__(self, description=None, rule_id=None):
        self.description = description  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBodyDataRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourceRenewPriceResponseBodyData(TeaModel):
    def __init__(self, price=None, rules=None):
        self.price = price  # type: GetResourceRenewPriceResponseBodyDataPrice
        self.rules = rules  # type: list[GetResourceRenewPriceResponseBodyDataRules]

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourceRenewPriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m['Price'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourceRenewPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourceRenewPriceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetResourceRenewPriceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetResourceRenewPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceRenewPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceRenewPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceRenewPriceResponse, self).to_map()
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
            temp_model = GetResourceRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_center_image_id=None, app_instance_group_id=None, app_instance_group_name=None,
                 page_number=None, page_size=None, product_type=None, region_id=None, status=None):
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(TeaModel):
    def __init__(self, app_id=None, app_name=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(self, amount=None, end_time=None, start_time=None):
        self.amount = amount  # type: int
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules(TeaModel):
    def __init__(self, recurrence_type=None, recurrence_values=None, timer_periods=None):
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_values = recurrence_values  # type: list[int]
        self.timer_periods = timer_periods  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods]

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool(TeaModel):
    def __init__(self, amount=None, max_scaling_amount=None, node_amount=None, node_capacity=None,
                 node_instance_type=None, node_pool_id=None, node_used=None, recurrence_schedules=None,
                 scaling_down_after_idle_minutes=None, scaling_node_amount=None, scaling_node_used=None, scaling_step=None,
                 scaling_usage_threshold=None, strategy_disable_date=None, strategy_enable_date=None, strategy_type=None, warm_up=None):
        self.amount = amount  # type: int
        self.max_scaling_amount = max_scaling_amount  # type: int
        self.node_amount = node_amount  # type: int
        self.node_capacity = node_capacity  # type: int
        self.node_instance_type = node_instance_type  # type: str
        self.node_pool_id = node_pool_id  # type: str
        self.node_used = node_used  # type: int
        self.recurrence_schedules = recurrence_schedules  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules]
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes  # type: int
        self.scaling_node_amount = scaling_node_amount  # type: int
        self.scaling_node_used = scaling_node_used  # type: int
        self.scaling_step = scaling_step  # type: int
        self.scaling_usage_threshold = scaling_usage_threshold  # type: str
        self.strategy_disable_date = strategy_disable_date  # type: str
        self.strategy_enable_date = strategy_enable_date  # type: str
        self.strategy_type = strategy_type  # type: str
        self.warm_up = warm_up  # type: bool

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.node_used is not None:
            result['NodeUsed'] = self.node_used
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_node_amount is not None:
            result['ScalingNodeAmount'] = self.scaling_node_amount
        if self.scaling_node_used is not None:
            result['ScalingNodeUsed'] = self.scaling_node_used
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('NodeUsed') is not None:
            self.node_used = m.get('NodeUsed')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingNodeAmount') is not None:
            self.scaling_node_amount = m.get('ScalingNodeAmount')
        if m.get('ScalingNodeUsed') is not None:
            self.scaling_node_used = m.get('ScalingNodeUsed')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo(TeaModel):
    def __init__(self, new_ota_version=None, ota_version=None, task_id=None):
        self.new_ota_version = new_ota_version  # type: str
        self.ota_version = ota_version  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_ota_version is not None:
            result['NewOtaVersion'] = self.new_ota_version
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewOtaVersion') is not None:
            self.new_ota_version = m.get('NewOtaVersion')
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModels(TeaModel):
    def __init__(self, amount=None, app_center_image_id=None, app_instance_group_id=None,
                 app_instance_group_name=None, app_instance_type=None, apps=None, charge_type=None, expired_time=None, gmt_create=None,
                 node_pool=None, os_type=None, ota_info=None, product_type=None, region_id=None, resource_status=None,
                 session_timeout=None, spec_id=None, status=None):
        self.amount = amount  # type: int
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.app_instance_type = app_instance_type  # type: str
        self.apps = apps  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps]
        self.charge_type = charge_type  # type: str
        self.expired_time = expired_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.node_pool = node_pool  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool]
        self.os_type = os_type  # type: str
        self.ota_info = ota_info  # type: ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_status = resource_status  # type: str
        self.session_timeout = session_timeout  # type: str
        self.spec_id = spec_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()
        if self.node_pool:
            for k in self.node_pool:
                if k:
                    k.validate()
        if self.ota_info:
            self.ota_info.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        result['NodePool'] = []
        if self.node_pool is not None:
            for k in self.node_pool:
                result['NodePool'].append(k.to_map() if k else None)
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.ota_info is not None:
            result['OtaInfo'] = self.ota_info.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        self.node_pool = []
        if m.get('NodePool') is not None:
            for k in m.get('NodePool'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k))
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OtaInfo') is not None:
            temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
            self.ota_info = temp_model.from_map(m['OtaInfo'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, app_instance_group_models=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.app_instance_group_models = app_instance_group_models  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModels]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.app_instance_group_models:
            for k in self.app_instance_group_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInstanceGroupModels'] = []
        if self.app_instance_group_models is not None:
            for k in self.app_instance_group_models:
                result['AppInstanceGroupModels'].append(k.to_map() if k else None)
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
        self.app_instance_group_models = []
        if m.get('AppInstanceGroupModels') is not None:
            for k in m.get('AppInstanceGroupModels'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModels()
                self.app_instance_group_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponse, self).to_map()
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
            temp_model = ListAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeInstanceTypeRequest(TeaModel):
    def __init__(self, biz_region_id=None, language=None, os_type=None, page_number=None, page_size=None,
                 product_type=None):
        self.biz_region_id = biz_region_id  # type: str
        self.language = language  # type: str
        self.os_type = os_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeInstanceTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.language is not None:
            result['Language'] = self.language
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels(TeaModel):
    def __init__(self, cpu=None, gpu=None, gpu_memory=None, max_capacity=None, memory=None, node_instance_type=None,
                 node_instance_type_family=None, node_type_name=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        self.gpu_memory = gpu_memory  # type: long
        self.max_capacity = max_capacity  # type: int
        self.memory = memory  # type: long
        self.node_instance_type = node_instance_type  # type: str
        self.node_instance_type_family = node_instance_type_family  # type: str
        self.node_type_name = node_type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory
        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_instance_type_family is not None:
            result['NodeInstanceTypeFamily'] = self.node_instance_type_family
        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodeInstanceTypeFamily') is not None:
            self.node_instance_type_family = m.get('NodeInstanceTypeFamily')
        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')
        return self


class ListNodeInstanceTypeResponseBody(TeaModel):
    def __init__(self, node_instance_type_models=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.node_instance_type_models = node_instance_type_models  # type: list[ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.node_instance_type_models:
            for k in self.node_instance_type_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodeInstanceTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInstanceTypeModels'] = []
        if self.node_instance_type_models is not None:
            for k in self.node_instance_type_models:
                result['NodeInstanceTypeModels'].append(k.to_map() if k else None)
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
        self.node_instance_type_models = []
        if m.get('NodeInstanceTypeModels') is not None:
            for k in m.get('NodeInstanceTypeModels'):
                temp_model = ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels()
                self.node_instance_type_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeInstanceTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodeInstanceTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodeInstanceTypeResponse, self).to_map()
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
            temp_model = ListNodeInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOtaTaskRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, ota_type=None, page_number=None, page_size=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.ota_type = ota_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOtaTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.ota_type is not None:
            result['OtaType'] = self.ota_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOtaTaskResponseBodyTaskList(TeaModel):
    def __init__(self, ota_version=None, task_display_status=None, task_id=None, task_start_time=None):
        self.ota_version = ota_version  # type: str
        self.task_display_status = task_display_status  # type: str
        self.task_id = task_id  # type: str
        self.task_start_time = task_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOtaTaskResponseBodyTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.task_display_status is not None:
            result['TaskDisplayStatus'] = self.task_display_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('TaskDisplayStatus') is not None:
            self.task_display_status = m.get('TaskDisplayStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        return self


class ListOtaTaskResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, task_list=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.task_list = task_list  # type: list[ListOtaTaskResponseBodyTaskList]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOtaTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
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
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListOtaTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOtaTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOtaTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOtaTaskResponse, self).to_map()
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
            temp_model = ListOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegionModels(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsResponseBodyRegionModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, region_models=None, request_id=None):
        self.region_models = region_models  # type: list[ListRegionsResponseBodyRegionModels]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.region_models:
            for k in self.region_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionModels'] = []
        if self.region_models is not None:
            for k in self.region_models:
                result['RegionModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_models = []
        if m.get('RegionModels') is not None:
            for k in m.get('RegionModels'):
                temp_model = ListRegionsResponseBodyRegionModels()
                self.region_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTenantConfigResponseBodyTenantConfigModel(TeaModel):
    def __init__(self, app_instance_group_expire_remind=None):
        self.app_instance_group_expire_remind = app_instance_group_expire_remind  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTenantConfigResponseBodyTenantConfigModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_expire_remind is not None:
            result['AppInstanceGroupExpireRemind'] = self.app_instance_group_expire_remind
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupExpireRemind') is not None:
            self.app_instance_group_expire_remind = m.get('AppInstanceGroupExpireRemind')
        return self


class ListTenantConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_config_model=None):
        self.request_id = request_id  # type: str
        self.tenant_config_model = tenant_config_model  # type: ListTenantConfigResponseBodyTenantConfigModel

    def validate(self):
        if self.tenant_config_model:
            self.tenant_config_model.validate()

    def to_map(self):
        _map = super(ListTenantConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_config_model is not None:
            result['TenantConfigModel'] = self.tenant_config_model.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantConfigModel') is not None:
            temp_model = ListTenantConfigResponseBodyTenantConfigModel()
            self.tenant_config_model = temp_model.from_map(m['TenantConfigModel'])
        return self


class ListTenantConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTenantConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTenantConfigResponse, self).to_map()
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
            temp_model = ListTenantConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogOffAllSessionsInAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogOffAllSessionsInAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class LogOffAllSessionsInAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogOffAllSessionsInAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LogOffAllSessionsInAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LogOffAllSessionsInAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LogOffAllSessionsInAppInstanceGroupResponse, self).to_map()
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
            temp_model = LogOffAllSessionsInAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppInstanceGroupAttributeRequestNodePool(TeaModel):
    def __init__(self, node_capacity=None, node_pool_id=None):
        self.node_capacity = node_capacity  # type: int
        self.node_pool_id = node_pool_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeRequestNodePool, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        return self


class ModifyAppInstanceGroupAttributeRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, app_instance_group_name=None, node_pool=None, product_type=None,
                 session_timeout=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.node_pool = node_pool  # type: ModifyAppInstanceGroupAttributeRequestNodePool
        self.product_type = product_type  # type: str
        self.session_timeout = session_timeout  # type: int

    def validate(self):
        if self.node_pool:
            self.node_pool.validate()

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('NodePool') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        return self


class ModifyAppInstanceGroupAttributeShrinkRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, app_instance_group_name=None, node_pool_shrink=None,
                 product_type=None, session_timeout=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.node_pool_shrink = node_pool_shrink  # type: str
        self.product_type = product_type  # type: str
        self.session_timeout = session_timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        return self


class ModifyAppInstanceGroupAttributeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppInstanceGroupAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAppInstanceGroupAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeResponse, self).to_map()
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
            temp_model = ModifyAppInstanceGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodePoolAttributeRequestNodePoolStrategy(TeaModel):
    def __init__(self, max_scaling_amount=None, scaling_down_after_idle_minutes=None, scaling_step=None,
                 scaling_usage_threshold=None, strategy_type=None):
        self.max_scaling_amount = max_scaling_amount  # type: int
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes  # type: int
        self.scaling_step = scaling_step  # type: int
        self.scaling_usage_threshold = scaling_usage_threshold  # type: str
        self.strategy_type = strategy_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodePoolAttributeRequestNodePoolStrategy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        return self


class ModifyNodePoolAttributeRequest(TeaModel):
    def __init__(self, biz_region_id=None, node_capacity=None, node_pool_strategy=None, pool_id=None,
                 product_type=None):
        self.biz_region_id = biz_region_id  # type: str
        self.node_capacity = node_capacity  # type: int
        self.node_pool_strategy = node_pool_strategy  # type: ModifyNodePoolAttributeRequestNodePoolStrategy
        self.pool_id = pool_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        if self.node_pool_strategy:
            self.node_pool_strategy.validate()

    def to_map(self):
        _map = super(ModifyNodePoolAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_strategy is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy.to_map()
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolStrategy') is not None:
            temp_model = ModifyNodePoolAttributeRequestNodePoolStrategy()
            self.node_pool_strategy = temp_model.from_map(m['NodePoolStrategy'])
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAttributeShrinkRequest(TeaModel):
    def __init__(self, biz_region_id=None, node_capacity=None, node_pool_strategy_shrink=None, pool_id=None,
                 product_type=None):
        self.biz_region_id = biz_region_id  # type: str
        self.node_capacity = node_capacity  # type: int
        self.node_pool_strategy_shrink = node_pool_strategy_shrink  # type: str
        self.pool_id = pool_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodePoolAttributeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_strategy_shrink is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy_shrink
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolStrategy') is not None:
            self.node_pool_strategy_shrink = m.get('NodePoolStrategy')
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAttributeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodePoolAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNodePoolAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyNodePoolAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNodePoolAttributeResponse, self).to_map()
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
            temp_model = ModifyNodePoolAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantConfigRequest(TeaModel):
    def __init__(self, app_instance_group_expire_remind=None):
        self.app_instance_group_expire_remind = app_instance_group_expire_remind  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_expire_remind is not None:
            result['AppInstanceGroupExpireRemind'] = self.app_instance_group_expire_remind
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupExpireRemind') is not None:
            self.app_instance_group_expire_remind = m.get('AppInstanceGroupExpireRemind')
        return self


class ModifyTenantConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantConfigResponseBody, self).to_map()
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


class ModifyTenantConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTenantConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTenantConfigResponse, self).to_map()
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
            temp_model = ModifyTenantConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageListAppInstanceGroupUserRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, page_number=None, page_size=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageListAppInstanceGroupUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class PageListAppInstanceGroupUserResponseBody(TeaModel):
    def __init__(self, request_id=None, users=None):
        self.request_id = request_id  # type: str
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageListAppInstanceGroupUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class PageListAppInstanceGroupUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PageListAppInstanceGroupUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PageListAppInstanceGroupUserResponse, self).to_map()
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
            temp_model = PageListAppInstanceGroupUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, auto_pay=None, period=None, period_unit=None, product_type=None,
                 promotion_id=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.product_type = product_type  # type: str
        self.promotion_id = promotion_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        return self


class RenewAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, order_id=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewAppInstanceGroupResponse, self).to_map()
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
            temp_model = RenewAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppInstanceGroupImageRequest(TeaModel):
    def __init__(self, app_center_image_id=None, app_instance_group_id=None, biz_region_id=None, product_type=None,
                 update_mode=None):
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.biz_region_id = biz_region_id  # type: str
        self.product_type = product_type  # type: str
        self.update_mode = update_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppInstanceGroupImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.update_mode is not None:
            result['UpdateMode'] = self.update_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('UpdateMode') is not None:
            self.update_mode = m.get('UpdateMode')
        return self


class UpdateAppInstanceGroupImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppInstanceGroupImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppInstanceGroupImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppInstanceGroupImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppInstanceGroupImageResponse, self).to_map()
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
            temp_model = UpdateAppInstanceGroupImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


