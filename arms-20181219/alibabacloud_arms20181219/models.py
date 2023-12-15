# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ARMSQueryDataSetRequestDimensions(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ARMSQueryDataSetRequestDimensions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ARMSQueryDataSetRequestOptionalDims(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ARMSQueryDataSetRequestOptionalDims, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ARMSQueryDataSetRequestRequiredDims(TeaModel):
    def __init__(self, key=None, type=None, value=None):
        self.key = key  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ARMSQueryDataSetRequestRequiredDims, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ARMSQueryDataSetRequest(TeaModel):
    def __init__(self, dataset_id=None, date_str=None, dimensions=None, hungry_mode=None, interval_in_sec=None,
                 is_drill_down=None, limit=None, max_time=None, measures=None, min_time=None, optional_dims=None,
                 order_by_key=None, reduce_tail=None, required_dims=None, security_token=None):
        self.dataset_id = dataset_id  # type: long
        self.date_str = date_str  # type: str
        self.dimensions = dimensions  # type: list[ARMSQueryDataSetRequestDimensions]
        self.hungry_mode = hungry_mode  # type: bool
        self.interval_in_sec = interval_in_sec  # type: int
        self.is_drill_down = is_drill_down  # type: bool
        self.limit = limit  # type: int
        self.max_time = max_time  # type: long
        self.measures = measures  # type: list[str]
        self.min_time = min_time  # type: long
        self.optional_dims = optional_dims  # type: list[ARMSQueryDataSetRequestOptionalDims]
        self.order_by_key = order_by_key  # type: str
        self.reduce_tail = reduce_tail  # type: bool
        self.required_dims = required_dims  # type: list[ARMSQueryDataSetRequestRequiredDims]
        self.security_token = security_token  # type: str

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()
        if self.optional_dims:
            for k in self.optional_dims:
                if k:
                    k.validate()
        if self.required_dims:
            for k in self.required_dims:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ARMSQueryDataSetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.date_str is not None:
            result['DateStr'] = self.date_str
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.hungry_mode is not None:
            result['HungryMode'] = self.hungry_mode
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.is_drill_down is not None:
            result['IsDrillDown'] = self.is_drill_down
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        result['OptionalDims'] = []
        if self.optional_dims is not None:
            for k in self.optional_dims:
                result['OptionalDims'].append(k.to_map() if k else None)
        if self.order_by_key is not None:
            result['OrderByKey'] = self.order_by_key
        if self.reduce_tail is not None:
            result['ReduceTail'] = self.reduce_tail
        result['RequiredDims'] = []
        if self.required_dims is not None:
            for k in self.required_dims:
                result['RequiredDims'].append(k.to_map() if k else None)
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DateStr') is not None:
            self.date_str = m.get('DateStr')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ARMSQueryDataSetRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('HungryMode') is not None:
            self.hungry_mode = m.get('HungryMode')
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('IsDrillDown') is not None:
            self.is_drill_down = m.get('IsDrillDown')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        self.optional_dims = []
        if m.get('OptionalDims') is not None:
            for k in m.get('OptionalDims'):
                temp_model = ARMSQueryDataSetRequestOptionalDims()
                self.optional_dims.append(temp_model.from_map(k))
        if m.get('OrderByKey') is not None:
            self.order_by_key = m.get('OrderByKey')
        if m.get('ReduceTail') is not None:
            self.reduce_tail = m.get('ReduceTail')
        self.required_dims = []
        if m.get('RequiredDims') is not None:
            for k in m.get('RequiredDims'):
                temp_model = ARMSQueryDataSetRequestRequiredDims()
                self.required_dims.append(temp_model.from_map(k))
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ARMSQueryDataSetResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ARMSQueryDataSetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ARMSQueryDataSetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ARMSQueryDataSetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ARMSQueryDataSetResponse, self).to_map()
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
            temp_model = ARMSQueryDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServicesRequest(TeaModel):
    def __init__(self, app_type=None, region_id=None):
        self.app_type = app_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetServicesResponseBodyDataDetailsDetails(TeaModel):
    def __init__(self, pid=None, region_id=None, service_name=None):
        self.pid = pid  # type: str
        self.region_id = region_id  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServicesResponseBodyDataDetailsDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetServicesResponseBodyDataDetails(TeaModel):
    def __init__(self, details=None):
        self.details = details  # type: list[GetServicesResponseBodyDataDetailsDetails]

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServicesResponseBodyDataDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = GetServicesResponseBodyDataDetailsDetails()
                self.details.append(temp_model.from_map(k))
        return self


class GetServicesResponseBodyDataServices(TeaModel):
    def __init__(self, services=None):
        self.services = services  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServicesResponseBodyDataServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.services is not None:
            result['Services'] = self.services
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Services') is not None:
            self.services = m.get('Services')
        return self


