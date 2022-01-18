# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BatchGetRequest(TeaModel):
    def __init__(self, compression_type=None, cursor=None, length=None, metric=None, namespace=None,
                 record_key_white_list=None):
        self.compression_type = compression_type  # type: str
        self.cursor = cursor  # type: str
        self.length = length  # type: int
        self.metric = metric  # type: str
        self.namespace = namespace  # type: str
        self.record_key_white_list = record_key_white_list  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compression_type is not None:
            result['CompressionType'] = self.compression_type
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.length is not None:
            result['Length'] = self.length
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.record_key_white_list is not None:
            result['RecordKeyWhiteList'] = self.record_key_white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompressionType') is not None:
            self.compression_type = m.get('CompressionType')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RecordKeyWhiteList') is not None:
            self.record_key_white_list = m.get('RecordKeyWhiteList')
        return self


class BatchGetResponseBodyDataRecords(TeaModel):
    def __init__(self, label_values=None, labels=None, measure_labels=None, measure_values=None, metric=None,
                 namespace=None, period=None, tag_values=None, tags=None, timestamp=None):
        self.label_values = label_values  # type: list[str]
        self.labels = labels  # type: list[str]
        self.measure_labels = measure_labels  # type: list[str]
        self.measure_values = measure_values  # type: list[str]
        self.metric = metric  # type: str
        self.namespace = namespace  # type: str
        self.period = period  # type: int
        self.tag_values = tag_values  # type: list[str]
        self.tags = tags  # type: list[str]
        self.timestamp = timestamp  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchGetResponseBodyDataRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_values is not None:
            result['LabelValues'] = self.label_values
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.measure_labels is not None:
            result['MeasureLabels'] = self.measure_labels
        if self.measure_values is not None:
            result['MeasureValues'] = self.measure_values
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.period is not None:
            result['Period'] = self.period
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LabelValues') is not None:
            self.label_values = m.get('LabelValues')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('MeasureLabels') is not None:
            self.measure_labels = m.get('MeasureLabels')
        if m.get('MeasureValues') is not None:
            self.measure_values = m.get('MeasureValues')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class BatchGetResponseBodyData(TeaModel):
    def __init__(self, compression_keys=None, compression_values=None, cursor=None, length=None, records=None):
        self.compression_keys = compression_keys  # type: list[str]
        self.compression_values = compression_values  # type: list[list[dict[str, any]]]
        self.cursor = cursor  # type: str
        self.length = length  # type: long
        self.records = records  # type: list[BatchGetResponseBodyDataRecords]

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchGetResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compression_keys is not None:
            result['CompressionKeys'] = self.compression_keys
        if self.compression_values is not None:
            result['CompressionValues'] = self.compression_values
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.length is not None:
            result['Length'] = self.length
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompressionKeys') is not None:
            self.compression_keys = m.get('CompressionKeys')
        if m.get('CompressionValues') is not None:
            self.compression_values = m.get('CompressionValues')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = BatchGetResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        return self


class BatchGetResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: BatchGetResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchGetResponseBody, self).to_map()
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
            temp_model = BatchGetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchGetResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchGetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchGetResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchGetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CursorRequestMatchers(TeaModel):
    def __init__(self, label=None, operator=None, value=None):
        self.label = label  # type: str
        self.operator = operator  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CursorRequestMatchers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CursorRequest(TeaModel):
    def __init__(self, end_time=None, matchers=None, metric=None, namespace=None, period=None, start_time=None):
        self.end_time = end_time  # type: long
        self.matchers = matchers  # type: list[CursorRequestMatchers]
        self.metric = metric  # type: str
        self.namespace = namespace  # type: str
        self.period = period  # type: int
        self.start_time = start_time  # type: long

    def validate(self):
        if self.matchers:
            for k in self.matchers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CursorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Matchers'] = []
        if self.matchers is not None:
            for k in self.matchers:
                result['Matchers'].append(k.to_map() if k else None)
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.period is not None:
            result['Period'] = self.period
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.matchers = []
        if m.get('Matchers') is not None:
            for k in m.get('Matchers'):
                temp_model = CursorRequestMatchers()
                self.matchers.append(temp_model.from_map(k))
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CursorShrinkRequest(TeaModel):
    def __init__(self, end_time=None, matchers_shrink=None, metric=None, namespace=None, period=None,
                 start_time=None):
        self.end_time = end_time  # type: long
        self.matchers_shrink = matchers_shrink  # type: str
        self.metric = metric  # type: str
        self.namespace = namespace  # type: str
        self.period = period  # type: int
        self.start_time = start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CursorShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.matchers_shrink is not None:
            result['Matchers'] = self.matchers_shrink
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.period is not None:
            result['Period'] = self.period
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Matchers') is not None:
            self.matchers_shrink = m.get('Matchers')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CursorResponseBodyData(TeaModel):
    def __init__(self, cursor=None):
        self.cursor = cursor  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CursorResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        return self


class CursorResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: CursorResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CursorResponseBody, self).to_map()
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
            temp_model = CursorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CursorResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CursorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CursorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CursorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


