# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateAlarmEventRequest(TeaModel):
    def __init__(self, alarm_id=None, alarm_timestamp=None, app_key=None, app_secret=None, attach=None,
                 dynamic_alarm_id=None, impact=None, link=None, message=None, monitor_detail=None, region=None, request_id=None,
                 source_key=None, source_system=None, strategy=None, title=None, uid=None):
        self.alarm_id = alarm_id  # type: str
        self.alarm_timestamp = alarm_timestamp  # type: long
        self.app_key = app_key  # type: str
        self.app_secret = app_secret  # type: str
        self.attach = attach  # type: str
        self.dynamic_alarm_id = dynamic_alarm_id  # type: str
        self.impact = impact  # type: str
        self.link = link  # type: str
        self.message = message  # type: str
        self.monitor_detail = monitor_detail  # type: str
        self.region = region  # type: str
        self.request_id = request_id  # type: str
        self.source_key = source_key  # type: str
        self.source_system = source_system  # type: str
        self.strategy = strategy  # type: str
        self.title = title  # type: str
        self.uid = uid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_timestamp is not None:
            result['AlarmTimestamp'] = self.alarm_timestamp
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.attach is not None:
            result['Attach'] = self.attach
        if self.dynamic_alarm_id is not None:
            result['DynamicAlarmId'] = self.dynamic_alarm_id
        if self.impact is not None:
            result['Impact'] = self.impact
        if self.link is not None:
            result['Link'] = self.link
        if self.message is not None:
            result['Message'] = self.message
        if self.monitor_detail is not None:
            result['MonitorDetail'] = self.monitor_detail
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_key is not None:
            result['SourceKey'] = self.source_key
        if self.source_system is not None:
            result['SourceSystem'] = self.source_system
        if self.strategy is not None:
            result['Strategy'] = self.strategy
        if self.title is not None:
            result['Title'] = self.title
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmTimestamp') is not None:
            self.alarm_timestamp = m.get('AlarmTimestamp')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Attach') is not None:
            self.attach = m.get('Attach')
        if m.get('DynamicAlarmId') is not None:
            self.dynamic_alarm_id = m.get('DynamicAlarmId')
        if m.get('Impact') is not None:
            self.impact = m.get('Impact')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MonitorDetail') is not None:
            self.monitor_detail = m.get('MonitorDetail')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceKey') is not None:
            self.source_key = m.get('SourceKey')
        if m.get('SourceSystem') is not None:
            self.source_system = m.get('SourceSystem')
        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class CreateAlarmEventResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAlarmEventResponseBody, self).to_map()
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


class CreateAlarmEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAlarmEventResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAlarmEventResponse, self).to_map()
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
            temp_model = CreateAlarmEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFaultDetailRequest(TeaModel):
    def __init__(self, app_key=None, app_secret=None, vid=None):
        self.app_key = app_key  # type: str
        self.app_secret = app_secret  # type: str
        self.vid = vid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFaultDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.vid is not None:
            result['Vid'] = self.vid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Vid') is not None:
            self.vid = m.get('Vid')
        return self


class GetFaultDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFaultDetailResponseBody, self).to_map()
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


class GetFaultDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFaultDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFaultDetailResponse, self).to_map()
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
            temp_model = GetFaultDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportInfluenceRequest(TeaModel):
    def __init__(self, app_key=None, app_secret=None, area=None, channel_code=None, cluster=None, create_id=None,
                 customer_impact_desc=None, fault_vid=None, issue_desc=None, product_line_id=None, regions=None, room=None, time=None,
                 total_desc=None):
        self.app_key = app_key  # type: str
        self.app_secret = app_secret  # type: str
        self.area = area  # type: str
        self.channel_code = channel_code  # type: str
        self.cluster = cluster  # type: str
        self.create_id = create_id  # type: str
        self.customer_impact_desc = customer_impact_desc  # type: str
        self.fault_vid = fault_vid  # type: str
        self.issue_desc = issue_desc  # type: str
        self.product_line_id = product_line_id  # type: long
        self.regions = regions  # type: str
        self.room = room  # type: str
        self.time = time  # type: long
        self.total_desc = total_desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportInfluenceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.area is not None:
            result['Area'] = self.area
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.cluster is not None:
            result['Cluster'] = self.cluster
        if self.create_id is not None:
            result['CreateId'] = self.create_id
        if self.customer_impact_desc is not None:
            result['CustomerImpactDesc'] = self.customer_impact_desc
        if self.fault_vid is not None:
            result['FaultVid'] = self.fault_vid
        if self.issue_desc is not None:
            result['IssueDesc'] = self.issue_desc
        if self.product_line_id is not None:
            result['ProductLineId'] = self.product_line_id
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.room is not None:
            result['Room'] = self.room
        if self.time is not None:
            result['Time'] = self.time
        if self.total_desc is not None:
            result['TotalDesc'] = self.total_desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')
        if m.get('CreateId') is not None:
            self.create_id = m.get('CreateId')
        if m.get('CustomerImpactDesc') is not None:
            self.customer_impact_desc = m.get('CustomerImpactDesc')
        if m.get('FaultVid') is not None:
            self.fault_vid = m.get('FaultVid')
        if m.get('IssueDesc') is not None:
            self.issue_desc = m.get('IssueDesc')
        if m.get('ProductLineId') is not None:
            self.product_line_id = m.get('ProductLineId')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('Room') is not None:
            self.room = m.get('Room')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('TotalDesc') is not None:
            self.total_desc = m.get('TotalDesc')
        return self


class ReportInfluenceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportInfluenceResponseBody, self).to_map()
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


class ReportInfluenceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportInfluenceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportInfluenceResponse, self).to_map()
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
            temp_model = ReportInfluenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportReasonDetailRequest(TeaModel):
    def __init__(self, app_key=None, app_secret=None, channel_code=None, create_id=None, detail_url=None,
                 fault_vid=None, reason=None):
        self.app_key = app_key  # type: str
        self.app_secret = app_secret  # type: str
        self.channel_code = channel_code  # type: str
        self.create_id = create_id  # type: str
        self.detail_url = detail_url  # type: str
        self.fault_vid = fault_vid  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportReasonDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.create_id is not None:
            result['CreateId'] = self.create_id
        if self.detail_url is not None:
            result['DetailUrl'] = self.detail_url
        if self.fault_vid is not None:
            result['FaultVid'] = self.fault_vid
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('CreateId') is not None:
            self.create_id = m.get('CreateId')
        if m.get('DetailUrl') is not None:
            self.detail_url = m.get('DetailUrl')
        if m.get('FaultVid') is not None:
            self.fault_vid = m.get('FaultVid')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ReportReasonDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportReasonDetailResponseBody, self).to_map()
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


class ReportReasonDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportReasonDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportReasonDetailResponse, self).to_map()
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
            temp_model = ReportReasonDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportRecoverActionRequest(TeaModel):
    def __init__(self, action_type=None, app_key=None, app_secret=None, channel_code=None, create_id=None,
                 current_desc=None, current_progress=None, expected_repaired_time=None, fault_vid=None, is_recovery=None,
                 product_line_id=None, recovery_duration=None, recovery_time=None):
        self.action_type = action_type  # type: int
        self.app_key = app_key  # type: str
        self.app_secret = app_secret  # type: str
        self.channel_code = channel_code  # type: str
        self.create_id = create_id  # type: str
        self.current_desc = current_desc  # type: str
        self.current_progress = current_progress  # type: int
        self.expected_repaired_time = expected_repaired_time  # type: long
        self.fault_vid = fault_vid  # type: str
        self.is_recovery = is_recovery  # type: int
        self.product_line_id = product_line_id  # type: long
        self.recovery_duration = recovery_duration  # type: long
        self.recovery_time = recovery_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportRecoverActionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.create_id is not None:
            result['CreateId'] = self.create_id
        if self.current_desc is not None:
            result['CurrentDesc'] = self.current_desc
        if self.current_progress is not None:
            result['CurrentProgress'] = self.current_progress
        if self.expected_repaired_time is not None:
            result['ExpectedRepairedTime'] = self.expected_repaired_time
        if self.fault_vid is not None:
            result['FaultVid'] = self.fault_vid
        if self.is_recovery is not None:
            result['IsRecovery'] = self.is_recovery
        if self.product_line_id is not None:
            result['ProductLineId'] = self.product_line_id
        if self.recovery_duration is not None:
            result['RecoveryDuration'] = self.recovery_duration
        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('CreateId') is not None:
            self.create_id = m.get('CreateId')
        if m.get('CurrentDesc') is not None:
            self.current_desc = m.get('CurrentDesc')
        if m.get('CurrentProgress') is not None:
            self.current_progress = m.get('CurrentProgress')
        if m.get('ExpectedRepairedTime') is not None:
            self.expected_repaired_time = m.get('ExpectedRepairedTime')
        if m.get('FaultVid') is not None:
            self.fault_vid = m.get('FaultVid')
        if m.get('IsRecovery') is not None:
            self.is_recovery = m.get('IsRecovery')
        if m.get('ProductLineId') is not None:
            self.product_line_id = m.get('ProductLineId')
        if m.get('RecoveryDuration') is not None:
            self.recovery_duration = m.get('RecoveryDuration')
        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')
        return self


class ReportRecoverActionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportRecoverActionResponseBody, self).to_map()
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


class ReportRecoverActionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportRecoverActionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportRecoverActionResponse, self).to_map()
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
            temp_model = ReportRecoverActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


