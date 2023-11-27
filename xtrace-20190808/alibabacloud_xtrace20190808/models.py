# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CheckCommercialStatusRequest(TeaModel):
    def __init__(self, region_id=None, service=None):
        self.region_id = region_id  # type: str
        self.service = service  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCommercialStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class CheckCommercialStatusResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckCommercialStatusResponseBody, self).to_map()
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


class CheckCommercialStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckCommercialStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckCommercialStatusResponse, self).to_map()
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
            temp_model = CheckCommercialStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTagKeyRequest(TeaModel):
    def __init__(self, end_time=None, region_id=None, service_name=None, span_name=None, start_time=None):
        # The timestamp of the end time of the time range to query. The timestamp is accurate to milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the application.
        self.service_name = service_name  # type: str
        # The name of the span.
        self.span_name = span_name  # type: str
        # The timestamp of the start time of the time range to query. The timestamp is accurate to milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTagKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetTagKeyResponseBodyTagKeys(TeaModel):
    def __init__(self, tag_key=None):
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTagKeyResponseBodyTagKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class GetTagKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_keys=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The tag keys.
        self.tag_keys = tag_keys  # type: GetTagKeyResponseBodyTagKeys

    def validate(self):
        if self.tag_keys:
            self.tag_keys.validate()

    def to_map(self):
        _map = super(GetTagKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagKeys') is not None:
            temp_model = GetTagKeyResponseBodyTagKeys()
            self.tag_keys = temp_model.from_map(m['TagKeys'])
        return self


class GetTagKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTagKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTagKeyResponse, self).to_map()
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
            temp_model = GetTagKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTagValRequest(TeaModel):
    def __init__(self, end_time=None, region_id=None, service_name=None, span_name=None, start_time=None,
                 tag_key=None):
        # The timestamp of the end time of the time range to query. The timestamp is accurate to milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the application.
        self.service_name = service_name  # type: str
        # The name of the span.
        self.span_name = span_name  # type: str
        # The timestamp of the start time of the time range to query. The timestamp is accurate to milliseconds.
        self.start_time = start_time  # type: long
        # The tag key.
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTagValRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class GetTagValResponseBodyTagValues(TeaModel):
    def __init__(self, tag_value=None):
        self.tag_value = tag_value  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTagValResponseBodyTagValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetTagValResponseBody(TeaModel):
    def __init__(self, request_id=None, tag_values=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The tag values.
        self.tag_values = tag_values  # type: GetTagValResponseBodyTagValues

    def validate(self):
        if self.tag_values:
            self.tag_values.validate()

    def to_map(self):
        _map = super(GetTagValResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            temp_model = GetTagValResponseBodyTagValues()
            self.tag_values = temp_model.from_map(m['TagValues'])
        return self


class GetTagValResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTagValResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTagValResponse, self).to_map()
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
            temp_model = GetTagValResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceRequest(TeaModel):
    def __init__(self, app_type=None, region_id=None, trace_id=None):
        # The type of the application. You can set the value to **XTRACE** or leave this parameter unspecified.
        self.app_type = app_type  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The unique ID of the trace.
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


class GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryListTagEntry(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key in the log event.
        self.key = key  # type: str
        # The tag value in the log event.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryListTagEntry, self).to_map()
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


class GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryList(TeaModel):
    def __init__(self, tag_entry=None):
        self.tag_entry = tag_entry  # type: list[GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryListTagEntry]

    def validate(self):
        if self.tag_entry:
            for k in self.tag_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryList, self).to_map()
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
                temp_model = GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryListTagEntry()
                self.tag_entry.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodySpansSpanLogEventListLogEvent(TeaModel):
    def __init__(self, tag_entry_list=None, timestamp=None):
        # The tags in the log event.
        self.tag_entry_list = tag_entry_list  # type: GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryList
        # The timestamp when the log event was generated.
        self.timestamp = timestamp  # type: long

    def validate(self):
        if self.tag_entry_list:
            self.tag_entry_list.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpansSpanLogEventListLogEvent, self).to_map()
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
            temp_model = GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryList()
            self.tag_entry_list = temp_model.from_map(m['TagEntryList'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetTraceResponseBodySpansSpanLogEventList(TeaModel):
    def __init__(self, log_event=None):
        self.log_event = log_event  # type: list[GetTraceResponseBodySpansSpanLogEventListLogEvent]

    def validate(self):
        if self.log_event:
            for k in self.log_event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpansSpanLogEventList, self).to_map()
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
                temp_model = GetTraceResponseBodySpansSpanLogEventListLogEvent()
                self.log_event.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodySpansSpanTagEntryListTagEntry(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key in the span.
        self.key = key  # type: str
        # The tag value in the span.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTraceResponseBodySpansSpanTagEntryListTagEntry, self).to_map()
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


class GetTraceResponseBodySpansSpanTagEntryList(TeaModel):
    def __init__(self, tag_entry=None):
        self.tag_entry = tag_entry  # type: list[GetTraceResponseBodySpansSpanTagEntryListTagEntry]

    def validate(self):
        if self.tag_entry:
            for k in self.tag_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpansSpanTagEntryList, self).to_map()
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
                temp_model = GetTraceResponseBodySpansSpanTagEntryListTagEntry()
                self.tag_entry.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodySpansSpan(TeaModel):
    def __init__(self, duration=None, have_stack=None, log_event_list=None, operation_name=None,
                 parent_span_id=None, result_code=None, rpc_id=None, service_ip=None, service_name=None, span_id=None,
                 tag_entry_list=None, timestamp=None, trace_id=None):
        # The time used to call the trace. Unit: milliseconds.
        self.duration = duration  # type: long
        # Indicates whether the span has child spans. Valid values:
        # 
        # - true: The span has child spans. 
        # - false: The span has no child spans.
        self.have_stack = have_stack  # type: bool
        # The log events in the trace.
        self.log_event_list = log_event_list  # type: GetTraceResponseBodySpansSpanLogEventList
        # The name of the span.
        self.operation_name = operation_name  # type: str
        # The ID of the parent span.
        self.parent_span_id = parent_span_id  # type: str
        # The status code.
        self.result_code = result_code  # type: str
        # The parent-child and sibling relationship between spans. For example, span 1.1 is the parent of span 1.1.1, and span 1.1.2 and span 1.1.1 are siblings.
        self.rpc_id = rpc_id  # type: str
        # The IP address of the server where the span resides.
        self.service_ip = service_ip  # type: str
        # The name of the application.
        self.service_name = service_name  # type: str
        # Span ID.
        self.span_id = span_id  # type: str
        # The tags in the span.
        self.tag_entry_list = tag_entry_list  # type: GetTraceResponseBodySpansSpanTagEntryList
        # The timestamp when the span was generated. Unit: microseconds.
        self.timestamp = timestamp  # type: long
        # The unique ID of the trace.
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.log_event_list:
            self.log_event_list.validate()
        if self.tag_entry_list:
            self.tag_entry_list.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpansSpan, self).to_map()
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
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_id is not None:
            result['SpanId'] = self.span_id
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
            temp_model = GetTraceResponseBodySpansSpanLogEventList()
            self.log_event_list = temp_model.from_map(m['LogEventList'])
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        if m.get('TagEntryList') is not None:
            temp_model = GetTraceResponseBodySpansSpanTagEntryList()
            self.tag_entry_list = temp_model.from_map(m['TagEntryList'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBodySpans(TeaModel):
    def __init__(self, span=None):
        self.span = span  # type: list[GetTraceResponseBodySpansSpan]

    def validate(self):
        if self.span:
            for k in self.span:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTraceResponseBodySpans, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Span'] = []
        if self.span is not None:
            for k in self.span:
                result['Span'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.span = []
        if m.get('Span') is not None:
            for k in m.get('Span'):
                temp_model = GetTraceResponseBodySpansSpan()
                self.span.append(temp_model.from_map(k))
        return self


class GetTraceResponseBody(TeaModel):
    def __init__(self, request_id=None, spans=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the trace.
        self.spans = spans  # type: GetTraceResponseBodySpans

    def validate(self):
        if self.spans:
            self.spans.validate()

    def to_map(self):
        _map = super(GetTraceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spans is not None:
            result['Spans'] = self.spans.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spans') is not None:
            temp_model = GetTraceResponseBodySpans()
            self.spans = temp_model.from_map(m['Spans'])
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


class ListIpOrHostsRequest(TeaModel):
    def __init__(self, end_time=None, region_id=None, service_name=None, start_time=None):
        # The timestamp of the end time of the time range to query. The timestamp is accurate to milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the application. If you do not set this parameter, the IP addresses of all applications in the specified region are returned.
        self.service_name = service_name  # type: str
        # The timestamp of the start time of the time range to query. The timestamp is accurate to milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIpOrHostsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListIpOrHostsResponseBodyIpNames(TeaModel):
    def __init__(self, ip_name=None):
        self.ip_name = ip_name  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIpOrHostsResponseBodyIpNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        return self


class ListIpOrHostsResponseBody(TeaModel):
    def __init__(self, ip_names=None, request_id=None):
        # The IP addresses.
        self.ip_names = ip_names  # type: ListIpOrHostsResponseBodyIpNames
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ip_names:
            self.ip_names.validate()

    def to_map(self):
        _map = super(ListIpOrHostsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_names is not None:
            result['IpNames'] = self.ip_names.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IpNames') is not None:
            temp_model = ListIpOrHostsResponseBodyIpNames()
            self.ip_names = temp_model.from_map(m['IpNames'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListIpOrHostsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIpOrHostsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIpOrHostsResponse, self).to_map()
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
            temp_model = ListIpOrHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(self, app_type=None, region_id=None):
        # The type of the application. You can set the value to **XTRACE** or leave this parameter unspecified.
        self.app_type = app_type  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesRequest, self).to_map()
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


class ListServicesResponseBodyServicesService(TeaModel):
    def __init__(self, pid=None, region_id=None, service_name=None):
        # The ID of the application.
        self.pid = pid  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the application.
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServicesResponseBodyServicesService, self).to_map()
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


class ListServicesResponseBodyServices(TeaModel):
    def __init__(self, service=None):
        self.service = service  # type: list[ListServicesResponseBodyServicesService]

    def validate(self):
        if self.service:
            for k in self.service:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServicesResponseBodyServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Service'] = []
        if self.service is not None:
            for k in self.service:
                result['Service'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.service = []
        if m.get('Service') is not None:
            for k in m.get('Service'):
                temp_model = ListServicesResponseBodyServicesService()
                self.service.append(temp_model.from_map(k))
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(self, request_id=None, services=None):
        # The ID of the region.
        self.request_id = request_id  # type: str
        # The applications.
        self.services = services  # type: ListServicesResponseBodyServices

    def validate(self):
        if self.services:
            self.services.validate()

    def to_map(self):
        _map = super(ListServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.services is not None:
            result['Services'] = self.services.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Services') is not None:
            temp_model = ListServicesResponseBodyServices()
            self.services = temp_model.from_map(m['Services'])
        return self


class ListServicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpanNamesRequest(TeaModel):
    def __init__(self, end_time=None, region_id=None, service_name=None, start_time=None):
        # The timestamp of the end time of the time range to query. The timestamp is accurate to milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The name of the application.
        self.service_name = service_name  # type: str
        # The timestamp of the start time of the time range to query. The timestamp is accurate to milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSpanNamesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListSpanNamesResponseBodySpanNames(TeaModel):
    def __init__(self, span_name=None):
        self.span_name = span_name  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSpanNamesResponseBodySpanNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        return self


class ListSpanNamesResponseBody(TeaModel):
    def __init__(self, request_id=None, span_names=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The span names.
        self.span_names = span_names  # type: ListSpanNamesResponseBodySpanNames

    def validate(self):
        if self.span_names:
            self.span_names.validate()

    def to_map(self):
        _map = super(ListSpanNamesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.span_names is not None:
            result['SpanNames'] = self.span_names.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpanNames') is not None:
            temp_model = ListSpanNamesResponseBodySpanNames()
            self.span_names = temp_model.from_map(m['SpanNames'])
        return self


class ListSpanNamesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSpanNamesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSpanNamesResponse, self).to_map()
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
            temp_model = ListSpanNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenXtraceServiceRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenXtraceServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenXtraceServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None, result=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenXtraceServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class OpenXtraceServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenXtraceServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenXtraceServiceResponse, self).to_map()
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
            temp_model = OpenXtraceServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricRequestFilters(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the field that you want to use to filter the returned entries.
        self.key = key  # type: str
        # The value of the field that you want to use to filter the returned entries.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMetricRequestFilters, self).to_map()
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


class QueryMetricRequest(TeaModel):
    def __init__(self, dimensions=None, end_time=None, filters=None, interval_in_sec=None, limit=None, measures=None,
                 metric=None, order=None, order_by=None, proxy_user_id=None, start_time=None):
        # The dimensions of the metric that you want to query.
        self.dimensions = dimensions  # type: list[str]
        # The timestamp of the end time of the time range to query. The timestamp is accurate to milliseconds.
        self.end_time = end_time  # type: long
        # The filter conditions.
        self.filters = filters  # type: list[QueryMetricRequestFilters]
        # The time interval at which you want to query metric data. Unit: milliseconds. Minimum value: 60000. 
        # 
        # > If you set this parameter to 2147483647, all data in the specified time interval is returned.
        self.interval_in_sec = interval_in_sec  # type: int
        # The maximum number of entries that you want to return.
        self.limit = limit  # type: int
        # The measures of the metric that you want to query.
        self.measures = measures  # type: list[str]
        # The name of the metric. Valid values:
        # 
        # - `appstat.incall`: trace statistics 
        # - `appstat.sql`: SQL statistics
        self.metric = metric  # type: str
        # The order in which you want to sort the returned entries. Valid values:
        # 
        # - ASC: ascending order 
        # - DESC: descending order
        self.order = order  # type: str
        # The field based on which you want to sort the returned entries.
        self.order_by = order_by  # type: str
        # The ID of the proxy user.
        self.proxy_user_id = proxy_user_id  # type: str
        # The timestamp of the start time of the time range to query. The timestamp is accurate to milliseconds.
        self.start_time = start_time  # type: long

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMetricRequest, self).to_map()
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
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
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
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
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
                temp_model = QueryMetricRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
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
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMetricResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The returned statistics.
        self.data = data  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMetricResponseBody, self).to_map()
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


class QueryMetricResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMetricResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMetricResponse, self).to_map()
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
            temp_model = QueryMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesRequestTag, self).to_map()
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


class SearchTracesRequest(TeaModel):
    def __init__(self, app_type=None, end_time=None, min_duration=None, operation_name=None, page_number=None,
                 page_size=None, region_id=None, reverse=None, service_ip=None, service_name=None, start_time=None, tag=None):
        # The type of the application. You can set the value to **XTRACE** or leave this parameter unspecified.
        self.app_type = app_type  # type: str
        # The timestamp of the end time of the time range to query. The timestamp is accurate to milliseconds.
        self.end_time = end_time  # type: long
        # The time more than which is used to call the trace. Unit: milliseconds. For example, a value of 100 specifies to return the traces that more than 100 milliseconds are used to call.
        self.min_duration = min_duration  # type: long
        # The name of the span.
        self.operation_name = operation_name  # type: str
        # The number of the page to return. For example, a value of 5 indicates page 5.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The ID of the region.
        self.region_id = region_id  # type: str
        # Specifies whether to sort the query results in chronological order or reverse chronological order. Default value: false. Valid values:
        # 
        # - true: reverse chronological order 
        # - false: chronological order
        self.reverse = reverse  # type: bool
        # The IP address that corresponds to the span.
        self.service_ip = service_ip  # type: str
        # The name of the application.
        self.service_name = service_name  # type: str
        # The timestamp of the start time of the time range to query. The timestamp is accurate to milliseconds.
        self.start_time = start_time  # type: long
        # The list of the tags.
        self.tag = tag  # type: list[SearchTracesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = SearchTracesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class SearchTracesResponseBodyPageBeanTraceInfosTraceInfo(TeaModel):
    def __init__(self, duration=None, operation_name=None, service_ip=None, service_name=None, tag_map=None,
                 timestamp=None, trace_id=None):
        # The time used to call the trace. Unit: milliseconds.
        self.duration = duration  # type: long
        # The name of the span.
        self.operation_name = operation_name  # type: str
        # The IP address of the server where the span resides.
        self.service_ip = service_ip  # type: str
        # The name of the application.
        self.service_name = service_name  # type: str
        # The map of tags.
        self.tag_map = tag_map  # type: dict[str, any]
        # The time when the span was generated. Unit: microseconds.
        self.timestamp = timestamp  # type: long
        # The ID of the trace.
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchTracesResponseBodyPageBeanTraceInfosTraceInfo, self).to_map()
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
        if self.tag_map is not None:
            result['TagMap'] = self.tag_map
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
        if m.get('TagMap') is not None:
            self.tag_map = m.get('TagMap')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesResponseBodyPageBeanTraceInfos(TeaModel):
    def __init__(self, trace_info=None):
        self.trace_info = trace_info  # type: list[SearchTracesResponseBodyPageBeanTraceInfosTraceInfo]

    def validate(self):
        if self.trace_info:
            for k in self.trace_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchTracesResponseBodyPageBeanTraceInfos, self).to_map()
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
                temp_model = SearchTracesResponseBodyPageBeanTraceInfosTraceInfo()
                self.trace_info.append(temp_model.from_map(k))
        return self


class SearchTracesResponseBodyPageBean(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, trace_infos=None):
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The total number of entries returned.
        self.total_count = total_count  # type: long
        # The information about the trace.
        self.trace_infos = trace_infos  # type: SearchTracesResponseBodyPageBeanTraceInfos

    def validate(self):
        if self.trace_infos:
            self.trace_infos.validate()

    def to_map(self):
        _map = super(SearchTracesResponseBodyPageBean, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.trace_infos is not None:
            result['TraceInfos'] = self.trace_infos.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TraceInfos') is not None:
            temp_model = SearchTracesResponseBodyPageBeanTraceInfos()
            self.trace_infos = temp_model.from_map(m['TraceInfos'])
        return self


class SearchTracesResponseBody(TeaModel):
    def __init__(self, page_bean=None, request_id=None):
        # The information about the returned page.
        self.page_bean = page_bean  # type: SearchTracesResponseBodyPageBean
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super(SearchTracesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTracesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
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


