# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class BatchAuditTest01Request(TeaModel):
    def __init__(self, name=None, batch_audit_test_01=None, demo_01=None, test_010101=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.batch_audit_test_01 = TeaConverter.to_unicode(batch_audit_test_01)  # type: unicode
        self.demo_01 = TeaConverter.to_unicode(demo_01)  # type: unicode
        self.test_010101 = test_010101  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.batch_audit_test_01 is not None:
            result['BatchAuditTest01'] = self.batch_audit_test_01
        if self.demo_01 is not None:
            result['Demo01'] = self.demo_01
        if self.test_010101 is not None:
            result['Test010101'] = self.test_010101
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BatchAuditTest01') is not None:
            self.batch_audit_test_01 = m.get('BatchAuditTest01')
        if m.get('Demo01') is not None:
            self.demo_01 = m.get('Demo01')
        if m.get('Test010101') is not None:
            self.test_010101 = m.get('Test010101')
        return self


class BatchAuditTest01ResponseBodyDemo01Demo011Demo011(TeaModel):
    def __init__(self, demo_0111=None):
        self.demo_0111 = TeaConverter.to_unicode(demo_0111)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.demo_0111 is not None:
            result['Demo0111'] = self.demo_0111
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Demo0111') is not None:
            self.demo_0111 = m.get('Demo0111')
        return self


class BatchAuditTest01ResponseBodyDemo01Demo011(TeaModel):
    def __init__(self, demo_011=None):
        self.demo_011 = demo_011  # type: list[BatchAuditTest01ResponseBodyDemo01Demo011Demo011]

    def validate(self):
        if self.demo_011:
            for k in self.demo_011:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Demo011'] = []
        if self.demo_011 is not None:
            for k in self.demo_011:
                result['Demo011'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.demo_011 = []
        if m.get('Demo011') is not None:
            for k in m.get('Demo011'):
                temp_model = BatchAuditTest01ResponseBodyDemo01Demo011Demo011()
                self.demo_011.append(temp_model.from_map(k))
        return self


class BatchAuditTest01ResponseBodyDemo01(TeaModel):
    def __init__(self, demo_011=None):
        self.demo_011 = demo_011  # type: BatchAuditTest01ResponseBodyDemo01Demo011

    def validate(self):
        if self.demo_011:
            self.demo_011.validate()

    def to_map(self):
        result = dict()
        if self.demo_011 is not None:
            result['Demo011'] = self.demo_011.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Demo011') is not None:
            temp_model = BatchAuditTest01ResponseBodyDemo01Demo011()
            self.demo_011 = temp_model.from_map(m['Demo011'])
        return self


class BatchAuditTest01ResponseBody(TeaModel):
    def __init__(self, request_id=None, demo_01=None, name=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.demo_01 = demo_01  # type: BatchAuditTest01ResponseBodyDemo01
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        if self.demo_01:
            self.demo_01.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.demo_01 is not None:
            result['Demo01'] = self.demo_01.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Demo01') is not None:
            temp_model = BatchAuditTest01ResponseBodyDemo01()
            self.demo_01 = temp_model.from_map(m['Demo01'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class BatchAuditTest01Response(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: BatchAuditTest01ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchAuditTest01ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FTApiAliasApiRequest(TeaModel):
    def __init__(self, name=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FTApiAliasApiResponseBody(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FTApiAliasApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: FTApiAliasApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FTApiAliasApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtDynamicAddressDubboRequest(TeaModel):
    def __init__(self, int_value=None, string_value=None):
        self.int_value = int_value  # type: int
        self.string_value = TeaConverter.to_unicode(string_value)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.int_value is not None:
            result['IntValue'] = self.int_value
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntValue') is not None:
            self.int_value = m.get('IntValue')
        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')
        return self


class FtDynamicAddressDubboResponseBody(TeaModel):
    def __init__(self, request_id=None, string_value=None, int_value=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.string_value = TeaConverter.to_unicode(string_value)  # type: unicode
        self.int_value = int_value  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        if self.int_value is not None:
            result['IntValue'] = self.int_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')
        if m.get('IntValue') is not None:
            self.int_value = m.get('IntValue')
        return self


class FtDynamicAddressDubboResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: FtDynamicAddressDubboResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FtDynamicAddressDubboResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtDynamicAddressHsfResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FtDynamicAddressHsfResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: FtDynamicAddressHsfResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FtDynamicAddressHsfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtEagleEyeRequest(TeaModel):
    def __init__(self, name=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtEagleEyeResponseBody(TeaModel):
    def __init__(self, eagle_eye_trace_id=None, request_id=None, name=None):
        self.eagle_eye_trace_id = TeaConverter.to_unicode(eagle_eye_trace_id)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.eagle_eye_trace_id is not None:
            result['eagleEyeTraceId'] = self.eagle_eye_trace_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('eagleEyeTraceId') is not None:
            self.eagle_eye_trace_id = m.get('eagleEyeTraceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtEagleEyeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: FtEagleEyeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FtEagleEyeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtFlowSpecialRequest(TeaModel):
    def __init__(self, name=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtFlowSpecialResponseBody(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtFlowSpecialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: FtFlowSpecialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FtFlowSpecialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtGatedLaunchPolicy4Request(TeaModel):
    def __init__(self, is_gated_launch=None):
        self.is_gated_launch = TeaConverter.to_unicode(is_gated_launch)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_gated_launch is not None:
            result['IsGatedLaunch'] = self.is_gated_launch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsGatedLaunch') is not None:
            self.is_gated_launch = m.get('IsGatedLaunch')
        return self


class FtGatedLaunchPolicy4ResponseBody(TeaModel):
    def __init__(self, is_gated_launch=None, request_id=None):
        self.is_gated_launch = TeaConverter.to_unicode(is_gated_launch)  # type: unicode
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_gated_launch is not None:
            result['IsGatedLaunch'] = self.is_gated_launch
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsGatedLaunch') is not None:
            self.is_gated_launch = m.get('IsGatedLaunch')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FtGatedLaunchPolicy4Response(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: FtGatedLaunchPolicy4ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FtGatedLaunchPolicy4ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtIpFlowControlRequest(TeaModel):
    def __init__(self, name=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtIpFlowControlResponseBody(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtIpFlowControlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: FtIpFlowControlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FtIpFlowControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtParamListRequestDisk(TeaModel):
    def __init__(self, type=None, size=None):
        self.type = type  # type: list[unicode]
        self.size = size  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class FtParamListRequest(TeaModel):
    def __init__(self, name=None, disk=None):
        self.name = TeaConverter.to_unicode(name)  # type: unicode
        self.disk = disk  # type: list[FtParamListRequestDisk]

    def validate(self):
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = FtParamListRequestDisk()
                self.disk.append(temp_model.from_map(k))
        return self


class FtParamListResponseBody(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.name = TeaConverter.to_unicode(name)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtParamListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: FtParamListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FtParamListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestFlowStrategy01Request(TeaModel):
    def __init__(self, names=None):
        self.names = names  # type: dict[unicode, any]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        return self


class TestFlowStrategy01ShrinkRequest(TeaModel):
    def __init__(self, names_shrink=None):
        self.names_shrink = TeaConverter.to_unicode(names_shrink)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.names_shrink is not None:
            result['Names'] = self.names_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names_shrink = m.get('Names')
        return self


class TestFlowStrategy01ResponseBody(TeaModel):
    def __init__(self, names=None, request_id=None, list=None):
        self.names = names  # type: list[unicode]
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.list = list  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.list is not None:
            result['List'] = self.list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('List') is not None:
            self.list = m.get('List')
        return self


class TestFlowStrategy01Response(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: TestFlowStrategy01ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TestFlowStrategy01ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestHttpApiRequest(TeaModel):
    def __init__(self, string_value=None, default_value=None, other_param=None, boolean_param=None):
        self.string_value = string_value  # type: dict[unicode, any]
        self.default_value = default_value  # type: dict[unicode, any]
        self.other_param = other_param  # type: dict[unicode, any]
        self.boolean_param = boolean_param  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.other_param is not None:
            result['OtherParam'] = self.other_param
        if self.boolean_param is not None:
            result['BooleanParam'] = self.boolean_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('OtherParam') is not None:
            self.other_param = m.get('OtherParam')
        if m.get('BooleanParam') is not None:
            self.boolean_param = m.get('BooleanParam')
        return self


class TestHttpApiShrinkRequest(TeaModel):
    def __init__(self, string_value_shrink=None, default_value_shrink=None, other_param_shrink=None,
                 boolean_param=None):
        self.string_value_shrink = TeaConverter.to_unicode(string_value_shrink)  # type: unicode
        self.default_value_shrink = TeaConverter.to_unicode(default_value_shrink)  # type: unicode
        self.other_param_shrink = TeaConverter.to_unicode(other_param_shrink)  # type: unicode
        self.boolean_param = boolean_param  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.string_value_shrink is not None:
            result['StringValue'] = self.string_value_shrink
        if self.default_value_shrink is not None:
            result['DefaultValue'] = self.default_value_shrink
        if self.other_param_shrink is not None:
            result['OtherParam'] = self.other_param_shrink
        if self.boolean_param is not None:
            result['BooleanParam'] = self.boolean_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StringValue') is not None:
            self.string_value_shrink = m.get('StringValue')
        if m.get('DefaultValue') is not None:
            self.default_value_shrink = m.get('DefaultValue')
        if m.get('OtherParam') is not None:
            self.other_param_shrink = m.get('OtherParam')
        if m.get('BooleanParam') is not None:
            self.boolean_param = m.get('BooleanParam')
        return self


class TestHttpApiResponseBody(TeaModel):
    def __init__(self, service_rpc_sign=None, params=None):
        self.service_rpc_sign = TeaConverter.to_unicode(service_rpc_sign)  # type: unicode
        self.params = TeaConverter.to_unicode(params)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service_rpc_sign is not None:
            result['ServiceRpcSign'] = self.service_rpc_sign
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceRpcSign') is not None:
            self.service_rpc_sign = m.get('ServiceRpcSign')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class TestHttpApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: TestHttpApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TestHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