class GetServicesResponseBodyData(TeaModel):
    def __init__(self, details=None, services=None):
        self.details = details  # type: GetServicesResponseBodyDataDetails
        self.services = services  # type: GetServicesResponseBodyDataServices

    def validate(self):
        if self.details:
            self.details.validate()
        if self.services:
            self.services.validate()

    def to_map(self):
        _map = super(GetServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.details is not None:
            result['Details'] = self.details.to_map()
        if self.services is not None:
            result['Services'] = self.services.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Details') is not None:
            temp_model = GetServicesResponseBodyDataDetails()
            self.details = temp_model.from_map(m['Details'])
        if m.get('Services') is not None:
            temp_model = GetServicesResponseBodyDataServices()
            self.services = temp_model.from_map(m['Services'])
        return self


class GetServicesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetServicesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetServicesResponseBody, self).to_map()
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
            temp_model = GetServicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetServicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServicesResponse, self).to_map()
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
            temp_model = GetServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceRequest(TeaModel):
    def __init__(self, app_type=None, region_id=None, trace_id=None):
        self.app_type = app_type  # type: str
        self.region_id = region_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBodyDataCallChainInfoLogEventListLogEventTagEntryListTagEntry(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceResponseBodyDataCallChainInfoLogEventListLogEventTagEntryListTagEntry, self).to_map()
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


