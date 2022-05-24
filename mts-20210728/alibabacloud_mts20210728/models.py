# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class QueryCopyrightRequest(TeaModel):
    def __init__(self, create_time_end=None, create_time_start=None, job_id=None, level=None, page_number=None,
                 page_size=None):
        # 创建时间截止
        self.create_time_end = create_time_end  # type: long
        # 创建时间起始
        self.create_time_start = create_time_start  # type: long
        # 任务id
        self.job_id = job_id  # type: str
        # 水印强度
        self.level = level  # type: long
        # 翻页下标
        self.page_number = page_number  # type: long
        # 每页数量
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCopyrightRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryCopyrightResponseBodyData(TeaModel):
    def __init__(self, callback=None, gmt_create=None, gmt_modified=None, input=None, job_id=None, level=None,
                 message=None, message_id=None, output=None, result=None, status=None, user_data=None, user_id=None):
        # 回调url
        self.callback = callback  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 水印视频输入
        self.input = input  # type: str
        # 任务id
        self.job_id = job_id  # type: str
        # 水印强度
        self.level = level  # type: long
        # 水印信息
        self.message = message  # type: str
        # 水印信息id
        self.message_id = message_id  # type: long
        # 水印视频输出
        self.output = output  # type: str
        # 任务结果
        self.result = result  # type: str
        # 状态
        self.status = status  # type: str
        # 用户数据
        self.user_data = user_data  # type: str
        # 用户ID
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCopyrightResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input is not None:
            result['Input'] = self.input
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.output is not None:
            result['Output'] = self.output
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryCopyrightResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, status_code=None):
        self.data = data  # type: list[QueryCopyrightResponseBodyData]
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCopyrightResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryCopyrightResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryCopyrightResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCopyrightResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCopyrightResponse, self).to_map()
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
            temp_model = QueryCopyrightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCopyrightExtractRequest(TeaModel):
    def __init__(self, job_id=None):
        # 任务id
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCopyrightExtractRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryCopyrightExtractResponseBodyData(TeaModel):
    def __init__(self, message=None):
        # 版权水印信息
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCopyrightExtractResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class QueryCopyrightExtractResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        self.data = data  # type: QueryCopyrightExtractResponseBodyData
        # 返回信息
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCopyrightExtractResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryCopyrightExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryCopyrightExtractResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCopyrightExtractResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCopyrightExtractResponse, self).to_map()
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
            temp_model = QueryCopyrightExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTraceAbRequest(TeaModel):
    def __init__(self, job_id=None, media_id=None):
        # 任务id
        self.job_id = job_id  # type: str
        # 媒体id
        self.media_id = media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTraceAbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class QueryTraceAbResponseBodyData(TeaModel):
    def __init__(self, callback=None, gmt_create=None, gmt_modified=None, input=None, job_id=None, level=None,
                 media_id=None, output=None, result=None, status=None, user_data=None, user_id=None):
        # 任务结果回调
        self.callback = callback  # type: str
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 最后修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 输入oss地址
        self.input = input  # type: str
        # 任务id
        self.job_id = job_id  # type: str
        # 水印强度
        self.level = level  # type: long
        # 媒体id
        self.media_id = media_id  # type: str
        # 输出地址
        self.output = output  # type: str
        # 任务结果
        self.result = result  # type: str
        # 任务状态
        self.status = status  # type: str
        # 用户数据
        self.user_data = user_data  # type: str
        # uid
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTraceAbResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input is not None:
            result['Input'] = self.input
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.output is not None:
            result['Output'] = self.output
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTraceAbResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        # 返回结构
        self.data = data  # type: list[QueryTraceAbResponseBodyData]
        # 返回信息
        self.message = message  # type: str
        # 请求id
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTraceAbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTraceAbResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryTraceAbResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTraceAbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTraceAbResponse, self).to_map()
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
            temp_model = QueryTraceAbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTraceExtractRequest(TeaModel):
    def __init__(self, job_id=None):
        # 任务id
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTraceExtractRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryTraceExtractResponseBodyData(TeaModel):
    def __init__(self, trace=None):
        # 溯源水印信息
        self.trace = trace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTraceExtractResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trace is not None:
            result['Trace'] = self.trace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')
        return self


class QueryTraceExtractResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        self.data = data  # type: QueryTraceExtractResponseBodyData
        # 返回信息
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTraceExtractResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryTraceExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryTraceExtractResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTraceExtractResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTraceExtractResponse, self).to_map()
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
            temp_model = QueryTraceExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTraceMuRequest(TeaModel):
    def __init__(self, create_time_end=None, create_time_start=None, job_id=None, level=None, message_id=None,
                 page_number=None, page_size=None):
        # 创建时间起始
        self.create_time_end = create_time_end  # type: long
        # 创建时间截止
        self.create_time_start = create_time_start  # type: long
        # 任务id
        self.job_id = job_id  # type: str
        # 水印强度
        self.level = level  # type: long
        # 水印信息id
        self.message_id = message_id  # type: long
        # 页偏移
        self.page_number = page_number  # type: long
        # 每页数量
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTraceMuRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.level is not None:
            result['Level'] = self.level
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTraceMuResponseBodyData(TeaModel):
    def __init__(self, gmt_create=None, gmt_modified=None, job_id=None, media_id=None, output=None, status=None,
                 trace=None, trace_id=None, user_data=None, user_id=None):
        # 创建时间
        self.gmt_create = gmt_create  # type: long
        # 最后修改时间
        self.gmt_modified = gmt_modified  # type: long
        # 任务id
        self.job_id = job_id  # type: str
        # 媒体id
        self.media_id = media_id  # type: str
        # 输出oss地址
        self.output = output  # type: str
        # 任务状态
        self.status = status  # type: str
        # 溯源水印信息
        self.trace = trace  # type: str
        # 溯源水印信息id
        self.trace_id = trace_id  # type: long
        # 用户自定义数据
        self.user_data = user_data  # type: str
        # uid
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTraceMuResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.output is not None:
            result['Output'] = self.output
        if self.status is not None:
            result['Status'] = self.status
        if self.trace is not None:
            result['Trace'] = self.trace
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryTraceMuResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        # 返回数据结构
        self.data = data  # type: list[QueryTraceMuResponseBodyData]
        # 返回信息
        self.message = message  # type: str
        # 请求id
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTraceMuResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTraceMuResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class QueryTraceMuResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTraceMuResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTraceMuResponse, self).to_map()
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
            temp_model = QueryTraceMuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitCopyrightExtractRequest(TeaModel):
    def __init__(self, call_back=None, input=None, url=None, user_data=None):
        # 任务完成回调
        self.call_back = call_back  # type: str
        # 输入文件oss地址
        self.input = input  # type: str
        # url链接
        self.url = url  # type: str
        # 用户数据
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitCopyrightExtractRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.input is not None:
            result['Input'] = self.input
        if self.url is not None:
            result['Url'] = self.url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitCopyrightExtractResponseBodyData(TeaModel):
    def __init__(self, job_id=None):
        # 任务id
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitCopyrightExtractResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitCopyrightExtractResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        self.data = data  # type: SubmitCopyrightExtractResponseBodyData
        # 返回消息
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitCopyrightExtractResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitCopyrightExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitCopyrightExtractResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitCopyrightExtractResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitCopyrightExtractResponse, self).to_map()
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
            temp_model = SubmitCopyrightExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitCopyrightJobRequest(TeaModel):
    def __init__(self, call_back=None, description=None, input=None, level=None, message=None, output=None,
                 start_time=None, total_time=None, url=None, user_data=None, visible_message=None):
        # 任务结果回调url
        self.call_back = call_back  # type: str
        # 水印信息描述
        self.description = description  # type: str
        # 输入的视频，oss三元组
        self.input = input  # type: str
        # 水印强度，取值1，2，3
        self.level = level  # type: long
        # 水印信息
        self.message = message  # type: str
        # 输出的视频，oss三元组
        self.output = output  # type: str
        # 水印起始时间(单位是秒)，不填写默认为0
        self.start_time = start_time  # type: long
        # 水印结束时间(单位是秒)，不填默认为60000
        self.total_time = total_time  # type: long
        # 外部url链接(Input和url二选一)
        self.url = url  # type: str
        # 用户自定义数据
        self.user_data = user_data  # type: str
        # 可见水印(必须是英文字符)
        self.visible_message = visible_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitCopyrightJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.description is not None:
            result['Description'] = self.description
        if self.input is not None:
            result['Input'] = self.input
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.url is not None:
            result['Url'] = self.url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.visible_message is not None:
            result['VisibleMessage'] = self.visible_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VisibleMessage') is not None:
            self.visible_message = m.get('VisibleMessage')
        return self


