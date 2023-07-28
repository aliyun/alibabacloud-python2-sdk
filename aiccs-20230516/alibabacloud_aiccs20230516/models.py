# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddBlacklistRequest(TeaModel):
    def __init__(self, expired_day=None, numbers=None, owner_id=None, remark=None, resource_owner_account=None,
                 resource_owner_id=None):
        # 有效天数
        self.expired_day = expired_day  # type: str
        # 号码列表
        self.numbers = numbers  # type: list[str]
        self.owner_id = owner_id  # type: long
        # 备注
        self.remark = remark  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBlacklistRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AddBlacklistShrinkRequest(TeaModel):
    def __init__(self, expired_day=None, numbers_shrink=None, owner_id=None, remark=None,
                 resource_owner_account=None, resource_owner_id=None):
        # 有效天数
        self.expired_day = expired_day  # type: str
        # 号码列表
        self.numbers_shrink = numbers_shrink  # type: str
        self.owner_id = owner_id  # type: long
        # 备注
        self.remark = remark  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBlacklistShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day
        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')
        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AddBlacklistResponseBodyModel(TeaModel):
    def __init__(self, un_handle_numbers=None):
        # 错误手机号
        self.un_handle_numbers = un_handle_numbers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBlacklistResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.un_handle_numbers is not None:
            result['UnHandleNumbers'] = self.un_handle_numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UnHandleNumbers') is not None:
            self.un_handle_numbers = m.get('UnHandleNumbers')
        return self


class AddBlacklistResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: AddBlacklistResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(AddBlacklistResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = AddBlacklistResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class AddBlacklistResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddBlacklistResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddBlacklistResponse, self).to_map()
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
            temp_model = AddBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTaskRequestCallTimeList(TeaModel):
    def __init__(self, call_time=None):
        self.call_time = call_time  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTaskRequestCallTimeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        return self


class AddTaskRequestSendSmsPlan(TeaModel):
    def __init__(self, intent_tags=None, sms_template_id=None):
        # 意向标签
        self.intent_tags = intent_tags  # type: list[str]
        # 短信模板ID
        self.sms_template_id = sms_template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTaskRequestSendSmsPlan, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_tags is not None:
            result['IntentTags'] = self.intent_tags
        if self.sms_template_id is not None:
            result['SmsTemplateId'] = self.sms_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentTags') is not None:
            self.intent_tags = m.get('IntentTags')
        if m.get('SmsTemplateId') is not None:
            self.sms_template_id = m.get('SmsTemplateId')
        return self