class GetTraceResponseBodyDataCallChainInfoLogEventListLogEventTagEntryList(TeaModel):
    def __init__(self, tag_entry=None):
        self.tag_entry = tag_entry  # type: list[GetTraceResponseBodyDataCallChainInfoLogEventListLogEventTagEntryListTagEntry]

    def validate(self):
        if self.tag_entry:
            for k in self.tag_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodyDataCallChainInfoLogEventListLogEventTagEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagEntry'] = []
        if self.tag_entry is not None:
            for k in self.tag_entry:
                result['TagEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_entry = []
        if m.get('TagEntry') is not None:
            for k in m.get('TagEntry'):
                temp_model = GetTraceResponseBodyDataCallChainInfoLogEventListLogEventTagEntryListTagEntry()
                self.tag_entry.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodyDataCallChainInfoLogEventListLogEvent(TeaModel):
    def __init__(self, tag_entry_list=None, timestamp=None):
        self.tag_entry_list = tag_entry_list  # type: GetTraceResponseBodyDataCallChainInfoLogEventListLogEventTagEntryList
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.tag_entry_list:
            self.tag_entry_list.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodyDataCallChainInfoLogEventListLogEvent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_entry_list is not None:
            result['TagEntryList'] = self.tag_entry_list.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagEntryList') is not None:
            temp_model = GetTraceResponseBodyDataCallChainInfoLogEventListLogEventTagEntryList()
            self.tag_entry_list = temp_model.from_map(m['TagEntryList'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetTraceResponseBodyDataCallChainInfoLogEventList(TeaModel):
    def __init__(self, log_event=None):
        self.log_event = log_event  # type: list[GetTraceResponseBodyDataCallChainInfoLogEventListLogEvent]

    def validate(self):
        if self.log_event:
            for k in self.log_event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodyDataCallChainInfoLogEventList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogEvent'] = []
        if self.log_event is not None:
            for k in self.log_event:
                result['LogEvent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.log_event = []
        if m.get('LogEvent') is not None:
            for k in m.get('LogEvent'):
                temp_model = GetTraceResponseBodyDataCallChainInfoLogEventListLogEvent()
                self.log_event.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodyDataCallChainInfoTagEntryListTagEntry(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceResponseBodyDataCallChainInfoTagEntryListTagEntry, self).to_map()
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


class GetTraceResponseBodyDataCallChainInfoTagEntryList(TeaModel):
    def __init__(self, tag_entry=None):
        self.tag_entry = tag_entry  # type: list[GetTraceResponseBodyDataCallChainInfoTagEntryListTagEntry]

    def validate(self):
        if self.tag_entry:
            for k in self.tag_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodyDataCallChainInfoTagEntryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagEntry'] = []
        if self.tag_entry is not None:
            for k in self.tag_entry:
                result['TagEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.tag_entry = []
        if m.get('TagEntry') is not None:
            for k in m.get('TagEntry'):
                temp_model = GetTraceResponseBodyDataCallChainInfoTagEntryListTagEntry()
                self.tag_entry.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodyDataCallChainInfo(TeaModel):
    def __init__(self, duration=None, have_stack=None, log_event_list=None, operation_name=None, result_code=None,
                 rpc_id=None, service_ip=None, service_name=None, tag_entry_list=None, timestamp=None, trace_id=None):
        self.duration = duration  # type: int
        self.have_stack = have_stack  # type: bool
        self.log_event_list = log_event_list  # type: GetTraceResponseBodyDataCallChainInfoLogEventList
        self.operation_name = operation_name  # type: str
        self.result_code = result_code  # type: str
        self.rpc_id = rpc_id  # type: str
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.tag_entry_list = tag_entry_list  # type: GetTraceResponseBodyDataCallChainInfoTagEntryList
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.log_event_list:
            self.log_event_list.validate()
        if self.tag_entry_list:
            self.tag_entry_list.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodyDataCallChainInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        if self.log_event_list is not None:
            result['LogEventList'] = self.log_event_list.to_map()
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.tag_entry_list is not None:
            result['TagEntryList'] = self.tag_entry_list.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        if m.get('LogEventList') is not None:
            temp_model = GetTraceResponseBodyDataCallChainInfoLogEventList()
            self.log_event_list = temp_model.from_map(m['LogEventList'])
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('TagEntryList') is not None:
            temp_model = GetTraceResponseBodyDataCallChainInfoTagEntryList()
            self.tag_entry_list = temp_model.from_map(m['TagEntryList'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBodyData(TeaModel):
    def __init__(self, call_chain_info=None):
        self.call_chain_info = call_chain_info  # type: list[GetTraceResponseBodyDataCallChainInfo]

    def validate(self):
        if self.call_chain_info:
            for k in self.call_chain_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallChainInfo'] = []
        if self.call_chain_info is not None:
            for k in self.call_chain_info:
                result['CallChainInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.call_chain_info = []
        if m.get('CallChainInfo') is not None:
            for k in m.get('CallChainInfo'):
                temp_model = GetTraceResponseBodyDataCallChainInfo()
                self.call_chain_info.append(temp_model.from_map(k))
        return self


class GetTraceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetTraceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTraceResponseBody, self).to_map()
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
            temp_model = GetTraceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTraceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTraceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTraceResponse, self).to_map()
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
            temp_model = GetTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MetricQueryRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MetricQueryRequestFilters, self).to_map()
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


class MetricQueryRequest(TeaModel):
    def __init__(self, dimensions=None, end_time=None, filters=None, iinterval_in_sec=None, limit=None,
                 measures=None, metric=None, order=None, order_by=None, security_token=None, start_time=None):
        self.dimensions = dimensions  # type: list[str]
        self.end_time = end_time  # type: long
        self.filters = filters  # type: list[MetricQueryRequestFilters]
        self.iinterval_in_sec = iinterval_in_sec  # type: int
        self.limit = limit  # type: int
        self.measures = measures  # type: list[str]
        self.metric = metric  # type: str
        self.order = order  # type: str
        self.order_by = order_by  # type: str
        self.security_token = security_token  # type: str
        self.start_time = start_time  # type: long

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(MetricQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.iinterval_in_sec is not None:
            result['IintervalInSec'] = self.iinterval_in_sec
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = MetricQueryRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('IintervalInSec') is not None:
            self.iinterval_in_sec = m.get('IintervalInSec')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class MetricQueryResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MetricQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MetricQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MetricQueryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MetricQueryResponse, self).to_map()
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
            temp_model = MetricQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesRequest(TeaModel):
    def __init__(self, app_type=None, end_time=None, min_duration=None, operation_name=None, region_id=None,
                 service_name=None, start_time=None, tag_1=None, tag_2=None):
        self.app_type = app_type  # type: str
        self.end_time = end_time  # type: long
        self.min_duration = min_duration  # type: long
        self.operation_name = operation_name  # type: str
        self.region_id = region_id  # type: str
        self.service_name = service_name  # type: str
        self.start_time = start_time  # type: long
        self.tag_1 = tag_1  # type: str
        self.tag_2 = tag_2  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_1 is not None:
            result['Tag1'] = self.tag_1
        if self.tag_2 is not None:
            result['Tag2'] = self.tag_2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tag1') is not None:
            self.tag_1 = m.get('Tag1')
        if m.get('Tag2') is not None:
            self.tag_2 = m.get('Tag2')
        return self


class SearchTracesResponseBodyDataTraceInfo(TeaModel):
    def __init__(self, duration=None, operation_name=None, service_ip=None, service_name=None, timestamp=None,
                 trace_id=None):
        self.duration = duration  # type: int
        self.operation_name = operation_name  # type: str
        self.service_ip = service_ip  # type: str
        self.service_name = service_name  # type: str
        self.timestamp = timestamp  # type: long
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesResponseBodyDataTraceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesResponseBodyData(TeaModel):
    def __init__(self, trace_info=None):
        self.trace_info = trace_info  # type: list[SearchTracesResponseBodyDataTraceInfo]

    def validate(self):
        if self.trace_info:
            for k in self.trace_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TraceInfo'] = []
        if self.trace_info is not None:
            for k in self.trace_info:
                result['TraceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.trace_info = []
        if m.get('TraceInfo') is not None:
            for k in m.get('TraceInfo'):
                temp_model = SearchTracesResponseBodyDataTraceInfo()
                self.trace_info.append(temp_model.from_map(k))
        return self


class SearchTracesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: SearchTracesResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SearchTracesResponseBody, self).to_map()
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
            temp_model = SearchTracesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTracesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchTracesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchTracesResponse, self).to_map()
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
            temp_model = SearchTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


