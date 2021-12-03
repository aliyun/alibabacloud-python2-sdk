# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class EnterpriseDingtalkGroupMember(TeaModel):
    def __init__(self, is_admin=None, mobile=None, name=None):
        # 是否企业钉群管理员
        self.is_admin = is_admin  # type: bool
        # 成员手机号
        self.mobile = mobile  # type: str
        # 成员姓名
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnterpriseDingtalkGroupMember, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CloseTaskOrderRequest(TeaModel):
    def __init__(self, order_id=None, user_name=None):
        # 任务单id
        self.order_id = order_id  # type: str
        # 操作人姓名
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseTaskOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CloseTaskOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # code
        self.code = code  # type: str
        # data
        self.data = data  # type: str
        # msg
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseTaskOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseTaskOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloseTaskOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseTaskOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloseTaskOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskOrderRequest(TeaModel):
    def __init__(self, customer_real_name=None, customer_user_id=None, important_description=None,
                 is_important=None, open_group_id=None, product_type=None, product_type_name=None, task_title=None):
        # 建单人姓名：快手客户
        self.customer_real_name = customer_real_name  # type: str
        # 建单人：固定值
        self.customer_user_id = customer_user_id  # type: str
        # 重要性描述
        self.important_description = important_description  # type: str
        # 是否紧急
        self.is_important = is_important  # type: str
        # 主群关联Id
        self.open_group_id = open_group_id  # type: str
        # productType
        self.product_type = product_type  # type: str
        # 问题分类名称
        self.product_type_name = product_type_name  # type: str
        # 任务单标题
        self.task_title = task_title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_real_name is not None:
            result['CustomerRealName'] = self.customer_real_name
        if self.customer_user_id is not None:
            result['CustomerUserId'] = self.customer_user_id
        if self.important_description is not None:
            result['ImportantDescription'] = self.important_description
        if self.is_important is not None:
            result['IsImportant'] = self.is_important
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.product_type_name is not None:
            result['ProductTypeName'] = self.product_type_name
        if self.task_title is not None:
            result['TaskTitle'] = self.task_title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerRealName') is not None:
            self.customer_real_name = m.get('CustomerRealName')
        if m.get('CustomerUserId') is not None:
            self.customer_user_id = m.get('CustomerUserId')
        if m.get('ImportantDescription') is not None:
            self.important_description = m.get('ImportantDescription')
        if m.get('IsImportant') is not None:
            self.is_important = m.get('IsImportant')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProductTypeName') is not None:
            self.product_type_name = m.get('ProductTypeName')
        if m.get('TaskTitle') is not None:
            self.task_title = m.get('TaskTitle')
        return self


class CreateTaskOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # code
        self.code = code  # type: str
        # 返回任务单号：OrderId
        self.data = data  # type: str
        # msg
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTaskOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTaskOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTaskOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskOrderByEventReportRequestEventBodyEventLocation(TeaModel):
    def __init__(self, domain=None):
        # domian域名
        self.domain = domain  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskOrderByEventReportRequestEventBodyEventLocation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CreateTaskOrderByEventReportRequestEventBody(TeaModel):
    def __init__(self, event_desc=None, event_id=None, event_level=None, event_location=None, event_time=None):
        # 当前告警描述信息
        self.event_desc = event_desc  # type: str
        # 事件id
        self.event_id = event_id  # type: str
        # 事件级别
        self.event_level = event_level  # type: str
        # 事件源标识，自定义和TAM在云企配置的Location指标一致
        self.event_location = event_location  # type: CreateTaskOrderByEventReportRequestEventBodyEventLocation
        # 事件上报时间
        self.event_time = event_time  # type: str

    def validate(self):
        if self.event_location:
            self.event_location.validate()

    def to_map(self):
        _map = super(CreateTaskOrderByEventReportRequestEventBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.event_location is not None:
            result['EventLocation'] = self.event_location.to_map()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('EventLocation') is not None:
            temp_model = CreateTaskOrderByEventReportRequestEventBodyEventLocation()
            self.event_location = temp_model.from_map(m['EventLocation'])
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        return self


class CreateTaskOrderByEventReportRequestExtinfo(TeaModel):
    def __init__(self, name=None, value=None):
        # 扩展信息名称
        self.name = name  # type: str
        # 扩展信息value值
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskOrderByEventReportRequestExtinfo, self).to_map()
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


