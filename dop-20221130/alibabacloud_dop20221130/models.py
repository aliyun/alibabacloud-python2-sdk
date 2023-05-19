# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetOssMetaDownloadRequest(TeaModel):
    def __init__(self, ds=None, expire=None, table_name=None):
        self.ds = ds  # type: str
        self.expire = expire  # type: long
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssMetaDownloadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ds is not None:
            result['ds'] = self.ds
        if self.expire is not None:
            result['expire'] = self.expire
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ds') is not None:
            self.ds = m.get('ds')
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class GetOssMetaDownloadResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, msg=None, request_id=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[str]
        self.error_code = error_code  # type: str
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssMetaDownloadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOssMetaDownloadResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOssMetaDownloadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOssMetaDownloadResponse, self).to_map()
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
            temp_model = GetOssMetaDownloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssMetaListRequest(TeaModel):
    def __init__(self, end=None, start=None, table_name=None):
        self.end = end  # type: str
        self.start = start  # type: str
        self.table_name = table_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssMetaListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class GetOssMetaListResponseBodyData(TeaModel):
    def __init__(self, ds=None, file_names=None, file_size=None, rows=None):
        self.ds = ds  # type: str
        self.file_names = file_names  # type: list[str]
        self.file_size = file_size  # type: str
        self.rows = rows  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssMetaListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ds is not None:
            result['ds'] = self.ds
        if self.file_names is not None:
            result['fileNames'] = self.file_names
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.rows is not None:
            result['rows'] = self.rows
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ds') is not None:
            self.ds = m.get('ds')
        if m.get('fileNames') is not None:
            self.file_names = m.get('fileNames')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('rows') is not None:
            self.rows = m.get('rows')
        return self


class GetOssMetaListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, msg=None, request_id=None, success=None):
        self.code = code  # type: long
        self.data = data  # type: list[GetOssMetaListResponseBodyData]
        self.error_code = error_code  # type: str
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOssMetaListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.msg is not None:
            result['Msg'] = self.msg
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
                temp_model = GetOssMetaListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOssMetaListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOssMetaListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOssMetaListResponse, self).to_map()
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
            temp_model = GetOssMetaListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitBackfill4ApiRequest(TeaModel):
    def __init__(self, end=None, package_id=None, start=None):
        self.end = end  # type: str
        self.package_id = package_id  # type: int
        self.start = start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitBackfill4ApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.package_id is not None:
            result['packageId'] = self.package_id
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('packageId') is not None:
            self.package_id = m.get('packageId')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class SubmitBackfill4ApiResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, msg=None, request_id=None, success=None, dy_code=None,
                 dy_message=None):
        # code
        self.code = code  # type: long
        # data
        self.data = data  # type: str
        self.error_code = error_code  # type: str
        self.msg = msg  # type: str
        # requestId
        self.request_id = request_id  # type: str
        # success
        self.success = success  # type: bool
        self.dy_code = dy_code  # type: str
        self.dy_message = dy_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitBackfill4ApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.dy_code is not None:
            result['dyCode'] = self.dy_code
        if self.dy_message is not None:
            result['dyMessage'] = self.dy_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('dyCode') is not None:
            self.dy_code = m.get('dyCode')
        if m.get('dyMessage') is not None:
            self.dy_message = m.get('dyMessage')
        return self


class SubmitBackfill4ApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitBackfill4ApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitBackfill4ApiResponse, self).to_map()
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
            temp_model = SubmitBackfill4ApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


