# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AppUseTimeReportHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppUseTimeReportHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AppUseTimeReportRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppUseTimeReportRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AppUseTimeReportRequestPayload(TeaModel):
    def __init__(self, action=None, is_privilege=None, resource_id=None, resource_type=None, step_code=None,
                 vip_type=None, origin_uuid=None):
        self.action = action  # type: str
        self.is_privilege = is_privilege  # type: int
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: int
        self.step_code = step_code  # type: str
        self.vip_type = vip_type  # type: int
        self.origin_uuid = origin_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppUseTimeReportRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.is_privilege is not None:
            result['IsPrivilege'] = self.is_privilege
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.step_code is not None:
            result['StepCode'] = self.step_code
        if self.vip_type is not None:
            result['VipType'] = self.vip_type
        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('IsPrivilege') is not None:
            self.is_privilege = m.get('IsPrivilege')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StepCode') is not None:
            self.step_code = m.get('StepCode')
        if m.get('VipType') is not None:
            self.vip_type = m.get('VipType')
        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')
        return self


class AppUseTimeReportRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppUseTimeReportRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AppUseTimeReportRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: AppUseTimeReportRequestDeviceInfo
        self.payload = payload  # type: AppUseTimeReportRequestPayload
        self.user_info = user_info  # type: AppUseTimeReportRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(AppUseTimeReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = AppUseTimeReportRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = AppUseTimeReportRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = AppUseTimeReportRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class AppUseTimeReportShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppUseTimeReportShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class AppUseTimeReportResponseBody(TeaModel):
    def __init__(self, ret_code=None, ret_msg=None, ret_value=None):
        self.ret_code = ret_code  # type: int
        self.ret_msg = ret_msg  # type: str
        self.ret_value = ret_value  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppUseTimeReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')
        return self


class AppUseTimeReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AppUseTimeReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppUseTimeReportResponse, self).to_map()
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
            temp_model = AppUseTimeReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReminderHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReminderHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateReminderRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReminderRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateReminderRequestPayloadRecurrenceRule(TeaModel):
    def __init__(self, day=None, days_of_month=None, days_of_week=None, end_date_time=None, freq=None, hour=None,
                 minute=None, month=None, second=None, start_date_time=None, year=None):
        self.day = day  # type: int
        self.days_of_month = days_of_month  # type: list[int]
        self.days_of_week = days_of_week  # type: list[int]
        self.end_date_time = end_date_time  # type: long
        self.freq = freq  # type: str
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.second = second  # type: int
        self.start_date_time = start_date_time  # type: long
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReminderRequestPayloadRecurrenceRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class CreateReminderRequestPayload(TeaModel):
    def __init__(self, content=None, is_debug=None, recurrence_rule=None):
        self.content = content  # type: str
        self.is_debug = is_debug  # type: bool
        self.recurrence_rule = recurrence_rule  # type: CreateReminderRequestPayloadRecurrenceRule

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super(CreateReminderRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('RecurrenceRule') is not None:
            temp_model = CreateReminderRequestPayloadRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        return self


class CreateReminderRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReminderRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateReminderRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: CreateReminderRequestDeviceInfo
        self.payload = payload  # type: CreateReminderRequestPayload
        self.user_info = user_info  # type: CreateReminderRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(CreateReminderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreateReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = CreateReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = CreateReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CreateReminderShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReminderShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CreateReminderResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, model=None, success=None):
        self.error_code = error_code  # type: str
        self.error_msg = error_msg  # type: str
        self.model = model  # type: long
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateReminderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateReminderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateReminderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateReminderResponse, self).to_map()
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
            temp_model = CreateReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReminderHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReminderHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteReminderRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReminderRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteReminderRequestPayload(TeaModel):
    def __init__(self, id=None, is_debug=None):
        self.id = id  # type: long
        self.is_debug = is_debug  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReminderRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class DeleteReminderRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReminderRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteReminderRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: DeleteReminderRequestDeviceInfo
        self.payload = payload  # type: DeleteReminderRequestPayload
        self.user_info = user_info  # type: DeleteReminderRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(DeleteReminderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = DeleteReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = DeleteReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = DeleteReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DeleteReminderShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReminderShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class DeleteReminderResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, success=None):
        self.error_code = error_code  # type: int
        self.error_msg = error_msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteReminderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteReminderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteReminderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteReminderResponse, self).to_map()
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
            temp_model = DeleteReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountForAppHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountForAppHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetAccountForAppRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountForAppRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetAccountForAppRequestPayload(TeaModel):
    def __init__(self, phone=None, origin_uuid=None):
        self.phone = phone  # type: str
        self.origin_uuid = origin_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountForAppRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')
        return self


class GetAccountForAppRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountForAppRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetAccountForAppRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: GetAccountForAppRequestDeviceInfo
        self.payload = payload  # type: GetAccountForAppRequestPayload
        self.user_info = user_info  # type: GetAccountForAppRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetAccountForAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetAccountForAppRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetAccountForAppRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetAccountForAppRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetAccountForAppShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountForAppShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetAccountForAppResponseBodyRetValue(TeaModel):
    def __init__(self, is_vip=None, str_vip_expire=None, vip_expire_at=None):
        self.is_vip = is_vip  # type: bool
        self.str_vip_expire = str_vip_expire  # type: str
        self.vip_expire_at = vip_expire_at  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccountForAppResponseBodyRetValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_vip is not None:
            result['IsVip'] = self.is_vip
        if self.str_vip_expire is not None:
            result['StrVipExpire'] = self.str_vip_expire
        if self.vip_expire_at is not None:
            result['VipExpireAt'] = self.vip_expire_at
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsVip') is not None:
            self.is_vip = m.get('IsVip')
        if m.get('StrVipExpire') is not None:
            self.str_vip_expire = m.get('StrVipExpire')
        if m.get('VipExpireAt') is not None:
            self.vip_expire_at = m.get('VipExpireAt')
        return self


class GetAccountForAppResponseBody(TeaModel):
    def __init__(self, ret_code=None, ret_msg=None, ret_value=None):
        self.ret_code = ret_code  # type: int
        self.ret_msg = ret_msg  # type: str
        self.ret_value = ret_value  # type: GetAccountForAppResponseBodyRetValue

    def validate(self):
        if self.ret_value:
            self.ret_value.validate()

    def to_map(self):
        _map = super(GetAccountForAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            temp_model = GetAccountForAppResponseBodyRetValue()
            self.ret_value = temp_model.from_map(m['RetValue'])
        return self


class GetAccountForAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccountForAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccountForAppResponse, self).to_map()
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
            temp_model = GetAccountForAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneNumberHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetPhoneNumberRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetPhoneNumberRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetPhoneNumberRequest(TeaModel):
    def __init__(self, device_info=None, user_info=None):
        self.device_info = device_info  # type: GetPhoneNumberRequestDeviceInfo
        self.user_info = user_info  # type: GetPhoneNumberRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetPhoneNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetPhoneNumberRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = GetPhoneNumberRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetPhoneNumberShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetPhoneNumberResponseBody(TeaModel):
    def __init__(self, phone_number=None):
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPhoneNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        return self


class GetPhoneNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPhoneNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPhoneNumberResponse, self).to_map()
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
            temp_model = GetPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReminderHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReminderHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetReminderRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReminderRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetReminderRequestPayload(TeaModel):
    def __init__(self, id=None, is_debug=None):
        self.id = id  # type: long
        self.is_debug = is_debug  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReminderRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class GetReminderRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReminderRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetReminderRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: GetReminderRequestDeviceInfo
        self.payload = payload  # type: GetReminderRequestPayload
        self.user_info = user_info  # type: GetReminderRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(GetReminderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetReminderShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReminderShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetReminderResponseBodyModelRemindResponsesRecurrenceRule(TeaModel):
    def __init__(self, day=None, days_of_month=None, days_of_week=None, end_date_time=None, freq=None, hour=None,
                 minute=None, month=None, second=None, start_date_time=None, year=None):
        self.day = day  # type: int
        self.days_of_month = days_of_month  # type: list[int]
        self.days_of_week = days_of_week  # type: list[int]
        self.end_date_time = end_date_time  # type: str
        self.freq = freq  # type: str
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.second = second  # type: int
        self.start_date_time = start_date_time  # type: str
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReminderResponseBodyModelRemindResponsesRecurrenceRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class GetReminderResponseBodyModelRemindResponses(TeaModel):
    def __init__(self, action_topic=None, day_desc=None, recurrence_rule=None, remind_id=None, remind_time=None,
                 repeat_count=None, week=None):
        self.action_topic = action_topic  # type: str
        self.day_desc = day_desc  # type: str
        self.recurrence_rule = recurrence_rule  # type: GetReminderResponseBodyModelRemindResponsesRecurrenceRule
        self.remind_id = remind_id  # type: long
        self.remind_time = remind_time  # type: str
        self.repeat_count = repeat_count  # type: int
        self.week = week  # type: str

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super(GetReminderResponseBodyModelRemindResponses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_topic is not None:
            result['ActionTopic'] = self.action_topic
        if self.day_desc is not None:
            result['DayDesc'] = self.day_desc
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        if self.remind_id is not None:
            result['RemindId'] = self.remind_id
        if self.remind_time is not None:
            result['RemindTime'] = self.remind_time
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.week is not None:
            result['Week'] = self.week
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionTopic') is not None:
            self.action_topic = m.get('ActionTopic')
        if m.get('DayDesc') is not None:
            self.day_desc = m.get('DayDesc')
        if m.get('RecurrenceRule') is not None:
            temp_model = GetReminderResponseBodyModelRemindResponsesRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')
        if m.get('RemindTime') is not None:
            self.remind_time = m.get('RemindTime')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('Week') is not None:
            self.week = m.get('Week')
        return self


class GetReminderResponseBodyModel(TeaModel):
    def __init__(self, remind_responses=None):
        self.remind_responses = remind_responses  # type: list[GetReminderResponseBodyModelRemindResponses]

    def validate(self):
        if self.remind_responses:
            for k in self.remind_responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetReminderResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RemindResponses'] = []
        if self.remind_responses is not None:
            for k in self.remind_responses:
                result['RemindResponses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.remind_responses = []
        if m.get('RemindResponses') is not None:
            for k in m.get('RemindResponses'):
                temp_model = GetReminderResponseBodyModelRemindResponses()
                self.remind_responses.append(temp_model.from_map(k))
        return self


class GetReminderResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, model=None, success=None):
        self.error_code = error_code  # type: int
        self.error_msg = error_msg  # type: str
        self.model = model  # type: GetReminderResponseBodyModel
        self.success = success  # type: bool

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(GetReminderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            temp_model = GetReminderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetReminderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetReminderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetReminderResponse, self).to_map()
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
            temp_model = GetReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRemindersHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRemindersHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListRemindersRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRemindersRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRemindersRequestPayload(TeaModel):
    def __init__(self, is_debug=None):
        self.is_debug = is_debug  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRemindersRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class ListRemindersRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRemindersRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRemindersRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: ListRemindersRequestDeviceInfo
        self.payload = payload  # type: ListRemindersRequestPayload
        self.user_info = user_info  # type: ListRemindersRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(ListRemindersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListRemindersRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = ListRemindersRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListRemindersRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListRemindersShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRemindersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListRemindersResponseBodyModelRemindResponsesRecurrenceRule(TeaModel):
    def __init__(self, day=None, days_of_month=None, days_of_week=None, end_date_time=None, freq=None, hour=None,
                 minute=None, month=None, second=None, start_date_time=None, year=None):
        self.day = day  # type: int
        self.days_of_month = days_of_month  # type: list[int]
        self.days_of_week = days_of_week  # type: list[int]
        self.end_date_time = end_date_time  # type: str
        self.freq = freq  # type: str
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.second = second  # type: int
        self.start_date_time = start_date_time  # type: str
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRemindersResponseBodyModelRemindResponsesRecurrenceRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class ListRemindersResponseBodyModelRemindResponses(TeaModel):
    def __init__(self, action_topic=None, day_desc=None, recurrence_rule=None, remind_id=None, remind_time=None,
                 repeat_count=None, week=None):
        self.action_topic = action_topic  # type: str
        self.day_desc = day_desc  # type: str
        self.recurrence_rule = recurrence_rule  # type: ListRemindersResponseBodyModelRemindResponsesRecurrenceRule
        self.remind_id = remind_id  # type: long
        self.remind_time = remind_time  # type: str
        self.repeat_count = repeat_count  # type: int
        self.week = week  # type: str

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super(ListRemindersResponseBodyModelRemindResponses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_topic is not None:
            result['ActionTopic'] = self.action_topic
        if self.day_desc is not None:
            result['DayDesc'] = self.day_desc
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        if self.remind_id is not None:
            result['RemindId'] = self.remind_id
        if self.remind_time is not None:
            result['RemindTime'] = self.remind_time
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.week is not None:
            result['Week'] = self.week
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionTopic') is not None:
            self.action_topic = m.get('ActionTopic')
        if m.get('DayDesc') is not None:
            self.day_desc = m.get('DayDesc')
        if m.get('RecurrenceRule') is not None:
            temp_model = ListRemindersResponseBodyModelRemindResponsesRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')
        if m.get('RemindTime') is not None:
            self.remind_time = m.get('RemindTime')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('Week') is not None:
            self.week = m.get('Week')
        return self


class ListRemindersResponseBodyModel(TeaModel):
    def __init__(self, remind_responses=None):
        self.remind_responses = remind_responses  # type: list[ListRemindersResponseBodyModelRemindResponses]

    def validate(self):
        if self.remind_responses:
            for k in self.remind_responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRemindersResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RemindResponses'] = []
        if self.remind_responses is not None:
            for k in self.remind_responses:
                result['RemindResponses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.remind_responses = []
        if m.get('RemindResponses') is not None:
            for k in m.get('RemindResponses'):
                temp_model = ListRemindersResponseBodyModelRemindResponses()
                self.remind_responses.append(temp_model.from_map(k))
        return self


class ListRemindersResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, model=None, success=None):
        self.error_code = error_code  # type: int
        self.error_msg = error_msg  # type: str
        self.model = model  # type: ListRemindersResponseBodyModel
        self.success = success  # type: bool

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(ListRemindersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            temp_model = ListRemindersResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRemindersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRemindersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRemindersResponse, self).to_map()
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
            temp_model = ListRemindersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PullCashierHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullCashierHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PullCashierRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullCashierRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PullCashierRequestPayload(TeaModel):
    def __init__(self, origin_uuid=None):
        self.origin_uuid = origin_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullCashierRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')
        return self


class PullCashierRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullCashierRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PullCashierRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: PullCashierRequestDeviceInfo
        self.payload = payload  # type: PullCashierRequestPayload
        self.user_info = user_info  # type: PullCashierRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(PullCashierRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = PullCashierRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = PullCashierRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = PullCashierRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class PullCashierShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullCashierShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class PullCashierResponseBody(TeaModel):
    def __init__(self, ret_code=None, ret_msg=None, ret_value=None):
        self.ret_code = ret_code  # type: int
        self.ret_msg = ret_msg  # type: str
        self.ret_value = ret_value  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PullCashierResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')
        return self


class PullCashierResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PullCashierResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PullCashierResponse, self).to_map()
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
            temp_model = PullCashierResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushNotificationsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushNotificationsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PushNotificationsRequestNotificationUnicastRequestSendTarget(TeaModel):
    def __init__(self, target_identity=None, target_type=None):
        self.target_identity = target_identity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushNotificationsRequestNotificationUnicastRequestSendTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class PushNotificationsRequestNotificationUnicastRequest(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, is_debug=None, message_template_id=None,
                 organization_id=None, place_holder=None, send_target=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.is_debug = is_debug  # type: bool
        self.message_template_id = message_template_id  # type: str
        self.organization_id = organization_id  # type: str
        self.place_holder = place_holder  # type: dict[str, str]
        self.send_target = send_target  # type: PushNotificationsRequestNotificationUnicastRequestSendTarget

    def validate(self):
        if self.send_target:
            self.send_target.validate()

    def to_map(self):
        _map = super(PushNotificationsRequestNotificationUnicastRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.send_target is not None:
            result['SendTarget'] = self.send_target.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('SendTarget') is not None:
            temp_model = PushNotificationsRequestNotificationUnicastRequestSendTarget()
            self.send_target = temp_model.from_map(m['SendTarget'])
        return self


class PushNotificationsRequestTenantInfo(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushNotificationsRequestTenantInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m=None):
        m = m or dict()
        return self


class PushNotificationsRequest(TeaModel):
    def __init__(self, notification_unicast_request=None, tenant_info=None):
        self.notification_unicast_request = notification_unicast_request  # type: PushNotificationsRequestNotificationUnicastRequest
        self.tenant_info = tenant_info  # type: PushNotificationsRequestTenantInfo

    def validate(self):
        if self.notification_unicast_request:
            self.notification_unicast_request.validate()
        if self.tenant_info:
            self.tenant_info.validate()

    def to_map(self):
        _map = super(PushNotificationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_unicast_request is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request.to_map()
        if self.tenant_info is not None:
            result['TenantInfo'] = self.tenant_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotificationUnicastRequest') is not None:
            temp_model = PushNotificationsRequestNotificationUnicastRequest()
            self.notification_unicast_request = temp_model.from_map(m['NotificationUnicastRequest'])
        if m.get('TenantInfo') is not None:
            temp_model = PushNotificationsRequestTenantInfo()
            self.tenant_info = temp_model.from_map(m['TenantInfo'])
        return self


class PushNotificationsShrinkRequest(TeaModel):
    def __init__(self, notification_unicast_request_shrink=None, tenant_info_shrink=None):
        self.notification_unicast_request_shrink = notification_unicast_request_shrink  # type: str
        self.tenant_info_shrink = tenant_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PushNotificationsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_unicast_request_shrink is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request_shrink
        if self.tenant_info_shrink is not None:
            result['TenantInfo'] = self.tenant_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotificationUnicastRequest') is not None:
            self.notification_unicast_request_shrink = m.get('NotificationUnicastRequest')
        if m.get('TenantInfo') is not None:
            self.tenant_info_shrink = m.get('TenantInfo')
        return self


class PushNotificationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(PushNotificationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class SendNotificationsHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendNotificationsHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SendNotificationsRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendNotificationsRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SendNotificationsRequestNotificationUnicastRequestSendTarget(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendNotificationsRequestNotificationUnicastRequestSendTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m=None):
        m = m or dict()
        return self


class SendNotificationsRequestNotificationUnicastRequest(TeaModel):
    def __init__(self, is_debug=None, message_template_id=None, place_holder=None, send_target=None):
        self.is_debug = is_debug  # type: bool
        self.message_template_id = message_template_id  # type: str
        self.place_holder = place_holder  # type: dict[str, str]
        self.send_target = send_target  # type: SendNotificationsRequestNotificationUnicastRequestSendTarget

    def validate(self):
        if self.send_target:
            self.send_target.validate()

    def to_map(self):
        _map = super(SendNotificationsRequestNotificationUnicastRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.send_target is not None:
            result['SendTarget'] = self.send_target.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('SendTarget') is not None:
            temp_model = SendNotificationsRequestNotificationUnicastRequestSendTarget()
            self.send_target = temp_model.from_map(m['SendTarget'])
        return self


class SendNotificationsRequestTenantInfo(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendNotificationsRequestTenantInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m=None):
        m = m or dict()
        return self


class SendNotificationsRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendNotificationsRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SendNotificationsRequest(TeaModel):
    def __init__(self, device_info=None, notification_unicast_request=None, tenant_info=None, user_info=None):
        self.device_info = device_info  # type: SendNotificationsRequestDeviceInfo
        self.notification_unicast_request = notification_unicast_request  # type: SendNotificationsRequestNotificationUnicastRequest
        self.tenant_info = tenant_info  # type: SendNotificationsRequestTenantInfo
        self.user_info = user_info  # type: SendNotificationsRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.notification_unicast_request:
            self.notification_unicast_request.validate()
        if self.tenant_info:
            self.tenant_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(SendNotificationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.notification_unicast_request is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request.to_map()
        if self.tenant_info is not None:
            result['TenantInfo'] = self.tenant_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = SendNotificationsRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('NotificationUnicastRequest') is not None:
            temp_model = SendNotificationsRequestNotificationUnicastRequest()
            self.notification_unicast_request = temp_model.from_map(m['NotificationUnicastRequest'])
        if m.get('TenantInfo') is not None:
            temp_model = SendNotificationsRequestTenantInfo()
            self.tenant_info = temp_model.from_map(m['TenantInfo'])
        if m.get('UserInfo') is not None:
            temp_model = SendNotificationsRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class SendNotificationsShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, notification_unicast_request_shrink=None, tenant_info_shrink=None,
                 user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.notification_unicast_request_shrink = notification_unicast_request_shrink  # type: str
        self.tenant_info_shrink = tenant_info_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendNotificationsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.notification_unicast_request_shrink is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request_shrink
        if self.tenant_info_shrink is not None:
            result['TenantInfo'] = self.tenant_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('NotificationUnicastRequest') is not None:
            self.notification_unicast_request_shrink = m.get('NotificationUnicastRequest')
        if m.get('TenantInfo') is not None:
            self.tenant_info_shrink = m.get('TenantInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class SendNotificationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(SendNotificationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateReminderHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReminderHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateReminderRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReminderRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateReminderRequestPayloadRecurrenceRule(TeaModel):
    def __init__(self, day=None, days_of_month=None, days_of_week=None, end_date_time=None, freq=None, hour=None,
                 minute=None, month=None, second=None, start_date_time=None, year=None):
        self.day = day  # type: int
        self.days_of_month = days_of_month  # type: list[int]
        self.days_of_week = days_of_week  # type: list[int]
        self.end_date_time = end_date_time  # type: long
        self.freq = freq  # type: str
        self.hour = hour  # type: int
        self.minute = minute  # type: int
        self.month = month  # type: int
        self.second = second  # type: int
        self.start_date_time = start_date_time  # type: long
        self.year = year  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReminderRequestPayloadRecurrenceRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class UpdateReminderRequestPayload(TeaModel):
    def __init__(self, content=None, id=None, is_debug=None, recurrence_rule=None):
        self.content = content  # type: str
        self.id = id  # type: long
        self.is_debug = is_debug  # type: bool
        self.recurrence_rule = recurrence_rule  # type: UpdateReminderRequestPayloadRecurrenceRule

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super(UpdateReminderRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('RecurrenceRule') is not None:
            temp_model = UpdateReminderRequestPayloadRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        return self


class UpdateReminderRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReminderRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateReminderRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: UpdateReminderRequestDeviceInfo
        self.payload = payload  # type: UpdateReminderRequestPayload
        self.user_info = user_info  # type: UpdateReminderRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(UpdateReminderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = UpdateReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = UpdateReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = UpdateReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class UpdateReminderShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReminderShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class UpdateReminderResponseBody(TeaModel):
    def __init__(self, error_code=None, error_msg=None, model=None, success=None):
        self.error_code = error_code  # type: int
        self.error_msg = error_msg  # type: str
        self.model = model  # type: long
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateReminderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateReminderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateReminderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateReminderResponse, self).to_map()
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
            temp_model = UpdateReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoAppReportHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoAppReportHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class VideoAppReportRequestDeviceInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoAppReportRequestDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class VideoAppReportRequestPayload(TeaModel):
    def __init__(self, end_time=None, is_login=None, is_vip=None, login_nick=None, origin_uuid=None, phone=None,
                 pkg_name=None, start_time=None):
        self.end_time = end_time  # type: long
        self.is_login = is_login  # type: bool
        self.is_vip = is_vip  # type: bool
        self.login_nick = login_nick  # type: str
        self.origin_uuid = origin_uuid  # type: str
        self.phone = phone  # type: str
        self.pkg_name = pkg_name  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoAppReportRequestPayload, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_login is not None:
            result['isLogin'] = self.is_login
        if self.is_vip is not None:
            result['isVip'] = self.is_vip
        if self.login_nick is not None:
            result['loginNick'] = self.login_nick
        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid
        if self.phone is not None:
            result['phone'] = self.phone
        if self.pkg_name is not None:
            result['pkgName'] = self.pkg_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isLogin') is not None:
            self.is_login = m.get('isLogin')
        if m.get('isVip') is not None:
            self.is_vip = m.get('isVip')
        if m.get('loginNick') is not None:
            self.login_nick = m.get('loginNick')
        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('pkgName') is not None:
            self.pkg_name = m.get('pkgName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class VideoAppReportRequestUserInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, id=None, id_type=None, organization_id=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.id = id  # type: str
        self.id_type = id_type  # type: str
        self.organization_id = organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoAppReportRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class VideoAppReportRequest(TeaModel):
    def __init__(self, device_info=None, payload=None, user_info=None):
        self.device_info = device_info  # type: VideoAppReportRequestDeviceInfo
        self.payload = payload  # type: VideoAppReportRequestPayload
        self.user_info = user_info  # type: VideoAppReportRequestUserInfo

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(VideoAppReportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = VideoAppReportRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = VideoAppReportRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = VideoAppReportRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class VideoAppReportShrinkRequest(TeaModel):
    def __init__(self, device_info_shrink=None, payload_shrink=None, user_info_shrink=None):
        self.device_info_shrink = device_info_shrink  # type: str
        self.payload_shrink = payload_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoAppReportShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class VideoAppReportResponseBody(TeaModel):
    def __init__(self, ret_code=None, ret_msg=None, ret_value=None):
        self.ret_code = ret_code  # type: int
        self.ret_msg = ret_msg  # type: str
        self.ret_value = ret_value  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(VideoAppReportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')
        return self


class VideoAppReportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VideoAppReportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VideoAppReportResponse, self).to_map()
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
            temp_model = VideoAppReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WakeUpAppHeaders(TeaModel):
    def __init__(self, common_headers=None, x_acs_aligenie_access_token=None, authorization=None):
        self.common_headers = common_headers  # type: dict[str, str]
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token  # type: str
        self.authorization = authorization  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WakeUpAppHeaders, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class WakeUpAppRequestTargetInfo(TeaModel):
    def __init__(self, encode_key=None, encode_type=None, organization_id=None, target_identity=None,
                 target_type=None):
        self.encode_key = encode_key  # type: str
        self.encode_type = encode_type  # type: str
        self.organization_id = organization_id  # type: str
        self.target_identity = target_identity  # type: str
        self.target_type = target_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(WakeUpAppRequestTargetInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class WakeUpAppRequest(TeaModel):
    def __init__(self, is_debug=None, path=None, target_info=None):
        self.is_debug = is_debug  # type: bool
        self.path = path  # type: str
        self.target_info = target_info  # type: WakeUpAppRequestTargetInfo

    def validate(self):
        if self.target_info:
            self.target_info.validate()

    def to_map(self):
        _map = super(WakeUpAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.path is not None:
            result['Path'] = self.path
        if self.target_info is not None:
            result['TargetInfo'] = self.target_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('TargetInfo') is not None:
            temp_model = WakeUpAppRequestTargetInfo()
            self.target_info = temp_model.from_map(m['TargetInfo'])
        return self


class WakeUpAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super(WakeUpAppResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