class CreateTaskOrderByEventReportRequest(TeaModel):
    def __init__(self, business=None, create_real_name=None, create_user_id=None, event_body=None, extinfo=None,
                 important_desc=None, join_child_group_user_ids=None, monitor_congregation=None, open_group_id=None,
                 product_type=None):
        # 告警所属业务
        self.business = business  # type: str
        # 提交人姓名
        self.create_real_name = create_real_name  # type: str
        # 提交人userId
        self.create_user_id = create_user_id  # type: str
        # 告警描述
        self.event_body = event_body  # type: CreateTaskOrderByEventReportRequestEventBody
        # 扩展信息
        self.extinfo = extinfo  # type: list[CreateTaskOrderByEventReportRequestExtinfo]
        # 当eventLevel为warn时，必传
        self.important_desc = important_desc  # type: str
        # 建单入群人员
        self.join_child_group_user_ids = join_child_group_user_ids  # type: str
        # 监控集如：视频业务的质量监控
        self.monitor_congregation = monitor_congregation  # type: str
        # 告警关联主群id
        self.open_group_id = open_group_id  # type: str
        # 问题分类
        self.product_type = product_type  # type: str

    def validate(self):
        if self.event_body:
            self.event_body.validate()
        if self.extinfo:
            for k in self.extinfo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTaskOrderByEventReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.create_real_name is not None:
            result['CreateRealName'] = self.create_real_name
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.event_body is not None:
            result['EventBody'] = self.event_body.to_map()
        result['Extinfo'] = []
        if self.extinfo is not None:
            for k in self.extinfo:
                result['Extinfo'].append(k.to_map() if k else None)
        if self.important_desc is not None:
            result['ImportantDesc'] = self.important_desc
        if self.join_child_group_user_ids is not None:
            result['JoinChildGroupUserIds'] = self.join_child_group_user_ids
        if self.monitor_congregation is not None:
            result['MonitorCongregation'] = self.monitor_congregation
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CreateRealName') is not None:
            self.create_real_name = m.get('CreateRealName')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('EventBody') is not None:
            temp_model = CreateTaskOrderByEventReportRequestEventBody()
            self.event_body = temp_model.from_map(m['EventBody'])
        self.extinfo = []
        if m.get('Extinfo') is not None:
            for k in m.get('Extinfo'):
                temp_model = CreateTaskOrderByEventReportRequestExtinfo()
                self.extinfo.append(temp_model.from_map(k))
        if m.get('ImportantDesc') is not None:
            self.important_desc = m.get('ImportantDesc')
        if m.get('JoinChildGroupUserIds') is not None:
            self.join_child_group_user_ids = m.get('JoinChildGroupUserIds')
        if m.get('MonitorCongregation') is not None:
            self.monitor_congregation = m.get('MonitorCongregation')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class CreateTaskOrderByEventReportShrinkRequest(TeaModel):
    def __init__(self, business=None, create_real_name=None, create_user_id=None, event_body_shrink=None,
                 extinfo_shrink=None, important_desc=None, join_child_group_user_ids=None, monitor_congregation=None,
                 open_group_id=None, product_type=None):
        # 告警所属业务
        self.business = business  # type: str
        # 提交人姓名
        self.create_real_name = create_real_name  # type: str
        # 提交人userId
        self.create_user_id = create_user_id  # type: str
        # 告警描述
        self.event_body_shrink = event_body_shrink  # type: str
        # 扩展信息
        self.extinfo_shrink = extinfo_shrink  # type: str
        # 当eventLevel为warn时，必传
        self.important_desc = important_desc  # type: str
        # 建单入群人员
        self.join_child_group_user_ids = join_child_group_user_ids  # type: str
        # 监控集如：视频业务的质量监控
        self.monitor_congregation = monitor_congregation  # type: str
        # 告警关联主群id
        self.open_group_id = open_group_id  # type: str
        # 问题分类
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskOrderByEventReportShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.create_real_name is not None:
            result['CreateRealName'] = self.create_real_name
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.event_body_shrink is not None:
            result['EventBody'] = self.event_body_shrink
        if self.extinfo_shrink is not None:
            result['Extinfo'] = self.extinfo_shrink
        if self.important_desc is not None:
            result['ImportantDesc'] = self.important_desc
        if self.join_child_group_user_ids is not None:
            result['JoinChildGroupUserIds'] = self.join_child_group_user_ids
        if self.monitor_congregation is not None:
            result['MonitorCongregation'] = self.monitor_congregation
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('CreateRealName') is not None:
            self.create_real_name = m.get('CreateRealName')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('EventBody') is not None:
            self.event_body_shrink = m.get('EventBody')
        if m.get('Extinfo') is not None:
            self.extinfo_shrink = m.get('Extinfo')
        if m.get('ImportantDesc') is not None:
            self.important_desc = m.get('ImportantDesc')
        if m.get('JoinChildGroupUserIds') is not None:
            self.join_child_group_user_ids = m.get('JoinChildGroupUserIds')
        if m.get('MonitorCongregation') is not None:
            self.monitor_congregation = m.get('MonitorCongregation')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class CreateTaskOrderByEventReportResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # code
        self.code = code  # type: str
        # 返回信息
        self.data = data  # type: str
        # msg
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTaskOrderByEventReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTaskOrderByEventReportResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateTaskOrderByEventReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTaskOrderByEventReportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTaskOrderByEventReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberRequest(TeaModel):
    def __init__(self, mobiles=None, open_group_id=None):
        self.mobiles = mobiles  # type: list[str]
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnterpriseDingtalkGroupCustomerMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest(TeaModel):
    def __init__(self, mobiles_shrink=None, open_group_id=None):
        self.mobiles_shrink = mobiles_shrink  # type: str
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobiles_shrink is not None:
            result['Mobiles'] = self.mobiles_shrink
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles_shrink = m.get('Mobiles')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        # 接口请求结果返回码
        self.code = code  # type: str
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEnterpriseDingtalkGroupCustomerMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEnterpriseDingtalkGroupCustomerMemberResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteEnterpriseDingtalkGroupCustomerMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDingtalkGroupRequest(TeaModel):
    def __init__(self, open_group_id=None):
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class GetEnterpriseDingtalkGroupResponseBodyData(TeaModel):
    def __init__(self, group_name=None, open_group_id=None):
        # 企业服务群的群名
        self.group_name = group_name  # type: str
        # 企业服务群的ID
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class GetEnterpriseDingtalkGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 接口请求结果返回码
        self.code = code  # type: str
        self.data = data  # type: GetEnterpriseDingtalkGroupResponseBodyData
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetEnterpriseDingtalkGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEnterpriseDingtalkGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnterpriseDingtalkGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnterpriseDingtalkGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEnterpriseDingtalkGroupCustomerMemberRequest(TeaModel):
    def __init__(self, mobile=None, open_group_id=None):
        self.mobile = mobile  # type: str
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupCustomerMemberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class GetEnterpriseDingtalkGroupCustomerMemberResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 接口请求结果返回码
        self.code = code  # type: str
        # 成员信息列表
        self.data = data  # type: EnterpriseDingtalkGroupMember
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupCustomerMemberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = EnterpriseDingtalkGroupMember()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEnterpriseDingtalkGroupCustomerMemberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEnterpriseDingtalkGroupCustomerMemberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEnterpriseDingtalkGroupCustomerMemberResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetEnterpriseDingtalkGroupCustomerMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDdTaskOrderRequest(TeaModel):
    def __init__(self, caller_parent_id=None, caller_type=None, caller_uid=None, open_group_id=None, order_id=None,
                 request_id=None, task_status=None):
        # callerParentId
        self.caller_parent_id = caller_parent_id  # type: long
        # callerType
        self.caller_type = caller_type  # type: str
        # callerUid
        self.caller_uid = caller_uid  # type: long
        # openGroupId
        self.open_group_id = open_group_id  # type: str
        # orderId
        self.order_id = order_id  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # taskStatus
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDdTaskOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class ListDdTaskOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # code
        self.code = code  # type: str
        # data
        self.data = data  # type: str
        # msg
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDdTaskOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDdTaskOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListDdTaskOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDdTaskOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDdTaskOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnterpriseDingtalkGroupCustomerMembersRequest(TeaModel):
    def __init__(self, open_group_id=None):
        # 企业服务群ID
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupCustomerMembersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class ListEnterpriseDingtalkGroupCustomerMembersResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 接口请求结果返回码
        self.code = code  # type: str
        # 企业服务群成员列表
        self.data = data  # type: list[EnterpriseDingtalkGroupMember]
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupCustomerMembersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = EnterpriseDingtalkGroupMember()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEnterpriseDingtalkGroupCustomerMembersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnterpriseDingtalkGroupCustomerMembersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupCustomerMembersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnterpriseDingtalkGroupCustomerMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnterpriseDingtalkGroupsResponseBodyData(TeaModel):
    def __init__(self, group_name=None, open_group_id=None):
        # 钉群名
        self.group_name = group_name  # type: str
        # 钉群ID
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class ListEnterpriseDingtalkGroupsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 接口请求结果返回码
        self.code = code  # type: str
        # 服务钉群数组
        self.data = data  # type: list[ListEnterpriseDingtalkGroupsResponseBodyData]
        # 错误信息, 当success=false的时候, 可以取到message
        self.message = message  # type: str
        # 接口请求的唯一ID, 每次调用requestID唯一
        self.request_id = request_id  # type: str
        # 调用接口返回是否成功, true代表调用正常
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEnterpriseDingtalkGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListEnterpriseDingtalkGroupsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListEnterpriseDingtalkGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEnterpriseDingtalkGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEnterpriseDingtalkGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductByGroupRequest(TeaModel):
    def __init__(self, open_group_id=None):
        # 主群关联Id
        self.open_group_id = open_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductByGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        return self


class ListProductByGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # code
        self.code = code  # type: str
        # data
        self.data = data  # type: str
        # msg
        self.message = message  # type: str
        # 接口交互动态值
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProductByGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProductByGroupResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListProductByGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProductByGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProductByGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskInfoRequest(TeaModel):
    def __init__(self, order_id=None):
        # 任务单ID
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class QueryTaskInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # code
        self.code = code  # type: str
        # data
        self.data = data  # type: str
        # msg
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTaskInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTaskInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTaskInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTaskInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplyMessageApiRequest(TeaModel):
    def __init__(self, msg_content=None, msg_type=None, open_group_id=None, order_id=None, user_id=None,
                 user_name=None):
        # 消息内容
        self.msg_content = msg_content  # type: str
        # 消息类型
        self.msg_type = msg_type  # type: str
        # 群Id
        self.open_group_id = open_group_id  # type: str
        # 任务单Id
        self.order_id = order_id  # type: str
        # 消息发送人Id
        self.user_id = user_id  # type: str
        # 消息发送人
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplyMessageApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_content is not None:
            result['MsgContent'] = self.msg_content
        if self.msg_type is not None:
            result['MsgType'] = self.msg_type
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgContent') is not None:
            self.msg_content = m.get('MsgContent')
        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ReplyMessageApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # code
        self.code = code  # type: str
        # data
        self.data = data  # type: str
        # msg
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplyMessageApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReplyMessageApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReplyMessageApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReplyMessageApiResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReplyMessageApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestOpenTaskOrderRequest(TeaModel):
    def __init__(self, open_group_id=None, order_id=None, reset_content=None, reset_type=None, user_name=None):
        # 主群关联Id
        self.open_group_id = open_group_id  # type: str
        # 任务单ID
        self.order_id = order_id  # type: str
        # 重开说明
        self.reset_content = reset_content  # type: str
        # 重开类型
        self.reset_type = reset_type  # type: str
        # 操作人姓名
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestOpenTaskOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_group_id is not None:
            result['OpenGroupId'] = self.open_group_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.reset_content is not None:
            result['ResetContent'] = self.reset_content
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OpenGroupId') is not None:
            self.open_group_id = m.get('OpenGroupId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ResetContent') is not None:
            self.reset_content = m.get('ResetContent')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class RestOpenTaskOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # code
        self.code = code  # type: str
        # data
        self.data = data  # type: str
        # msg
        self.message = message  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestOpenTaskOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestOpenTaskOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RestOpenTaskOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestOpenTaskOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestOpenTaskOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


