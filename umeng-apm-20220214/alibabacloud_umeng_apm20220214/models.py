# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetStatTrendRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, end_date=None, start_date=None, type=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.end_date = end_date  # type: str
        self.start_date = start_date  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStatTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetStatTrendResponseBodyData(TeaModel):
    def __init__(self, affected_user_count=None, affected_user_rate=None, error_count=None, error_rate=None,
                 time_point=None):
        self.affected_user_count = affected_user_count  # type: long
        self.affected_user_rate = affected_user_rate  # type: long
        self.error_count = error_count  # type: long
        self.error_rate = error_rate  # type: long
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStatTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_user_count is not None:
            result['affectedUserCount'] = self.affected_user_count
        if self.affected_user_rate is not None:
            result['affectedUserRate'] = self.affected_user_rate
        if self.error_count is not None:
            result['errorCount'] = self.error_count
        if self.error_rate is not None:
            result['errorRate'] = self.error_rate
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('affectedUserCount') is not None:
            self.affected_user_count = m.get('affectedUserCount')
        if m.get('affectedUserRate') is not None:
            self.affected_user_rate = m.get('affectedUserRate')
        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')
        if m.get('errorRate') is not None:
            self.error_rate = m.get('errorRate')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        return self


class GetStatTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[GetStatTrendResponseBodyData]
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetStatTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetStatTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetStatTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStatTrendResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStatTrendResponse, self).to_map()
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
            temp_model = GetStatTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSymUploadParamRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, file_name=None, file_type=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSymUploadParamRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        return self


class GetSymUploadParamResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, callback=None, key=None, policy=None, signature=None, upload_address=None):
        self.access_key_id = access_key_id  # type: str
        self.callback = callback  # type: str
        self.key = key  # type: str
        self.policy = policy  # type: str
        self.signature = signature  # type: str
        self.upload_address = upload_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSymUploadParamResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.callback is not None:
            result['callback'] = self.callback
        if self.key is not None:
            result['key'] = self.key
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        if self.upload_address is not None:
            result['uploadAddress'] = self.upload_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('callback') is not None:
            self.callback = m.get('callback')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('uploadAddress') is not None:
            self.upload_address = m.get('uploadAddress')
        return self


class GetSymUploadParamResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None, trace_id=None):
        self.code = code  # type: long
        self.data = data  # type: GetSymUploadParamResponseBodyData
        self.msg = msg  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetSymUploadParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetSymUploadParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class GetSymUploadParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSymUploadParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSymUploadParamResponse, self).to_map()
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
            temp_model = GetSymUploadParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTodayStatTrendRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, type=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTodayStatTrendRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTodayStatTrendResponseBodyData(TeaModel):
    def __init__(self, affected_user_count=None, affected_user_rate=None, error_count=None, error_rate=None,
                 time_point=None):
        self.affected_user_count = affected_user_count  # type: long
        self.affected_user_rate = affected_user_rate  # type: long
        self.error_count = error_count  # type: long
        self.error_rate = error_rate  # type: long
        self.time_point = time_point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTodayStatTrendResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_user_count is not None:
            result['affectedUserCount'] = self.affected_user_count
        if self.affected_user_rate is not None:
            result['affectedUserRate'] = self.affected_user_rate
        if self.error_count is not None:
            result['errorCount'] = self.error_count
        if self.error_rate is not None:
            result['errorRate'] = self.error_rate
        if self.time_point is not None:
            result['timePoint'] = self.time_point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('affectedUserCount') is not None:
            self.affected_user_count = m.get('affectedUserCount')
        if m.get('affectedUserRate') is not None:
            self.affected_user_rate = m.get('affectedUserRate')
        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')
        if m.get('errorRate') is not None:
            self.error_rate = m.get('errorRate')
        if m.get('timePoint') is not None:
            self.time_point = m.get('timePoint')
        return self


class GetTodayStatTrendResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[GetTodayStatTrendResponseBodyData]
        self.msg = msg  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetTodayStatTrendResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetTodayStatTrendResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTodayStatTrendResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTodayStatTrendResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTodayStatTrendResponse, self).to_map()
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
            temp_model = GetTodayStatTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