class SubmitCopyrightJobResponseBodyData(TeaModel):
    def __init__(self, job_id=None):
        # 任务id
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitCopyrightJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitCopyrightJobResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        # 返回数据
        self.data = data  # type: SubmitCopyrightJobResponseBodyData
        # 返回信息
        self.message = message  # type: str
        # 请求Id
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitCopyrightJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitCopyrightJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitCopyrightJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitCopyrightJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitCopyrightJobResponse, self).to_map()
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
            temp_model = SubmitCopyrightJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitImageCopyrightRequest(TeaModel):
    def __init__(self, input=None, level=None, message=None, output=None, url=None):
        # 需要加水印的图片oss地址(Input和url二选一)
        self.input = input  # type: str
        # 水印强度
        self.level = level  # type: long
        # 水印信息
        self.message = message  # type: str
        # 水印图片输出oss地址
        self.output = output  # type: str
        # 外部url链接(Input和url二选一)
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitImageCopyrightRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['Input'] = self.input
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SubmitImageCopyrightResponseBodyData(TeaModel):
    def __init__(self, job_id=None):
        # 任务id
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitImageCopyrightResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitImageCopyrightResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        # 返回数据
        self.data = data  # type: SubmitImageCopyrightResponseBodyData
        # 返回信息
        self.message = message  # type: str
        # 请求id
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitImageCopyrightResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitImageCopyrightResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitImageCopyrightResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitImageCopyrightResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitImageCopyrightResponse, self).to_map()
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
            temp_model = SubmitImageCopyrightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTraceAbRequest(TeaModel):
    def __init__(self, call_back=None, cipher_base_64ed=None, input=None, level=None, output=None, start_time=None,
                 total_time=None, url=None, user_data=None):
        # 任务结果回调
        self.call_back = call_back  # type: str
        # 密钥base64串
        self.cipher_base_64ed = cipher_base_64ed  # type: str
        # 溯源水印ab流处理视频输入
        self.input = input  # type: str
        # 水印强度
        self.level = level  # type: long
        # 溯源水印ab流处理输出
        self.output = output  # type: str
        # 嵌入水印开始时间
        self.start_time = start_time  # type: long
        # 嵌入水印总时长
        self.total_time = total_time  # type: long
        # 外部url链接(Input和url二选一)
        self.url = url  # type: str
        # 用户自定义数据，最大长度1024个字节
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTraceAbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.cipher_base_64ed is not None:
            result['CipherBase64ed'] = self.cipher_base_64ed
        if self.input is not None:
            result['Input'] = self.input
        if self.level is not None:
            result['Level'] = self.level
        if self.output is not None:
            result['Output'] = self.output
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.url is not None:
            result['Url'] = self.url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('CipherBase64ed') is not None:
            self.cipher_base_64ed = m.get('CipherBase64ed')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitTraceAbResponseBodyData(TeaModel):
    def __init__(self, job_id=None, media_id=None):
        # 任务ID
        self.job_id = job_id  # type: str
        # 媒体id
        self.media_id = media_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTraceAbResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class SubmitTraceAbResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        # 返回数据
        self.data = data  # type: SubmitTraceAbResponseBodyData
        # 返回信息
        self.message = message  # type: str
        # 请求Id
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitTraceAbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitTraceAbResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitTraceAbResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitTraceAbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTraceAbResponse, self).to_map()
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
            temp_model = SubmitTraceAbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTraceExtractRequest(TeaModel):
    def __init__(self, call_back=None, input=None, url=None, user_data=None):
        # 任务完成回调
        self.call_back = call_back  # type: str
        # 输入文件oss地址
        self.input = input  # type: str
        # url链接
        self.url = url  # type: str
        # 用户数据
        self.user_data = user_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTraceExtractRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_back is not None:
            result['CallBack'] = self.call_back
        if self.input is not None:
            result['Input'] = self.input
        if self.url is not None:
            result['Url'] = self.url
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallBack') is not None:
            self.call_back = m.get('CallBack')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class SubmitTraceExtractResponseBodyData(TeaModel):
    def __init__(self, job_id=None):
        # 任务id
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTraceExtractResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitTraceExtractResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        self.data = data  # type: SubmitTraceExtractResponseBodyData
        # 返回消息
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitTraceExtractResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitTraceExtractResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitTraceExtractResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitTraceExtractResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTraceExtractResponse, self).to_map()
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
            temp_model = SubmitTraceExtractResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTracemuRequest(TeaModel):
    def __init__(self, key_uri=None, media_id=None, output=None, trace=None):
        # 密钥服务器uri
        self.key_uri = key_uri  # type: str
        # ab流处理后的媒体id
        self.media_id = media_id  # type: str
        # m3u8文件输出oss地址
        self.output = output  # type: str
        # 溯源水印信息
        self.trace = trace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTracemuRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_uri is not None:
            result['KeyUri'] = self.key_uri
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.output is not None:
            result['Output'] = self.output
        if self.trace is not None:
            result['Trace'] = self.trace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeyUri') is not None:
            self.key_uri = m.get('KeyUri')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')
        return self


class SubmitTracemuResponseBodyData(TeaModel):
    def __init__(self, code=None, job_id=None):
        # 生成m3u8文件的code
        self.code = code  # type: str
        # 任务id
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTracemuResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class SubmitTracemuResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, status_code=None):
        # 返回数据
        self.data = data  # type: SubmitTracemuResponseBodyData
        # 返回信息
        self.message = message  # type: str
        # 请求Id
        self.request_id = request_id  # type: str
        # 状态码
        self.status_code = status_code  # type: long

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitTracemuResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestID'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SubmitTracemuResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestID') is not None:
            self.request_id = m.get('RequestID')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SubmitTracemuResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitTracemuResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTracemuResponse, self).to_map()
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
            temp_model = SubmitTracemuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