class AddTaskRequest(TeaModel):
    def __init__(self, call_time_list=None, callback_url=None, max_concurrency=None, name=None, owner_id=None,
                 play_sleep_val=None, play_times=None, recall_type=None, record_path=None, repeat_count=None, repeat_interval=None,
                 repeat_reason=None, repeat_times=None, resource_owner_account=None, resource_owner_id=None, send_sms_plan=None,
                 start_time=None, task_type=None, template_id=None, template_type=None):
        # 外呼时间
        self.call_time_list = call_time_list  # type: list[AddTaskRequestCallTimeList]
        # 回调地址
        self.callback_url = callback_url  # type: str
        # 并发数
        self.max_concurrency = max_concurrency  # type: long
        # 任务名称
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        # 播放间隔时长
        self.play_sleep_val = play_sleep_val  # type: long
        # 录音播放次数
        self.play_times = play_times  # type: long
        # 重呼配置
        self.recall_type = recall_type  # type: long
        # 录音地址
        self.record_path = record_path  # type: str
        # 重呼次数
        self.repeat_count = repeat_count  # type: long
        # 重呼间隔
        self.repeat_interval = repeat_interval  # type: long
        # 重呼条件
        self.repeat_reason = repeat_reason  # type: list[str]
        # 重呼时间
        self.repeat_times = repeat_times  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 短信发送规则
        self.send_sms_plan = send_sms_plan  # type: list[AddTaskRequestSendSmsPlan]
        # 任务启动日期
        self.start_time = start_time  # type: str
        # 任务类型
        self.task_type = task_type  # type: long
        # 话术模板ID
        self.template_id = template_id  # type: long
        # 话术模板类型
        self.template_type = template_type  # type: long

    def validate(self):
        if self.call_time_list:
            for k in self.call_time_list:
                if k:
                    k.validate()
        if self.send_sms_plan:
            for k in self.send_sms_plan:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallTimeList'] = []
        if self.call_time_list is not None:
            for k in self.call_time_list:
                result['CallTimeList'].append(k.to_map() if k else None)
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_sleep_val is not None:
            result['PlaySleepVal'] = self.play_sleep_val
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.recall_type is not None:
            result['RecallType'] = self.recall_type
        if self.record_path is not None:
            result['RecordPath'] = self.record_path
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.repeat_reason is not None:
            result['RepeatReason'] = self.repeat_reason
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['SendSmsPlan'] = []
        if self.send_sms_plan is not None:
            for k in self.send_sms_plan:
                result['SendSmsPlan'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.call_time_list = []
        if m.get('CallTimeList') is not None:
            for k in m.get('CallTimeList'):
                temp_model = AddTaskRequestCallTimeList()
                self.call_time_list.append(temp_model.from_map(k))
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlaySleepVal') is not None:
            self.play_sleep_val = m.get('PlaySleepVal')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')
        if m.get('RecordPath') is not None:
            self.record_path = m.get('RecordPath')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('RepeatReason') is not None:
            self.repeat_reason = m.get('RepeatReason')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.send_sms_plan = []
        if m.get('SendSmsPlan') is not None:
            for k in m.get('SendSmsPlan'):
                temp_model = AddTaskRequestSendSmsPlan()
                self.send_sms_plan.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class AddTaskShrinkRequest(TeaModel):
    def __init__(self, call_time_list_shrink=None, callback_url=None, max_concurrency=None, name=None,
                 owner_id=None, play_sleep_val=None, play_times=None, recall_type=None, record_path=None, repeat_count=None,
                 repeat_interval=None, repeat_reason_shrink=None, repeat_times_shrink=None, resource_owner_account=None,
                 resource_owner_id=None, send_sms_plan_shrink=None, start_time=None, task_type=None, template_id=None,
                 template_type=None):
        # 外呼时间
        self.call_time_list_shrink = call_time_list_shrink  # type: str
        # 回调地址
        self.callback_url = callback_url  # type: str
        # 并发数
        self.max_concurrency = max_concurrency  # type: long
        # 任务名称
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        # 播放间隔时长
        self.play_sleep_val = play_sleep_val  # type: long
        # 录音播放次数
        self.play_times = play_times  # type: long
        # 重呼配置
        self.recall_type = recall_type  # type: long
        # 录音地址
        self.record_path = record_path  # type: str
        # 重呼次数
        self.repeat_count = repeat_count  # type: long
        # 重呼间隔
        self.repeat_interval = repeat_interval  # type: long
        # 重呼条件
        self.repeat_reason_shrink = repeat_reason_shrink  # type: str
        # 重呼时间
        self.repeat_times_shrink = repeat_times_shrink  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 短信发送规则
        self.send_sms_plan_shrink = send_sms_plan_shrink  # type: str
        # 任务启动日期
        self.start_time = start_time  # type: str
        # 任务类型
        self.task_type = task_type  # type: long
        # 话术模板ID
        self.template_id = template_id  # type: long
        # 话术模板类型
        self.template_type = template_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_time_list_shrink is not None:
            result['CallTimeList'] = self.call_time_list_shrink
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_sleep_val is not None:
            result['PlaySleepVal'] = self.play_sleep_val
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.recall_type is not None:
            result['RecallType'] = self.recall_type
        if self.record_path is not None:
            result['RecordPath'] = self.record_path
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.repeat_reason_shrink is not None:
            result['RepeatReason'] = self.repeat_reason_shrink
        if self.repeat_times_shrink is not None:
            result['RepeatTimes'] = self.repeat_times_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_sms_plan_shrink is not None:
            result['SendSmsPlan'] = self.send_sms_plan_shrink
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallTimeList') is not None:
            self.call_time_list_shrink = m.get('CallTimeList')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlaySleepVal') is not None:
            self.play_sleep_val = m.get('PlaySleepVal')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')
        if m.get('RecordPath') is not None:
            self.record_path = m.get('RecordPath')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('RepeatReason') is not None:
            self.repeat_reason_shrink = m.get('RepeatReason')
        if m.get('RepeatTimes') is not None:
            self.repeat_times_shrink = m.get('RepeatTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendSmsPlan') is not None:
            self.send_sms_plan_shrink = m.get('SendSmsPlan')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class AddTaskResponseBodyModel(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddTaskResponseBodyModel, self).to_map()
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


class AddTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: AddTaskResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(AddTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = AddTaskResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class AddTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddTaskResponse, self).to_map()
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
            temp_model = AddTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgentCancelCallRequest(TeaModel):
    def __init__(self, agent_id=None, agent_tag=None, numbers=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, tags=None):
        # 坐席ID
        self.agent_id = agent_id  # type: long
        # 坐席标签
        self.agent_tag = agent_tag  # type: str
        # 号码列表
        self.numbers = numbers  # type: list[str]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 用户自定义标签列表
        self.tags = tags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AgentCancelCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AgentCancelCallShrinkRequest(TeaModel):
    def __init__(self, agent_id=None, agent_tag=None, numbers_shrink=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, tags_shrink=None):
        # 坐席ID
        self.agent_id = agent_id  # type: long
        # 坐席标签
        self.agent_tag = agent_tag  # type: str
        # 号码列表
        self.numbers_shrink = numbers_shrink  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 用户自定义标签列表
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AgentCancelCallShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag
        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')
        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class AgentCancelCallResponseBodyModel(TeaModel):
    def __init__(self, un_handle_numbers=None):
        # 错误手机列表
        self.un_handle_numbers = un_handle_numbers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AgentCancelCallResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.un_handle_numbers is not None:
            result['UnHandleNumbers'] = self.un_handle_numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UnHandleNumbers') is not None:
            self.un_handle_numbers = m.get('UnHandleNumbers')
        return self


class AgentCancelCallResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: AgentCancelCallResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(AgentCancelCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = AgentCancelCallResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class AgentCancelCallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AgentCancelCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AgentCancelCallResponse, self).to_map()
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
            temp_model = AgentCancelCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgentRecoverCallRequest(TeaModel):
    def __init__(self, agent_id=None, agent_tag=None, begin_import_time=None, end_import_time=None, numbers=None,
                 owner_id=None, resource_owner_account=None, resource_owner_id=None, tags=None):
        # 坐席ID
        self.agent_id = agent_id  # type: long
        # 坐席标签
        self.agent_tag = agent_tag  # type: str
        # 查询开始导入时间
        self.begin_import_time = begin_import_time  # type: str
        # 查询结束导入时间
        self.end_import_time = end_import_time  # type: str
        # 号码列表
        self.numbers = numbers  # type: list[str]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 用户自定义标签列表
        self.tags = tags  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AgentRecoverCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag
        if self.begin_import_time is not None:
            result['BeginImportTime'] = self.begin_import_time
        if self.end_import_time is not None:
            result['EndImportTime'] = self.end_import_time
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')
        if m.get('BeginImportTime') is not None:
            self.begin_import_time = m.get('BeginImportTime')
        if m.get('EndImportTime') is not None:
            self.end_import_time = m.get('EndImportTime')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class AgentRecoverCallShrinkRequest(TeaModel):
    def __init__(self, agent_id=None, agent_tag=None, begin_import_time=None, end_import_time=None,
                 numbers_shrink=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, tags_shrink=None):
        # 坐席ID
        self.agent_id = agent_id  # type: long
        # 坐席标签
        self.agent_tag = agent_tag  # type: str
        # 查询开始导入时间
        self.begin_import_time = begin_import_time  # type: str
        # 查询结束导入时间
        self.end_import_time = end_import_time  # type: str
        # 号码列表
        self.numbers_shrink = numbers_shrink  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 用户自定义标签列表
        self.tags_shrink = tags_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AgentRecoverCallShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag
        if self.begin_import_time is not None:
            result['BeginImportTime'] = self.begin_import_time
        if self.end_import_time is not None:
            result['EndImportTime'] = self.end_import_time
        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')
        if m.get('BeginImportTime') is not None:
            self.begin_import_time = m.get('BeginImportTime')
        if m.get('EndImportTime') is not None:
            self.end_import_time = m.get('EndImportTime')
        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class AgentRecoverCallResponseBodyModel(TeaModel):
    def __init__(self, un_handle_numbers=None):
        # 错误手机列表
        self.un_handle_numbers = un_handle_numbers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AgentRecoverCallResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.un_handle_numbers is not None:
            result['UnHandleNumbers'] = self.un_handle_numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UnHandleNumbers') is not None:
            self.un_handle_numbers = m.get('UnHandleNumbers')
        return self


class AgentRecoverCallResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: AgentRecoverCallResponseBodyModel
        self.request_id = request_id  # type: str
        # 坐席标签
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(AgentRecoverCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = AgentRecoverCallResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class AgentRecoverCallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AgentRecoverCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AgentRecoverCallResponse, self).to_map()
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
            temp_model = AgentRecoverCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailsRequest(TeaModel):
    def __init__(self, batch_id=None, end_time=None, number_status=None, numbers=None, owner_id=None, page_no=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None, start_time=None, task_id=None):
        # 批次id
        self.batch_id = batch_id  # type: long
        # 结束导入时间
        self.end_time = end_time  # type: str
        # 号码状态
        self.number_status = number_status  # type: long
        # 号码列表
        self.numbers = numbers  # type: list[str]
        self.owner_id = owner_id  # type: long
        # 页数
        self.page_no = page_no  # type: long
        # 每页条数
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 开始导入时间
        self.start_time = start_time  # type: str
        # 任务id
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.number_status is not None:
            result['NumberStatus'] = self.number_status
        if self.numbers is not None:
            result['Numbers'] = self.numbers
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
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NumberStatus') is not None:
            self.number_status = m.get('NumberStatus')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
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
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetailsShrinkRequest(TeaModel):
    def __init__(self, batch_id=None, end_time=None, number_status=None, numbers_shrink=None, owner_id=None,
                 page_no=None, page_size=None, resource_owner_account=None, resource_owner_id=None, start_time=None,
                 task_id=None):
        # 批次id
        self.batch_id = batch_id  # type: long
        # 结束导入时间
        self.end_time = end_time  # type: str
        # 号码状态
        self.number_status = number_status  # type: long
        # 号码列表
        self.numbers_shrink = numbers_shrink  # type: str
        self.owner_id = owner_id  # type: long
        # 页数
        self.page_no = page_no  # type: long
        # 每页条数
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 开始导入时间
        self.start_time = start_time  # type: str
        # 任务id
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.number_status is not None:
            result['NumberStatus'] = self.number_status
        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink
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
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NumberStatus') is not None:
            self.number_status = m.get('NumberStatus')
        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')
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
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetailsResponseBodyModelList(TeaModel):
    def __init__(self, batch_id=None, call_desc=None, call_id=None, call_status=None, call_type=None,
                 import_time=None, intercept_reason=None, number=None, number_desc=None, number_md5=None, number_status=None,
                 tag=None, task_id=None):
        # 批次号
        self.batch_id = batch_id  # type: long
        # 呼叫状态描述
        self.call_desc = call_desc  # type: str
        # 外呼ID
        self.call_id = call_id  # type: str
        # 呼叫状态
        self.call_status = call_status  # type: long
        # 外呼类型
        self.call_type = call_type  # type: long
        # 导入时间
        self.import_time = import_time  # type: str
        # 拦截原因
        self.intercept_reason = intercept_reason  # type: str
        # 外呼号码
        self.number = number  # type: str
        # 号码状态描述
        self.number_desc = number_desc  # type: str
        # 外呼号码MD5
        self.number_md5 = number_md5  # type: str
        # 号码状态
        self.number_status = number_status  # type: long
        # 用户自定义标签
        self.tag = tag  # type: str
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetailsResponseBodyModelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.call_desc is not None:
            result['CallDesc'] = self.call_desc
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_status is not None:
            result['CallStatus'] = self.call_status
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.import_time is not None:
            result['ImportTime'] = self.import_time
        if self.intercept_reason is not None:
            result['InterceptReason'] = self.intercept_reason
        if self.number is not None:
            result['Number'] = self.number
        if self.number_desc is not None:
            result['NumberDesc'] = self.number_desc
        if self.number_md5 is not None:
            result['NumberMD5'] = self.number_md5
        if self.number_status is not None:
            result['NumberStatus'] = self.number_status
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('CallDesc') is not None:
            self.call_desc = m.get('CallDesc')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('ImportTime') is not None:
            self.import_time = m.get('ImportTime')
        if m.get('InterceptReason') is not None:
            self.intercept_reason = m.get('InterceptReason')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('NumberDesc') is not None:
            self.number_desc = m.get('NumberDesc')
        if m.get('NumberMD5') is not None:
            self.number_md5 = m.get('NumberMD5')
        if m.get('NumberStatus') is not None:
            self.number_status = m.get('NumberStatus')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetailsResponseBodyModel(TeaModel):
    def __init__(self, list=None, page_no=None, page_size=None, total_count=None, total_page=None):
        self.list = list  # type: list[DetailsResponseBodyModelList]
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.total_page = total_page  # type: float

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetailsResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DetailsResponseBodyModelList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DetailsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: DetailsResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(DetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = DetailsResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DetailsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetailsResponse, self).to_map()
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
            temp_model = DetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditTaskRequestCallTimeList(TeaModel):
    def __init__(self, call_time=None):
        self.call_time = call_time  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditTaskRequestCallTimeList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        return self


class EditTaskRequestSendSmsPlan(TeaModel):
    def __init__(self, intent_tags=None, sms_template_id=None):
        # 意向标签
        self.intent_tags = intent_tags  # type: list[str]
        # 短信模板ID
        self.sms_template_id = sms_template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditTaskRequestSendSmsPlan, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_tags is not None:
            result['IntentTags'] = self.intent_tags
        if self.sms_template_id is not None:
            result['SmsTemplateId'] = self.sms_template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentTags') is not None:
            self.intent_tags = m.get('IntentTags')
        if m.get('SmsTemplateId') is not None:
            self.sms_template_id = m.get('SmsTemplateId')
        return self


class EditTaskRequest(TeaModel):
    def __init__(self, call_time_list=None, callback_url=None, max_concurrency=None, name=None, owner_id=None,
                 play_sleep_val=None, play_times=None, recall_type=None, record_path=None, repeat_count=None, repeat_interval=None,
                 repeat_reason=None, repeat_times=None, resource_owner_account=None, resource_owner_id=None, send_sms_plan=None,
                 status=None, task_id=None, template_id=None, template_type=None):
        # 外呼时间
        self.call_time_list = call_time_list  # type: list[EditTaskRequestCallTimeList]
        # 回调地址
        self.callback_url = callback_url  # type: str
        # 并发数
        self.max_concurrency = max_concurrency  # type: long
        # 任务名称
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        # 播放间隔时长
        self.play_sleep_val = play_sleep_val  # type: long
        # 录音播放次数
        self.play_times = play_times  # type: long
        # 重呼配置
        self.recall_type = recall_type  # type: long
        # 录音地址
        self.record_path = record_path  # type: str
        # 重呼次数
        self.repeat_count = repeat_count  # type: long
        # 重呼间隔
        self.repeat_interval = repeat_interval  # type: long
        # 重呼条件
        self.repeat_reason = repeat_reason  # type: list[long]
        # 重呼时间
        self.repeat_times = repeat_times  # type: list[str]
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 短信发送规则
        self.send_sms_plan = send_sms_plan  # type: list[EditTaskRequestSendSmsPlan]
        # 任务状态
        self.status = status  # type: long
        # 任务id
        self.task_id = task_id  # type: long
        # 话术模板ID
        self.template_id = template_id  # type: long
        # 话术模板类型
        self.template_type = template_type  # type: long

    def validate(self):
        if self.call_time_list:
            for k in self.call_time_list:
                if k:
                    k.validate()
        if self.send_sms_plan:
            for k in self.send_sms_plan:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(EditTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallTimeList'] = []
        if self.call_time_list is not None:
            for k in self.call_time_list:
                result['CallTimeList'].append(k.to_map() if k else None)
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_sleep_val is not None:
            result['PlaySleepVal'] = self.play_sleep_val
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.recall_type is not None:
            result['RecallType'] = self.recall_type
        if self.record_path is not None:
            result['RecordPath'] = self.record_path
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.repeat_reason is not None:
            result['RepeatReason'] = self.repeat_reason
        if self.repeat_times is not None:
            result['RepeatTimes'] = self.repeat_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['SendSmsPlan'] = []
        if self.send_sms_plan is not None:
            for k in self.send_sms_plan:
                result['SendSmsPlan'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.call_time_list = []
        if m.get('CallTimeList') is not None:
            for k in m.get('CallTimeList'):
                temp_model = EditTaskRequestCallTimeList()
                self.call_time_list.append(temp_model.from_map(k))
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlaySleepVal') is not None:
            self.play_sleep_val = m.get('PlaySleepVal')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')
        if m.get('RecordPath') is not None:
            self.record_path = m.get('RecordPath')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('RepeatReason') is not None:
            self.repeat_reason = m.get('RepeatReason')
        if m.get('RepeatTimes') is not None:
            self.repeat_times = m.get('RepeatTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.send_sms_plan = []
        if m.get('SendSmsPlan') is not None:
            for k in m.get('SendSmsPlan'):
                temp_model = EditTaskRequestSendSmsPlan()
                self.send_sms_plan.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class EditTaskShrinkRequest(TeaModel):
    def __init__(self, call_time_list_shrink=None, callback_url=None, max_concurrency=None, name=None,
                 owner_id=None, play_sleep_val=None, play_times=None, recall_type=None, record_path=None, repeat_count=None,
                 repeat_interval=None, repeat_reason_shrink=None, repeat_times_shrink=None, resource_owner_account=None,
                 resource_owner_id=None, send_sms_plan_shrink=None, status=None, task_id=None, template_id=None, template_type=None):
        # 外呼时间
        self.call_time_list_shrink = call_time_list_shrink  # type: str
        # 回调地址
        self.callback_url = callback_url  # type: str
        # 并发数
        self.max_concurrency = max_concurrency  # type: long
        # 任务名称
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        # 播放间隔时长
        self.play_sleep_val = play_sleep_val  # type: long
        # 录音播放次数
        self.play_times = play_times  # type: long
        # 重呼配置
        self.recall_type = recall_type  # type: long
        # 录音地址
        self.record_path = record_path  # type: str
        # 重呼次数
        self.repeat_count = repeat_count  # type: long
        # 重呼间隔
        self.repeat_interval = repeat_interval  # type: long
        # 重呼条件
        self.repeat_reason_shrink = repeat_reason_shrink  # type: str
        # 重呼时间
        self.repeat_times_shrink = repeat_times_shrink  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 短信发送规则
        self.send_sms_plan_shrink = send_sms_plan_shrink  # type: str
        # 任务状态
        self.status = status  # type: long
        # 任务id
        self.task_id = task_id  # type: long
        # 话术模板ID
        self.template_id = template_id  # type: long
        # 话术模板类型
        self.template_type = template_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_time_list_shrink is not None:
            result['CallTimeList'] = self.call_time_list_shrink
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_sleep_val is not None:
            result['PlaySleepVal'] = self.play_sleep_val
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.recall_type is not None:
            result['RecallType'] = self.recall_type
        if self.record_path is not None:
            result['RecordPath'] = self.record_path
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.repeat_reason_shrink is not None:
            result['RepeatReason'] = self.repeat_reason_shrink
        if self.repeat_times_shrink is not None:
            result['RepeatTimes'] = self.repeat_times_shrink
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_sms_plan_shrink is not None:
            result['SendSmsPlan'] = self.send_sms_plan_shrink
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallTimeList') is not None:
            self.call_time_list_shrink = m.get('CallTimeList')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlaySleepVal') is not None:
            self.play_sleep_val = m.get('PlaySleepVal')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')
        if m.get('RecordPath') is not None:
            self.record_path = m.get('RecordPath')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('RepeatReason') is not None:
            self.repeat_reason_shrink = m.get('RepeatReason')
        if m.get('RepeatTimes') is not None:
            self.repeat_times_shrink = m.get('RepeatTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendSmsPlan') is not None:
            self.send_sms_plan_shrink = m.get('SendSmsPlan')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class EditTaskResponseBodyModel(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditTaskResponseBodyModel, self).to_map()
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


class EditTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: EditTaskResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(EditTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = EditTaskResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class EditTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EditTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditTaskResponse, self).to_map()
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
            temp_model = EditTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportNumberRequestCustomers(TeaModel):
    def __init__(self, client_url=None, number=None, number_md5=None, properties=None, tag=None):
        self.client_url = client_url  # type: str
        self.number = number  # type: str
        self.number_md5 = number_md5  # type: str
        self.properties = properties  # type: dict[str, any]
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportNumberRequestCustomers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_url is not None:
            result['ClientUrl'] = self.client_url
        if self.number is not None:
            result['Number'] = self.number
        if self.number_md5 is not None:
            result['NumberMD5'] = self.number_md5
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientUrl') is not None:
            self.client_url = m.get('ClientUrl')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('NumberMD5') is not None:
            self.number_md5 = m.get('NumberMD5')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ImportNumberRequest(TeaModel):
    def __init__(self, customers=None, fail_return=None, out_id=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, task_id=None):
        self.customers = customers  # type: list[ImportNumberRequestCustomers]
        self.fail_return = fail_return  # type: long
        self.out_id = out_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long

    def validate(self):
        if self.customers:
            for k in self.customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ImportNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Customers'] = []
        if self.customers is not None:
            for k in self.customers:
                result['Customers'].append(k.to_map() if k else None)
        if self.fail_return is not None:
            result['FailReturn'] = self.fail_return
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.customers = []
        if m.get('Customers') is not None:
            for k in m.get('Customers'):
                temp_model = ImportNumberRequestCustomers()
                self.customers.append(temp_model.from_map(k))
        if m.get('FailReturn') is not None:
            self.fail_return = m.get('FailReturn')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ImportNumberShrinkRequest(TeaModel):
    def __init__(self, customers_shrink=None, fail_return=None, out_id=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.customers_shrink = customers_shrink  # type: str
        self.fail_return = fail_return  # type: long
        self.out_id = out_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportNumberShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customers_shrink is not None:
            result['Customers'] = self.customers_shrink
        if self.fail_return is not None:
            result['FailReturn'] = self.fail_return
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Customers') is not None:
            self.customers_shrink = m.get('Customers')
        if m.get('FailReturn') is not None:
            self.fail_return = m.get('FailReturn')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ImportNumberResponseBodyModel(TeaModel):
    def __init__(self, batch_id=None, code=None, data=None, import_num=None, message=None):
        self.batch_id = batch_id  # type: long
        self.code = code  # type: long
        self.data = data  # type: str
        self.import_num = import_num  # type: long
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportNumberResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.import_num is not None:
            result['ImportNum'] = self.import_num
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ImportNum') is not None:
            self.import_num = m.get('ImportNum')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ImportNumberResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: ImportNumberResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(ImportNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ImportNumberResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ImportNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportNumberResponse, self).to_map()
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
            temp_model = ImportNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageRequest(TeaModel):
    def __init__(self, numbers=None, owner_id=None, page_no=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.numbers = numbers  # type: list[str]
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.numbers is not None:
            result['Numbers'] = self.numbers
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
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
        return self


class PageShrinkRequest(TeaModel):
    def __init__(self, numbers_shrink=None, owner_id=None, page_no=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.numbers_shrink = numbers_shrink  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')
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
        return self


class PageResponseBodyModelList(TeaModel):
    def __init__(self, create_time=None, expiration_time=None, number=None, number_md5=None, remark=None):
        # 添加时间
        self.create_time = create_time  # type: str
        # 过期时间
        self.expiration_time = expiration_time  # type: str
        # 手机号码
        self.number = number  # type: str
        # 手机号MD5
        self.number_md5 = number_md5  # type: str
        # 备注
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageResponseBodyModelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time
        if self.number is not None:
            result['Number'] = self.number
        if self.number_md5 is not None:
            result['NumberMD5'] = self.number_md5
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('NumberMD5') is not None:
            self.number_md5 = m.get('NumberMD5')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class PageResponseBodyModel(TeaModel):
    def __init__(self, list=None, page_no=None, page_size=None, total_count=None, total_page=None):
        self.list = list  # type: list[PageResponseBodyModelList]
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.total_page = total_page  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PageResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = PageResponseBodyModelList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class PageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: PageResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(PageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = PageResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class PageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PageResponse, self).to_map()
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
            temp_model = PageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsTemplateCreateRequest(TeaModel):
    def __init__(self, content=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, sign=None,
                 sms_type=None, template_name=None, template_type=None):
        # 短信内容
        self.content = content  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 短信签名
        self.sign = sign  # type: str
        # 短信类型
        self.sms_type = sms_type  # type: long
        # 模板名称
        self.template_name = template_name  # type: str
        # 模板类型
        self.template_type = template_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsTemplateCreateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.sms_type is not None:
            result['SmsType'] = self.sms_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class SmsTemplateCreateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.timestamp = timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsTemplateCreateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class SmsTemplateCreateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SmsTemplateCreateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SmsTemplateCreateResponse, self).to_map()
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
            temp_model = SmsTemplateCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmsTemplatePageListRequest(TeaModel):
    def __init__(self, owner_id=None, page_no=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, sign=None, sms_type=None, status=None, template_id=None, template_type=None):
        self.owner_id = owner_id  # type: long
        # 页码
        self.page_no = page_no  # type: long
        # 每页条数
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 短信签名
        self.sign = sign  # type: str
        # 短信类型
        self.sms_type = sms_type  # type: long
        # 模板状态
        self.status = status  # type: long
        # 模板ID
        self.template_id = template_id  # type: long
        # 模板类型
        self.template_type = template_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsTemplatePageListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.sms_type is not None:
            result['SmsType'] = self.sms_type
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class SmsTemplatePageListResponseBodyModelList(TeaModel):
    def __init__(self, content=None, create_time=None, properties=None, short_url_task_id=None, sign=None,
                 sms_type=None, status=None, template_id=None, template_name=None, template_type=None):
        # 短信内容
        self.content = content  # type: str
        # 创建时间
        self.create_time = create_time  # type: str
        # 模板所需参数
        self.properties = properties  # type: str
        # 智能短链ID
        self.short_url_task_id = short_url_task_id  # type: long
        # 短信签名
        self.sign = sign  # type: str
        # 短信类型
        self.sms_type = sms_type  # type: str
        # 模板状态
        self.status = status  # type: long
        # 模板ID
        self.template_id = template_id  # type: long
        # 模板名称
        self.template_name = template_name  # type: str
        # 模板类型
        self.template_type = template_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmsTemplatePageListResponseBodyModelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.short_url_task_id is not None:
            result['ShortUrlTaskId'] = self.short_url_task_id
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.sms_type is not None:
            result['SmsType'] = self.sms_type
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('ShortUrlTaskId') is not None:
            self.short_url_task_id = m.get('ShortUrlTaskId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class SmsTemplatePageListResponseBodyModel(TeaModel):
    def __init__(self, list=None, page_no=None, page_size=None, total_count=None, total_page=None):
        self.list = list  # type: list[SmsTemplatePageListResponseBodyModelList]
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.total_page = total_page  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SmsTemplatePageListResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = SmsTemplatePageListResponseBodyModelList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class SmsTemplatePageListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: SmsTemplatePageListResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(SmsTemplatePageListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = SmsTemplatePageListResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class SmsTemplatePageListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SmsTemplatePageListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SmsTemplatePageListResponse, self).to_map()
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
            temp_model = SmsTemplatePageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaskCallChatsRequest(TeaModel):
    def __init__(self, agent_id=None, agent_tag=None, call_id=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, task_id=None):
        # 坐席ID
        self.agent_id = agent_id  # type: long
        # 坐席标签
        self.agent_tag = agent_tag  # type: str
        # 外呼ID
        self.call_id = call_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCallChatsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TaskCallChatsResponseBodyModel(TeaModel):
    def __init__(self, content=None, create_time=None, from_number=None):
        # 说话内容
        self.content = content  # type: str
        # 说话时间
        self.create_time = create_time  # type: str
        # 说话号码
        self.from_number = from_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCallChatsResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.from_number is not None:
            result['FromNumber'] = self.from_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FromNumber') is not None:
            self.from_number = m.get('FromNumber')
        return self


class TaskCallChatsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: list[TaskCallChatsResponseBodyModel]
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TaskCallChatsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = TaskCallChatsResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class TaskCallChatsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TaskCallChatsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TaskCallChatsResponse, self).to_map()
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
            temp_model = TaskCallChatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaskCallInfoRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCallInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TaskCallInfoResponseBodyModel(TeaModel):
    def __init__(self, finish_total=None, total=None, un_call_total=None):
        self.finish_total = finish_total  # type: long
        self.total = total  # type: long
        self.un_call_total = un_call_total  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCallInfoResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_total is not None:
            result['FinishTotal'] = self.finish_total
        if self.total is not None:
            result['Total'] = self.total
        if self.un_call_total is not None:
            result['UnCallTotal'] = self.un_call_total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FinishTotal') is not None:
            self.finish_total = m.get('FinishTotal')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('UnCallTotal') is not None:
            self.un_call_total = m.get('UnCallTotal')
        return self


class TaskCallInfoResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: TaskCallInfoResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(TaskCallInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = TaskCallInfoResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class TaskCallInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TaskCallInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TaskCallInfoResponse, self).to_map()
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
            temp_model = TaskCallInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaskCallListRequest(TeaModel):
    def __init__(self, batch_id=None, call_date=None, end_call_date=None, intent_tags=None, numbers=None,
                 owner_id=None, page=None, page_size=None, resource_owner_account=None, resource_owner_id=None, task_id=None):
        # 导入号码时返回的批次号
        self.batch_id = batch_id  # type: str
        # 开始外呼时间
        self.call_date = call_date  # type: str
        # 结束外呼时间
        self.end_call_date = end_call_date  # type: str
        # 意向标签
        self.intent_tags = intent_tags  # type: list[str]
        # 号码列表
        self.numbers = numbers  # type: list[str]
        self.owner_id = owner_id  # type: long
        # 页数
        self.page = page  # type: long
        # 每页外呼记录数,正整数，默认10000
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCallListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.call_date is not None:
            result['CallDate'] = self.call_date
        if self.end_call_date is not None:
            result['EndCallDate'] = self.end_call_date
        if self.intent_tags is not None:
            result['IntentTags'] = self.intent_tags
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')
        if m.get('EndCallDate') is not None:
            self.end_call_date = m.get('EndCallDate')
        if m.get('IntentTags') is not None:
            self.intent_tags = m.get('IntentTags')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TaskCallListShrinkRequest(TeaModel):
    def __init__(self, batch_id=None, call_date=None, end_call_date=None, intent_tags_shrink=None,
                 numbers_shrink=None, owner_id=None, page=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, task_id=None):
        # 导入号码时返回的批次号
        self.batch_id = batch_id  # type: str
        # 开始外呼时间
        self.call_date = call_date  # type: str
        # 结束外呼时间
        self.end_call_date = end_call_date  # type: str
        # 意向标签
        self.intent_tags_shrink = intent_tags_shrink  # type: str
        # 号码列表
        self.numbers_shrink = numbers_shrink  # type: str
        self.owner_id = owner_id  # type: long
        # 页数
        self.page = page  # type: long
        # 每页外呼记录数,正整数，默认10000
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCallListShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.call_date is not None:
            result['CallDate'] = self.call_date
        if self.end_call_date is not None:
            result['EndCallDate'] = self.end_call_date
        if self.intent_tags_shrink is not None:
            result['IntentTags'] = self.intent_tags_shrink
        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')
        if m.get('EndCallDate') is not None:
            self.end_call_date = m.get('EndCallDate')
        if m.get('IntentTags') is not None:
            self.intent_tags_shrink = m.get('IntentTags')
        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TaskCallListResponseBodyModelList(TeaModel):
    def __init__(self, add_wx=None, add_wx_status=None, agent_extension=None, agent_id=None,
                 agent_speaking_duration=None, agent_speaking_time=None, agent_tag=None, answer_recall=None, answer_time=None,
                 batch_id=None, call_begin_time=None, call_id=None, call_times=None, call_type=None, chat_record=None,
                 gateway=None, hangup_time=None, hangup_type=None, import_time=None, individual_tag=None,
                 intent_description=None, intent_tag=None, intercept_reason=None, keywords=None, number=None, number_md5=None,
                 properties=None, remark=None, ring_time=None, sms=None, speaking_duration=None, speaking_time=None,
                 speaking_turns=None, status=None, status_code=None, status_description=None, tag=None, task_id=None,
                 template_id=None, transfer_status=None, transfer_status_code=None):
        # 加微
        self.add_wx = add_wx  # type: long
        # 加微进度
        self.add_wx_status = add_wx_status  # type: str
        # 坐席分机
        self.agent_extension = agent_extension  # type: str
        # 坐席ID
        self.agent_id = agent_id  # type: long
        # 人工通话时长
        self.agent_speaking_duration = agent_speaking_duration  # type: long
        # 人工通话时长
        self.agent_speaking_time = agent_speaking_time  # type: str
        # 坐席标签
        self.agent_tag = agent_tag  # type: str
        # 是否接通重呼
        self.answer_recall = answer_recall  # type: long
        # 接通时间
        self.answer_time = answer_time  # type: str
        # 批次ID
        self.batch_id = batch_id  # type: str
        # 开始通话时间
        self.call_begin_time = call_begin_time  # type: str
        # 外呼ID
        self.call_id = call_id  # type: str
        # 呼叫次数
        self.call_times = call_times  # type: str
        # 外呼类型
        self.call_type = call_type  # type: long
        # 对话录音
        self.chat_record = chat_record  # type: str
        # 外呼网关
        self.gateway = gateway  # type: str
        # 挂断时间
        self.hangup_time = hangup_time  # type: str
        # 挂机方式
        self.hangup_type = hangup_type  # type: long
        # 导入时间
        self.import_time = import_time  # type: str
        # 个性标签
        self.individual_tag = individual_tag  # type: str
        # 意向说明
        self.intent_description = intent_description  # type: str
        # 意向标签
        self.intent_tag = intent_tag  # type: str
        # 拦截原因
        self.intercept_reason = intercept_reason  # type: str
        # 回复关键词
        self.keywords = keywords  # type: str
        # 外呼号码
        self.number = number  # type: str
        # 外呼号码MD5
        self.number_md5 = number_md5  # type: str
        # 参数
        self.properties = properties  # type: str
        # 备注
        self.remark = remark  # type: str
        # 振铃时长
        self.ring_time = ring_time  # type: long
        # 挂机短信
        self.sms = sms  # type: str
        # AI通话时长
        self.speaking_duration = speaking_duration  # type: long
        # AI通话时长
        self.speaking_time = speaking_time  # type: str
        # 对话轮次
        self.speaking_turns = speaking_turns  # type: str
        # 外呼状态
        self.status = status  # type: str
        # 外呼状态编码
        self.status_code = status_code  # type: long
        # 外呼状态描述
        self.status_description = status_description  # type: str
        # 用户自定义标签
        self.tag = tag  # type: str
        # 外呼任务ID
        self.task_id = task_id  # type: long
        # AI话术ID
        self.template_id = template_id  # type: long
        # 转人工状态
        self.transfer_status = transfer_status  # type: str
        # 转人工状态编码
        self.transfer_status_code = transfer_status_code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCallListResponseBodyModelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_wx is not None:
            result['AddWx'] = self.add_wx
        if self.add_wx_status is not None:
            result['AddWxStatus'] = self.add_wx_status
        if self.agent_extension is not None:
            result['AgentExtension'] = self.agent_extension
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_speaking_duration is not None:
            result['AgentSpeakingDuration'] = self.agent_speaking_duration
        if self.agent_speaking_time is not None:
            result['AgentSpeakingTime'] = self.agent_speaking_time
        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag
        if self.answer_recall is not None:
            result['AnswerRecall'] = self.answer_recall
        if self.answer_time is not None:
            result['AnswerTime'] = self.answer_time
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.call_begin_time is not None:
            result['CallBeginTime'] = self.call_begin_time
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_times is not None:
            result['CallTimes'] = self.call_times
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.chat_record is not None:
            result['ChatRecord'] = self.chat_record
        if self.gateway is not None:
            result['Gateway'] = self.gateway
        if self.hangup_time is not None:
            result['HangupTime'] = self.hangup_time
        if self.hangup_type is not None:
            result['HangupType'] = self.hangup_type
        if self.import_time is not None:
            result['ImportTime'] = self.import_time
        if self.individual_tag is not None:
            result['IndividualTag'] = self.individual_tag
        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description
        if self.intent_tag is not None:
            result['IntentTag'] = self.intent_tag
        if self.intercept_reason is not None:
            result['InterceptReason'] = self.intercept_reason
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.number is not None:
            result['Number'] = self.number
        if self.number_md5 is not None:
            result['NumberMD5'] = self.number_md5
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.ring_time is not None:
            result['RingTime'] = self.ring_time
        if self.sms is not None:
            result['Sms'] = self.sms
        if self.speaking_duration is not None:
            result['SpeakingDuration'] = self.speaking_duration
        if self.speaking_time is not None:
            result['SpeakingTime'] = self.speaking_time
        if self.speaking_turns is not None:
            result['SpeakingTurns'] = self.speaking_turns
        if self.status is not None:
            result['Status'] = self.status
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.status_description is not None:
            result['StatusDescription'] = self.status_description
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.transfer_status is not None:
            result['TransferStatus'] = self.transfer_status
        if self.transfer_status_code is not None:
            result['TransferStatusCode'] = self.transfer_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddWx') is not None:
            self.add_wx = m.get('AddWx')
        if m.get('AddWxStatus') is not None:
            self.add_wx_status = m.get('AddWxStatus')
        if m.get('AgentExtension') is not None:
            self.agent_extension = m.get('AgentExtension')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentSpeakingDuration') is not None:
            self.agent_speaking_duration = m.get('AgentSpeakingDuration')
        if m.get('AgentSpeakingTime') is not None:
            self.agent_speaking_time = m.get('AgentSpeakingTime')
        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')
        if m.get('AnswerRecall') is not None:
            self.answer_recall = m.get('AnswerRecall')
        if m.get('AnswerTime') is not None:
            self.answer_time = m.get('AnswerTime')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('CallBeginTime') is not None:
            self.call_begin_time = m.get('CallBeginTime')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTimes') is not None:
            self.call_times = m.get('CallTimes')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('ChatRecord') is not None:
            self.chat_record = m.get('ChatRecord')
        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')
        if m.get('HangupTime') is not None:
            self.hangup_time = m.get('HangupTime')
        if m.get('HangupType') is not None:
            self.hangup_type = m.get('HangupType')
        if m.get('ImportTime') is not None:
            self.import_time = m.get('ImportTime')
        if m.get('IndividualTag') is not None:
            self.individual_tag = m.get('IndividualTag')
        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')
        if m.get('IntentTag') is not None:
            self.intent_tag = m.get('IntentTag')
        if m.get('InterceptReason') is not None:
            self.intercept_reason = m.get('InterceptReason')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('NumberMD5') is not None:
            self.number_md5 = m.get('NumberMD5')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RingTime') is not None:
            self.ring_time = m.get('RingTime')
        if m.get('Sms') is not None:
            self.sms = m.get('Sms')
        if m.get('SpeakingDuration') is not None:
            self.speaking_duration = m.get('SpeakingDuration')
        if m.get('SpeakingTime') is not None:
            self.speaking_time = m.get('SpeakingTime')
        if m.get('SpeakingTurns') is not None:
            self.speaking_turns = m.get('SpeakingTurns')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('StatusDescription') is not None:
            self.status_description = m.get('StatusDescription')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TransferStatus') is not None:
            self.transfer_status = m.get('TransferStatus')
        if m.get('TransferStatusCode') is not None:
            self.transfer_status_code = m.get('TransferStatusCode')
        return self


class TaskCallListResponseBodyModel(TeaModel):
    def __init__(self, list=None, page_no=None, page_size=None, total_count=None, total_page=None):
        self.list = list  # type: list[TaskCallListResponseBodyModelList]
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long
        self.total_page = total_page  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TaskCallListResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = TaskCallListResponseBodyModelList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class TaskCallListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: TaskCallListResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(TaskCallListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = TaskCallListResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class TaskCallListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TaskCallListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TaskCallListResponse, self).to_map()
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
            temp_model = TaskCallListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaskCancelCallRequest(TeaModel):
    def __init__(self, numbers=None, owner_id=None, resource_owner_account=None, resource_owner_id=None, tags=None,
                 task_id=None):
        self.numbers = numbers  # type: list[str]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tags = tags  # type: list[str]
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCancelCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TaskCancelCallShrinkRequest(TeaModel):
    def __init__(self, numbers_shrink=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 tags_shrink=None, task_id=None):
        self.numbers_shrink = numbers_shrink  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tags_shrink = tags_shrink  # type: str
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCancelCallShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TaskCancelCallResponseBodyModel(TeaModel):
    def __init__(self, un_handle_numbers=None):
        # 错误手机号
        self.un_handle_numbers = un_handle_numbers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskCancelCallResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.un_handle_numbers is not None:
            result['UnHandleNumbers'] = self.un_handle_numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UnHandleNumbers') is not None:
            self.un_handle_numbers = m.get('UnHandleNumbers')
        return self


class TaskCancelCallResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.model = model  # type: TaskCancelCallResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(TaskCancelCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = TaskCancelCallResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class TaskCancelCallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TaskCancelCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TaskCancelCallResponse, self).to_map()
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
            temp_model = TaskCancelCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaskListRequest(TeaModel):
    def __init__(self, create_time=None, last_call_time=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, task_id=None):
        # 创建时间
        self.create_time = create_time  # type: str
        # 最后外呼时间
        self.last_call_time = last_call_time  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_call_time is not None:
            result['LastCallTime'] = self.last_call_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastCallTime') is not None:
            self.last_call_time = m.get('LastCallTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TaskListResponseBodyModelIntentTags(TeaModel):
    def __init__(self, intent_description=None, intent_tag=None):
        # 意向标签描述
        self.intent_description = intent_description  # type: str
        # 意向标签ID
        self.intent_tag = intent_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskListResponseBodyModelIntentTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description
        if self.intent_tag is not None:
            result['IntentTag'] = self.intent_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')
        if m.get('IntentTag') is not None:
            self.intent_tag = m.get('IntentTag')
        return self


class TaskListResponseBodyModel(TeaModel):
    def __init__(self, allow_call_time=None, allow_call_time_format=None, allow_day_of_week=None, call_type=None,
                 create_time=None, import_time=None, intent_tags=None, invalid_re_call=None, last_call_time=None,
                 max_concurrency=None, personality_tags=None, priority=None, properties=None, recall_type=None, send_sms=None,
                 sms_name=None, status=None, task_id=None, task_name=None, template_name=None):
        # 外呼时间段
        self.allow_call_time = allow_call_time  # type: str
        # 外呼时间段格式化
        self.allow_call_time_format = allow_call_time_format  # type: str
        # 外呼时间
        self.allow_day_of_week = allow_day_of_week  # type: str
        # 外呼类型
        self.call_type = call_type  # type: long
        # 创建时间
        self.create_time = create_time  # type: str
        # 最近导入时间
        self.import_time = import_time  # type: str
        # 意向标签列表
        self.intent_tags = intent_tags  # type: list[TaskListResponseBodyModelIntentTags]
        # 接通重呼次数
        self.invalid_re_call = invalid_re_call  # type: long
        # 最后外呼时间
        self.last_call_time = last_call_time  # type: str
        # 最大并发数
        self.max_concurrency = max_concurrency  # type: long
        # 个性标签列表
        self.personality_tags = personality_tags  # type: list[str]
        # 优先任务
        self.priority = priority  # type: long
        # 任务所需参数
        self.properties = properties  # type: str
        # 自动重呼
        self.recall_type = recall_type  # type: long
        # 发送短信
        self.send_sms = send_sms  # type: long
        # 短信模板
        self.sms_name = sms_name  # type: str
        # 任务状态
        self.status = status  # type: long
        # 任务ID
        self.task_id = task_id  # type: long
        # 任务名称
        self.task_name = task_name  # type: str
        # 话术模板名称
        self.template_name = template_name  # type: str

    def validate(self):
        if self.intent_tags:
            for k in self.intent_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TaskListResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_call_time is not None:
            result['AllowCallTime'] = self.allow_call_time
        if self.allow_call_time_format is not None:
            result['AllowCallTimeFormat'] = self.allow_call_time_format
        if self.allow_day_of_week is not None:
            result['AllowDayOfWeek'] = self.allow_day_of_week
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.import_time is not None:
            result['ImportTime'] = self.import_time
        result['IntentTags'] = []
        if self.intent_tags is not None:
            for k in self.intent_tags:
                result['IntentTags'].append(k.to_map() if k else None)
        if self.invalid_re_call is not None:
            result['InvalidReCall'] = self.invalid_re_call
        if self.last_call_time is not None:
            result['LastCallTime'] = self.last_call_time
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.personality_tags is not None:
            result['PersonalityTags'] = self.personality_tags
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.recall_type is not None:
            result['RecallType'] = self.recall_type
        if self.send_sms is not None:
            result['SendSms'] = self.send_sms
        if self.sms_name is not None:
            result['SmsName'] = self.sms_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowCallTime') is not None:
            self.allow_call_time = m.get('AllowCallTime')
        if m.get('AllowCallTimeFormat') is not None:
            self.allow_call_time_format = m.get('AllowCallTimeFormat')
        if m.get('AllowDayOfWeek') is not None:
            self.allow_day_of_week = m.get('AllowDayOfWeek')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImportTime') is not None:
            self.import_time = m.get('ImportTime')
        self.intent_tags = []
        if m.get('IntentTags') is not None:
            for k in m.get('IntentTags'):
                temp_model = TaskListResponseBodyModelIntentTags()
                self.intent_tags.append(temp_model.from_map(k))
        if m.get('InvalidReCall') is not None:
            self.invalid_re_call = m.get('InvalidReCall')
        if m.get('LastCallTime') is not None:
            self.last_call_time = m.get('LastCallTime')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('PersonalityTags') is not None:
            self.personality_tags = m.get('PersonalityTags')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')
        if m.get('SendSms') is not None:
            self.send_sms = m.get('SendSms')
        if m.get('SmsName') is not None:
            self.sms_name = m.get('SmsName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class TaskListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: list[TaskListResponseBodyModel]
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TaskListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = TaskListResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class TaskListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TaskListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TaskListResponse, self).to_map()
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
            temp_model = TaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaskRecoverCallRequest(TeaModel):
    def __init__(self, begin_import_time=None, end_import_time=None, numbers=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, tags=None, task_id=None):
        # 查询开始导入时间
        self.begin_import_time = begin_import_time  # type: str
        # 查询结束导入时间
        self.end_import_time = end_import_time  # type: str
        # 号码列表
        self.numbers = numbers  # type: list[str]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 用户自定义标签列表
        self.tags = tags  # type: list[str]
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskRecoverCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_import_time is not None:
            result['BeginImportTime'] = self.begin_import_time
        if self.end_import_time is not None:
            result['EndImportTime'] = self.end_import_time
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginImportTime') is not None:
            self.begin_import_time = m.get('BeginImportTime')
        if m.get('EndImportTime') is not None:
            self.end_import_time = m.get('EndImportTime')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TaskRecoverCallShrinkRequest(TeaModel):
    def __init__(self, begin_import_time=None, end_import_time=None, numbers_shrink=None, owner_id=None,
                 resource_owner_account=None, resource_owner_id=None, tags_shrink=None, task_id=None):
        # 查询开始导入时间
        self.begin_import_time = begin_import_time  # type: str
        # 查询结束导入时间
        self.end_import_time = end_import_time  # type: str
        # 号码列表
        self.numbers_shrink = numbers_shrink  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 用户自定义标签列表
        self.tags_shrink = tags_shrink  # type: str
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskRecoverCallShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_import_time is not None:
            result['BeginImportTime'] = self.begin_import_time
        if self.end_import_time is not None:
            result['EndImportTime'] = self.end_import_time
        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginImportTime') is not None:
            self.begin_import_time = m.get('BeginImportTime')
        if m.get('EndImportTime') is not None:
            self.end_import_time = m.get('EndImportTime')
        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TaskRecoverCallResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: dict[str, any]
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TaskRecoverCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class TaskRecoverCallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TaskRecoverCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TaskRecoverCallResponse, self).to_map()
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
            temp_model = TaskRecoverCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TemplateListRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, template_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 必须空参
        self.template_id = template_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TemplateListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class TemplateListResponseBodyModel(TeaModel):
    def __init__(self, intent_tags=None, personality_tags=None, properties=None, template_id=None,
                 template_name=None, template_type=None):
        # 意向标签
        self.intent_tags = intent_tags  # type: list[dict[str, any]]
        # 个性标签
        self.personality_tags = personality_tags  # type: list[str]
        # 话术所需参数
        self.properties = properties  # type: str
        # AI话术ID
        self.template_id = template_id  # type: long
        # 话术模板名称
        self.template_name = template_name  # type: str
        # 模板类型
        self.template_type = template_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(TemplateListResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intent_tags is not None:
            result['IntentTags'] = self.intent_tags
        if self.personality_tags is not None:
            result['PersonalityTags'] = self.personality_tags
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntentTags') is not None:
            self.intent_tags = m.get('IntentTags')
        if m.get('PersonalityTags') is not None:
            self.personality_tags = m.get('PersonalityTags')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class TemplateListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: list[TemplateListResponseBodyModel]
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TemplateListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = TemplateListResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class TemplateListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TemplateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TemplateListResponse, self).to_map()
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
            temp_model = TemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAgentStatusRequest(TeaModel):
    def __init__(self, agent_id=None, agent_status=None, agent_tag=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        # 坐席ID
        self.agent_id = agent_id  # type: long
        # 坐席状态 1:在线；2:忙碌；3:小休；4:离线
        self.agent_status = agent_status  # type: long
        # 坐席标签
        self.agent_tag = agent_tag  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAgentStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateAgentStatusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: dict[str, any]
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAgentStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class UpdateAgentStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAgentStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAgentStatusResponse, self).to_map()
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
            temp_model = UpdateAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskCustomerRequestCustomers(TeaModel):
    def __init__(self, cancel=None, number=None, properties=None, tag=None):
        # 是否取消外呼 0否，1是
        self.cancel = cancel  # type: long
        # 电话号码
        self.number = number  # type: str
        # 需根据具体任务参数要求传输
        self.properties = properties  # type: dict[str, any]
        # 用户自定义标签
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskCustomerRequestCustomers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancel is not None:
            result['Cancel'] = self.cancel
        if self.number is not None:
            result['Number'] = self.number
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cancel') is not None:
            self.cancel = m.get('Cancel')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class UpdateTaskCustomerRequest(TeaModel):
    def __init__(self, customers=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 task_id=None):
        # 外呼客户
        self.customers = customers  # type: list[UpdateTaskCustomerRequestCustomers]
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        if self.customers:
            for k in self.customers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateTaskCustomerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Customers'] = []
        if self.customers is not None:
            for k in self.customers:
                result['Customers'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.customers = []
        if m.get('Customers') is not None:
            for k in m.get('Customers'):
                temp_model = UpdateTaskCustomerRequestCustomers()
                self.customers.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateTaskCustomerShrinkRequest(TeaModel):
    def __init__(self, customers_shrink=None, owner_id=None, resource_owner_account=None, resource_owner_id=None,
                 task_id=None):
        # 外呼客户
        self.customers_shrink = customers_shrink  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        # 任务ID
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskCustomerShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customers_shrink is not None:
            result['Customers'] = self.customers_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Customers') is not None:
            self.customers_shrink = m.get('Customers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateTaskCustomerResponseBodyModel(TeaModel):
    def __init__(self, un_handle_numbers=None):
        # 错误手机列表
        self.un_handle_numbers = un_handle_numbers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTaskCustomerResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.un_handle_numbers is not None:
            result['UnHandleNumbers'] = self.un_handle_numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UnHandleNumbers') is not None:
            self.un_handle_numbers = m.get('UnHandleNumbers')
        return self


class UpdateTaskCustomerResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None, timestamp=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.model = model  # type: UpdateTaskCustomerResponseBodyModel
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(UpdateTaskCustomerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = UpdateTaskCustomerResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class UpdateTaskCustomerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTaskCustomerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTaskCustomerResponse, self).to_map()
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
            temp_model = UpdateTaskCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


