# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetOssUploadParamRequest(TeaModel):
    def __init__(self, app_version=None, data_source_id=None, file_name=None, file_type=None):
        self.app_version = app_version  # type: str
        self.data_source_id = data_source_id  # type: str
        self.file_name = file_name  # type: str
        self.file_type = file_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssUploadParamRequest, self).to_map()
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


class GetOssUploadParamResponseBodyData(TeaModel):
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
        _map = super(GetOssUploadParamResponseBodyData, self).to_map()
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


class GetOssUploadParamResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None, msg=None, success=None, trace_id=None):
        self.request_id = request_id  # type: str
        # code
        self.code = code  # type: long
        # data
        self.data = data  # type: GetOssUploadParamResponseBodyData
        self.msg = msg  # type: str
        self.success = success  # type: bool
        # traceId
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOssUploadParamResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetOssUploadParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class GetOssUploadParamResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOssUploadParamResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOssUploadParamResponse, self).to_map()
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
            temp_model = GetOssUploadParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadNotaryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, detail_msg=None, msg=None):
        # code
        self.code = code  # type: long
        self.data = data  # type: str
        self.detail_msg = detail_msg  # type: str
        self.msg = msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadNotaryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.detail_msg is not None:
            result['detailMsg'] = self.detail_msg
        if self.msg is not None:
            result['msg'] = self.msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('detailMsg') is not None:
            self.detail_msg = m.get('detailMsg')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        return self


class UploadNotaryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UploadNotaryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadNotaryResponse, self).to_map()
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
            temp_model = UploadNotaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


